"""Original Nail Technician learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='nail-technicians',
    title='Nail Technician English',
    cover_label='ENGLISH FOR NAIL SERVICES',
    cover_title='Nail\nTechnician',
    cover_size=40,
    tagline='Precise details. Clear agreement.',
    audience='For nail technicians, salon receptionists, assistants, and nail-service team leads.',
    map_intro='Eight lessons on consultations, shapes, finishes, quotes, concerns, station updates, and bookings. Three additional conversations cover curing-system checks, tool turnover, and precise nail-art placement.',
    notes_title='Small details change the whole request.',
    notes_intro='A useful nail-service conversation separates length, shape, color, coverage, finish, product, design placement, price, and permission. Confirming those details prevents a familiar label or attractive reference from silently replacing what the client actually wants.',
    field_notes=[
        ('Describe before naming', 'A client may say full set while wanting no added length. Ask about the desired result before assuming that the service label or long reference image settles the request.', '"You want the current short length retained; no extensions are requested."'),
        ('Keep visual dimensions separate', 'Matte concerns shine, sheer concerns coverage, and pink concerns color. None of those words by itself identifies a product system or confirms that a particular service is suitable.', '"Low shine and a visible nail line are the appearance preferences; product selection is still open."'),
        ('Quote the whole option', 'When nail art is charged per nail, give the number of decorated nails and the total including the base service. A lower quantity should not become an unannounced reduction in the agreed design.', '"Two decorated nails add $10 to the $30 base service, for a $40 total."'),
        ('State the exact stage', 'A tidy station may still await required checks. A review is not a promised correction, a consultation request is not a booking, and a health referral does not approve a cosmetic service.', '"Station two is confirmed ready; station three still has incomplete checks."'),
    ],
    scope_note='All clients, salons, prices, sample descriptions, and incidents are fictional. This book teaches workplace English, not nail procedures, product removal, disinfection methods, medical diagnosis, treatment, or legal requirements. Follow professional training, current product instructions, actual salon procedures, applicable local rules, and emergency arrangements. Health concerns belong with an appropriate healthcare professional; cosmetic-service suitability requires its own salon assessment. No example authorizes covering an unexplained concern with product.',
    sources=[
        dict(title='US Food and Drug Administration. Nail Care Products.',
             url='https://www.fda.gov/cosmetics/cosmetic-products/nail-care-products',
             note='Background for product directions, warnings, and the distinction between cosmetic services and treatment of health problems. No medical or chemical procedure is taught.', checked='10 October 2026'),
        dict(title='Occupational Safety and Health Administration. Health Hazards in Nail Salons.',
             url='https://www.osha.gov/nail-salons',
             note='Context for chemical, biological, and ergonomic concerns and the need for actual workplace checks. The readiness dialogue does not supply disinfection instructions.', checked='10 October 2026'),
        dict(title='OPI. How to Shape Nails.',
             url='https://www.opi.com/blog/nail-care/how-to-shape-nails',
             note='Manufacturer vocabulary for visible shape distinctions such as almond, square, and squoval. The book compares appearances and does not reproduce shaping steps or durability claims.', checked='10 October 2026'),
        dict(title='Creative Nail Design. Troubleshooting and FAQs: PLEXIGEL Q&A.',
             url='https://www.cnd.com/pages/troubleshooting-faqs',
             note='The linked manufacturer FAQ distinguishes enhancement uses and product-dependent removal. This book teaches terminology without endorsing a product or reproducing application instructions.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying the service and the intended length',
    scene='The picture is long; the request is short',
    skill='Clarify the desired length before treating an ambiguous service label or reference photograph as an instruction.',
    brief='Client Zoe booked an overlay but calls the appointment a full set when speaking to technician Lin. Zoe points to a long reference image, then explains that the current short length should be kept. No work has begun. Lin clarifies that the intended discussion is a natural-nail overlay without adding length, not automatically extensions. The image is a reference for the look, not permission to copy its length. Product choice, any further design details, and suitability still need the normal consultation.',
    cast='Zoe | Client\nLin | Nail technician',
    culture=('Check the meaning without correcting the person', 'Clients often learn service words from friends, menus, or social media, where the same label may be used differently. Ask what result they want, explain the relevant distinction plainly, and avoid making the client feel that knowing the salon vocabulary was a condition of asking.'),
    a='''What length does Zoe want? | The current short length retained | The full length in the photograph | A longer extension on every nail | An unspecified amount added | Zoe explicitly wants the existing short length rather than the long reference.
What was booked? | An overlay | A confirmed extension service | A removal appointment only | A completed full set | The booking says overlay even though Zoe uses another label in conversation.
What does the reference image authorize by itself? | No automatic length change | Extensions on every nail | Any product the technician chooses | A guaranteed exact match | An image starts the discussion but does not replace explicit agreement about length.''',
    vocabulary='''natural nail | Client's own nail rather than an added enhancement. | identify the natural nail
nail plate | Hard visible part of the natural nail. | refer to the nail plate
nail bed | Tissue beneath the nail plate. | distinguish nail bed and plate
free edge | Part of the nail extending beyond its attachment at the fingertip. | discuss the free edge
overlay | Coating over a nail surface; the exact service needs clarification. | clarify the overlay
natural-nail overlay | Coating applied over the existing natural nail without necessarily adding length. | discuss a natural-nail overlay
extension | Added length beyond the existing natural nail. | confirm whether extensions are wanted
enhancement | Added material used to change nail appearance or structure. | clarify the enhancement
full set | Common service label whose intended scope must be confirmed. | clarify the full-set request
tip | Preformed component used in some nail-extension services. | identify an extension tip
form | Temporary support used in some sculpted-enhancement services. | distinguish a form from a tip
builder gel | Gel product category used to create enhancement structure. | discuss builder gel terminology
acrylic | Common salon term for liquid-and-powder enhancement systems. | clarify the acrylic service
gel polish | Light-cured color-coating category, distinct from all enhancement services. | distinguish gel polish
lacquer | Conventional nail-polish category, distinct from gel polish. | identify nail lacquer
service label | Name used on a booking or menu. | clarify the service label
reference image | Picture used to discuss selected visual features. | interpret the reference image
retained length | Existing length the client wants to keep. | confirm retained length
added length | Extra length created by an extension service. | decline added length
current length | Length present before the proposed service begins. | check the current length
length preference | Client's stated choice about how long the result should be. | record the length preference
consultation | Discussion of the request, suitability, and proposed service. | complete the consultation
service scope | Specific work included in the agreed appointment. | confirm the service scope
read-back | Repetition of key details to verify understanding. | give a length read-back''',
    precision='Overlay is a broad coating term, and full set can be used loosely. In this conversation, the client wants a natural-nail overlay at the current short length, with no extensions requested. Confirm the result before relying on either label.',
    precision_extra='A gel-polish color service and a structural enhancement are not interchangeable labels. The desired short length does not select a product system or establish suitability. Keep those decisions within the actual consultation and professional process.',
    phrases='''Clarify the label | When you say full set, do you mean added length?\nAsk about the result | Would you like to keep your current length?\nRefer to the booking | Your booking currently says overlay.\nSeparate image and instruction | The photo shows long nails, but we should confirm your own length preference.\nConfirm the practical choice | You want your current short length retained.\nExplain the proposed term | We are discussing a natural-nail overlay without added length.\nKeep extensions separate | No extensions are requested at this stage.\nAvoid a product assumption | We have not selected the product system yet.\nCheck the visual feature | Which part of the image do you want to use as a reference?\nConfirm before starting | No work has begun, so let us settle the details first.\nAvoid embarrassment | Service names can be used differently; the result you want is what matters.\nDistinguish scope | Adding length would be a different part of the service discussion.\nInvite correction | Please correct me if short does not describe what you mean.\nKeep assessment open | Suitability still needs the normal consultation.\nRead back the request | Current short length, natural-nail overlay discussion, no extensions.\nClose the clarification | The picture does not override your confirmed length preference.''',
    notes='''Keep versus add | Keep preserves the existing length; add proposes an extension.\nFull set | Confirm what the client means instead of treating the label as self-explanatory.\nNatural-nail overlay | This specifies the surface and avoids assuming the overlay includes an extension tip.\nReference only | An image may illustrate one feature without authorizing all of them.\nAt this stage | The current request is clear while product and suitability decisions remain open.\nRead-back | Repeating the agreed length catches a consequential misunderstanding before work starts.''',
    d='''Which question resolves the key ambiguity? | Do you want added length, or your current short length kept? | Which payment method do you prefer? | Shall I copy the longest nail in the picture? | Does full set always mean extensions? | The question directly checks the client's actual length preference rather than assuming the label.
Which summary is accurate? | Natural-nail overlay discussion at current short length, with no extensions requested. | Long extensions confirmed from the image. | Product system selected by the word short. | The reference authorizes an exact copy. | The summary preserves the clarified length and leaves other service decisions open.
Which product statement is supported? | Product selection still needs clarification. | Gel polish and every builder gel are the same. | Acrylic is required whenever a photo is long. | No consultation is needed for short nails. | The case does not select a system or bypass the normal consultation.
Which response avoids blaming the client for terminology? | Service names vary; let us confirm the result you want. | Your booking says overlay, so I will ignore the picture. | Full set means extensions here, so I will add length. | We can copy the photograph now and check your preference afterwards. | The response invites clarification respectfully instead of treating vocabulary knowledge as a prerequisite.''',
    dialogue='''Zoe | I'm here for a full set. I brought this picture, but please don't make them this long. I want to keep my own length.
Lin | Your booking says [[overlay::Overlay is the booked service; the word alone does not authorize extensions or choose a product.]]. Do you want material over your existing nails, without adding length beyond them?
Zoe | Yes, that's what I meant. I heard someone call it a full set and assumed that was the right name.
Lin | That's fine. The [[service label::A service label names an appointment, but checking the desired result resolves differences in how people use it.]] can be used differently. Your short-length preference is more useful than guessing from the name.
Zoe | Good. I like the look in the photograph, but the long nails would get in my way at work.
Lin | We'll use the [[reference image::The image supplies visual ideas but does not replace Zoe's explicit decision to retain short nails.]] to discuss the look, not copy every feature. No extra length is requested.
Zoe | So an overlay and extensions aren't the same thing? I'd like to know what the menu means next time.
Lin | [[Extensions::Extensions add length beyond the existing natural nail, which Zoe has declined in this case.]] add length. Here we're discussing material over the nail you already have, without adding to it.
Zoe | And the hard part I can see is the nail plate? I've heard that called the nail bed too.
Lin | The [[nail plate::The plate is the hard visible nail; the nail bed is the tissue beneath it.]] is the hard visible part. The nail bed is the tissue underneath, so those terms aren't interchangeable.
Zoe | That helps. What about builder gel and gel polish? I thought anything with gel in the name was the same service.
Lin | [[Builder gel::Builder gel is used to create enhancement structure; gel polish names a color-coating category, not an identical service.]] is used for enhancement structure. Gel polish is a color-coating category. We'll discuss which service is appropriate rather than treat them as synonyms.
Zoe | I haven't chosen a material yet. I'd like you to explain the options before we settle on one.
Lin | Certainly. The [[product system::The product system remains unselected even after the length preference has been clarified.]] is still open. Keeping the nails short doesn't answer that question by itself.
Zoe | Please keep that short-length request on the booking. I don't want the picture confusing anyone else who helps today.
Lin | I'll record your [[retained length::Retained length means the existing short length Zoe wants preserved rather than extended.]] clearly, along with no extensions requested. We can then continue with the other design details.
Zoe | Could you repeat the main point before we start? I want to be sure I explained it properly.
Lin | Here's the [[read-back::The read-back lets Zoe verify that her stated preference has not been replaced by the long reference.]]: natural-nail overlay discussion, current short length kept, no extensions. Product and suitability still need consultation.
Zoe | Yes, that's right. I want the look discussed, not the long length copied.
Lin | Understood. That's the [[length preference::The length preference is settled while other service choices remain open and no work has begun.]] we'll work from. Nothing has begun, so we can clarify the remaining choices first.''',
    rehearsal=["Read the booking clarification, stressing keep my own length and without adding length.","Switch roles and read the plate-versus-bed and builder-gel-versus-gel-polish exchanges with the definitions intact.","Complete and check the transfer; retain medium length rather than the short length used in the main dialogue."],
    transfer_title='Clarify another overlay request',
    transfer_setup='A client shows a long reference but wants the existing medium length retained. The discussion is a natural-nail overlay with no extensions requested. Product choice is still open, and no work has begun.',
    transfer='''Technician: "The current ___ length should be retained." | medium | Medium is the existing length the client explicitly wants to keep.
Client: "No ___ are requested." | extensions | The long image does not change the client's no-added-length request.
Technician: "Product choice remains ___." | open | A length preference does not select the product system or establish suitability.
Client: "No work has ___." | begun | Clarification takes place before the service starts in the supplied scenario.'''
))


BOOK['units'].append(unit(
    title='Comparing shape and practical length',
    scene='A shape that fits the working day',
    skill='Compare sample silhouettes and lengths while preserving a practical requirement and avoiding unsupported durability claims.',
    brief='Client Amara likes a long almond sample but needs a short result for keyboard work. Technician Kai also has a short squoval sample, with a straighter free-edge outline and softened corners. The almond sample narrows toward a rounded tip and is visibly longer. Amara chooses the short squoval appearance for discussion. No method, exact measurement, or guarantee against breakage or discomfort is established. Kai must distinguish the visible comparison from a promise about how either shape will perform on the actual nails.',
    cast='Amara | Client\nKai | Nail technician',
    culture=('A practical preference is not a lesser choice', 'Avoid praising one shape as universally better or more professional. Ask how the client uses their hands, compare the supplied samples neutrally, and preserve the stated length limit. The client should not feel pressured to copy a dramatic display sample.'),
    a='''What practical requirement does Amara state? | A short result for keyboard work | The longest possible extension | A guaranteed unbreakable shape | A specified filing method | The client wants short nails because of the way they use a keyboard.
Which sample is short in this case? | The squoval sample | The almond sample | Both are described as long | Neither sample has a length | The brief explicitly contrasts a short squoval sample with a long almond sample.
What does Amara choose for discussion? | The short squoval appearance | A guaranteed damage-proof result | The exact long almond sample | An unassessed extension method | The choice concerns the sample appearance, not a technique or durability guarantee.''',
    vocabulary='''silhouette | Outer visible outline of a nail shape. | compare the silhouettes
almond | Shape narrowing toward a rounded, almond-like tip. | describe the almond sample
squoval | Shape combining a straighter edge with softened corners. | explain the squoval outline
square | Shape with a straighter free edge and more defined corners. | identify the square shape
round | Shape with a rounded free-edge outline. | compare a round shape
oval | Elongated rounded shape without a sharply pointed tip. | describe an oval outline
stiletto | Shape narrowing to a pronounced pointed tip. | identify the stiletto sample
coffin | Tapered shape ending in a comparatively flat tip. | describe the coffin silhouette
tapered sides | Side outlines that narrow toward the tip. | compare tapered sides
rounded tip | Tip with a curved rather than sharp endpoint. | identify the rounded tip
softened corners | Corners with a gentler rounded outline. | describe softened corners
straight edge | Outline appearing relatively flat across the end. | identify the straight edge
sample display | Set of examples used to compare visible choices. | use the sample display
length reference | Agreed example or measurement used to discuss length. | confirm a length reference
practical requirement | Everyday need affecting the client's preference. | record the practical requirement
keyboard work | Work involving regular typing or use of keys. | discuss keyboard work
daily use | How the client normally uses their hands. | ask about daily use
preferred outline | Shape the client selects for discussion. | confirm the preferred outline
symmetry | Visual balance between corresponding sides or nails. | discuss symmetry
proportion | Relationship between dimensions such as length and width. | compare proportions
breakage | Breaking of a nail or enhancement, not prevented by a verbal guarantee. | avoid a breakage guarantee
comfort expectation | What the client hopes will feel manageable in use. | clarify the comfort expectation
measurement | Specific quantified length, not established by a broad label alone. | agree on a measurement
suitability assessment | Professional review of whether the proposed service fits the actual situation. | complete a suitability assessment''',
    precision='This comparison concerns the two supplied samples: long almond and short squoval. Squoval describes an outline, not an absolute length in every salon. The selected short appearance still needs an agreed length reference and normal assessment.',
    precision_extra='A client can prefer short nails for keyboard work without proving that every short shape will be comfortable or resistant to breakage. Describe appearance and practical priorities; do not convert a preference into a performance guarantee.',
    phrases='''Ask about daily use | What length feels practical for your keyboard work?\nAcknowledge the attraction | You like the almond outline in this sample.\nIdentify the conflict | This particular almond sample is longer than your stated preference.\nDescribe the alternative | The squoval sample shown here is short.\nExplain the corners | It has a straighter edge with softened corners.\nExplain the almond tip | The almond sample narrows toward a rounded tip.\nSeparate shape and length | Let us compare the outline and the length as two details.\nPreserve the practical limit | Your priority is a short result.\nAvoid a durability promise | I cannot promise that either shape prevents breakage.\nAvoid a comfort guarantee | The sample alone cannot establish how it will feel in daily use.\nCheck the chosen appearance | Is the short squoval sample closer to what you want?\nLeave the method open | We have not agreed on a technical method yet.\nConfirm a reference | We still need a clear length reference for your actual nails.\nKeep the comparison neutral | The shapes look different; neither is automatically better for everyone.\nRead back the priority | Short length for keyboard work, with the squoval appearance preferred.\nConfirm before proceeding | We will settle the remaining details before starting.''',
    notes='''Shape versus length | Almond and squoval describe outlines; long and short describe relative length.\nThis sample | Limits the claim to the example being compared rather than every version of the shape.\nCloser to | Expresses preference without promising an exact photographic copy.\nNeed versus guarantee | A practical need informs assessment but does not establish performance.\nRounded versus round | A rounded tip can appear within an almond shape; round is also a whole-shape label.\nBefore starting | Length and method questions should be resolved before an irreversible change.''',
    d='''Which comparison is accurate? | This almond sample is long and tapered; this squoval sample is short with softened corners. | Every almond nail has the same length. | Squoval guarantees no breakage. | The short sample proves every service is suitable. | The comparison stays with the supplied visible features and avoids universal claims.
Which question best clarifies the next detail? | What length reference shall we agree on for your actual nails? | Shall I assume the long sample overrides your work needs? | Do you accept a guaranteed unbreakable result? | Can we skip the consultation because the sample is short? | The exact practical length remains to be clarified on the client's actual nails.
Which promise is unsupported? | This shape will never cause discomfort or break. | The squoval sample has softened corners. | You prefer short length for keyboard work. | No method has been agreed yet. | Neither comfort nor breakage prevention is established by the visual sample.
What does the selected sample establish? | A preferred appearance for discussion | An exact universal measurement | An approved technical procedure | A guarantee for every daily task | The client selects the visible direction while assessment and exact details remain open.''',
    dialogue='''Amara | I like this almond sample, but it looks much longer than I could manage at work. I spend most of the day using a keyboard.
Kai | The [[practical requirement::Practical requirement is the client's need for short nails during keyboard work, which should remain central to the comparison.]] is a short result, then. We can compare the shape you like without assuming you want the full length of this display sample.
Amara | Yes. I like the tapered shape, but that length would make typing awkward for me.
Kai | The [[almond::Almond identifies the sample's narrowing outline and rounded tip, separate from the long length shown in this particular example.]] outline narrows toward a rounded tip. In this particular sample, that outline is shown at a visibly longer length.
Amara | What is the name of the shorter one beside it? The end looks straighter, but the corners do not look sharply square.
Kai | That is the [[squoval::Squoval describes the straighter edge with softened corners shown in the shorter alternative sample.]] sample. It combines a straighter end with softened corners, and the example here is short.
Amara | I think the shorter one is closer. Could we use that shape without copying the long sample?
Kai | Certainly. We are comparing the [[silhouettes::Silhouettes are the visible outer outlines, not instructions about which product or technique must be used.]] and lengths first. The technical method and the appropriate service still need their own discussion.
Amara | The shorter one seems less likely to get in my way. Does that mean it will definitely be comfortable when I type?
Kai | I cannot give a [[comfort guarantee::Comfort guarantee would promise a daily-use outcome that the sample alone cannot establish for this client.]] from a sample. Your work needs help guide the consultation, but they do not prove how a particular result will feel on your actual nails.
Amara | Does squoval mean it won't break? A friend told me it was the strongest shape.
Kai | A [[breakage::Breakage is a possible outcome that cannot be ruled out merely by choosing a named shape or looking at a display.]] promise like that would be too strong. We can discuss your preferences and the assessment without claiming a shape is unbreakable.
Amara | Then let us use the short squoval as the appearance I prefer. I do not want the long almond length copied.
Kai | I will record the [[preferred outline::Preferred outline is the squoval appearance Amara chooses for discussion, while rejecting the long sample's length.]] and your short-length priority together. That keeps the visual choice connected to the practical reason you gave.
Amara | How short do you mean on my nails? Could you show me before you start?
Kai | Yes, we still need an agreed [[length reference::Length reference is the specific example or measurement to confirm on the actual nails, beyond the broad word short.]] for your actual nails. The word short is useful, but it should not be the only detail in the final agreement.
Amara | Good. Please keep the softened corners in the discussion too. That is part of what I like about the second sample.
Kai | I will. [[Softened corners::Softened corners distinguish the chosen squoval appearance from a more sharply square outline in this comparison.]] are part of the visible shape you prefer, separate from the exact length we still need to confirm.
Amara | Yes, short with those softer corners. Let's check the actual length together.
Kai | Correct. The [[suitability assessment::Suitability assessment remains part of the normal professional process; selecting an appearance does not establish a method or guaranteed performance.]] and remaining details still matter. We have a clear direction: short length for keyboard work, with the squoval appearance preferred.''',
    rehearsal=["Read the comparison using almond, squoval, rounded tip, and softened corners.","Switch roles. Read the keyboard-work request without turning the client's preference into a guarantee against breakage.","Complete and check the round-shape transfer, then read the shape and length as separate choices."],
    transfer_title='Separate shape from a guarantee',
    transfer_setup='A client compares a long oval sample with a short round sample. They choose the short round appearance for keyboard work. No exact measurement or guarantee against breakage is agreed.',
    transfer='''Technician: "The preferred shape is ___." | round | The client chooses the round appearance from the two supplied samples.
Client: "My practical priority is ___ length." | short | Short length is the stated preference for keyboard work.
Technician: "The exact ___ still needs agreement." | measurement | The broad length preference does not supply a specific agreed measurement.
Client: "No guarantee against ___ has been made." | breakage | The visual choice does not establish that the nails cannot break.'''
))


BOOK['units'].append(unit(
    title='Explaining color, coverage, and finish',
    scene='Sheer pink, without the shine',
    skill='Separate color, coverage, and finish while leaving an unspecified product system open for consultation.',
    brief='Client Dana asks technician Noor for matte pink but points to a sheer glossy swatch. Dana explains that the desired result has low shine while the natural nail line remains visible. The selected swatch illustrates the preferred pink color and transparency, but not the preferred finish. The booking does not specify conventional lacquer or gel polish. Noor records the appearance as sheer pink with a low-shine finish, leaving product selection and suitability open rather than assuming the swatch chooses the whole service.',
    cast='Dana | Client\nNoor | Nail technician',
    culture=('Separate the details kindly', 'A client is not being inconsistent when one sample illustrates only part of a request. Ask which features they like and translate the answer into separate appearance choices. Avoid overwhelming the client with product names before the desired color, coverage, and finish are clear.'),
    a='''Which appearance does Dana want? | Sheer pink with low shine | Opaque pink with high gloss | Clear colorless polish with glitter | Every feature of the glossy swatch | Dana wants the pink and transparency of the swatch but a lower-shine finish.
What should remain visible? | The natural nail line | Only a solid opaque coating | A confirmed product label | An extension form | The client specifically wants the nail line visible through the color.
Which product category is booked? | Neither lacquer nor gel polish is specified | Gel polish is confirmed | Lacquer is confirmed | Both are automatically selected | The booking leaves the product category unspecified, so it requires clarification.''',
    vocabulary='''swatch | Sample showing a color or finish for comparison. | compare the swatch
shade | Particular variation of a color. | choose a pink shade
hue | Basic color family, such as pink or red. | describe the hue
undertone | Subtle underlying color character. | compare undertones
coverage | Degree to which the applied color conceals what is beneath it. | clarify the coverage
sheer | Translucent enough for some underlying nail detail to remain visible. | request sheer coverage
semi-sheer | Partially translucent, between very sheer and fully opaque. | compare semi-sheer coverage
opaque | Concealing the underlying nail rather than allowing it to show through. | distinguish opaque coverage
translucency | Degree to which light and underlying detail show through. | describe translucency
nail line | Visible boundary toward the nail's free edge, used here as an appearance reference. | retain a visible nail line
finish | Surface appearance, including the level of shine. | clarify the finish
matte | Low-shine or non-glossy surface appearance. | request a matte finish
glossy | Shiny surface appearance. | identify the glossy swatch
satin | Soft-sheen appearance between matte and high gloss in a given range. | compare a satin finish
sheen | Degree of reflected shine. | describe the sheen
shimmer | Fine reflective sparkle within a color effect. | identify shimmer
glitter | Visible reflective particles used for a decorative effect. | distinguish glitter from gloss
metallic | Appearance resembling reflective metal. | describe a metallic effect
pearlescent | Soft luminous effect resembling the sheen of a pearl. | compare a pearlescent effect
top coat | Finishing coating whose properties depend on the product system. | discuss the top coat
color coat | Layer providing the selected color effect. | identify the color coat
product system | Compatible set of products and procedures for a service. | confirm the product system
appearance specification | Separate agreed details of color, coverage, and finish. | record the appearance specification
curing lamp | Light source specified for curing a compatible gel system; not selected by wattage alone. | verify the curing lamp''',
    precision='Matte and sheer answer different questions. Matte concerns shine; sheer concerns how much underlying nail remains visible. The client can request both. The glossy swatch illustrates the preferred color and coverage, not the agreed final shine.',
    precision_extra='A swatch is not a product-selection shortcut. The booking does not identify lacquer or gel polish, and the appearance request does not determine compatibility, suitability, or application steps. Those details remain within the actual consultation.',
    phrases='''Separate the choices | Let us check color, coverage, and finish one at a time.\nConfirm the color | Pink is the color you prefer.\nAsk about visibility | Do you want the natural nail line to remain visible?\nExplain sheer | Sheer coverage allows some nail detail to show through.\nExplain opaque | Opaque coverage conceals the underlying nail.\nExplain matte | Matte describes a low-shine finish.\nDescribe the swatch | This swatch is sheer and glossy.\nIdentify the mismatch | You like its pink color and coverage, but not its shine.\nConfirm the combined request | You want sheer pink with a low-shine finish.\nAvoid a false conflict | Sheer and matte describe different features, so they are not opposites.\nClarify the booking | The booking does not specify lacquer or gel polish.\nKeep product choice open | We still need to discuss the product system.\nAvoid copying everything | Selecting this swatch does not select every feature it shows.\nAsk for a read-back | Is visible nail line and low shine the right summary?\nAvoid an application promise | We have not confirmed the product or method yet.\nClose the appearance discussion | The appearance is clear; product selection remains open.''',
    notes='''Coverage versus finish | Coverage concerns concealment; finish concerns surface appearance.\nSheer versus clear | Sheer color can be tinted while still allowing underlying detail to show.\nMatte versus opaque | Low shine does not necessarily mean full concealment of the nail.\nBut not | This phrase selects some sample features while explicitly rejecting another.\nUnspecified | An absent product category is a question to clarify, not permission to guess.\nOne at a time | Separating dimensions reduces confusion without turning the conversation into a lecture.''',
    d='''Which statement explains the client's request? | Sheer concerns visibility through the color; matte concerns shine. | Sheer always means glossy. | Matte always means opaque. | Pink automatically means gel polish. | Coverage and finish are independent appearance dimensions in this consultation.
Which swatch feature is not wanted? | Its glossy finish | Its pink color | Its sheer coverage | Its visible underlying detail | The client likes the color and transparency but asks for low shine.
Which record is accurate? | Sheer pink, low shine, product category not yet specified. | Glossy opaque pink, gel polish confirmed. | Colorless glitter, lacquer confirmed. | Every swatch feature accepted without discussion. | The record preserves the three appearance details and unresolved product choice.
Which question best checks coverage? | Do you want the nail line to show through? | Would you like a shinier surface? | Do you prefer warm pink or cool pink? | Would you like a fine shimmer in the color? | Visibility of the nail line directly clarifies the desired coverage.''',
    dialogue='''Dana | I want matte pink, like this sample. I like seeing a little of the nail through it, but I don't want it so shiny.
Noor | Let's check [[coverage::Coverage concerns how much underlying nail detail is concealed, not the amount of reflected shine.]] first. Do you want the natural nail line to show through the pink?
Dana | Yes. I want some color, just not a solid block that hides the nail underneath.
Noor | That's [[sheer::Sheer coverage allows some underlying detail to show through a tinted color.]] coverage. It describes the see-through quality, not the shine on top.
Dana | Oh, I thought sheer meant shiny. The sheer samples I looked at all seemed glossy.
Noor | Those samples combine two features. Their [[finish::Finish describes the surface appearance, which can be discussed separately from coverage.]] is glossy, but their coverage is sheer.
Dana | Then this pink is right, and the transparency is right. It's the shiny surface I'd like changed.
Noor | I'll record [[matte::Matte identifies Dana's requested low-shine surface, unlike the glossy reference.]] as the finish preference. That keeps the low-shine request separate from the color.
Dana | What would opaque look like? Is that another word for dark pink, or does it mean something else?
Noor | [[Opaque::Opaque means the underlying nail is concealed; it does not simply mean the color is dark.]] means you wouldn't see the underlying nail through the color. Pale colors can be opaque too.
Dana | Then I don't mean opaque. Please keep the nail line visible even though I don't want a glossy finish.
Noor | Yes. The [[nail line::The nail line is the underlying detail Dana wants to retain through the sheer pink coverage.]] stays in the appearance description. Low shine doesn't mean it has to be hidden.
Dana | Have I already booked gel polish? I don't remember choosing between that and ordinary polish on the form.
Noor | No [[product category::The booking specifies neither lacquer nor gel polish, so the appearance request cannot settle that choice.]] is listed. We should discuss lacquer and gel polish separately from this swatch.
Dana | Could you explain the difference before I choose? I don't want to agree just because I pointed to this one.
Noor | Of course. We'll discuss the [[product system::The product system is still to be selected through consultation, not inferred from the chosen color sample.]] and the service involved. The sample has only helped clarify the look.
Dana | So my request is pink, slightly see-through, and not shiny. Is that the right way to put it?
Noor | Yes. That's a clear [[appearance specification::The appearance specification records color, coverage, and finish together without selecting application products.]]: sheer pink with low shine.
Dana | Great. Keep those three points together, please. I'd be disappointed if matte turned into a completely solid pink.
Noor | I'll note the [[sample mismatch::The mismatch is limited to the sample's gloss, not its pink color or sheer coverage.]] too: you like this swatch's color and transparency, but not its glossy surface.''',
    rehearsal=["Read the swatch dialogue. Stress sheer for coverage and matte for shine.","Switch roles and read the opaque explanation; preserve the distinction between pale color and see-through coverage.","Complete and check the blue-color transfer. Read color, coverage, finish, and the unresolved product category separately."],
    transfer_title='Decode another color request',
    transfer_setup='A client wants opaque blue with a glossy finish. They do not want the nail line visible. The booking leaves lacquer versus gel polish unspecified.',
    transfer='''Technician: "The requested color is ___." | blue | Blue is the chosen color family in this new scenario.
Client: "I want ___ coverage." | opaque | Opaque matches the wish to conceal the underlying nail line.
Technician: "The requested finish is ___." | glossy | Glossy specifies the chosen shine independently of coverage.
Reception: "The product category remains ___." | unspecified | The appearance request does not choose lacquer or gel polish.'''
))


BOOK['units'].append(unit(
    title='Agreeing on nail art and a complete quote',
    scene='Two accent nails within forty dollars',
    skill='Calculate a per-nail addition, offer complete priced alternatives, and confirm quantity and placement before starting.',
    brief='Client Ben wants simple line art on four nails but has a total limit of $40. Technician Rosa explains this fictional menu: the base service is $30, simple line art is $5 per nail, and no other charges apply in the exercise. Four decorated nails would cost $50. Two decorated nails would cost $40, or the base service alone would cost $30. Ben chooses two decorated nails, one ring fingernail on each hand. Rosa confirms that two means the total across both hands, not two on each hand.',
    cast='Ben | Client\nRosa | Nail technician',
    culture=('Make the quantity visible in the price', 'Per-nail charges can be misunderstood as per-hand or whole-set prices. State the quantity, the additional amount, and the complete total together. Offering a smaller design within a budget is helpful only if the client explicitly chooses the change.'),
    a='''What would four decorated nails cost in total? | $50 | $40 | $20 | $35 | Four nails at five dollars add twenty dollars to the thirty-dollar base.
Which option meets the $40 limit with art? | Two decorated nails plus the base service | Four decorated nails plus the base service | Two decorated nails on each hand | The art charge alone without the base | Two nails add ten dollars, making the complete total forty dollars.
Which placement is selected? | One ring fingernail on each hand | Two nails on each hand | Four nails on the left hand | All ten nails | One ring fingernail on each hand gives the agreed total of two decorated nails.''',
    vocabulary='''nail art | Decorative design added to the nail appearance. | specify the nail art
line art | Design formed primarily with lines. | quote simple line art
accent nail | Nail given a distinct decorative treatment from the others. | select an accent nail
decorated nail | Nail included in the agreed art quantity. | count decorated nails
plain color | Color without the additional decorative design. | choose plain color
placement | Specific nail or area where the design appears. | confirm design placement
orientation | Direction in which a design faces. | clarify the orientation
motif | Repeated or distinct decorative element. | choose a motif
stripe | Long narrow decorative line or band. | describe a stripe
dot detail | Decorative element made of small dots. | clarify the dot detail
negative space | Deliberately uncovered area within a design. | identify negative space
French tip | Design emphasizing a contrasting appearance at the nail tip. | discuss a French-tip design
ombre | Gradual visual transition between colors or tones. | describe an ombre effect
per-nail charge | Price applying to each decorated nail individually. | explain the per-nail charge
base price | Cost of the underlying service before art additions. | state the base price
art subtotal | Total charge for the decorative additions alone. | calculate the art subtotal
complete quote | Total price for the specifically described option. | give a complete quote
budget limit | Maximum total the client agrees to spend. | respect the budget limit
smile line | Curved boundary between a contrasting French tip and the rest of the nail design. | describe a crisp smile line
ring fingernail | Nail on the finger between the middle and little fingers. | identify the ring fingernail
each hand | Separately referring to the left and right hands. | confirm one on each hand
both hands | Referring to the two hands together. | total across both hands
design approval | Agreement to the specified design and placement. | obtain design approval
additional charge | Amount added beyond the base service. | state the additional charge''',
    precision='Four decorated nails cost $20 in art charges, making $50 with the base service. Two decorated nails cost $10 in art charges, making $40 total. Two on each hand would be four in total and exceed the stated budget.',
    precision_extra='The accepted option is two decorated nails in total, specifically one ring fingernail on each hand. Do not quietly reduce the original four-nail request or increase the selected two-nail version. Quantity and placement both need agreement.',
    phrases='''Ask about the limit | Is $40 your total budget, including the base service?\nState the base price | The base service is $30.\nExplain the unit charge | Simple line art is $5 per decorated nail.\nCalculate the first option | Four decorated nails add $20, making $50 total.\nOffer the smaller option | Two decorated nails add $10, making $40 total.\nPreserve the plain option | The base service alone is $30.\nKeep totals complete | These totals include the base service and the stated art quantity.\nAsk for a choice | Would you prefer two decorated nails or the base service alone?\nConfirm the reduction | You are choosing two instead of the original four.\nClarify both hands | Do you mean two in total across both hands?\nCheck placement | Which two nails would you like decorated?\nName the fingers | One ring fingernail on each hand gives two in total.\nAvoid silent additions | We will confirm any additional art before changing the price.\nRead back the design | Simple line art on the two ring fingernails.\nRead back the total | The agreed total is $40.\nConfirm before starting | Let us settle quantity, placement, and price before beginning.''',
    notes='''Per versus total | Per nail gives a unit charge; total includes all selected nails and the base service.\nEach versus both | One on each hand equals two across both hands.\nSubtotal | The art subtotal excludes the base price and is not the amount for the entire service.\nInstead of | This marks an accepted change from four decorated nails to two.\nUp to | A budget up to $40 is a limit, not permission to exceed it with unmentioned additions.\nPlacement | Agreeing on two nails still leaves the specific fingers to be confirmed.''',
    d='''Which quote is complete? | Two decorated nails at $10 plus the $30 base: $40 total. | Two nails cost $10, with the base omitted. | Four nails cost $40 including the base. | Two nails on each hand cost $40 total. | The correct quote states quantity, art subtotal, base price, and final total.
What does one ring fingernail on each hand mean? | Two decorated nails in total | Four decorated nails in total | One decorated nail in total | Every fingernail on both hands | One selected finger on each of two hands gives two decorated nails.
Which response wrongly assumes agreement? | I reduced your four-nail design without asking so the bill fits. | Two decorated nails would total $40. | The base service alone is $30. | Which two nails would you like decorated? | A budget constraint does not authorize silently changing the requested design quantity.
Which change would exceed the accepted quantity? | Decorating two nails on each hand | Decorating one ring fingernail per hand | Keeping the art subtotal at $10 | Leaving the other nails without this art | Two per hand produces four decorated nails rather than the accepted two.''',
    dialogue='''Ben | I would like the simple line design on four nails, but I need to keep the whole appointment at forty dollars. Does that work?
Rosa | Let me give you the [[complete quote::Complete quote includes the base service and all selected art, so the client can compare the actual total with the budget.]] before we choose. The base service is thirty dollars, and simple line art is five dollars for each decorated nail.
Ben | I had thought five dollars meant the whole design, not five for every nail. What would the four-nail version come to?
Rosa | The [[per-nail charge::Per-nail charge applies five dollars to each of four nails, creating twenty dollars in art charges rather than one five-dollar fee.]] makes four decorated nails twenty dollars extra. Added to the thirty-dollar base service, that gives a total of fifty dollars.
Ben | That is more than I can spend today. Is there a smaller version that stays within forty without changing the base service?
Rosa | Two decorated nails would have an [[art subtotal::Art subtotal is ten dollars for two nails and must be added to the thirty-dollar base to reach the complete forty-dollar price.]] of ten dollars. With the base service, the complete total would be forty dollars.
Ben | And if I decide not to have any art at all, would the base service still be available at thirty?
Rosa | Yes. The [[base price::Base price remains thirty dollars for the service without the optional line art, giving a second option within the client's limit.]] is thirty dollars without the art. Your two choices within the limit are the base alone or the base with two decorated nails.
Ben | Let's do two with the line design, then. I can manage forty, but not fifty today.
Rosa | I will confirm that [[quantity reduction::Quantity reduction is the client's explicit choice to move from four decorated nails to two, not a silent change made by the technician.]] with you: two decorated nails instead of four, for forty dollars in total.
Ben | When you say two, is that two on each hand or two altogether? I want to make sure I am counting the same way.
Rosa | Two altogether, across [[both hands::Both hands means the combined total for left and right, so two across both hands is not two on each hand.]]. Two on each hand would be four nails and would return the total to fifty dollars.
Ben | Then one on each hand sounds right. I would like the ring fingernails decorated, with the other nails left without that line design.
Rosa | That gives one [[accent nail::Accent nail is the individually decorated nail, here one ring fingernail on each hand for two in total.]] on each hand. I will specify the two ring fingernails so the placement is not left to an assumption.
Ben | Yes, these two. Please leave the others plain; I like the design better on the ring fingers.
Rosa | The [[placement::Placement identifies the exact nails receiving the art, which is a separate detail from the overall quantity of two.]] is now clear: the ring fingernail on your left hand and the ring fingernail on your right.
Ben | Good. And forty is still the complete total, not forty plus another amount for selecting those fingers?
Rosa | Correct. Your [[budget limit::Budget limit is forty dollars for the entire selected service, and the confirmed option meets it with no other charges in this fictional menu.]] is met by this option. There are no other charges in this comparison, and the two-nail art total remains ten dollars.
Ben | That's agreed: both ring fingernails, forty dollars altogether. No extra art today.
Rosa | I have your [[design approval::Design approval covers the specified two ring fingernails, simple line art, and forty-dollar total, not further unrequested additions.]] for that exact option. We will confirm any later change before altering the quantity, placement, or price, rather than adding something without asking.''',
    rehearsal=["Read the quotation aloud: $30 base, $5 per nail, four nails $50 total, two nails $40 total.","Switch roles for the placement exchange. Say one on each hand and two altogether distinctly.","Complete the new $35-plus-art transfer, check the calculation, and read the complete $43 total rather than only the art subtotal."],
    transfer_title='Recalculate another art quote',
    transfer_setup='A base service costs $35. Art costs $4 per nail, with no other charges. The client has a $43 limit and chooses one decorated nail on each hand.',
    transfer='''Technician: "The selected quantity is ___ nails." | two | One decorated nail on each of two hands gives two nails total.
Client: "The art subtotal is ___ dollars." | eight | Two nails multiplied by four dollars gives eight dollars for art.
Technician: "The complete total is ___ dollars." | forty-three | The thirty-five-dollar base plus eight dollars of art totals forty-three.
Client: "That total meets my budget ___." | limit | The total equals the stated maximum without exceeding it.'''
))


BOOK['units'].append(unit(
    title='Responding to discomfort and uncertain nail concerns',
    scene='Do not cover an unexplained concern',
    skill='Pause a cosmetic request, preserve the client report, and distinguish healthcare referral from salon service approval.',
    brief='Before any service starts, client Elena reports unexplained tenderness beside one nail. Elena wants technician Dev to cover the area with product for an event. Dev pauses that request and recommends assessment by an appropriate healthcare professional without naming a condition or suggesting treatment. Elena agrees to seek appropriate advice. The salon must separately assess whether a cosmetic service is suitable. No product has been applied, no cause is established, and the healthcare referral does not guarantee that the salon will approve the requested service.',
    cast='Elena | Client\nDev | Nail technician',
    culture=('A clear boundary can still be kind', 'Acknowledge why the event matters without making appearance more important than an unexplained concern. Use the client\'s own description, state what you cannot establish, and explain the next step calmly. A referral should not sound like either a diagnosis or a promise of later approval.'),
    a='''What does Elena report? | Unexplained tenderness beside one nail | A confirmed medical diagnosis | A reaction after today's product application | A completed cosmetic repair | The client reports tenderness before any service, with no established cause.
What happens to the covering request? | It is paused | Product is applied immediately | It is approved after a guess | It becomes a treatment prescription | Dev pauses the cosmetic request rather than covering an unexplained concern.
What does referral establish? | A route to appropriate health assessment, not service approval | A guarantee of a manicure | A confirmed cause | Permission to conceal the area | Referral addresses the health concern while cosmetic-service suitability remains a separate decision.''',
    vocabulary='''tenderness | Reported soreness or sensitivity, particularly with touch or pressure. | report tenderness
nail fold | Skin bordering the nail plate. | identify the nail-fold area
adjacent skin | Skin beside the nail or another specified area. | describe adjacent skin
redness | Visible red appearance, if actually observed or reported. | record reported redness
swelling | Enlargement or puffiness, if actually observed or reported. | describe reported swelling
irritation | Uncomfortable response that should not be assigned a cause without assessment. | report possible irritation
allergic reaction | Health response requiring appropriate assessment, not a salon guess. | refer a suspected allergic reaction
sensitivity | Reported heightened response to touch or a substance. | clarify reported sensitivity
unexplained concern | Concern whose cause has not been established. | acknowledge an unexplained concern
symptom description | Client's words about what they experience. | preserve the symptom description
affected area | Specific location involved in the reported concern. | identify the affected area
onset | Time when the reported concern began. | clarify reported onset
pre-existing concern | Concern present before the proposed service begins. | record a pre-existing concern
cosmetic request | Request to alter appearance, distinct from healthcare treatment. | pause the cosmetic request
covering product | Product proposed to conceal an area or change its appearance. | decline to apply a covering product
service pause | Temporary stop pending the appropriate next steps. | maintain the service pause
healthcare professional | Appropriately qualified person who assesses health concerns. | refer to a healthcare professional
referral | Direction to an appropriate professional or service for further assessment. | explain the referral
diagnosis | Identification of a health condition through appropriate clinical assessment. | avoid giving a diagnosis
treatment advice | Recommendation intended to address a health condition. | avoid unsupported treatment advice
cosmetic suitability | Whether the proposed cosmetic service is appropriate after assessment. | assess cosmetic suitability
service approval | Salon decision authorizing a specific service under its process. | distinguish service approval
event deadline | Client's preferred timing because of an upcoming event. | acknowledge the event deadline
factual note | Record limited to the reported or observed facts and agreed actions. | make a factual note''',
    precision='Tenderness is the reported concern, not a diagnosis. It was present before any service began. The request to cover it is paused, with no product applied. Refer the health question without naming a cause or recommending treatment.',
    precision_extra='Healthcare assessment and salon service approval answer different questions. A referral does not guarantee that a cosmetic service will be suitable or approved afterward. Keep the event deadline, health concern, and unapproved service request distinct.',
    phrases='''Acknowledge the concern | Thank you for telling me about the tenderness.\nClarify the location | You are describing the area beside this nail.\nState the timing | This was reported before any service began.\nPause the request | I will pause the request to cover that area with product.\nAvoid a diagnosis | I cannot determine what is causing the tenderness.\nRefer appropriately | Please have the concern assessed by an appropriate healthcare professional.\nAvoid treatment advice | I cannot recommend a treatment for an unexplained health concern.\nAcknowledge the event | I understand why you wanted a cosmetic result for the event.\nKeep the boundary | The event does not establish that applying product is suitable.\nState what has not happened | No product has been applied.\nSeparate the decisions | The salon must assess cosmetic suitability separately.\nAvoid a future guarantee | The referral does not guarantee service approval afterward.\nPreserve the client's words | I will record tenderness beside one nail, without adding a condition name.\nConfirm the next step | You will seek appropriate healthcare advice about the concern.\nKeep the request pending | The cosmetic request remains paused.\nClose factually | No cause is established and no covering service is approved.''',
    notes='''Beside versus on | Beside locates the concern next to the nail rather than automatically on the nail plate.\nReported versus diagnosed | A client report supplies information but does not identify a medical condition.\nBefore | The sequence prevents the record from incorrectly attributing the concern to today's service.\nPause versus treat | Pausing a request does not provide treatment for the underlying concern.\nReferral versus clearance | Referral seeks appropriate assessment and does not itself approve a cosmetic service.\nEvent pressure | A deadline explains the client's preference but does not replace suitability assessment.''',
    d='''Which note stays factual? | Tenderness beside one nail reported before service; covering request paused. | Infection confirmed by the technician. | Today's product caused the condition. | Product applied to solve the concern. | The correct note preserves location, timing, and action without diagnosis or invented causation.
Which response overpromises? | After the referral, we will definitely perform the requested service. | The cosmetic request remains paused. | No product has been applied. | The cause has not been established. | Referral does not guarantee that the salon will later approve cosmetic work.
Which next step addresses the health question? | Assessment by an appropriate healthcare professional | Covering the area for the event | Selecting a color to conceal it | Guessing from an unrelated photograph | The unexplained health concern needs appropriate assessment rather than cosmetic concealment.
Which distinction matters? | Healthcare assessment and cosmetic-service suitability are separate decisions. | A client deadline equals service approval. | Tenderness always identifies one condition. | A referral is a treatment prescription. | The salon must separately assess the cosmetic service instead of treating referral as approval.''',
    dialogue='''Elena | Before we start, I should mention that the area beside this nail is tender. Could you cover it with product so it looks better for my event?
Dev | Thank you for telling me. I will [[pause::Pause means stopping the covering request before product is applied, rather than carrying on because the client has an event.]] that request for now. The tenderness needs appropriate attention before we make assumptions about a cosmetic service.
Elena | I do not know what caused it. I was hoping the appointment could still go ahead because the event is important to me.
Dev | I understand the [[event deadline::Event deadline explains why Elena wants a cosmetic result but does not establish that applying a product is suitable.]]. It matters to your plans, but it does not tell us whether applying product to the area is suitable.
Elena | It's beside this nail, not all over my hand. Can you see where I'm pointing?
Dev | You are reporting [[tenderness::Tenderness is Elena's own description of the sensation beside one nail, not a diagnosis of its cause.]] beside this nail. I will keep that description rather than add a condition name or assume a cause.
Elena | Yes. It was there before I arrived, and nothing from today's appointment has been put on it.
Dev | I will record it as a [[pre-existing concern::Pre-existing concern means it was present before the proposed service, preventing an inaccurate claim that today's product application caused it.]]. No product has been applied today, and no service has started.
Elena | Who should I ask about it? I haven't had it checked, and I don't know what's causing it.
Dev | Please have the concern assessed by an appropriate [[healthcare professional::Healthcare professional identifies the appropriate route for assessing an unexplained health concern, rather than asking the nail technician to diagnose or treat it.]]. I cannot determine the cause or recommend treatment from this salon conversation.
Elena | If I get advice, can I come back for the service afterwards?
Dev | No. The [[referral::Referral directs Elena toward appropriate health assessment; it does not itself approve the proposed cosmetic service or guarantee a later appointment.]] does not guarantee that. The salon must separately decide whether the proposed cosmetic service is suitable through its normal process.
Elena | So I need advice about the soreness first, and then we'd discuss whether the nail service can go ahead.
Dev | Exactly. [[Cosmetic suitability::Cosmetic suitability is the separate salon assessment of the proposed appearance service, not a substitute for healthcare assessment.]] is not established simply by making a referral. We should not promise approval before the relevant decisions have been made.
Elena | Please just note what I told you. Nobody has diagnosed it yet.
Dev | I will make a [[factual note::Factual note records the reported tenderness, its timing, the paused request, and the referral without inventing a diagnosis.]] with your description, the fact that it was reported before service, and the request to cover it being paused.
Elena | That is accurate. I will seek appropriate healthcare advice, and I understand that you are not suggesting a treatment here.
Dev | Correct. I am not giving a [[diagnosis::Diagnosis identifies a health condition through appropriate clinical assessment, which the technician has not performed or claimed.]] or treatment advice. The immediate salon decision is not to apply a covering product to this unexplained concern.
Elena | Okay, I won't ask you to cover it. I'll get advice about the tenderness first.
Dev | The [[service approval::Service approval has not been given: the covering request remains paused even though the client agrees to seek healthcare advice.]] remains unresolved. No cause is established, no product has been applied, and the cosmetic request stays paused while you seek the appropriate advice.''',
    rehearsal=["Read the opening with a calm, firm pause before any product is applied.","Switch roles and read the referral exchange. Do not substitute an invented diagnosis for tenderness.","Complete and check the transfer; preserve the separate health assessment and unassessed cosmetic suitability."],
    transfer_title='Separate referral from service approval',
    transfer_setup='Before service, a client reports unexplained soreness beside one nail. No product is applied. The covering request is paused, and the client is directed to an appropriate healthcare professional. Salon suitability remains unassessed.',
    transfer='''Technician: "The reported concern is ___ beside one nail." | soreness | Soreness is the supplied client description, not an inferred condition.
Client: "No product has been ___." | applied | The scenario explicitly keeps the cosmetic application from starting.
Technician: "The covering request remains ___." | paused | Referral does not restart or authorize the cosmetic service.
Reception: "Cosmetic suitability is still ___." | unassessed | The salon must assess suitability separately from the healthcare referral.'''
))


BOOK['units'].append(unit(
    title='Giving a clear station-readiness update',
    scene='Tidy is not confirmed ready',
    skill='Distinguish visible tidiness from completed readiness checks and offer a verified alternative without inventing a release time.',
    brief='Receptionist Maya needs a station for a waiting client. Technician Owen reports that station three looks tidy but its required readiness checks are incomplete. Responsible technician Rosa has confirmed station two ready. Owen offers station two and keeps station three marked pending until its actual checks are completed and readiness is confirmed through the salon process. No completion time for station three is known. This is a communication task, not a set of cleaning, disinfection, equipment, or chemical-use instructions.',
    cast='Maya | Receptionist\nOwen | Nail technician',
    culture=('Use status words colleagues can act on', 'Tidy, nearly done, and should be fine may sound reassuring while leaving an essential check unclear. Give the specific station, verified status, and available next step. A waiting client creates a scheduling need, not evidence that unfinished checks can be treated as complete.'),
    a='''Which station is confirmed ready? | Station two | Station three | Both stations | Neither station | Rosa has confirmed station two ready through the relevant salon process.
What is station three's status? | Tidy, with required checks incomplete | Confirmed ready because it looks tidy | Permanently closed | Already in use with approval | Appearance and readiness differ; station three still has incomplete required checks.
What time will station three be ready? | No completion time is known | Exactly five minutes from now | Before the client sits down | It was ready earlier | The case supplies no verified completion time for the pending station.''',
    vocabulary='''station | Designated work area for a client service. | identify the station
readiness check | Required review before a station is confirmed available for use. | complete a readiness check
confirmed ready | Status supported by the responsible person's completed process. | report confirmed-ready status
pending status | State of waiting for an unfinished check or decision. | keep the pending status
tidiness | Visible orderliness, not proof of completed hygiene or readiness checks. | distinguish tidiness from readiness
cleaning | Removal of dirt or material, distinct from every further required process. | distinguish cleaning from disinfection
disinfection | Process intended to control specified microorganisms under applicable instructions. | refer to disinfection requirements
single-use item | Item intended for one use under its instructions. | identify a single-use item
reusable implement | Tool intended for repeated use subject to the required processing. | identify a reusable implement
service tray | Surface or container holding items for a service. | identify the service tray
work surface | Surface used during the service. | check work-surface status
clean storage | Designated storage for appropriately prepared items. | identify clean storage
used-item area | Designated place for items awaiting the required handling. | identify the used-item area
waste container | Receptacle for waste under the applicable procedure. | check the waste container
product label | Product information including identity, instructions, and warnings. | consult the product label
safety data sheet | Document describing a product's hazards and relevant safety information. | locate the safety data sheet
ventilation | Movement or exchange of air through the relevant workplace system. | report a ventilation concern
local exhaust | System capturing airborne material near its source. | identify local exhaust
personal protective equipment | Equipment used to reduce exposure to workplace hazards. | confirm required personal protective equipment
check record | Record showing what has been checked and its status. | update the check record
responsible technician | Person accountable for the relevant station confirmation. | name the responsible technician
release confirmation | Statement that the station has met the required readiness process. | await release confirmation
sterilization | Validated process eliminating viable microorganisms including bacterial spores; not a synonym for storage. | distinguish disinfection from sterilization
cross-contamination | Transfer of unwanted microorganisms or material between tools, surfaces, or people. | prevent cross-contamination''',
    precision='Station three is tidy but not confirmed ready because required checks are incomplete. Station two is confirmed ready by Rosa. Offer the verified alternative without silently upgrading station three or inventing a completion time.',
    precision_extra='Cleaning, disinfection, storage, product information, and equipment terms describe different parts of real workplace systems. This lesson does not supply procedures or authorize a shortcut. Use actual instructions, training, and the responsible confirmation process.',
    phrases='''Identify the station | Station three is the one still awaiting checks.\nDescribe only what is known | It looks tidy, but its required checks are incomplete.\nAvoid an appearance shortcut | Tidiness does not establish confirmed readiness.\nState the verified alternative | Station two has been confirmed ready.\nName the confirmation source | Rosa is the responsible technician who confirmed it.\nOffer a workable next step | We can offer the client station two.\nKeep the pending status | Station three should remain marked pending.\nAvoid a guessed time | I do not have a confirmed completion time for station three.\nAcknowledge the wait | I know the client is waiting; we have a verified alternative.\nAsk a precise question | Which station has completed the required readiness process?\nKeep procedures separate | The checks must follow the actual salon process.\nPrevent an inaccurate update | Please do not change three to ready because the surface looks clear.\nRead back the numbers | Two is confirmed ready; three is pending.\nConfirm the next update | We will update three after the required confirmation.\nGive a client-facing message | A confirmed-ready station is available for you.\nClose the handover | Use the verified status, not an estimate based on appearance.''',
    notes='''Tidy versus ready | Visible order does not prove that all required checks are complete.\nTwo versus three | Read back the station numbers to prevent a correct status attaching to the wrong place.\nConfirmed by | Names the responsible source rather than implying personal observation of every check.\nPending | This means unfinished, not failed forever or ready for immediate use.\nAvailable alternative | An actual ready station gives a useful option without pressuring an incomplete one.\nNo completion time | An unknown time should remain unknown until a reliable update is available.''',
    d='''Which handover is accurate? | Two confirmed ready by Rosa; three tidy with checks incomplete. | Both ready because the room looks neat. | Three ready and two awaiting review. | Three ready in five minutes without a source. | The correct message preserves both station numbers and their different verified statuses.
Which message should reception give the client? | A confirmed-ready station is available at station two. | Station three is ready because its table is empty. | All checks are optional when someone is waiting. | Station three will definitely be ready immediately. | Station two provides the verified option without inventing readiness for station three.
What would justify updating station three's status? | Completion of its required checks and the actual readiness confirmation | A shorter queue | A tidy appearance alone | A client's willingness to sit there | Readiness must follow the required process rather than appearance or scheduling pressure.
Which question is most precise? | Has station three received the required readiness confirmation? | Does everything seem fine? | Is the tabletop at station three clear of used items? | Has the waiting client agreed to use station three? | The question asks about the specific unresolved status rather than a vague impression.''',
    dialogue='''Maya | Can I seat the waiting client at station three? The table looks clear from here.
Owen | Not yet. It's [[tidy::Tidy describes appearance only; station three still has incomplete required readiness checks.]], but the readiness checks aren't complete. Station two is the one Rosa has confirmed ready.
Maya | Two, not three. Thanks for catching that. I'll move the client to two rather than leave them standing at reception.
Owen | Yes, that's the [[available alternative::Station two is the verified alternative; using it does not change station three's unfinished status.]]. Three needs to stay out of use until the remaining checks are finished and confirmed.
Maya | The board says almost ready beside three. Should that say pending instead?
Owen | Yes. [[Pending::Pending clearly indicates unfinished checks, whereas almost ready can be mistaken for permission to start.]] makes the status clearer. Almost ready could encourage someone else to seat a client there.
Maya | I'll change the label. Do you know how long the remaining checks will take?
Owen | I don't have a confirmed [[completion time::No reliable completion time is supplied for station three, so a waiting estimate would be invented.]] yet. Please don't promise the next client five minutes on that basis.
Maya | All right. For the client who's here, I'll say we have another station available now.
Owen | That works. Station two is [[confirmed ready::Rosa has confirmed station two through the salon process; that status cannot be transferred to station three.]]; we don't need to give the client a detailed account of the unfinished checks elsewhere.
Maya | Who confirmed two? I'd like to put the name in the note so the next receptionist can see it.
Owen | Rosa is the [[responsible technician::Rosa is the named source of the station-two confirmation, avoiding an anonymous or assumed approval.]]. She's already given that confirmation, so you can name her.
Maya | Good. Does a cleared work surface at three tell us anything about the tools that will be used there?
Owen | Not by itself. The [[readiness check::The readiness check must cover the actual required items; surface appearance alone does not verify tools or other controls.]] follows our actual process. An empty table doesn't establish that the tools or other requirements are ready.
Maya | Then I'll leave the station pending, even if the client says they're happy to sit there.
Owen | Correct. We still need the [[release confirmation::Release confirmation is the actual readiness decision after the required checks, not the client's willingness to use the station.]] after the checks. Their willingness doesn't complete our responsibilities.
Maya | Let me repeat it: two ready, confirmed by Rosa; three pending, no confirmed time. Is that everything?
Owen | That's an accurate [[read-back::The read-back connects the correct station number with its status, confirmation source, and timing limit.]]. It should prevent the ready label ending up beside the wrong station.
Maya | I'll offer two now and wait for an actual update before changing three on the board.
Owen | Thanks. Keep that [[readiness handover::The handover gives an immediately usable option while retaining the pending station's actual status.]] for the next receptionist too, so nobody has to guess from what the room looks like.''',
    rehearsal=["Read the station exchange, clearly contrasting two ready with three pending.","Switch roles. Read the no-confirmed-time response without adding a five-minute estimate.","Complete and check the transfer; read station one as ready and station five as pending, using the new confirming name."],
    transfer_title='Read back different station numbers',
    transfer_setup='Station five is tidy but has incomplete required checks. Station one is confirmed ready by technician Jo. No completion time is known for five. A waiting client can be offered one.',
    transfer='''Reception: "The verified alternative is station ___." | one | Jo has confirmed station one ready, making it the available option.
Technician: "Station five remains ___." | pending | Its required checks are incomplete despite the tidy appearance.
Reception: "The confirming technician for one is ___." | Jo | Jo is the named source of the station-one readiness confirmation.
Technician: "Five has no confirmed completion ___." | time | The brief supplies no reliable time for station five to become ready.'''
))


BOOK['units'].append(unit(
    title='Handling a chip or design concern',
    scene='The lettering faces the wrong way',
    skill='Acknowledge a documented design-direction mismatch and offer a review without promising an unassessed correction.',
    brief='Client Imani contacts receptionist Alex because the line-art lettering on the finished nails faces away from the client. Imani requested lettering facing toward the client, and the service record confirms that original direction. A review with technician Rosa is available today at 4:00 with no review fee. Imani accepts that review. No correction method, correction price, refund, or completion time has been assessed or approved. Alex must recognize the documented mismatch without claiming that the no-fee review guarantees a free or immediate particular correction.',
    cast='Imani | Client\nAlex | Receptionist',
    culture=('A specific acknowledgment prevents a circular complaint', 'When the record confirms a requested detail, acknowledge it directly rather than asking the client to defend the same preference repeatedly. Then separate the review arrangement from any remedy that still needs assessment. Clear limits are more useful than a vague promise to make everything right.'),
    a='''What direction was requested and recorded? | Lettering facing toward the client | Lettering facing away from the client | No direction was discussed | A direction chosen later by reception | The service record confirms the client's original toward-client request.
What is available today? | A no-fee review at 4:00 | A guaranteed full correction at 4:00 | An approved refund at 4:00 | A completed replacement design | The available appointment is a review, not a preapproved remedy.
What does no review fee mean? | The review itself has no charge | Every possible correction is free | Every future service is free | A refund has already been paid | The fee statement applies only to the review, not unassessed additional work.''',
    vocabulary='''design concern | Client's issue with an aspect of the finished decoration. | acknowledge a design concern
lettering | Letters used as part of the nail-art design. | check the lettering
facing toward | Oriented so the relevant front faces the named viewer. | confirm lettering facing toward the client
facing away | Oriented in the opposite direction from the named viewer. | report lettering facing away
orientation mismatch | Difference between the agreed and delivered direction. | acknowledge an orientation mismatch
viewing perspective | Position from which the design is meant to be read. | clarify the viewing perspective
legibility | Ease of reading the lettering. | discuss legibility
design brief | Agreed description of the requested decoration. | refer to the design brief
service record | Record of the original request and service details. | check the service record
documented request | Preference supported by the existing record. | acknowledge the documented request
finished result | Appearance after the service has been performed. | review the finished result
chip | Small area of product or coating that has broken away. | report a chip
lifting | Separation of enhancement material from the nail surface. | report lifting
wear concern | Report about how the result has changed during use. | record a wear concern
review appointment | Meeting to examine a concern before deciding a response. | confirm the review appointment
review fee | Charge for the assessment appointment itself. | clarify the review fee
correction method | Proposed way of addressing an assessed design issue. | assess the correction method
correction estimate | Provisional price or time for a proposed remedy. | provide a correction estimate
remedy decision | Decision about what response is appropriate. | separate the remedy decision
refund approval | Authorized decision to return money. | distinguish refund approval
completion promise | Commitment about when work will be finished. | avoid an unsupported completion promise
specific acknowledgment | Recognition of the exact issue rather than a generic apology. | give a specific acknowledgment
case note | Factual record of the concern and agreed next step. | update the case note
review confirmation | Agreement on the time and purpose of the review. | send the review confirmation''',
    precision='The record supports the original toward-client direction, while the client reports that the finished lettering faces away. Acknowledge that mismatch specifically. The accepted 4:00 appointment is a review, not a promised correction.',
    precision_extra='No review fee applies to the assessment itself. The case does not establish any correction method, charge, refund, or finish time. Do not expand a limited fee statement into a guarantee about every possible remedy.',
    phrases='''Acknowledge the detail | You requested the lettering facing toward you.\nUse the record | The service record confirms that direction.\nDescribe the concern | You are reporting that the finished lettering faces away.\nAvoid an argument over preference | We do not need to treat the recorded direction as a new request.\nOffer the review | Rosa can review the concern today at 4:00.\nState the limited fee fact | There is no fee for that review.\nSeparate review from remedy | The correction needs assessment before we promise a method.\nAvoid expanding the fee statement | No review fee does not establish the price of unassessed further work.\nKeep refund status clear | No refund has been approved.\nAvoid a finish-time promise | We have not established when any correction could be completed.\nAsk for acceptance | Would you like the 4:00 review?\nConfirm the purpose | The appointment is to examine the design-direction concern.\nPreserve the orientation | I will record toward you as the original request.\nKeep the report precise | This concern is about direction, not a reported chip.\nRead back the arrangement | Today at 4:00 with Rosa, for a no-fee review.\nClose with the next step | We will discuss any proposed remedy after the review.''',
    notes='''Toward versus away | These words reverse the meaning, so name the viewer as well as the direction.\nRecorded versus newly requested | The record supports an original preference, not a later change of mind.\nReview versus correction | One examines the concern; the other performs additional work.\nNo fee for | The phrase limits the no-charge statement to the named activity.\nAvailable versus accepted | The review becomes the agreed arrangement after the client chooses it.\nConcern type | Direction, chipping, and lifting are different reports and should not be substituted for one another.''',
    d='''Which acknowledgment matches the record? | You requested lettering facing toward you, and that direction is recorded. | You never specified a direction. | You requested lettering facing away. | You are changing the original design brief. | The existing service record supports the client's original toward-client direction.
Which promise exceeds the supplied facts? | Every correction will be free and completed during the review. | The review has no fee. | Rosa is available at 4:00. | No refund has been approved. | Correction price, method, and completion time have not been assessed or approved.
Which concern should the case note identify? | A lettering-orientation mismatch | A confirmed product allergy | A reported chip that was never mentioned | A guaranteed removal procedure | The complaint concerns design direction rather than an invented health or wear issue.
Which confirmation is accurate after acceptance? | Today at 4:00 with Rosa for a no-fee review of the direction concern. | A full correction at 4:00 with every cost waived. | A refund already processed. | A new paid design unrelated to the original record. | The confirmation states the agreed review and its limited fee scope.''',
    dialogue='''Imani | I'm calling about the lettering on my nails. I asked to read it facing toward me, but it's facing away.
Alex | I've found the [[service record::The record confirms the original toward-client request, rather than a new preference after the service.]]. It says toward the client, just as you've described.
Imani | Thank you. I don't want this treated as changing my mind. I explained the direction during the appointment.
Alex | I understand. You're reporting an [[orientation mismatch::The mismatch concerns the delivered lettering direction compared with the documented request, not chipping or product wear.]], not asking us to replace the original request with a new one.
Imani | Can Rosa look at it today? I can come back if there's an appointment.
Alex | She has a [[review appointment::The available 4:00 appointment is to review the concern, not a promised completed correction.]] at four. She can look at the lettering with you and discuss what happens next.
Imani | Would I have to pay just to come back and show her the problem?
Alex | There's no [[review fee::No review fee applies to the assessment itself; it does not settle the cost of every possible remedy.]]. I haven't assessed any further work, so I can't give a correction price on this call.
Imani | I see. Can you tell me how she'd change it, or does she need to see the nails first?
Alex | She needs to assess the [[correction method::The method has not been assessed, so the receptionist should not promise a particular procedure.]] with you first. I don't want to promise a procedure we haven't discussed.
Imani | Please don't start anything else without explaining it. I'd like to know exactly what's being proposed.
Alex | Certainly. A [[remedy decision::The remedy decision follows review and agreement; accepting the appointment does not approve additional work automatically.]] comes after that discussion. Booking the review doesn't commit you to further work.
Imani | And how long would I be there? I need to arrange the rest of my afternoon.
Alex | I can't make a [[completion promise::A review start time does not establish when an unassessed correction could finish.]] for a correction yet. Four is the review time, not a guaranteed finish time.
Imani | All right, I'll take the four o'clock review. Please make the note specific, not just unhappy with nails.
Alex | The [[case note::The case note preserves the exact documented direction and reported result rather than a vague complaint.]] will say toward you requested and recorded, but finished lettering reported as facing away.
Imani | Exactly. The letters should be readable from where I'm sitting. Nothing has chipped; it's the direction.
Alex | I'll keep your [[viewing perspective::The client is the intended reader, which explains the toward-versus-away distinction.]] clear. I won't substitute a wear problem for the concern you're actually reporting.
Imani | Thank you. Could you send me the time and Rosa's name so I can check them?
Alex | Yes. The [[review confirmation::The confirmation covers the accepted time, named technician, and no-fee review, not an approved correction or refund.]] is today at four with Rosa, no charge for the review. No correction or refund has been approved during this call.''',
    rehearsal=["Read the concern from the client's viewpoint. Contrast toward me with away from me.","Switch roles and read the review arrangement. Stress no fee for the review, without promising a correction's price or finish time.","Complete and check the reversed-direction transfer, then read the new 11:00 review details exactly."],
    transfer_title='Confirm a different design review',
    transfer_setup='The record says lettering should face away from the client, but the client reports it faces toward them. A no-fee review with Jo tomorrow at 11:00 is accepted. No correction method or price is agreed.',
    transfer='''Reception: "The recorded direction is ___ from the client." | away | Away is the documented original direction in this new case.
Client: "The accepted review is tomorrow at ___." | 11:00 | The brief gives eleven o'clock as the agreed review time.
Reception: "The review itself has no ___." | fee | The no-charge statement applies specifically to the review appointment.
Reception: "No correction method is ___." | agreed | Accepting the review does not establish a particular correction plan.'''
))


BOOK['units'].append(unit(
    title='Scheduling follow-up and handing over exact requests',
    scene='Friday is a request, not a booking',
    skill='Hand over the desired appearance, unknown existing product, and pending consultation without inventing removal time or an infill booking.',
    brief='Technician Sora hands a client request to receptionist Malik. The client wants plain color next Friday at 10:00 and declines nail art. An existing product is present, but its identity is unknown. Reception must arrange a consultation before confirming removal duration or whether an infill is appropriate. Friday at 10:00 is only a requested time; no appointment has been accepted or booked. Malik takes responsibility for discussing consultation availability while keeping the product uncertainty and no-art preference explicit.',
    cast='Sora | Nail technician\nMalik | Receptionist',
    culture=('Do not let a convenient slot decide the service', 'A client may ask for a familiar time before the existing product or needed service is understood. Record the requested time without treating it as a confirmed slot. An accurate handover keeps the next colleague from promising a duration or infill based on an unidentified product.'),
    a='''What appearance does the client request? | Plain color with no nail art | Four decorated nails | A confirmed extension design | A specific removal method | The client requests plain color and explicitly declines additional nail art.
What is unknown? | The identity of the existing product | Whether any product is present | The requested day and time | The no-art preference | An existing product is reported, but its identity has not been established.
What is Friday at 10:00? | A requested time, not a booking | An accepted appointment | A guaranteed removal completion time | A confirmed infill service | The brief explicitly leaves the requested time unaccepted and unbooked.''',
    vocabulary='''existing product | Material already on the client's nails before a new service. | identify the existing product
product identity | Exact identifying information about the material present. | confirm product identity
unidentified product | Existing material whose type or identity is not established. | record an unidentified product
service history | Relevant record of earlier nail services and products. | review service history
previous provider | Professional or salon that performed an earlier service. | clarify the previous provider
removal consultation | Discussion and assessment before confirming a removal service. | arrange a removal consultation
removal duration | Time needed for removing an identified product under the actual process. | assess removal duration
soak-off | Product-removal category used for materials designed for the relevant solvent process. | clarify a soak-off category
file-off | Product-removal category involving controlled filing under professional procedures. | distinguish a file-off category
infill | Maintenance service addressing growth in an existing enhancement when appropriate. | assess whether an infill is suitable
rebalance | Maintenance term for restoring enhancement structure as the nail grows. | discuss rebalance terminology
regrowth area | New growth visible near the base of an existing enhancement. | identify the regrowth area
maintenance appointment | Follow-up service whose scope depends on assessment. | clarify the maintenance appointment
plain-color request | Preference for color without added decorative art. | preserve the plain-color request
declined option | Service element the client has explicitly not selected. | record the declined option
requested time | Preferred slot that has not necessarily been offered or accepted. | record the requested time
confirmed appointment | Booking with the relevant details agreed. | distinguish a confirmed appointment
availability discussion | Conversation about possible times, not automatic acceptance. | hold an availability discussion
consultation prerequisite | Consultation needed before confirming further service details. | explain the consultation prerequisite
provisional duration | Tentative time estimate not yet a firm service allocation. | avoid an unsupported provisional duration
handover owner | Person responsible for the next action after the handover. | name the handover owner
client confirmation | Explicit acceptance of the relevant appointment or service details. | obtain client confirmation
pending action | Next step that remains unfinished. | identify the pending action
status correction | Amendment replacing an inaccurate status with the true one. | make a status correction''',
    precision='The client wants plain color, no nail art, and Friday at 10:00. Those are a preference and a requested time, not a booking. The unidentified existing product means removal duration and infill suitability cannot be confirmed from the supplied facts.',
    precision_extra='Soak-off, file-off, infill, and rebalance are not interchangeable booking labels. This lesson provides no removal instructions. The consultation must establish the actual product and appropriate service before reception promises a duration or confirms an infill.',
    phrases='''Open the handover | I have a plain-color request with an unidentified existing product.\nState the appearance | The client wants plain color and no nail art.\nRecord the requested slot | Friday at 10:00 is the preferred time.\nPrevent a booking assumption | That time is requested, not booked.\nName the uncertainty | We do not yet know which product is present.\nKeep history accurate | Unknown product does not mean no existing product.\nExplain the prerequisite | A consultation is needed before confirming removal time.\nAvoid a standard-time guess | I cannot assign a removal duration from the current information.\nKeep infill open | Whether an infill is appropriate still needs assessment.\nSeparate service categories | Removal and infill are not the same booking decision.\nAssign the next action | Reception will discuss consultation availability.\nAvoid inventing acceptance | No appointment date has been accepted yet.\nPreserve the declined option | Please keep no nail art explicit in the record.\nAsk for a read-back | Can you repeat the request and the unresolved details?\nCorrect the status | Change confirmed to requested if that entry was made prematurely.\nClose the handover | Consultation pending; removal time and infill unconfirmed.''',
    notes='''Unknown versus absent | The product is present but unidentified; do not erase it from the history.\nRequested versus confirmed | A preferred time becomes a booking only through the actual confirmation process.\nBefore | Consultation is a prerequisite to confirming the unassessed service details.\nRemoval versus infill | One removes material; the other maintains an existing enhancement when suitable.\nNo nail art | This is an explicit exclusion, not an invitation to choose a simpler design silently.\nOwner versus completion | Reception accepting the next action does not mean the consultation has occurred.''',
    d='''Which handover is accurate? | Plain color, no art, Friday 10:00 requested; existing product unidentified. | Infill booked Friday with standard removal time. | No existing product because its name is unknown. | Nail art approved during reception handover. | The correct handover preserves appearance, timing status, and the unresolved product identity.
What must precede confirmation of removal time? | The consultation needed to assess the existing product and service | Assuming every product removes identically | Selecting the shortest available slot | Treating Friday as already booked | The brief requires consultation before a removal duration can be confirmed.
Which phrase makes an unsupported commitment? | Your infill is confirmed for Friday at ten. | Friday at ten is your requested time. | Reception will discuss consultation availability. | No nail art is requested. | Neither infill suitability nor an accepted appointment is established.
What does reception taking responsibility mean? | Reception owns the next availability discussion. | Consultation has already been completed. | Existing product is now identified. | Removal duration is automatically confirmed. | Ownership assigns the pending action without changing any unfinished assessment or booking status.''',
    dialogue='''Sora | I need to hand over a follow-up request. The client wants plain color next Friday at ten, but there is an existing product we have not identified.
Malik | I will separate the [[plain-color request::Plain-color request records the desired appearance without selecting a removal method, infill, or confirmed appointment.]] from the service assessment. Is nail art wanted, or should the record explicitly say that it has been declined?
Sora | No art. The client specifically asked for plain color, even on the accent nails.
Malik | I will preserve that [[declined option::Declined option is nail art, which the client explicitly excludes rather than leaving open for an unrequested design choice.]]. Plain color and no nail art should remain together in the appearance note.
Sora | Thank you. Friday at ten is the time the client requested, but we did not offer a confirmed appointment or get acceptance of a slot.
Malik | Then the [[requested time::Requested time is Friday at 10:00 as a preference, not an accepted or confirmed appointment.]] stays requested. I will not enter it as a booking just because the client named a day and an hour.
Sora | Exactly. We also cannot assume what removal involves. The client says there is product on the nails but cannot identify it.
Malik | I will record an [[unidentified product::Unidentified product means material is present but its identity is unknown; it must not be recorded as no product.]], not no product. That distinction matters before anyone promises a standard removal time.
Sora | Could you arrange the consultation first? We don't know enough to book a removal slot yet.
Malik | The [[consultation prerequisite::Consultation prerequisite means assessment must come before confirming removal duration or whether an infill is appropriate.]] is clear. I will discuss consultation availability rather than confirm an unassessed removal or infill service.
Sora | Good. The client may use infill as a general word for the next visit, but we have not established whether that is appropriate here.
Malik | An [[infill::Infill is a maintenance service for an existing enhancement when suitable; its name does not establish that it is appropriate for this unidentified product.]] is not automatically the right booking just because it is a familiar term. Its suitability still needs assessment through the consultation.
Sora | Please don't quote the usual removal time. We still don't know what we're dealing with.
Malik | I will leave [[removal duration::Removal duration is the time needed for the actual service, which cannot be confirmed from an unidentified product or another client's appointment.]] unconfirmed. The product and relevant service need to be understood before a meaningful time allocation is promised.
Sora | Could you read back the handover now? I want to catch any wording that makes the Friday preference sound more definite than it is.
Malik | Plain color, no nail art, Friday at ten requested but unbooked, and existing product unidentified. The [[pending action::Pending action is the consultation availability discussion, which has not yet resulted in an accepted appointment or assessed service.]] is to discuss a consultation before confirming removal time or infill suitability.
Sora | Yes. Please offer consultation times and get the client's agreement before sending a booking confirmation.
Malik | I will be the [[handover owner::Handover owner identifies Malik as responsible for the next discussion without claiming that the consultation or booking has already been completed.]] for the availability discussion. Taking responsibility does not change the unbooked status or resolve the product uncertainty.
Sora | Thanks. Explain that we need to check the existing material so we can plan the right appointment.
Malik | I will explain the purpose and seek [[client confirmation::Client confirmation is the explicit agreement still needed for an offered consultation appointment; a requested time alone does not provide it.]] for any offered slot. The record will remain precise: request received, consultation pending, and no removal duration or infill booking confirmed.''',
    rehearsal=["Read the handover, keeping plain color and no art together as the appearance request.","Switch roles. Stress product present but unidentified and Friday requested but unbooked.","Complete and check the Tuesday transfer; read the consultation step without confirming a removal duration or infill."],
    transfer_title='Hand over another unbooked request',
    transfer_setup='A client requests plain color on Tuesday at 2:00, with no nail art. Existing product is unidentified. Reception owns the consultation availability discussion before removal time or infill suitability can be confirmed.',
    transfer='''Technician: "The requested day is ___." | Tuesday | Tuesday is the stated preference, not proof of an accepted appointment.
Reception: "Existing product remains ___." | unidentified | Product is present, but its identity has not been established.
Technician: "The next availability discussion belongs to ___." | reception | Reception is assigned the pending consultation discussion in the handover.
Reception: "Removal time cannot yet be ___." | confirmed | Consultation must precede confirmation of the unassessed removal duration.'''
))
