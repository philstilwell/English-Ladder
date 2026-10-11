"""Original Carpentry and Remodeling learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='carpentry-remodeling',
    title='Carpentry & Remodeling English',
    cover_label='ENGLISH FOR JOINERY, FIT-OUTS, AND CLIENT REVIEWS',
    cover_title='Carpentry and\nRemodeling',
    cover_size=36,
    tagline='Precise details. Clear agreements.',
    audience='For carpenters, remodelers, joinery installers, workshop coordinators, and client-facing project staff.',
    map_intro='Eight practical conversations: clarify a dimension, compare trim samples, resolve conflicting drawings, report concealed-condition concerns, separate extras, coordinate trades, correct a fit claim, and hand over an outstanding part.',
    notes_title='Clarify the detail before it becomes a commitment.',
    notes_intro='Carpentry conversations connect drawings, materials, people, and site conditions. Precise English identifies the reference behind a dimension, separates observations from diagnoses, and makes clear what is agreed, available, delivered, or still awaiting review.',
    field_notes=[
        ('Name the measurement reference', 'A number without a reference can be misunderstood. Distinguish an opening dimension, a frame dimension, and usable passage. Ask the designer to resolve an unclear note instead of silently choosing an interpretation.', '"The drawing says 900 millimeters, but it does not identify the opening reference."'),
        ('Compare samples on stated attributes', 'Material construction, grain, profile, finish, price, and timing are different attributes. Compare only what is known about the actual samples; do not turn one quoted lead time into a universal rule about a material.', '"Both match the profile; sample A has pronounced grain and the longer quoted lead time."'),
        ('Describe the visible condition first', 'A projecting drawer front and stained subfloor can be described without inventing their cause. Correct inaccurate claims promptly and refer technical assessment to the appropriate person.', '"D3 projects at the left edge; I have not assessed the cause or remedy."'),
        ('Keep dates attached to their purpose', 'Delivery, access, a review meeting, a callback, and a return visit are separate arrangements. State the owner and status of each instead of compressing them into a single promise.', '"Mina will call Friday; the return-visit date is still unconfirmed."'),
    ],
    scope_note='All clients, drawings, materials, dimensions, products, prices, schedules, and site conditions in these cases are fictional. This book teaches workplace English, not structural assessment, building-code compliance, tool operation, demolition, installation, or legal interpretation. Follow actual project documents, manufacturer instructions, site controls, competent assessments, and applicable requirements. The scenarios do not authorize fabrication from conflicting drawings, entry to unreleased areas, concealed-condition work, substitutions, extra work, or changes to warranty terms.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Carpenters.',
             url='https://www.bls.gov/ooh/construction-and-extraction/carpenters.htm',
             note='Occupational context for reading plans, discussing measurements and materials, installation work, and client communication. No employment forecasts or credential requirements are reproduced.', checked='10 October 2026'),
        dict(title='Architectural Woodwork Institute. AWI 100: Manufacturer / Supplier Responsibility.',
             url='https://awinet.org/standards/submittals/requirements-category/manufacturer-supplier-responsibility/',
             note='Context for shop drawings, material samples, explicit change requests, and coordinated review. Fictional drawing conflicts and review times are not requirements stated by this source.', checked='10 October 2026'),
        dict(title='Andersen Windows and Doors. Window and Door Glossary.',
             url='https://www.andersenwindows.com/support/window-door-glossary',
             note='Background terminology for openings, frames, trim, and door components. No product-specific dimensions, installation allowances, or compliance claims are transferred to the cases.', checked='10 October 2026'),
        dict(title='Occupational Safety and Health Administration. Woodworking: Hazards and Solutions.',
             url='https://www.osha.gov/woodworking/hazards-solutions',
             note='Context for respecting trained roles and actual safety controls. The book provides no machine-operation, chemical-use, or concealed-condition assessment procedure.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming openings and measurement references',
    scene='What does 900 millimeters describe?',
    skill='Identify an unclear measurement reference, correct an assumption, and obtain designer clarification before treating the dimension as usable passage.',
    brief='Client Hana and carpenter Ellis review a hall drawing labeled door opening: 900 millimeters. Hana assumes the figure describes clear passage width. The note does not identify a rough or finished opening, and no door has been ordered. Ellis must clarify the ambiguity without inventing a frame allowance or asserting a usable width. Designer Priya can explain which reference the dimension uses. The conversation concerns interpretation and referral, not a construction method or a compliance decision.',
    cast='Hana | Client\nEllis | Carpenter',
    culture=('A precise number can still carry an unclear meaning', 'A client may reasonably read an opening dimension as the space available to pass through. Acknowledge that interpretation, explain the missing reference in ordinary words, and ask the designer to clarify it. Do not make uncertainty sound like a mistake the client should have recognized.'),
    a='''What does the drawing label say? | Door opening: 900 millimeters, without a rough or finished reference | Clear passage guaranteed at 900 millimeters | Door already ordered at a verified size | Finished frame allowance confirmed | The note supplies a number but does not identify the opening reference.
What is Hana assuming? | That 900 millimeters is clear passage width | That a door has already arrived | That Priya has clarified the note | That the frame is not required | Hana reads the number as usable passage, which has not been established.
What is the appropriate next step? | Ask Priya to clarify the measurement reference | Invent a frame allowance | Order a door from the ambiguous note | Certify the opening as compliant | Priya can clarify the reference; the conversation does not establish an order size or compliance.''',
    vocabulary='''opening dimension | Measurement describing an opening using a stated reference. | clarify the opening dimension
rough opening | Structural opening before the door assembly and relevant finishes are installed. | confirm the rough-opening reference
finished opening | Opening measured at the specified completed surfaces. | identify the finished opening
clear passage | Unobstructed usable space through an opening under the stated conditions. | confirm the clear passage
door leaf | Moving panel of a door. | distinguish the door leaf
door frame | Surrounding assembly supporting and locating the door. | identify the door frame
jamb | Frame member; side jambs and the head jamb identify different positions. | identify the side jamb
head | Upper horizontal member or part of an opening. | identify the frame head
threshold | Lower part at the base of a doorway. | refer to the threshold
casing | Trim around a door or window opening. | identify the casing
architrave | Term commonly used for decorative trim around an opening. | compare the architrave profile
millimeter | Metric unit equal to one thousandth of a meter. | state the dimension in millimeters
dimension line | Drawing line indicating the extent of a measurement. | follow the dimension line
reference face | Surface from which a dimension is measured. | identify the reference face
datum | Stated reference point, line, or level for measurements. | confirm the datum
nominal size | Designated size that may differ from an actual measured size. | distinguish nominal size
actual dimension | Measured or specifically defined physical size. | verify the actual dimension
frame allowance | Space allowed for the specified frame arrangement. | verify the frame allowance
clearance | Space between components or around an operating part. | clarify the required clearance
door schedule | Drawing or document listing specified doors and their attributes. | check the door schedule
drawing note | Written instruction or information on a drawing. | clarify the drawing note
designer clarification | Explanation from the responsible design professional. | request designer clarification
order size | Dimensions used to specify a product for purchase. | confirm the order size
dimension reference | Point, surface, or condition a measurement describes. | establish the dimension reference''',
    precision='The only established figure is 900 millimeters in an unclear opening note. Rough opening, finished opening, door size, and clear passage are not interchangeable labels. No conversion or allowance is supplied, and no door has been ordered.',
    precision_extra='Ask what the measurement runs between and what stage of construction it describes. A clarification can resolve the drawing meaning; it does not by itself establish a code-compliance finding. Do not calculate a usable width from an invented frame thickness.',
    phrases='''Locate the note | The hall drawing labels the door opening as 900 millimeters.\nClarify the assumption | Are you reading that as the clear passage width?\nName the ambiguity | The note does not say rough or finished opening.\nExplain the distinction | The opening reference and the usable passage are not necessarily the same.\nAsk about the reference | What surfaces does this dimension run between?\nKeep the number intact | I am not changing the figure of 900 millimeters.\nAvoid inventing an allowance | We do not have a confirmed frame allowance here.\nPreserve the order status | No door has been ordered.\nRefer the interpretation | Priya can clarify the measurement reference.\nAvoid a usable-width promise | I cannot confirm 900 millimeters of clear passage from this note.\nDistinguish product size | We should not treat this as the order size yet.\nAsk for explicit wording | Could the clarification identify the opening type?\nPreserve the client need | I will explain that your question concerns usable passage.\nAvoid a compliance claim | This conversation does not establish compliance.\nRead back the query | Does 900 refer to the rough opening, finished opening, or another reference?\nClose with the next step | I will request clarification before presenting the dimension as a confirmed usable width.''',
    notes='''Labels versus establishes | A drawing label states a number but may not establish its precise reference.\nClear | Describes unobstructed space, not merely a named opening size.\nRun between | Natural phrasing for the endpoints of a dimension.\nNot necessarily | Rejects an unsupported equivalence without asserting a specific alternative.\nNo order yet | Prevents the clarification discussion from sounding like a change to a placed order.\nReference | Names what the number actually measures, rather than questioning arithmetic.''',
    d='''Which question targets the missing information? | Does 900 millimeters refer to the rough opening, finished opening, or another reference? | Can we subtract an assumed frame width from 900? | Does 900 refer to the door leaf already selected? | Can we call 900 the usable width until someone objects? | The question asks what the stated dimension describes without assuming an interpretation.
Which reassurance is unsupported? | You will definitely have 900 millimeters of usable passage. | The note gives a 900-millimeter figure. | No door is ordered. | Priya can clarify the reference. | The note does not establish usable passage, so the reassurance exceeds the evidence.
What should remain unchanged in the query? | The stated 900-millimeter figure and the uncertainty about its reference | A guessed frame deduction | A fabricated confirmed order size | A claim that the drawing means finished opening | The query preserves the actual figure while asking for its unresolved meaning.
Which distinction matters for ordering? | An unclear opening note is not a confirmed door order size. | All opening and door dimensions are identical. | Client interpretation automatically authorizes an order. | A precise number removes every need for clarification. | The dimension reference must be clarified before it can support an appropriate product specification.''',
    dialogue='''Hana | Before we order the hall door, can I check this 900-millimeter note? I'm expecting that much space to walk through with the door open.
Ellis | The [[dimension reference::Dimension reference identifies what the 900-millimeter figure measures, which the current note does not make clear.]] is missing. It says door opening, but doesn't identify a rough opening, finished opening, or another measurement. I can't promise the walking space from that.
Hana | Right, I'm interested in the gap I can actually use, not the width of the door leaf. Have I been reading the wrong measurement?
Ellis | You're asking about [[clear passage::Clear passage is the usable unobstructed space Hana wants to understand, not automatically the dimension on the drawing.]]. It's a different question from the door's size, and the note doesn't establish that usable width.
Hana | When you say rough, do you mean the measurement isn't accurate? I'd prefer an exact figure before we choose anything.
Ellis | No, [[rough opening::Rough opening refers to the structural opening before the assembly and relevant finishes, not an approximate estimate of usable width.]] describes the structural opening before the assembly and relevant finishes. Rough names a construction stage here, not a rough guess.
Hana | I see. So which surfaces does this particular arrow measure between? The drawing isn't clear enough for me to tell.
Ellis | That's the missing [[reference face::Reference face names a surface used for measurement; the drawing note does not identify those surfaces clearly.]] information. We need the surfaces identified; subtracting a guessed allowance could give you a very misleading answer.
Hana | Has anyone already bought a door against that number? I'd rather raise it now than discover it doesn't give us the passage we need.
Ellis | No door is ordered, and the [[order size::Order size is not established by the ambiguous note, and no door has been ordered in this case.]] isn't confirmed. We're clarifying the drawing before purchasing, not changing an existing order.
Hana | Can Priya settle the meaning? She prepared the design, and I'd like her to understand why I'm asking about the space.
Ellis | I'll request [[designer clarification::Designer clarification is the appropriate route for resolving the intended measurement reference without a guessed interpretation.]] from Priya and include your question about walking through the doorway. She needs both the note and the practical concern.
Hana | Please don't change 900 to a different number in the message. I'm asking what it means, not instructing her to redesign it.
Ellis | Agreed. I'll quote the [[opening dimension::Opening dimension remains the stated 900 millimeters; the query concerns its meaning rather than a requested numerical change.]] of 900 millimeters exactly and ask which construction stage and measurement surfaces it refers to.
Hana | Would the frame take some of that space? I'm not asking you to work it out now, but I don't want it overlooked.
Ellis | The [[door frame::Door frame is a distinct component whose dimensions must not be silently equated with usable passage or the ambiguous opening note.]] is a separate component to consider. Its dimensions aren't supplied here, so I won't invent a thickness or a resulting clear width.
Hana | And we're not confirming that the doorway meets a particular access requirement today? I don't want to pass that on as settled.
Ellis | Correct. Resolving the [[drawing note::Drawing note needs an explanation of its measurement reference; the clarification conversation is not a compliance assessment.]] isn't a compliance assessment. We'll keep that distinction clear when we pass the question to Priya.
Hana | Then the message is: what does 900 measure, and what usable passage will this arrangement give? No order until the reference is resolved.
Ellis | Yes. The [[actual dimension::Actual dimension of the usable passage is not verified; the next step is clarification, not a width guarantee or product order.]] of that passage remains unverified. I'll send the query with the original note, without promising a width or a product size.''',
    transfer_title='Clarify before naming the usable width',
    transfer_setup='Complete the exchange about the hall drawing. Keep the given number, missing reference, unverified passage, and designer referral distinct.',
    transfer='''Client: "The drawing says ___ millimeters." | 900 | The stated figure is 900 millimeters, although its reference is unclear.
Carpenter: "The note does not identify rough or ___ opening." | finished | Finished is the alternative opening reference the note does not clarify.
Client: "My concern is the clear ___." | passage | Passage identifies the usable space Hana wants to understand.
Carpenter: "I will ask the ___ to clarify the reference." | designer | The designer can clarify the intended reference without the carpenter inventing it.''',
    rehearsal=["Read turns 1-10, stressing opening, passage, and ordered when each distinction changes the meaning.","Switch roles for turns 11-20; quote 900 exactly and keep Priya's clarification separate from a width guarantee.","Complete and check the four-line exchange. Read it aloud without subtracting an invented frame allowance."],
))

BOOK['units'].append(unit(
    title='Selecting timber, trim, and visible finishes',
    scene='Two oak samples, different trade-offs',
    skill='Compare specified material, appearance, profile, and quoted lead time without inventing quality rankings or selecting for the client.',
    brief='For a study remodel, carpenter Mei compares two trim samples with client Oliver. Sample A is solid oak with pronounced grain and a quoted ten-day lead time. Sample B is oak-veneered trim with a more uniform appearance and a quoted four-day lead time. Both match the requested profile. No sample is selected, and no price comparison, durability ranking, or installation date is supplied. Mei must keep the comparison tied to these samples rather than generalize about every solid or veneered product.',
    cast='Oliver | Client\nMei | Carpenter',
    culture=('Compare attributes without selling an unsupported conclusion', 'A client may ask which product is better when the real choice involves several preferences. Compare the known attributes side by side and clarify the selection status. Avoid implying that a shorter quoted lead time means better quality or that a material name establishes every performance characteristic.'),
    a='''Which description belongs to sample A? | Solid oak, pronounced grain, ten-day quoted lead time | Oak veneer, uniform appearance, four days | Plastic trim, no grain, immediate delivery | A selected product with a confirmed installation date | Sample A has the specified solid-oak construction, pronounced grain, and ten-day quote.
What do the samples have in common? | Both match the requested profile | Both have the same quoted lead time | Both have identical grain appearance | Both have already been selected | The shared attribute is the requested profile, not construction, appearance, or timing.
What remains undecided? | Which sample to select | Whether B has the shorter quoted lead time | Whether A is solid oak | Whether both match the profile | No selection has been made, although the comparison attributes are stated.''',
    vocabulary='''solid oak | Material made from oak wood rather than an oak surface veneer over a core. | specify solid oak trim
oak veneer | Thin oak layer applied over a supporting material. | identify the oak veneer
veneered trim | Trim with a veneer surface over a core. | compare veneered trim
timber | Wood prepared or used for building and joinery. | specify the timber
trim | Finishing material used at edges, joints, or decorative features. | compare the trim samples
profile | Cross-sectional shape of a trim piece or molding. | match the requested profile
grain | Visible pattern associated with the wood's structure. | compare the grain
pronounced grain | Strongly visible wood pattern. | describe pronounced grain
uniform appearance | More consistent visual character across the sample. | describe a uniform appearance
core material | Supporting material beneath a surface layer. | identify the core material
face veneer | Veneer on the visible face of a product. | specify the face veneer
edge treatment | Way the edge of a component is finished or covered. | clarify the edge treatment
finish sample | Example showing a proposed surface appearance. | review the finish sample
sheen | Degree of surface reflectivity. | compare the sheen
clear finish | Coating that allows underlying material to remain visible. | specify a clear finish
opaque finish | Coating that hides the underlying material's appearance. | distinguish an opaque finish
stain | Coloring treatment used to change wood's appearance. | clarify the stain color
quoted lead time | Supply interval stated in a quotation or proposal. | compare quoted lead times
selection status | Whether a choice has been made. | confirm the selection status
material construction | How a product is made up of its constituent materials. | compare material construction
visual preference | Appearance favored by the client. | clarify the visual preference
sample approval | Acceptance of a particular reference sample. | record sample approval
performance claim | Statement about how a product will function or endure. | avoid an unsupported performance claim
installation date | Scheduled day for fitting work at the site. | confirm the installation date''',
    precision='Sample A has pronounced grain and a ten-day quoted lead time. Sample B has a more uniform appearance and a four-day quote. Both match the profile. These are sample-specific facts, not universal claims about solid oak and veneered products.',
    precision_extra='No prices, durability results, finish specifications, or installation dates are given. A shorter lead time does not establish a lower price or better performance. Comparing options does not mean the client has approved either sample or placed an order.',
    phrases='''Open the comparison | Both samples match the requested profile.\nDescribe A's construction | Sample A is solid oak.\nDescribe B's construction | Sample B is oak-veneered trim.\nDescribe A's appearance | A has more pronounced grain.\nDescribe B's appearance | B has a more uniform appearance.\nState A's timing | A has a quoted ten-day lead time.\nState B's timing | B has a quoted four-day lead time.\nMake a bounded comparison | B has the shorter quoted lead time for these two samples.\nAvoid a price inference | We do not have a price comparison here.\nAvoid a quality ranking | The material names alone do not establish which will perform better.\nPreserve the shared feature | The profile is not the difference between them.\nClarify the preference | Is the more visible grain the appearance you prefer?\nSeparate discussion and selection | Discussing A does not mean you have selected it.\nKeep the date distinction | A quoted lead time is not an installation appointment.\nPreserve the decision status | No sample is selected yet.\nSummarize the trade-off | The known differences are construction, appearance, and quoted lead time.''',
    notes='''More pronounced | Compares the visible grain of these samples without declaring one superior.\nMore uniform | Describes appearance, not guaranteed consistency of every future piece.\nBoth | Signals the shared profile rather than identical materials.\nQuoted | Attributes the timing to the supplied quotation rather than a universal delivery rule.\nBetter | Needs a stated criterion before it becomes a meaningful comparison.\nSelected | A decision status that must not be inferred from a favorable comment.''',
    d='''Which comparison is fully supported? | A is solid oak with pronounced grain and ten days; B is veneered with a more uniform look and four days. | A is cheaper and B is stronger. | B always lasts longer than solid oak. | A is booked for installation in ten days. | The comparison uses the stated construction, appearance, and quoted timing without adding unsupported claims.
Which attribute does not distinguish the samples? | The requested profile, which both match | Solid versus veneered construction | Pronounced versus more uniform appearance | Ten versus four quoted days | Both samples meet the requested profile, so it is their shared attribute.
Which statement overgeneralizes? | Veneered trim always arrives in four days. | B is quoted at four days. | A is quoted at ten days. | Neither sample is selected. | The four-day quote belongs to sample B, not every veneered product.
How should Mei record Oliver's interest in A? | A is under discussion; no selection has been made. | A has been purchased and installed. | Both samples are rejected. | B is approved because it is quicker. | Interest or discussion alone does not establish selection, purchase, or installation.''',
    dialogue='''Oliver | Both shapes look right for the study. Before I choose, what is actually different between these samples apart from the price, which I haven't seen?
Mei | There is a difference in [[material construction::Material construction distinguishes solid oak in A from oak veneer over a supporting material in B.]]. Sample A is solid oak, while sample B is oak-veneered trim. Both match the profile you requested for the study.
Oliver | A's grain stands out much more against this wall color. B looks quieter. Is that just what we're seeing in these particular pieces?
Mei | A has [[pronounced grain::Pronounced grain describes the stronger visible pattern on sample A without making a quality or durability claim.]], and B has a more uniform appearance. Those are the visual differences stated for these samples, not a ranking of quality.
Oliver | So B has real oak on the surface, over something else? What is underneath it, or don't we have that specification here?
Mei | Yes, [[oak veneer::Oak veneer is the thin oak surface layer over a supporting material; it is not the same construction as solid oak.]] refers to that surface layer. I do not have a specification for the supporting material here, so I should not name a core that is not listed.
Oliver | Remind me which one has the shorter lead time. I don't want to mistake a supplier quote for the day you'll fit it.
Mei | The [[quoted lead time::Quoted lead time is ten days for A and four for B; these figures do not establish installation appointments.]] is ten days for A and four days for B. Those are supply quotes, not confirmed installation appointments.
Oliver | That makes B six days quicker on the quote. I still prefer A's grain, so I'm not ready to choose on timing alone.
Mei | Exactly. Your [[visual preference::Visual preference concerns the appearance Oliver favors and remains one consideration alongside the stated timing and construction.]] and the timing are separate considerations. We can compare them without deciding that one sample is better in every respect.
Oliver | And I wouldn't lose this edge shape by choosing B? The study trim needs the profile we've already discussed.
Mei | Both match the requested [[profile::Profile is the cross-sectional shape, which both samples match; it is not a difference between these options.]]. The known differences here are construction, grain appearance, and quoted lead time, not the shape you specified.
Oliver | Do we have prices or durability information yet? I don't want to assume veneered automatically means cheaper or less hard-wearing.
Mei | We do not have a price comparison. I also cannot support a [[performance claim::Performance claim would assert durability or function not supplied by the sample comparison; material names alone do not establish it.]] about which lasts longer from the information on these two samples.
Oliver | I'm leaning toward A, but please don't order it on that basis. I still need the missing details before I approve anything.
Mei | I will keep the [[selection status::Selection status remains undecided; Oliver's favorable comment about A is not approval or an order instruction.]] open. We can note your interest in A without recording it as an approved sample or a placed order.
Oliver | Can you keep the finish details and prices as outstanding questions? They matter to the decision as well as the grain and lead time.
Mei | We can keep those as separate questions before [[sample approval::Sample approval has not been given; the missing comparisons and Oliver's final choice remain unresolved.]]. Nothing in this discussion establishes a finish specification, a price, or a guarantee about future product performance.
Oliver | Let me read that back: A, solid oak, stronger grain, ten days; B, veneered, more uniform, four days. Neither has an installation booking.
Mei | Correct, and neither quote is an [[installation date::Installation date is not supplied by either lead-time quote, and no sample selection or fitting appointment is confirmed.]]. Both match the profile, no sample is selected, and the other details remain to be confirmed before a decision.''',
    transfer_title='Compare without choosing for the client',
    transfer_setup='Complete the sample comparison. Use the stated construction, appearance, lead time, and decision status; do not add prices or durability claims.',
    transfer='''Carpenter: "Sample A is solid ___." | oak | Oak is the stated solid material used for sample A.
Client: "B has the more ___ appearance." | uniform | Uniform describes B relative to the pronounced grain of A.
Carpenter: "B has a quoted ___-day lead time." | four | Four days is B's quoted supply interval, not an installation date.
Client: "Neither sample is ___ yet." | selected | No selection has been made despite discussion of both samples.''',
    rehearsal=["Read turns 1-10 with a partner, stressing A, B, ten days, and four days.","Switch roles for turns 11-20; separate matching profile from price, performance, and approval.","Complete and check the short exchange. Read the corrected comparison without turning a supply quote into an installation date."],
))

BOOK['units'].append(unit(
    title='Reading details and resolving drawing conflicts',
    scene='Two reveals on revision B',
    skill='Identify a drawing conflict precisely, preserve revision and location details, and request clarification without choosing a dimension by convenience.',
    brief='Carpenter Arun and coordinator Lena review cabinet drawings before a fabrication-release review due at 14:00. Elevation C4 revision B shows a 20-millimeter reveal at an end panel. Section S2 revision B shows 15 millimeters at the same panel. The designer has not clarified which dimension applies. Both sheets carry the same revision letter, so the team cannot resolve the discrepancy by assuming one is a later issue. No dimension is authorized through this conversation.',
    cast='Arun | Carpenter\nLena | Project coordinator',
    culture=('Make a conflict easy to answer', 'A useful clarification request contains both drawing references, their revisions, the exact location, and the conflicting values. Include the review deadline as a coordination fact, not a reason to guess. Shared revision labels do not make incompatible dimensions agree.'),
    a='''What conflict is shown? | C4 revision B gives 20 millimeters; S2 revision B gives 15 at the same panel | C4 gives 15 and S2 gives 20 at different rooms | Both drawings give 20 | One drawing is revision C | The two revision-B sheets give different reveal values at the same end panel.
What is due at 14:00? | The fabrication-release review | Guaranteed installation completion | A confirmed designer reply | Delivery of all cabinets | The supplied time belongs to the review, not a promised answer or completed fabrication.
Who has not yet clarified the dimension? | The designer | A customer who already approved 20 | A fabricator who already approved 15 | A supplier who changed the drawings | The designer has not resolved which dimension applies.''',
    vocabulary='''elevation | Drawing view showing a face of an object or building. | read the cabinet elevation
section | Drawing view representing a cut through an object or assembly. | compare the section
reveal | Defined visible gap or exposed setback between adjacent components. | confirm the reveal dimension
end panel | Panel forming or covering an exposed end of cabinetry. | identify the end panel
revision | Identified issue or update of a drawing or document. | verify the revision
drawing conflict | Inconsistent information between relevant drawings. | flag a drawing conflict
dimension discrepancy | Difference between dimensions that should describe the same detail. | report a dimension discrepancy
fabrication | Manufacture of components or assemblies. | clarify before fabrication
release review | Review of readiness or permission to issue work for the next stage. | attend the release review
shop drawing | Detailed production or installation drawing for a specific assembly. | review the shop drawing
detail reference | Identifier pointing to a particular drawing detail. | include the detail reference
sheet number | Identifier of a drawing sheet. | quote the sheet number
revision cloud | Drawing mark identifying an area of change. | locate the revision cloud
superseded drawing | Earlier drawing replaced by a later authorized issue. | identify a superseded drawing
design intent | Intended design result communicated through the project information. | clarify the design intent
request for information | Formal or recorded query seeking missing or unclear project information. | submit a request for information
clarification response | Reply resolving a stated information question. | await the clarification response
applicable dimension | Measurement confirmed as relevant to the detail. | verify the applicable dimension
fabrication release | Authorization or controlled issue allowing production to proceed. | confirm fabrication release
review deadline | Time by which a review is due. | state the review deadline
unresolved detail | Information point not yet clarified. | flag an unresolved detail
cross-reference | Link between related drawing views or documents. | check the cross-reference
kerf | Width of material removed by a cut, distinct from blade plate thickness. | allow for the kerf
cut list | List of required parts, quantities, and finished dimensions. | review the cut list''',
    precision='The difference is five millimeters, but calculating that difference does not identify the correct reveal. Both C4 and S2 are revision B and refer to the same panel. Neither sheet is established as superseded or authoritative over the other.',
    precision_extra='14:00 is the fabrication-release review time. It is not an instruction to choose a dimension, a confirmed designer-response time, or evidence that fabrication is released. Refer both values and the precise location through the actual project clarification process.',
    phrases='''Flag the issue | I found a conflict at the cabinet end panel.\nCite the first view | Elevation C4 revision B shows a 20-millimeter reveal.\nCite the second view | Section S2 revision B shows 15 millimeters.\nConfirm the shared location | Both dimensions refer to the same end panel.\nCheck the issue labels | Both sheets are marked revision B.\nState the difference | The values differ by five millimeters.\nReject a revision shortcut | We cannot identify a newer sheet from those labels alone.\nName the missing answer | The designer has not clarified which dimension applies.\nRequest a decision | Please confirm the applicable reveal dimension.\nPreserve the review time | The fabrication-release review is due at 14:00.\nAvoid a response promise | That review time is not a guaranteed designer-response time.\nKeep production status separate | The conflict discussion does not authorize fabrication.\nKeep both references | I will include C4 and S2 in the query.\nAvoid averaging | I will not use the midpoint as an invented solution.\nAsk for an explicit response | The reply needs to identify the dimension for this panel.\nClose with the current status | The detail remains unresolved pending clarification.''',
    notes='''At the same panel | Establishes that the two values conflict rather than describe separate locations.\nRevision B | A shared issue label, not proof that the content agrees.\nApplies | Asks which dimension governs the specific detail.\nDue for review | Describes a planned decision point without implying approval.\nPending clarification | Keeps the question open until a response resolves it.\nFive-millimeter difference | Correct arithmetic that does not answer which value is intended.''',
    d='''Which query is complete? | At the same end panel, C4 rev B shows 20 mm and S2 rev B shows 15 mm; please clarify for the 14:00 release review. | Please confirm 20 mm on C4 without mentioning S2. | Use 15 mm because the section must take precedence. | Release at 17.5 mm as a compromise between the views. | The complete query includes location, both references, conflicting values, and the review time.
Which proposed shortcut is unsupported? | Average the values and fabricate a 17.5-millimeter reveal. | Ask the designer to clarify. | Preserve both revision labels. | Flag the unresolved detail for review. | No authority is given to invent a midpoint or release fabrication from conflicting dimensions.
What do the revision labels establish? | Both sheets are marked B, not which dimension is correct | C4 is definitely newer | S2 is superseded | The reveal is automatically 20 | The shared letter does not identify precedence or resolve the inconsistent detail.
Which status is accurate at the end? | The reveal remains unresolved and fabrication is not authorized by this conversation. | The designer has approved 15. | The review deadline authorizes 20. | Installation is complete. | No designer clarification or fabrication authorization is supplied during the exchange.''',
    dialogue='''Arun | Lena, can we stop on the end-panel detail before the release review? The elevation and section give different reveals at the same panel.
Lena | Give me each [[sheet number::Sheet number locates each drawing precisely for the designer's review of the conflict.]] and revision, please. I want the designer to find the conflict without having to guess which cabinet we're discussing.
Arun | Elevation C4, revision B: twenty millimeters. Section S2, also revision B: fifteen. I've checked that they point to this same end panel.
Lena | That's a five-millimeter [[dimension discrepancy::Dimension discrepancy is 20 versus 15 millimeters at the same end panel, not two unrelated measurements.]]. Has the designer answered it in a separate message, or are we still waiting for the intended reveal?
Arun | Still waiting. The workshop has asked which figure to use. I can't choose twenty just because the elevation is the clearer view.
Lena | Nor can we choose fifteen for convenience. We need a [[clarification response::Clarification response must resolve the intended dimension; convenience or drawing readability does not establish the correct value.]] identifying the intended value and the detail it applies to.
Arun | Someone thought S2 might be the old sheet. Both labels say B, though, and I haven't found anything establishing that either has been replaced.
Lena | Then don't mark it a [[superseded drawing::Superseded drawing would mean an earlier issue had been replaced; the shared B labels do not establish that status.]]. Matching revision letters don't resolve a conflict or tell us that the elevation takes precedence.
Arun | The fabrication-release review is at fourteen hundred. Can the query say that, so the designer understands the timing without reading the whole schedule?
Lena | I'll include the [[review deadline::Review deadline is 14:00 for the fabrication-release review, not an agreed designer-response time or automatic production permission.]]. It's the review time, not a promised response time, and it doesn't give us permission to pick a dimension.
Arun | Put both values in the actual question, please. If the message just says end-panel query, it may come back asking for the missing numbers.
Lena | I'll state the [[drawing conflict::Drawing conflict keeps both incompatible values and their references visible in the handoff.]] in one sentence: C4 rev B shows twenty, S2 rev B shows fifteen, at the same end panel.
Arun | And ask specifically for the reveal. I don't want this turned into a request to recheck every dimension in the cabinet package.
Lena | Agreed. The [[applicable dimension::Applicable dimension concerns the reveal at this end panel, not every cabinet measurement.]] is the reveal at this location. A precise query doesn't imply we've verified the rest of the package.
Arun | If the answer hasn't arrived by the review, what goes in the record? Leaving the box empty could make it look resolved.
Lena | Record an [[unresolved detail::Unresolved detail keeps the unanswered reveal question visible instead of allowing silence to imply that it has been settled.]], with the query reference. No reply is not approval of either figure, and the conflicting values must remain visible.
Arun | The other suggestion was seventeen and a half, splitting the difference. That would keep everyone moving, but it's not on either drawing.
Lena | Averaging isn't [[design intent::Design intent requires clarification; averaging the conflicting values invents a result instead of establishing it.]]. Seventeen and a half would be a third, invented dimension, not a resolution of the two we were given.
Arun | Understood. I'll bring both sheets to the fourteen-hundred review and keep the reveal outstanding. Can you send the specific question now?
Lena | Yes. The query doesn't grant [[fabrication release::Fabrication release is not granted here; the reveal still requires designer clarification.]]. I'll preserve both references, values, and the unresolved status so the release decision isn't based on an assumption.''',
    transfer_title='Refer the conflicting detail',
    transfer_setup='Complete the drawing query using both references and values. Keep the shared revision and the unresolved status intact.',
    transfer='''Carpenter: "Elevation ___ revision B shows 20 millimeters." | C4 | C4 is the elevation reference carrying the 20-millimeter reveal.
Coordinator: "Section S2 revision B shows ___ millimeters." | 15 | Fifteen millimeters is the conflicting value on section S2.
Carpenter: "Both refer to the same end ___." | panel | The shared panel location is why the values conflict.
Coordinator: "The designer has not yet ___ the applicable dimension." | clarified | No clarification has resolved the conflict or authorized a dimension.''',
    rehearsal=["Read turns 1-10; pronounce both sheet references, revision letters, and millimeter values distinctly.","Switch roles for turns 11-20. Stress unresolved and keep the 14:00 review distinct from release.","Check the short exchange, then read it without replacing the conflict with an average or assumed drawing precedence."],
))

BOOK['units'].append(unit(
    title='Discussing concealed conditions without guessing',
    scene='Staining is not a structural finding',
    skill='Describe an exposed condition, explain what cannot be seen, and refer a structural concern without diagnosing concealed timber.',
    brief='At a laundry remodel, client Theo notices dark staining on exposed subfloor beside the laundry doorway. He asks carpenter Nia whether the joists are rotten. The joists are not visible, and Nia has not assessed structural condition. Project lead Sam can arrange a qualified assessment. Nia must describe the visible staining and the limits of her knowledge without confirming decay, declaring the structure sound, identifying a cause, or promising a repair.',
    cast='Theo | Client\nNia | Carpenter',
    culture=('Take the concern seriously without guessing', 'A worried client may hear uncertainty as evasiveness. Give a concrete observation and explain the visibility limit before naming the assessment route. Neither alarming certainty nor unsupported reassurance helps the client understand what is actually known.'),
    a='''What is visible? | Dark staining on exposed subfloor beside the laundry doorway | Rotten joists confirmed by assessment | Repaired structural members | A verified leak source | Only the staining on the exposed subfloor is directly visible.
What limits Nia's conclusion? | The joists are not visible and structural condition has not been assessed | A completed assessment proves no concern | The client has already supplied a diagnosis | Every concealed member has been inspected | The concealed joists and lack of structural assessment prevent a supported diagnosis.
What can Sam arrange? | A qualified assessment | A repair already completed | A guaranteed replacement price | A finding that the structure is sound | Sam can arrange assessment, but no finding, repair, or price is supplied.''',
    vocabulary='''subfloor | Supporting floor layer beneath the finished floor covering. | describe the exposed subfloor
joist | Structural member supporting a floor or ceiling over a span. | refer to the concealed joists
floor covering | Visible finish material laid over the floor base. | distinguish the floor covering
exposed surface | Area visible after a covering is absent or removed. | describe the exposed surface
concealed condition | State of material or construction hidden from view. | refer a concealed-condition concern
dark staining | Visible discoloration with a dark appearance. | report dark staining
discoloration | Change in the apparent color of a surface. | describe the discoloration
timber decay | Deterioration of wood through biological action. | avoid diagnosing timber decay
structural condition | State of components relevant to carrying loads. | request assessment of structural condition
load-bearing member | Component intended to support structural loads. | identify the load-bearing member
moisture source | Origin of water or dampness affecting an area. | investigate the moisture source
water ingress | Entry of water into an area or construction. | report a concern about water ingress
inspection access | Ability to reach or view an area for examination. | confirm inspection access
visibility limit | Boundary of what can actually be seen. | explain the visibility limit
qualified assessor | Person competent to examine the relevant condition. | refer to a qualified assessor
assessment scope | Matters included in a specified examination. | confirm the assessment scope
site observation | Condition directly noticed at the location. | record a site observation
unsupported diagnosis | Conclusion about a problem without adequate assessment. | avoid an unsupported diagnosis
structural finding | Conclusion reached through appropriate structural assessment. | distinguish a structural finding
repair proposal | Suggested work to address an established issue. | await a repair proposal
investigation status | Current stage of checking an unresolved concern. | report the investigation status
laundry doorway | Opening at the entrance to the laundry area. | locate the laundry doorway
condition report | Record describing an examined or observed state. | prepare an accurate condition report
referral route | Process for passing a concern to the appropriate person. | explain the referral route''',
    precision='The visible staining is on the exposed subfloor, not on visible joists. Theo raises possible rot as a question. The joists are concealed and structural condition has not been assessed, so neither decay nor structural soundness is established.',
    precision_extra='The location and appearance can be recorded without naming a cause. Sam can arrange a qualified assessment, but the dialogue does not authorize opening up construction, select a testing method, or establish a repair scope, price, or timetable.',
    phrases='''Name the observation | I can see dark staining on the exposed subfloor.\nLocate it precisely | It is beside the laundry doorway.\nAcknowledge the concern | I understand why you are asking about the joists.\nState the visibility limit | The joists are not visible here.\nState the assessment limit | I have not assessed the structural condition.\nAvoid a diagnosis | I cannot confirm that the joists are rotten.\nAvoid false reassurance | I cannot declare them sound from this view either.\nKeep cause open | The cause of the staining has not been established.\nSeparate surfaces | The visible subfloor and the concealed joists are different parts.\nRefer the concern | Sam can arrange a qualified assessment.\nAvoid a repair promise | No repair scope or price is established.\nPreserve the client's question | I will include your concern about possible decay.\nUse neutral wording | Dark staining observed; concealed condition unassessed.\nAvoid an invented finding | There is no structural finding to report yet.\nKeep the next step clear | The next step is assessment, not a guessed repair.\nRead back the record | Staining beside the laundry doorway, with joists not visible and cause unknown.''',
    notes='''Rotten | A diagnosis the client asks about, not a finding the worker can confirm.\nExposed versus concealed | Distinguishes what can be seen from what remains hidden.\nCannot confirm | Limits certainty without asserting that the concern is impossible.\nEither | Helps balance an unsupported negative conclusion with an unsupported reassurance.\nArrange | Names a next step without claiming it has already happened.\nUnassessed | Means no relevant assessment has been made, not that the condition is acceptable.''',
    d='''Which report separates observation from diagnosis? | Dark staining is visible on the subfloor; the concealed joists have not been assessed. | The joists are rotten because the subfloor is dark. | The whole floor is structurally sound. | A leak has definitely damaged every joist. | The report states the visible fact and preserves the unassessed concealed condition.
Which answer to Theo is unsupported? | The joists are definitely sound because we cannot see damage. | The joists are not visible. | Structural condition has not been assessed. | Sam can arrange an assessment. | Inability to see the joists cannot establish that they are structurally sound.
Which location should the referral include? | Beside the laundry doorway | An invented roof leak location | Every wall in the house | A joist already exposed elsewhere | The supplied location helps the assessor identify the actual observed area.
What remains unknown? | The cause, concealed structural condition, and any required repair | Whether staining is visible | Whether Theo asked about rot | Whether the joists are concealed | No assessment has established the cause, structural condition, or appropriate repair.''',
    dialogue='''Theo | Nia, this dark patch by the laundry door looks worrying. Is that rot in the joists, or am I jumping to conclusions?
Nia | What I can identify is [[dark staining::Dark staining is the observed discoloration on the exposed subfloor, not a confirmed finding of decay in concealed joists.]] on the exposed subfloor. The joists aren't visible, and I haven't assessed the structural condition.
Theo | I thought what we're looking at might be the joists themselves. Are those different from this exposed layer?
Nia | Yes. This is the [[subfloor::Subfloor is the visible supporting floor layer in this case, distinct from the concealed joists about which Theo asks.]]; the joists beneath it are concealed. A mark here doesn't tell us whether those hidden members have decay.
Theo | So you can record the stain, but not my guess about what caused it as though it's a finding?
Nia | Exactly. I'll separate the [[site observation::Site observation preserves the visible staining and its location without turning the client's proposed explanation into a diagnosis.]] from your question: visible discoloration here, and a concern about the condition of the concealed joists.
Theo | Could it be coming from the laundry? That was my first thought because it's so close to the doorway.
Nia | The [[moisture source::Moisture source has not been established; the question about water does not prove where it came from or what it affected.]] isn't established. The location is useful to report, but it doesn't prove a leak or tell us where any water came from.
Theo | Who should look into it? I'd like someone qualified to assess it before I'm told the floor needs replacing.
Nia | I'll contact Sam to arrange a [[qualified assessor::Qualified assessor is the appropriate person to examine the relevant concern; no completed assessment or finding exists yet.]]. The referral will give the location, what is exposed, and what we cannot currently see.
Theo | Does that mean replacement is likely? I'm trying to work out whether we need to budget for a much bigger job.
Nia | We don't have a [[repair proposal::Repair proposal is not established by requesting an assessment; replacement, cost, and disruption have not been determined.]] yet. Asking for an assessment doesn't establish replacement, a price, or the disruption involved.
Theo | Would it be reasonable to say the joists are probably fine until someone finds damage? Or is that going too far as well?
Nia | The [[visibility limit::Visibility limit prevents both a confirmed decay diagnosis and a claim that concealed structural members are sound.]] works both ways. I can't confirm decay, but hidden joists also prevent me from assuring you that the structure is sound.
Theo | All right. Please don't describe today's conversation as a structural inspection. I can imagine that getting repeated later as an all-clear.
Nia | I'll keep the [[investigation status::Investigation status remains unassessed for structural condition; describing staining is not equivalent to completing an inspection.]] explicit: structural condition not assessed. The visible concern is being referred, not diagnosed or signed off.
Theo | Can you read the location back? There are two laundry doors, and I don't want the person coming out to review the wrong patch.
Nia | The note identifies the exposed subfloor beside this [[laundry doorway::Laundry doorway is the specific location of the observation, allowing the referral to identify the relevant area accurately.]], with the staining shown in the referral record. It also states that the joists are concealed.
Theo | Yes, that's the area. Please give Sam the question as well as the observation, so it doesn't become just a cosmetic stain report.
Nia | I will use that [[referral route::Referral route passes the concern to Sam for arranging qualified assessment, without inventing a diagnosis or authorizing a repair.]] and include your concern about possible decay. I won't add a repair conclusion or a claim of structural safety.''',
    transfer_title='Describe what is visible',
    transfer_setup='Complete the report to the project lead. Keep the observed surface separate from the concealed joists and the unperformed assessment.',
    transfer='''Carpenter: "Dark staining is visible on the exposed ___." | subfloor | Subfloor is the visible layer carrying the reported staining.
Client: "The joists are not ___." | visible | The joists remain concealed, so their condition cannot be judged from this view.
Carpenter: "Structural condition has not been ___." | assessed | No structural assessment has occurred in the supplied case facts.
Client: "Please ask Sam to arrange a qualified ___." | assessment | Assessment is the available next step, not a confirmed diagnosis or repair.''',
    rehearsal=["Read turns 1-10 with a partner; distinguish the visible subfloor from the concealed joists.","Switch roles for turns 11-20. Retain both limits: no confirmed decay and no assurance of structural soundness.","Check the transfer answers, then read the referral with the location and Sam's role intact."],
))

BOOK['units'].append(unit(
    title='Separating requested extras from agreed work',
    scene='A bench beyond the skirting scope',
    skill='Explain the agreed task, clarify an additional request, and discuss a separate quotation without implying approval or completion timing.',
    brief='At a bedroom remodel, carpenter Jules reviews the scope with client Amara. The agreed work is replacing skirting only. Decorating is excluded. Amara asks for a built-in bench as an extra. Jules can arrange a separate quotation, but no bench dimensions, price, or completion date are agreed. The conversation must distinguish the existing trim work from the requested bench and must not imply that decorating or a free extra is included.',
    cast='Amara | Client\nJules | Carpenter',
    culture=('A helpful referral can preserve a firm scope limit', 'An additional request often arises when a client sees the room taking shape. Acknowledge the idea, identify the existing agreement, and offer the actual quotation route. Avoid making the client feel dismissed while also avoiding a casual promise that creates a different expectation.'),
    a='''What is included in the current scope? | Replacing bedroom skirting only | A built-in bench and full decorating | All bedroom furniture | A confirmed bench installation | The agreed scope is limited to replacing the bedroom skirting.
What is the new request? | A built-in bench | The skirting replacement already agreed | A completed painting inspection | A warranty extension | Amara requests a built-in bench in addition to the existing work.
What can Jules arrange? | A separate quotation, with dimensions, price, and date still unagreed | A free bench completed tomorrow | Automatic decorating | A confirmed bench design already approved | The separate quotation route is available, but the bench terms have not been established.''',
    vocabulary='''skirting | Trim along the base of an internal wall, often called baseboard. | replace the skirting
baseboard | Common North American term for trim at the foot of an internal wall. | compare baseboard profiles
built-in bench | Fixed seating integrated into a room or fitted assembly. | request a built-in bench
agreed scope | Work explicitly included in the current agreement. | confirm the agreed scope
scope exclusion | Work or condition left outside the agreement. | explain the scope exclusion
decorating | Surface finishing work such as painting or wallpapering. | distinguish decorating from carpentry
additional work | Task requested beyond the existing scope. | quote for additional work
separate quotation | Distinct price proposal for specified extra work. | arrange a separate quotation
bench dimensions | Measurements defining the proposed bench. | agree the bench dimensions
design brief | Statement of the requirements for a proposed design. | clarify the design brief
seat height | Vertical position of a seat surface from a stated reference. | confirm the seat height
seat depth | Front-to-back dimension of a seat surface. | clarify the seat depth
overall length | Full end-to-end measurement of an item. | confirm the overall length
finish requirement | Specified surface appearance or treatment. | clarify the finish requirement
quotation scope | Tasks and terms covered by a price proposal. | define the quotation scope
variation | Agreed or proposed change to the original work arrangement. | record a proposed variation
change authorization | Permission to alter the agreed work. | obtain change authorization
price agreement | Acceptance of a stated cost for defined work. | confirm the price agreement
completion commitment | Agreed promise about when work will finish. | avoid an unsupported completion commitment
book matching | Pairing consecutive veneer leaves by alternating their faces for mirrored grain. | specify book matching
measurement visit | Attendance to establish relevant dimensions. | discuss a measurement visit
client approval | Acceptance from the client through the relevant process. | record client approval
existing contract | Current agreement governing the booked work. | distinguish the existing contract
scope handoff | Transfer of the task description for further review or quotation. | make a clear scope handoff''',
    precision='Replacing the bedroom skirting is the only agreed task. The bench is an additional request, and decorating is excluded. A separate quotation can be arranged, but the request itself does not establish bench measurements, an accepted price, or a completion date.',
    precision_extra='Do not convert a sketch, preference, or informal conversation into an agreed design. The case provides no bench dimensions or finish specification. Keep the current task intact while passing the extra request through the actual quotation and approval process.',
    phrases='''Acknowledge the idea | I understand you would like a built-in bench as well.\nName the agreement | The current scope is replacing the bedroom skirting only.\nState the exclusion | Decorating is excluded from this booking.\nSeparate the extra | The bench is additional work, not part of the existing task.\nOffer the next step | I can arrange a separate quotation.\nKeep dimensions open | We have not agreed the bench dimensions.\nKeep price open | There is no agreed bench price yet.\nKeep timing open | No completion date is confirmed for the bench.\nAvoid a free-extra promise | I cannot treat the bench as a free addition.\nAvoid bundling decorating | A bench request does not add painting to the current scope.\nClarify the proposal | We need a defined bench request for the quotation.\nSeparate asking and approving | Asking for a quote does not approve the extra work.\nPreserve existing work | The skirting replacement remains the agreed task.\nAvoid designing by assumption | I will not put guessed measurements into the handoff.\nRead back the request | Built-in bench requested; dimensions, price, and timing unresolved.\nClose with the route | I will pass the bench request for a separate quotation.''',
    notes='''Only | Makes the limit of the current skirting scope explicit.\nAs well | Introduces an addition without proving it is included.\nQuote for | Describes pricing a defined proposal rather than authorizing the work.\nNot yet agreed | Preserves the possibility of a later agreement without inventing one now.\nExcluded | Applies to decorating in the current booking, not necessarily every future service.\nProposed variation | Identifies a possible change before it becomes an authorized one.''',
    d='''Which scope summary is accurate? | Skirting replacement only; decorating excluded; bench requested separately. | Bench and decorating already included. | All bedroom work is free because the crew is present. | The skirting task has been cancelled. | The summary preserves the existing task, the exclusion, and the separate new request.
Which response is helpful without overpromising? | I can arrange a separate quotation, with dimensions and timing still to be agreed. | I guarantee a bench tomorrow at no charge. | The question itself changes the contract. | I will invent dimensions to speed things up. | The quotation route acknowledges the request while preserving the unresolved bench details.
What does requesting a quote establish? | Interest in having the extra work priced, not approval to perform it | A final price agreement | A confirmed completion date | Approval of any design | A quotation request is not acceptance of terms or authorization of the additional work.
Which item must remain excluded from the current booking? | Decorating | Skirting replacement | Recording the bench request | Clarifying the existing task | Decorating is explicitly excluded and is not added by the bench discussion.''',
    dialogue='''Amara | While you're doing the bedroom skirting, could you also build a bench along that wall? I'm wondering whether it could be added to this visit.
Jules | I can pass on the idea, but the [[agreed scope::Agreed scope is bedroom skirting replacement only; the bench request does not automatically belong to that agreement.]] is skirting replacement only. A built-in bench would be a separate item rather than part of the existing task.
Amara | I realize it isn't another piece of skirting. I thought being here already might make it simpler, but I haven't worked out the details.
Jules | It is [[additional work::Additional work describes the bench beyond the existing skirting task, even though both would be in the same bedroom.]], and we need a defined proposal for it. Being on site does not establish the dimensions, the price, or when it could be completed.
Amara | Could I get a separate price before I decide? I'm asking for an option, not telling you to start building it.
Jules | I can arrange a [[separate quotation::Separate quotation is the available route for pricing the bench request; it is not an accepted price or permission to begin.]]. Asking for that quote does not mean you have approved the bench or agreed to pay an amount we have not supplied.
Amara | I haven't settled the length or depth. When I pointed at the wall, I didn't mean that the bench must fill the whole space.
Jules | I will keep the [[bench dimensions::Bench dimensions are not agreed; a pointing gesture does not establish length, depth, height, or a final design.]] unresolved. The handoff will describe a built-in bench request without turning your gesture into a fixed length or depth.
Amara | What about painting? I know decorating isn't in the present booking. Would a bench quote need to say explicitly whether finishing is included?
Jules | The current [[scope exclusion::Scope exclusion keeps decorating outside the existing booking; the bench discussion does not silently add painting or other finishing work.]] remains decorating. The bench request does not add painting to today's agreement, and any proposed finish would need to be stated in its own quotation.
Amara | Yes, I'd rather see what's covered than compare prices that mean different things. The finish could affect which proposal I accept.
Jules | A clear [[quotation scope::Quotation scope identifies what a proposed price covers, including any stated finish requirements, rather than relying on an unstated assumption.]] matters. We should not promise a finish, a design, or a service that has not been defined in the proposal.
Amara | Could it be finished this week? I'm asking whether that's possible, but I don't want you to put a date into the quote without checking.
Jules | No [[completion commitment::Completion commitment for the bench is absent; interest in the idea and a quotation referral do not establish a finish date.]] has been made for the bench. I cannot give you a confirmed date before the proposed work and arrangements are agreed.
Amara | Then today's skirting job stays as agreed while the bench is priced separately. Is there anything in this discussion that changes the existing booking?
Jules | I will preserve the [[existing contract::Existing contract continues to cover the skirting replacement; discussing a bench does not cancel or replace that task.]] scope. The skirting remains the agreed task, and the bench will be recorded as a separate request for pricing.
Amara | Good. Please don't take my interest as approval. I'll review the defined proposal and price before giving a decision on the extra work.
Jules | Correct. [[Change authorization::Change authorization has not been given; a future decision would need to establish the additional work through the relevant process.]] has not happened in this conversation. I will not describe your interest as approval to start building or to choose measurements for you.
Amara | Please pass on: built-in bedroom bench requested for a separate quote; size, finish, price, and timing unresolved. No instruction to proceed.
Jules | I will make that [[scope handoff::Scope handoff transfers the bench request with its unresolved dimensions, price, and timing while preserving the skirting-only agreement.]] clearly. The note will keep the bench proposal separate, preserve the decorating exclusion, and leave the unagreed details open for the quotation process.''',
    transfer_title='Keep an extra request separate',
    transfer_setup='Complete the client exchange about the bedroom work. Preserve the original task, excluded decorating, separate quotation, and unresolved bench dimensions.',
    transfer='''Carpenter: "The agreed task is replacing the ___." | skirting | Skirting replacement is the only work included in the current agreement.
Client: "Decorating remains ___." | excluded | The current booking excludes decorating, even after the bench question.
Carpenter: "I can arrange a separate ___ for the bench." | quotation | A quotation can be arranged without approving or pricing the work now.
Client: "The bench dimensions are not yet ___." | agreed | No bench measurements have been established or accepted during the conversation.''',
    rehearsal=["Read turns 1-10; separate the existing skirting agreement from the proposed bench and decorating.","Switch roles for turns 11-20. Stress quotation, authorization, and unresolved timing.","Check and read the transfer, keeping the quote request separate from permission to begin."],
))

BOOK['units'].append(unit(
    title='Coordinating access and other trades',
    scene='Delivery confirmed, study access unresolved',
    skill='Report delivery, room access, review timing, and storage restrictions as separate arrangements when coordinating with other trades.',
    brief='Carpenter Ben updates site coordinator Farah on the study joinery. Delivery is confirmed for Tuesday morning, but the decorator has not released the study for carpentry access. The hallway is available for a separate trim review at 11:00, not for material storage. Farah needs a precise status report. Ben must not turn the delivery confirmation into installation access, or the hallway review arrangement into permission to leave delivered joinery there.',
    cast='Farah | Site coordinator\nBen | Carpenter',
    culture=('Coordinate by purpose, not just by place and time', 'A room can be available for one activity and unavailable for another. State the purpose attached to each arrangement. Trade coordination works best when delivery, access, review, and storage are reported separately, with the unresolved dependency visible.'),
    a='''What is confirmed? | Joinery delivery for Tuesday morning | Study access for installation | Hallway material storage | Completion of decorating | Only the delivery arrangement is confirmed for Tuesday morning.
What remains unresolved? | The decorator has not released the study for carpentry access | Whether the hallway review is at 11:00 | Whether delivery is Tuesday morning | Whether hallway storage is permitted | Study access is unresolved because the decorator has not released that area.
What is the hallway available for? | A separate trim review at 11:00, not storage | All delivered material storage | Automatic study installation | Unrestricted use by every trade | The hallway permission is specific to the trim review and excludes material storage.''',
    vocabulary='''joinery | Fitted woodwork or related manufactured components for a project. | coordinate the joinery delivery
delivery slot | Agreed time period for receiving goods. | confirm the delivery slot
trade coordination | Arrangement of work between different specialist teams. | improve trade coordination
access release | Confirmation that a defined area is available for the specified work. | request an access release
decorator | Trade worker responsible for agreed surface finishing work. | coordinate with the decorator
carpentry access | Permission and readiness to enter an area for carpentry work. | confirm carpentry access
work area | Location assigned for a particular task. | identify the work area
trim review | Check or discussion of the specified trim details. | attend the trim review
storage permission | Authorization to leave materials in a defined location. | confirm storage permission
material staging | Temporary positioning of materials before use or movement. | distinguish material staging from a review
site coordinator | Person coordinating site arrangements across people or tasks. | update the site coordinator
dependency | Condition that another action relies on. | identify the access dependency
area readiness | Whether a location is prepared for the intended activity. | confirm area readiness
handover between trades | Transfer of an area or task from one trade to another. | coordinate the handover between trades
installation access | Availability of an area for fitting work. | verify installation access
confirmed delivery | Agreed arrival arrangement for goods. | report the confirmed delivery
moisture content | Water mass expressed here as a percentage of oven-dry wood mass. | report wood moisture content
purpose-specific access | Permission limited to a named activity. | respect purpose-specific access
equilibrium moisture content | Wood moisture at balance with surrounding temperature and humidity. | distinguish equilibrium moisture content
logistics update | Report on movement, receipt, access, or related arrangements. | give a logistics update
storage location | Place where materials may be held. | confirm the storage location
schedule dependency | Arrangement that must be resolved for a later task to proceed. | report a schedule dependency
status readback | Repetition of key arrangements to check understanding. | provide a status readback
coordination query | Question seeking clarification of interdependent arrangements. | raise a coordination query''',
    precision='Tuesday morning belongs to the confirmed delivery. Study access is not released. The 11:00 hallway arrangement is for a trim review only, and hallway storage is not permitted. These are separate facts, not a single approval for delivery, storage, and installation.',
    precision_extra='The scenario does not establish a substitute storage location, a new delivery slot, or the time when the decorator will release the study. Report the unresolved dependency to Farah without inventing a workaround or blaming another trade for an unverified delay.',
    phrases='''Start with delivery | The joinery delivery is confirmed for Tuesday morning.\nSeparate the room status | The study has not been released for carpentry access.\nName the dependency | We still need the decorator's access release.\nAvoid merging permissions | Delivery confirmation does not establish installation access.\nState the review arrangement | The hallway is available for the trim review at 11:00.\nState the restriction | The hallway is not available for material storage.\nClarify the purpose | That access is for a review, not for staging the delivery.\nKeep an alternative open | No alternative storage location is confirmed here.\nAvoid changing the booking | I have not changed the delivery slot.\nAvoid guessing readiness | I do not have a confirmed study-release time.\nPreserve trade coordination | Please keep the access question visible in the coordination update.\nAvoid assigning blame | I am reporting the release status, not a cause of delay.\nRead back the arrangements | Tuesday delivery, study unreleased, 11:00 hallway review, no hallway storage.\nAsk for clarification | Can you coordinate the unresolved access arrangement?\nKeep installation separate | No installation start is established by this update.\nClose with the open item | Study access remains the unresolved dependency.''',
    notes='''Confirmed for | Attaches a definite arrangement to its specific purpose.\nReleased for | Refers to authorization or readiness for the named work, not every use of the room.\nAvailable for review | Does not imply permission to store materials in the same location.\nNot for storage | An explicit restriction that must remain in the handoff.\nStill need | Flags a dependency without inventing its cause or resolution.\nSeparate | Prevents one agreed arrangement from silently authorizing another.''',
    d='''Which status report is accurate? | Tuesday-morning delivery confirmed; study access unreleased; hallway review at 11:00; no hallway storage. | All rooms ready because delivery is confirmed. | Hallway storage approved until decorating finishes. | Study installation guaranteed at 11:00. | The report preserves each arrangement and the specific hallway restriction.
Which inference is unsupported? | A confirmed delivery means the study is ready for installation. | The hallway review has a stated time. | Storage in the hallway is excluded. | Study release remains unresolved. | Delivery and room access are separate arrangements, so one does not prove the other.
What can Farah coordinate next? | The unresolved study-access arrangement | A completed installation already claimed | A storage location assumed without approval | A new delivery time invented by Ben | Farah needs the unresolved access dependency, not an unauthorized substitute arrangement.
Which hallway statement should be corrected? | We can store the joinery there because the trim review is allowed. | The review is at 11:00. | The hallway is available for the specified review. | Storage permission is absent. | Permission for the review does not authorize material storage in the hallway.''',
    dialogue='''Farah | Ben, I have Tuesday delivery in the diary and an eleven-o'clock review. Does that mean the study will be ready to install, or am I combining separate arrangements?
Ben | The [[delivery slot::Delivery slot is Tuesday morning for the joinery; it does not establish room access, storage permission, or installation readiness.]] is confirmed for Tuesday morning. The study, however, has not been released by the decorator for carpentry access.
Farah | Is the decorator finished with the study? I don't want the delivery confirmation to be read as permission for the installers to enter that room.
Ben | No confirmed [[access release::Access release for the study has not been given, and no release time is supplied in the case.]] time is available. I want that dependency kept visible rather than treated as settled in the delivery update.
Farah | Then what exactly is booked for eleven in the hallway? The word access in the message is a bit too broad for me.
Ben | The hallway is available for a [[trim review::Trim review is the specific activity allowed in the hallway at 11:00; it is not a material-storage arrangement.]] at 11:00. That is a separate activity, and the hallway is not available for material storage.
Farah | Can the joinery wait in the hallway until the study is released? I'm asking before anyone puts that location on the delivery instructions.
Ben | No alternative [[storage location::Storage location is not confirmed elsewhere, and the hallway is explicitly excluded from material storage.]] is confirmed here. I should not invent one or assume that a room available for a discussion can receive the delivery.
Farah | So the delivery is still Tuesday morning, even though we don't yet have a permitted storage arrangement? Please don't invent a new slot in the update.
Ben | I have not changed the [[confirmed delivery::Confirmed delivery remains Tuesday morning; reporting the access conflict does not itself reschedule the supplier.]]. Tuesday morning is still the stated slot. The update flags the mismatch without claiming that a replacement plan exists.
Farah | And we can't advertise Tuesday installation just because the material is arriving? The room release is still the missing part.
Ben | No. [[Installation access::Installation access is unresolved because the study has not been released; a delivered product does not authorize fitting work there.]] remains unresolved. Delivery, room release, and the start of fitting work should not be compressed into one promise.
Farah | Please put that distinction in the coordination message. What would you say without blaming the decorator for a delay we haven't established?
Ben | That is the right [[logistics update::Logistics update reports the actual arrangements and unresolved dependency without inventing a cause or blaming another trade.]] to give. I am reporting the current release status, not a reason for it or a claim that another trade has missed a deadline.
Farah | Read the four statuses back separately, please. I want delivery, study access, review access, and storage to be unmistakable.
Ben | Here is the [[status readback::Status readback repeats delivery, access, review, and storage separately so no permission is lost or expanded in the handoff.]]: Tuesday-morning delivery confirmed; study unreleased; hallway trim review at 11:00; no material storage in the hallway.
Farah | Do we know when the study will be released? If not, keep that unknown rather than using eleven o'clock as a convenient estimate.
Ben | Yes. The [[schedule dependency::Schedule dependency is the unresolved study access, which remains distinct from the already confirmed delivery and review arrangements.]] is still the study release. No alternative storage, changed delivery slot, or installation start has been established in this update.
Farah | All right. Please flag the unresolved coordination to me. The hallway review permission mustn't turn into a general storage or installation permission.
Ben | Exactly. [[Purpose-specific access::Purpose-specific access limits the hallway arrangement to the trim review; it does not authorize storage or substitute for study access.]] is the key point for the hallway. I will keep the review permission and the storage restriction together whenever I pass the update on.''',
    transfer_title='Keep four arrangements separate',
    transfer_setup='Complete the coordinator update. Preserve the confirmed delivery, unreleased study, hallway review time, and storage restriction.',
    transfer='''Carpenter: "Delivery is confirmed for ___ morning." | Tuesday | Tuesday morning is the delivery slot, not a confirmed installation start.
Coordinator: "The study has not been ___ for carpentry access." | released | The decorator has not released the study for the intended work.
Carpenter: "The hallway trim review is at ___." | 11:00 | Eleven o'clock is the separate trim-review time supplied in the case.
Coordinator: "The hallway is not available for material ___." | storage | Storage is explicitly excluded even though the hallway review is allowed.''',
    rehearsal=["Read turns 1-10 with a partner, distinguishing Tuesday delivery from study access and the hallway review.","Switch roles for turns 11-20. Read the four statuses without adding a storage location or installation time.","Check and read the transfer. Keep 11:00 attached to the review only."],
))

BOOK['units'].append(unit(
    title='Reviewing fit, appearance, and snagging',
    scene='Correcting the claim about drawer D3',
    skill='Withdraw an inaccurate overall claim, describe a specific alignment observation, and record follow-up without guessing the remedy.',
    brief='During a wardrobe review, carpenter Luis tells client Priya that all fronts are flush. Priya points out drawer D3: its left edge projects beyond the neighboring front. Luis has not assessed the cause or remedy. He must correct his earlier statement and add the specific observation for follow-up. The conversation does not establish a measured offset, a tolerance failure, a damaged runner, or an agreed repair and completion time.',
    cast='Priya | Client\nLuis | Carpenter',
    culture=('A direct correction protects trust', 'When a client identifies an exception to an overall claim, acknowledge it explicitly. Correct the claim and record the observable detail. Avoid defending the original wording, minimizing the concern without a standard, or promising a repair before the cause has been assessed.'),
    a='''Which earlier statement must Luis correct? | All fronts are flush | D3 needs follow-up | The cause is unassessed | No repair time is agreed | Luis claimed all fronts were flush, which conflicts with the specific visible exception.
What does Priya identify? | D3's left edge projects beyond the neighboring front | Every drawer is broken | A confirmed damaged runner | A measured five-millimeter offset | The supplied observation concerns D3's projecting left edge, without a measurement or cause.
What should Luis do next in the conversation? | Correct the claim and record the specific observation for follow-up | Deny the visible exception | Promise a replacement runner immediately | Declare the projection acceptable without assessment | The supported response is an explicit correction and accurate follow-up record, not a guessed remedy.''',
    vocabulary='''flush | Aligned in the same plane at the relevant surfaces. | check whether the fronts are flush
drawer front | Visible face panel of a drawer. | identify the drawer front
neighboring front | Adjacent visible face used as a comparison. | compare the neighboring front
projecting edge | Edge extending beyond a stated reference surface. | describe the projecting edge
left edge | Left-hand boundary of the identified component. | locate the left edge
alignment | Relative positioning of components or surfaces. | review the alignment
offset | Displacement between specified reference positions or surfaces. | measure the offset
tolerance | Permitted variation under an applicable specification. | check the applicable tolerance
snag | Item requiring attention during a completion or quality review. | record a snag
snagging list | Record of items requiring follow-up before agreed closure. | add to the snagging list
punch list | Common North American term for a list of completion or correction items. | update the punch list
fit review | Examination of how components align or work together. | conduct a fit review
appearance review | Examination of visible finish and presentation. | record an appearance review
drawer runner | Mechanism or support guiding a drawer's movement. | inspect the drawer runner
hinge | Joint allowing a door or panel to pivot. | identify the hinge
adjustment | Change to a component's setting or position. | assess the need for adjustment
remedy | Action intended to correct an established problem. | assess the appropriate remedy
root cause | Underlying reason for an observed problem. | investigate the root cause
correction of record | Amendment of an inaccurate earlier statement. | make a correction of record
specific exception | Identified case that contradicts a general claim. | acknowledge the specific exception
quality claim | Statement about the condition or standard of work. | qualify the quality claim
follow-up item | Matter retained for further checking or action. | record a follow-up item
slip matching | Placing consecutive veneer leaves alongside each other in the same face orientation. | compare slip matching
closeout status | Whether review and required follow-up are complete. | preserve the closeout status''',
    precision='Luis must withdraw all fronts are flush because D3 provides a specific exception. The observation is a projecting left edge relative to the neighboring front. It does not establish the projection amount, applicable tolerance, underlying cause, or correct remedy.',
    precision_extra='Record the component identifier, side, and comparison surface so follow-up is specific. Do not convert projects into a claim that the drawer is broken, or a possible adjustment into an agreed repair. The item remains open pending the appropriate assessment.',
    phrases='''Correct the earlier statement | I need to correct what I said about all the fronts being flush.\nAcknowledge the exception | You are right to point out D3.\nName the component | The observation concerns drawer D3.\nLocate the edge | Its left edge projects beyond the neighboring front.\nAvoid a guessed measurement | I have not established the amount of the offset.\nAvoid a tolerance claim | I have not checked the applicable tolerance.\nKeep the cause open | The cause has not been assessed.\nKeep the remedy open | I have not determined the appropriate remedy.\nAvoid blaming hardware | I cannot call the runner defective from this observation alone.\nRecord the follow-up | I will add the specific item to the snagging list.\nPreserve the comparison | The neighboring front is the reference in this observation.\nAvoid minimizing | I will not dismiss it as acceptable without checking.\nAvoid a repair promise | No repair method or completion time is agreed.\nLimit the finding | This identifies D3, not every drawer in the wardrobe.\nRead back the item | D3 left edge projects; cause and remedy unassessed.\nClose honestly | The earlier overall claim is corrected and this item remains open.''',
    notes='''All | A universal claim contradicted by even one verified exception.\nProjects beyond | Describes relative position without supplying a measured amount.\nLeft edge | Makes the observation more useful than saying the drawer looks wrong.\nUnassessed | Keeps an observation separate from a technical conclusion.\nCorrect what I said | Directly withdraws an inaccurate statement rather than quietly changing the subject.\nOpen item | Acknowledgement and recording do not establish that correction is complete.''',
    d='''Which opening corrects the earlier claim? | I need to correct that: D3's left edge is not flush with the neighboring front. | D3 is an exception, but the overall flush claim can stay unchanged. | D3 projects, so its runner needs replacement. | D3 looks close enough to accept without checking tolerance. | The opening explicitly withdraws the inaccurate overall claim and identifies the exception.
Which snag entry is precise? | D3 left edge projects beyond neighboring front; cause and remedy unassessed. | All drawers broken and replacement approved. | Wardrobe fine; no follow-up. | Five-millimeter failure repaired. | The entry preserves the component, side, reference surface, and unassessed cause and remedy.
Which conclusion is unsupported? | A replacement runner is definitely required. | D3 needs follow-up. | The left edge projects. | The earlier all-fronts claim needs correction. | No assessment establishes that the runner caused the projection or needs replacement.
What remains open after recording the item? | Cause, remedy, and any completion arrangement | Whether Luis made the earlier claim | Whether Priya identified D3 | Which edge is described | Recording the observation does not determine the cause, repair, or completion timing.''',
    dialogue='''Priya | Luis, you said all the fronts were flush. D3's left edge is sitting forward of the neighboring front. Can you check what you told me?
Luis | You're right; I need a [[correction of record::Correction of record explicitly withdraws the inaccurate claim that all fronts are flush in light of the D3 observation.]]. All fronts are flush was too broad. D3 is an exception, and I withdraw that overall statement.
Priya | Thank you. I don't want the list to say wardrobe problem, though. Someone coming back needs to know which edge we're discussing.
Luis | I'll identify the [[drawer front::Drawer front is D3's visible face, the specific component Priya wants recorded rather than a vague whole-wardrobe concern.]] as D3 and specify its left edge relative to the neighboring front. That is the visible difference.
Priya | Is it a runner fault? I wondered whether adjusting the hardware would bring it back, but I don't know what's behind it.
Luis | The [[root cause::Root cause remains unassessed; the visible projection does not establish a runner defect or another explanation.]] hasn't been assessed. I can't call the runner defective or promise that a particular adjustment will correct the position.
Priya | How far does it project? I can see the edge, but I haven't measured it, and I don't want my estimate repeated as a measurement.
Luis | The [[offset::Offset is the amount of displacement between the fronts; no measured value is supplied by the visible observation alone.]] isn't established numerically. I'll record the observation without inventing a millimeter figure or treating an estimate as a checked dimension.
Priya | So we can't call it within tolerance yet? Earlier I thought you were saying the whole installation had passed that comparison.
Luis | I haven't checked the applicable [[tolerance::Tolerance is the permitted variation under the relevant specification; no comparison with that requirement has been completed here.]] for this item. I won't dismiss it as acceptable, or make the opposite specification finding, without that check.
Priya | Please make sure it stays on the follow-up list. I don't want a general handover tick to hide this particular point.
Luis | I'll add it to the [[snagging list::Snagging list records the specific D3 item for follow-up; it does not establish that every drawer has the same condition.]]: D3, left edge projects beyond the neighboring front, with cause and appropriate action still to be assessed.
Priya | Does correcting your earlier statement mean you're saying every drawer is wrong now? That's not what I'm asking you to report.
Luis | No. The [[quality claim::Quality claim that all fronts were flush must be corrected rather than retained as a conflicting statement beside the new observation.]] is narrowed by this specific exception. We have identified D3; we haven't established that all the other fronts have the same issue.
Priya | Can you tell me what will be done and when, or do those both have to wait for the follow-up assessment?
Luis | The [[remedy::Remedy is the corrective action, which has not been determined; therefore no method or completion time can be promised here.]] hasn't been determined, and no completion time is agreed. I'll avoid turning a possible adjustment into an approved repair promise.
Priya | Then read me the item as it will appear. I'd like the edge and comparison surface to survive the handoff.
Luis | The [[follow-up item::Follow-up item is the precise D3 left-edge projection, with cause and remedy left unassessed for the next review.]] says D3's left edge projects beyond the neighboring front; amount, cause, tolerance comparison, and appropriate action are not established.
Priya | That's accurate. Please keep it open after today's discussion. Correcting the wording doesn't itself put the front into the right position.
Luis | Agreed. The [[closeout status::Closeout status remains open for D3 because recording the observation and correcting a statement do not complete the necessary follow-up.]] stays open. I've corrected what I said, but the physical item and its follow-up still need to be resolved.''',
    transfer_title='Correct and record the exception',
    transfer_setup='Complete the review exchange. Correct the universal claim, identify the projecting edge, and leave the cause and remedy unresolved.',
    transfer='''Carpenter: "I need to correct my claim that all fronts are ___." | flush | Flush was the inaccurate overall claim contradicted by D3's projecting edge.
Client: "The specific drawer is ___." | D3 | D3 identifies the drawer that needs the recorded follow-up.
Carpenter: "Its ___ edge projects beyond the neighboring front." | left | Left identifies the side of the visible projection in the case.
Client: "The cause and remedy remain ___." | unassessed | Neither cause nor remedy has been determined by the observation alone.''',
    rehearsal=["Read turns 1-10; make Luis's correction explicit and identify D3's left edge.","Switch roles for turns 11-20; distinguish the observed projection from a tolerance decision or repair promise.","Check the transfer, then read it with the neighboring front named as the comparison."],
))

BOOK['units'].append(unit(
    title='Handing over records and return visits',
    scene='Documents received, one cover outstanding',
    skill='Confirm supplied documents, record an undelivered part, and distinguish an accepted callback commitment from an unconfirmed return visit.',
    brief='At a cabinet handover, owner Daniel receives the cabinet drawings and the correct finish care sheet from joinery lead Mina. A replacement shelf pin cover is due but has not arrived. Mina accepts responsibility for supplier follow-up and commits to calling Daniel on Friday. No return-visit date is confirmed. Warranty terms remain those in the supplied document; Mina must not invent wider coverage or imply that receiving the documents means every outstanding item is complete.',
    cast='Daniel | Owner\nMina | Joinery lead',
    culture=('Close completed items without hiding the remainder', 'A useful handover can acknowledge documents received while retaining an outstanding part and its follow-up. Name the responsible person and the precise commitment. A promise to call is valuable on its own and should not be expanded into a promised visit or changed warranty.'),
    a='''Which documents does Daniel receive? | Cabinet drawings and the correct finish care sheet | Only an unrelated product leaflet | A new verbal warranty replacing the document | A completed supplier investigation | The case confirms delivery of the cabinet drawings and the correct care sheet.
What remains outstanding? | A replacement shelf pin cover that is due but not delivered | All cabinet drawings | The correct care sheet | A confirmed Friday installation | The replacement cover has not arrived, so that item remains open.
What does Mina commit to? | Supplier follow-up and a Friday call, with no confirmed return visit | A Friday return visit and unlimited warranty | A delivered cover already fitted | A guaranteed supplier arrival time | Mina owns supplier follow-up and promises the call, not a visit or delivery date.''',
    vocabulary='''handover pack | Collection of documents supplied at a project handover. | confirm the handover pack
cabinet drawing | Drawing showing the relevant cabinet arrangement or details. | provide the cabinet drawings
care sheet | Instructions for looking after a specified finish or product. | supply the correct care sheet
finish identification | Confirmation of the surface treatment a document applies to. | check finish identification
shelf pin | Small support component used to locate or carry a shelf. | identify the shelf pin
pin cover | Cover associated with the specified pin or fitting. | identify the replacement pin cover
replacement part | Component supplied to replace a specified item. | track the replacement part
outstanding item | Matter not yet completed, delivered, or resolved. | retain an outstanding item
due delivery | Expected arrival that has not necessarily occurred. | distinguish due delivery from receipt
supplier follow-up | Contact with the supplier about an unresolved matter. | accept supplier follow-up
action owner | Person responsible for carrying out a defined next step. | name the action owner
callback commitment | Promise to make a return call at a stated time. | confirm the callback commitment
return visit | Later attendance at the property. | arrange a return visit
appointment confirmation | Explicit agreement of a visit arrangement. | await appointment confirmation
warranty document | Written terms describing the applicable warranty. | refer to the warranty document
coverage | Matters included under the stated warranty terms. | verify the documented coverage
exclusion | Matter outside the applicable terms or scope. | check a stated exclusion
document receipt | Confirmation that a document has been received. | record document receipt
part receipt | Confirmation that a component has physically arrived. | verify part receipt
fitting status | Whether the relevant part has been installed or fitted. | confirm fitting status
handover record | Note of documents, completed work, and unresolved items at transfer. | update the handover record
open-item tracker | Record used to follow unresolved matters to completion. | update the open-item tracker
commitment boundary | Limit of what has actually been promised. | preserve the commitment boundary
closure evidence | Information supporting that an item is genuinely complete. | obtain closure evidence''',
    precision='The drawings and correct care sheet are received. The replacement cover is not. Mina accepts supplier follow-up and a Friday call, but no visit date is confirmed. Unlike a requested callback, the Friday call is an explicit commitment in this case.',
    precision_extra='Keep warranty wording tied to the supplied document instead of paraphrasing it into a broader promise. Receipt of documents does not prove that the replacement part has arrived, been fitted, or closed. No supplier delivery date or return appointment is supplied.',
    phrases='''Confirm the documents | You have the cabinet drawings and the correct finish care sheet.\nIdentify the open item | The replacement shelf pin cover is still outstanding.\nState receipt accurately | It is due, but it has not been delivered.\nAccept ownership | I will follow up with the supplier.\nName the owner | Mina owns that supplier follow-up.\nMake the stated commitment | I will call you on Friday.\nSeparate call and visit | Friday is the callback commitment, not a confirmed return visit.\nKeep attendance open | The return-visit date is not confirmed.\nAvoid a delivery promise | I do not have a confirmed arrival date for the cover.\nUse the supplied terms | The warranty remains as stated in the supplied document.\nAvoid wider coverage | I am not adding a new warranty promise verbally.\nKeep records separate | Document receipt does not close the outstanding part.\nPreserve fitting status | I will not record an undelivered part as fitted.\nRead back the handover | Documents received, cover outstanding, supplier follow-up with Mina, Friday call.\nAvoid premature closure | The cover item stays open pending the actual outcome.\nClose with a clear boundary | The call is committed; delivery and return attendance are not yet confirmed.''',
    notes='''Due versus delivered | Expected arrival and actual receipt are different statuses.\nI will call | An explicit commitment, stronger than a request for someone to call.\nFriday | Applies to the phone call, not automatically to delivery or site attendance.\nAs stated | Refers back to the supplied warranty wording without changing it.\nOutstanding | Keeps the unresolved cover visible after other handover items are complete.\nReceived versus fitted | Physical arrival and installation are separate stages.''',
    d='''Which handover summary is correct? | Drawings and care sheet received; cover outstanding; Mina follows up and calls Friday; visit unconfirmed. | Everything delivered and fitted Friday. | No documents received. | Warranty expanded and supplier delivery guaranteed. | The summary preserves completed documents, the open part, ownership, call, and unconfirmed visit.
What does Mina's Friday commitment cover? | A phone call to Daniel | A confirmed installation visit | Guaranteed cover delivery | A new warranty term | Mina explicitly commits to calling Friday, while delivery and attendance remain unconfirmed.
Which warranty statement is appropriate? | The terms remain those in the supplied document. | Everything is covered forever. | A verbal handover automatically replaces the document. | Every outstanding item is excluded without reading the terms. | The case authorizes no change to the supplied warranty terms in either direction.
What is insufficient evidence to close the cover item? | Receipt of the drawings and care sheet alone | Verified actual completion of the relevant follow-up | Confirmation of the actual outcome through the project process | Evidence that the unresolved item has genuinely been addressed | Receiving documents does not establish delivery, fitting, or resolution of the replacement cover.''',
    dialogue='''Daniel | I've received the cabinet drawings and care sheet. Before you leave, can we run through the missing cover and the follow-up?
Mina | Yes. The [[handover pack::Handover pack includes the cabinet drawings and correct finish care sheet already received; the replacement cover remains a separate open item.]] documents are with you, including the correct sheet for the finish. The replacement shelf pin cover is still outstanding.
Daniel | It's the replacement shelf-pin cover we're waiting for, correct? I haven't received it just because its name appears in the handover pack.
Mina | We are waiting for [[part receipt::Part receipt has not occurred because the replacement shelf pin cover is due but has not been delivered.]]. The cover is due, but it has not been delivered. I should not describe it as here or ready to fit.
Daniel | Who will chase the supplier? I'd prefer one named contact so I don't have to repeat the same question to several people.
Mina | I accept the [[supplier follow-up::Supplier follow-up is Mina's accepted responsibility for the outstanding cover, rather than an unassigned action for someone else.]]. I will contact the supplier about the cover, and the record should name me as the person responsible.
Daniel | Can you give me a firm time for the next update, even if the supplier hasn't confirmed the delivery by then?
Mina | I will call you on Friday. That is my [[callback commitment::Callback commitment is Mina's explicit promise to call Friday, distinct from a request or a confirmed delivery arrangement.]], so you have a definite contact point rather than an open-ended note to wait for news.
Daniel | When you say Friday, do you mean you'll call, or that someone will come and fit the part? Those are different arrangements for me.
Mina | It is the call, not [[appointment confirmation::Appointment confirmation for a return visit has not been given; Friday identifies the promised call only.]]. No return-visit date is confirmed, and I do not have a confirmed arrival date for the part to give you.
Daniel | Thanks. I won't keep Friday free for a visit. Please make the written note just as clear for anyone else who picks this up.
Mina | I will preserve the [[commitment boundary::Commitment boundary limits the Friday promise to a call, without expanding it into delivery or physical attendance.]]. The entry will show supplier follow-up with Mina and a Friday call, with the return visit still unconfirmed.
Daniel | One more thing: does today's conversation change the warranty? I have the document and don't want to rely on a different verbal promise.
Mina | The [[warranty document::Warranty document remains the source of the applicable terms; Mina does not add or remove coverage through this handover conversation.]] remains the reference. I am not adding broader coverage verbally or changing the terms supplied with your records.
Daniel | Then I'll keep the finish-care instructions separate from the warranty terms. Neither document confirms that the missing part has arrived.
Mina | Exactly. The [[care sheet::Care sheet contains the relevant finish-care information and is already received; it is distinct from warranty terms and the open-part record.]] and warranty document have different purposes. Receiving them does not establish that the replacement cover has arrived or been fitted.
Daniel | Could you read back what is complete and what remains open? I'd like the documents acknowledged without the part being marked done.
Mina | The [[handover record::Handover record must distinguish received documents from the undelivered cover and preserve Mina's follow-up and Friday-call commitment.]] says drawings and correct care sheet received; replacement cover outstanding; supplier follow-up owned by Mina; Friday callback committed; return date unconfirmed.
Daniel | That's clear. Please keep the cover open until its actual outcome is confirmed, and call Friday as agreed even if the delivery is still unresolved.
Mina | I will retain it in the [[open-item tracker::Open-item tracker keeps the replacement cover unresolved until the actual outcome supports closure, rather than closing it because documents were supplied.]]. We can acknowledge the documents received while keeping the part, its follow-up, and any later attendance arrangement visible.''',
    transfer_title='Confirm the promise without expanding it',
    transfer_setup='Complete the handover exchange. Distinguish received documents, the undelivered cover, Mina as owner, and the Friday callback.',
    transfer='''Owner: "The drawings and correct care sheet are ___." | received | The case confirms that both documents have reached the owner.
Lead: "The replacement cover has not been ___." | delivered | The cover is due but has not arrived, so it remains outstanding.
Owner: "___ owns the supplier follow-up." | Mina | Mina explicitly accepts responsibility for contacting the supplier about the cover.
Lead: "I will call ___; the return visit is not confirmed." | Friday | Friday is the committed call date, not an agreed return visit.''',
    rehearsal=["Read turns 1-10, stressing received documents, outstanding cover, and Mina's ownership.","Switch roles for turns 11-20; make Friday a committed call, not a delivery or visit.","Check and read the transfer. Keep the open part separate from the completed document handover."],
))
