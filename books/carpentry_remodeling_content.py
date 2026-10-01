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
             note='Occupational context for reading plans, discussing measurements and materials, installation work, and client communication. No employment forecasts or credential requirements are reproduced.', checked='1 October 2026'),
        dict(title='Architectural Woodwork Institute. AWI 100: Manufacturer / Supplier Responsibility.',
             url='https://awinet.org/standards/submittals/requirements-category/manufacturer-supplier-responsibility/',
             note='Context for shop drawings, material samples, explicit change requests, and coordinated review. Fictional drawing conflicts and review times are not requirements stated by this source.', checked='1 October 2026'),
        dict(title='Andersen Windows and Doors. Window and Door Glossary.',
             url='https://www.andersenwindows.com/support/window-door-glossary',
             note='Background terminology for openings, frames, trim, and door components. No product-specific dimensions, installation allowances, or compliance claims are transferred to the cases.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Woodworking: Hazards and Solutions.',
             url='https://www.osha.gov/woodworking/hazards-solutions',
             note='Context for respecting trained roles and actual safety controls. The book provides no machine-operation, chemical-use, or concealed-condition assessment procedure.', checked='1 October 2026'),
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
jamb | Vertical side member of an opening or frame. | refer to the jamb
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
    d='''Which question targets the missing information? | Does 900 millimeters refer to the rough opening, finished opening, or another reference? | Why is 900 always the clear passage? | Which door has already been delivered? | How can we omit the frame? | The question asks what the stated dimension describes without assuming an interpretation.
Which reassurance is unsupported? | You will definitely have 900 millimeters of usable passage. | The note gives a 900-millimeter figure. | No door is ordered. | Priya can clarify the reference. | The note does not establish usable passage, so the reassurance exceeds the evidence.
What should remain unchanged in the query? | The stated 900-millimeter figure and the uncertainty about its reference | A guessed frame deduction | A fabricated confirmed order size | A claim that the drawing means finished opening | The query preserves the actual figure while asking for its unresolved meaning.
Which distinction matters for ordering? | An unclear opening note is not a confirmed door order size. | All opening and door dimensions are identical. | Client interpretation automatically authorizes an order. | A precise number removes every need for clarification. | The dimension reference must be clarified before it can support an appropriate product specification.''',
    dialogue='''Hana | The hall drawing says the door opening is 900 millimeters. That should give us 900 millimeters to walk through, should it not?
Ellis | I see why you read it that way, but the [[dimension reference::Dimension reference identifies what the 900-millimeter figure measures, which the current note does not make clear.]] is unclear. The note does not say whether it describes a rough opening, a finished opening, or something else.
Hana | I was thinking about the space available when the door is open. I am not asking for the width of the door panel itself.
Ellis | Your question is about [[clear passage::Clear passage is the usable unobstructed space Hana wants to understand, not automatically the dimension on the drawing.]]. That is an important distinction. I cannot confirm that usable width from this note without knowing the reference behind the figure.
Hana | What does rough opening mean in ordinary language? I have heard the term, but I do not want to assume it means a rough estimate.
Ellis | A [[rough opening::Rough opening refers to the structural opening before the assembly and relevant finishes, not an approximate estimate of usable width.]] is the structural opening before the door assembly and relevant finishes. Rough describes the construction stage here, not an approximate guess at the measurement.
Hana | That helps. So the frame and the completed surfaces can matter to what the figure means, but we do not yet know which surfaces the note uses.
Ellis | Exactly. We need to identify the [[reference face::Reference face names a surface used for measurement; the drawing note does not identify those surfaces clearly.]] or faces the dimension runs between. I should not invent that information or quietly subtract an allowance.
Hana | Has a door already been ordered using this number? If it has, I would like the office to know that my question concerns the usable space.
Ellis | No door has been ordered. We do not have a confirmed [[order size::Order size is not established by the ambiguous note, and no door has been ordered in this case.]] from this conversation, so I am not describing a change to an existing purchase.
Hana | Good. Who can tell us what the designer intended? I would rather get the wording clarified than have us choose whichever interpretation sounds most likely.
Ellis | Priya can provide [[designer clarification::Designer clarification is the appropriate route for resolving the intended measurement reference without a guessed interpretation.]]. I will send the note and explain that your concern is the usable passage through the hall doorway.
Hana | Please keep the original number in the question. I do not want someone to think I asked to change it before we understand what it describes.
Ellis | I will preserve the [[opening dimension::Opening dimension remains the stated 900 millimeters; the query concerns its meaning rather than a requested numerical change.]] of 900 millimeters exactly as written. The query will ask what it measures, not propose a different number.
Hana | Would it be sensible to ask whether the number comes from the frame dimensions? I do not want to leave that possible interpretation hidden.
Ellis | We can ask for an explicit reference, including whether the [[door frame::Door frame is a distinct component whose dimensions must not be silently equated with usable passage or the ambiguous opening note.]] is part of it. We should not decide the answer ourselves or assume a particular frame thickness.
Hana | And we should not tell anyone the opening meets a requirement just because there is a clear number on the drawing. That would need its own checking.
Ellis | Correct. Clarifying the [[drawing note::Drawing note needs an explanation of its measurement reference; the clarification conversation is not a compliance assessment.]] is not a compliance assessment. We are resolving the language and reference before relying on it as a usable-width statement.
Hana | Please ask Priya to say whether it is rough opening, finished opening, or another reference, and to address my question about the passage when the door is open.
Ellis | I will include all of that. The [[actual dimension::Actual dimension of the usable passage is not verified; the next step is clarification, not a width guarantee or product order.]] of the usable passage remains unverified here. I will not promise 900 millimeters of clear space or place an order on that assumption.''',
    transfer_title='Clarify before naming the usable width',
    transfer_setup='Complete the exchange about the hall drawing. Keep the given number, missing reference, unverified passage, and designer referral distinct.',
    transfer='''Client: "The drawing says ___ millimeters." | 900 | The stated figure is 900 millimeters, although its reference is unclear.
Carpenter: "The note does not identify rough or ___ opening." | finished | Finished is the alternative opening reference the note does not clarify.
Client: "My concern is the clear ___." | passage | Passage identifies the usable space Hana wants to understand.
Carpenter: "I will ask the ___ to clarify the reference." | designer | The designer can clarify the intended reference without the carpenter inventing it.''',
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
    dialogue='''Oliver | I like the shape of both pieces. Is there a practical difference between these two oak samples, or is it mainly the way the surface looks?
Mei | There is a difference in [[material construction::Material construction distinguishes solid oak in A from oak veneer over a supporting material in B.]]. Sample A is solid oak, while sample B is oak-veneered trim. Both match the profile you requested for the study.
Oliver | The pattern on A seems stronger. That could work with the room, although B looks calmer when I hold it beside the wall color.
Mei | A has [[pronounced grain::Pronounced grain describes the stronger visible pattern on sample A without making a quality or durability claim.]], and B has a more uniform appearance. Those are the visual differences stated for these samples, not a ranking of quality.
Oliver | When you say veneered, do you mean that the oak is the visible surface over another material? I want to describe it correctly when we discuss the choice.
Mei | Yes, [[oak veneer::Oak veneer is the thin oak surface layer over a supporting material; it is not the same construction as solid oak.]] refers to that surface layer. I do not have a specification for the supporting material here, so I should not name a core that is not listed.
Oliver | What about timing? I remember one option was quicker, but I cannot remember which quote belonged to which sample or whether those were installation dates.
Mei | The [[quoted lead time::Quoted lead time is ten days for A and four for B; these figures do not establish installation appointments.]] is ten days for A and four days for B. Those are supply quotes, not confirmed installation appointments.
Oliver | Then B has the shorter quote by six days. That matters to me, but it does not automatically make it the right choice if I prefer A's appearance.
Mei | Exactly. Your [[visual preference::Visual preference concerns the appearance Oliver favors and remains one consideration alongside the stated timing and construction.]] and the timing are separate considerations. We can compare them without deciding that one sample is better in every respect.
Oliver | Are the edges shaped differently? I do not want a quicker option if it changes the profile I asked for around the study.
Mei | Both match the requested [[profile::Profile is the cross-sectional shape, which both samples match; it is not a difference between these options.]]. The known differences here are construction, grain appearance, and quoted lead time, not the shape you specified.
Oliver | Is B less expensive? I know that might seem likely to some people, but I would rather compare an actual figure than make an assumption.
Mei | We do not have a price comparison. I also cannot support a [[performance claim::Performance claim would assert durability or function not supplied by the sample comparison; material names alone do not establish it.]] about which lasts longer from the information on these two samples.
Oliver | I am leaning toward the stronger grain, but I have not decided. Please do not take that comment as permission to order A before I confirm.
Mei | I will keep the [[selection status::Selection status remains undecided; Oliver's favorable comment about A is not approval or an order instruction.]] open. We can note your interest in A without recording it as an approved sample or a placed order.
Oliver | Good. I want to compare the finish details and prices when those are available, rather than use the lead-time difference to stand in for everything else.
Mei | We can keep those as separate questions before [[sample approval::Sample approval has not been given; the missing comparisons and Oliver's final choice remain unresolved.]]. Nothing in this discussion establishes a finish specification, a price, or a guarantee about future product performance.
Oliver | For now, the summary is solid oak and stronger grain with ten days for A; oak veneer and a more uniform look with four days for B.
Mei | Correct, and neither quote is an [[installation date::Installation date is not supplied by either lead-time quote, and no sample selection or fitting appointment is confirmed.]]. Both match the profile, no sample is selected, and the other details remain to be confirmed before a decision.''',
    transfer_title='Compare without choosing for the client',
    transfer_setup='Complete the sample comparison. Use the stated construction, appearance, lead time, and decision status; do not add prices or durability claims.',
    transfer='''Carpenter: "Sample A is solid ___." | oak | Oak is the stated solid material used for sample A.
Client: "B has the more ___ appearance." | uniform | Uniform describes B relative to the pronounced grain of A.
Carpenter: "B has a quoted ___-day lead time." | four | Four days is B's quoted supply interval, not an installation date.
Client: "Neither sample is ___ yet." | selected | No selection has been made despite discussion of both samples.''',
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
millimeter difference | Difference expressed in the specified metric unit. | state the millimeter difference
document status | Current issue, approval, or review state of a document. | preserve the document status''',
    precision='The difference is five millimeters, but calculating that difference does not identify the correct reveal. Both C4 and S2 are revision B and refer to the same panel. Neither sheet is established as superseded or authoritative over the other.',
    precision_extra='14:00 is the fabrication-release review time. It is not an instruction to choose a dimension, a confirmed designer-response time, or evidence that fabrication is released. Refer both values and the precise location through the actual project clarification process.',
    phrases='''Flag the issue | I found a conflict at the cabinet end panel.\nCite the first view | Elevation C4 revision B shows a 20-millimeter reveal.\nCite the second view | Section S2 revision B shows 15 millimeters.\nConfirm the shared location | Both dimensions refer to the same end panel.\nCheck the issue labels | Both sheets are marked revision B.\nState the difference | The values differ by five millimeters.\nReject a revision shortcut | We cannot identify a newer sheet from those labels alone.\nName the missing answer | The designer has not clarified which dimension applies.\nRequest a decision | Please confirm the applicable reveal dimension.\nPreserve the review time | The fabrication-release review is due at 14:00.\nAvoid a response promise | That review time is not a guaranteed designer-response time.\nKeep production status separate | The conflict discussion does not authorize fabrication.\nKeep both references | I will include C4 and S2 in the query.\nAvoid averaging | I will not use the midpoint as an invented solution.\nAsk for an explicit response | The reply needs to identify the dimension for this panel.\nClose with the current status | The detail remains unresolved pending clarification.''',
    notes='''At the same panel | Establishes that the two values conflict rather than describe separate locations.\nRevision B | A shared issue label, not proof that the content agrees.\nApplies | Asks which dimension governs the specific detail.\nDue for review | Describes a planned decision point without implying approval.\nPending clarification | Keeps the question open until a response resolves it.\nFive-millimeter difference | Correct arithmetic that does not answer which value is intended.''',
    d='''Which query is complete? | At the same end panel, C4 rev B shows 20 mm and S2 rev B shows 15 mm; please clarify for the 14:00 release review. | Please fix the cabinet sometime. | Use 20 because it is larger. | Both sheets agree because they are revision B. | The complete query includes location, both references, conflicting values, and the review time.
Which proposed shortcut is unsupported? | Average the values and fabricate a 17.5-millimeter reveal. | Ask the designer to clarify. | Preserve both revision labels. | Flag the unresolved detail for review. | No authority is given to invent a midpoint or release fabrication from conflicting dimensions.
What do the revision labels establish? | Both sheets are marked B, not which dimension is correct | C4 is definitely newer | S2 is superseded | The reveal is automatically 20 | The shared letter does not identify precedence or resolve the inconsistent detail.
Which status is accurate at the end? | The reveal remains unresolved and fabrication is not authorized by this conversation. | The designer has approved 15. | The review deadline authorizes 20. | Installation is complete. | No designer clarification or fabrication authorization is supplied during the exchange.''',
    dialogue='''Arun | Before the release review, I need to flag the end panel on the cabinet drawings. The two views give different reveal dimensions at the same location.
Lena | Which references are involved? I need the [[sheet number::Sheet number locates each drawing precisely for the designer's review of the conflict.]] and revision for each view, not just the two measurements, so the query is easy to follow.
Arun | Elevation C4 revision B shows 20 millimeters. Section S2 revision B shows 15 millimeters. I have checked that both refer to this same end panel.
Lena | Then the [[dimension discrepancy::Dimension discrepancy is 20 versus 15 millimeters at the same end panel, not two unrelated measurements.]] is five millimeters at one detail. Has the designer already responded anywhere, or is the applicable value still unconfirmed?
Arun | The designer has not clarified it. I do not want to choose 20 because the elevation is easier to read or 15 because it uses less space.
Lena | Agreed. We need a [[clarification response::Clarification response must resolve the intended dimension; convenience or drawing readability does not establish the correct value.]] that identifies which dimension applies. Neither of those reasons is a design decision we can substitute for the missing answer.
Arun | Both sheets say B. Someone asked whether the section might be older, but I cannot support that from the labels we have in front of us.
Lena | We should not call either a [[superseded drawing::Superseded drawing would mean an earlier issue had been replaced; the shared B labels do not establish that status.]] on that basis. The shared revision letter does not tell us that one view overrides the other.
Arun | The fabrication-release review is due at 14:00. Please include that, because the unresolved panel detail will matter when the team checks readiness.
Lena | I will state the [[review deadline::Review deadline is 14:00 for the fabrication-release review, not an agreed designer-response time or automatic production permission.]] precisely. It explains the coordination need, but it does not guarantee a designer response by then or authorize us to guess.
Arun | Could the query quote both values in the same sentence? If only one appears in the subject line, the other might get lost when it is forwarded.
Lena | Yes. I will describe the [[drawing conflict::Drawing conflict keeps both incompatible values and their references visible in the handoff.]] as C4 revision B, 20 millimeters, versus S2 revision B, 15 millimeters, at the same end panel.
Arun | Good. And please ask for the reveal specifically. We are not asking the designer to recheck every cabinet dimension before answering this one point.
Lena | I will ask for the [[applicable dimension::Applicable dimension concerns the reveal at this end panel, not every cabinet measurement.]] for the reveal at that panel. The request can be specific without pretending the rest of the drawings have been verified.
Arun | What should the review record say if the answer has not arrived? I do not want an empty note to look as though the discrepancy disappeared.
Lena | It should preserve the [[unresolved detail::Unresolved detail keeps the unanswered reveal question visible instead of allowing silence to imply that it has been settled.]]. The absence of a reply does not resolve it, and the record should not say either dimension has been approved.
Arun | There was also a suggestion to split the difference. That would produce a number, but it would not tell us what the designer intended.
Lena | Correct. A midpoint is not [[design intent::Design intent requires clarification; averaging the conflicting values invents a result instead of establishing it.]]. We should not turn 17.5 millimeters into an invented solution simply because it lies between the two drawing values.
Arun | Please send the precise query and carry the unresolved status into the 14:00 review. I will not describe this conversation as permission to fabricate the panel.
Lena | I will keep [[fabrication release::Fabrication release is not granted here; the reveal still requires designer clarification.]] separate from the query. Both references, the shared revision, the conflicting reveal, and the review time will remain explicit in the handoff.''',
    transfer_title='Refer the conflicting detail',
    transfer_setup='Complete the drawing query using both references and values. Keep the shared revision and the unresolved status intact.',
    transfer='''Carpenter: "Elevation ___ revision B shows 20 millimeters." | C4 | C4 is the elevation reference carrying the 20-millimeter reveal.
Coordinator: "Section S2 revision B shows ___ millimeters." | 15 | Fifteen millimeters is the conflicting value on section S2.
Carpenter: "Both refer to the same end ___." | panel | The shared panel location is why the values conflict.
Coordinator: "The designer has not yet ___ the applicable dimension." | clarified | No clarification has resolved the conflict or authorized a dimension.''',
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
    dialogue='''Theo | This dark patch beside the laundry doorway worries me. Does it mean the joists underneath are rotten, or can you tell from what is exposed?
Nia | I can see [[dark staining::Dark staining is the observed discoloration on the exposed subfloor, not a confirmed finding of decay in concealed joists.]] on the subfloor. I cannot confirm rot in the joists because they are not visible and I have not assessed structural condition.
Theo | I thought the boards we can see might be the structural members themselves. Are we talking about two different parts of the floor?
Nia | Yes. The exposed [[subfloor::Subfloor is the visible supporting floor layer in this case, distinct from the concealed joists about which Theo asks.]] and the joists beneath it are different parts. Seeing a mark on this surface does not establish the condition of the concealed members.
Theo | So the mark is real, but my explanation for it is only a possibility. I would prefer the report to say that clearly.
Nia | I will record the [[site observation::Site observation preserves the visible staining and its location without turning the client's proposed explanation into a diagnosis.]] and your question separately. The note can say where the staining is without claiming that a particular cause has been found.
Theo | Could it be from water coming into the laundry area? I am trying to understand the next question, not asking you to guess a repair.
Nia | The [[moisture source::Moisture source has not been established; the question about water does not prove where it came from or what it affected.]] has not been established. I should not name a leak or another source from this appearance alone.
Theo | Who can assess it properly? I do not want the concern lost because we cannot see the joists during this conversation.
Nia | Sam, the project lead, can arrange a [[qualified assessor::Qualified assessor is the appropriate person to examine the relevant concern; no completed assessment or finding exists yet.]] to review the concern. I will include the location and the fact that the joists are not visible.
Theo | Does arranging that assessment mean we already know the floor needs replacing? I am concerned about both the disruption and the cost.
Nia | No [[repair proposal::Repair proposal is not established by requesting an assessment; replacement, cost, and disruption have not been determined.]] is established. An assessment request does not mean replacement has been decided, and I do not have a repair price to quote.
Theo | Equally, I suppose you cannot tell me everything is sound simply because you have not seen a damaged joist. They are still hidden.
Nia | Correct. The [[visibility limit::Visibility limit prevents both a confirmed decay diagnosis and a claim that concealed structural members are sound.]] works both ways. I cannot confirm decay, but I cannot use the lack of a visible joist as reassurance that the structure is sound.
Theo | That is clearer than a yes or no. Please make sure the report does not describe the stain as a completed structural inspection.
Nia | I will keep the [[investigation status::Investigation status remains unassessed for structural condition; describing staining is not equivalent to completing an inspection.]] accurate. There is a visible concern and a referral to arrange, not a completed structural inspection or a technical finding.
Theo | Can you read back the location and the unanswered question? I want Sam to understand exactly what prompted me to ask about the floor.
Nia | Dark staining on exposed subfloor beside the [[laundry doorway::Laundry doorway is the specific location of the observation, allowing the referral to identify the relevant area accurately.]]; joists not visible; structural condition not assessed; client asks whether decay may be present.
Theo | That is the question I meant. Please send it to Sam so the assessment can be arranged before anyone gives me a repair conclusion.
Nia | I will follow that [[referral route::Referral route passes the concern to Sam for arranging qualified assessment, without inventing a diagnosis or authorizing a repair.]]. The message will preserve what is seen, what is concealed, and what remains unknown, without adding a repair recommendation.''',
    transfer_title='Describe what is visible',
    transfer_setup='Complete the report to the project lead. Keep the observed surface separate from the concealed joists and the unperformed assessment.',
    transfer='''Carpenter: "Dark staining is visible on the exposed ___." | subfloor | Subfloor is the visible layer carrying the reported staining.
Client: "The joists are not ___." | visible | The joists remain concealed, so their condition cannot be judged from this view.
Carpenter: "Structural condition has not been ___." | assessed | No structural assessment has occurred in the supplied case facts.
Client: "Please ask Sam to arrange a qualified ___." | assessment | Assessment is the available next step, not a confirmed diagnosis or repair.''',
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
provisional idea | Initial proposal not yet fully defined or agreed. | record a provisional idea
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
    dialogue='''Amara | While you are replacing the skirting, could you build a bench along that bedroom wall too? It would make the room more useful.
Jules | I can pass on the idea, but the [[agreed scope::Agreed scope is bedroom skirting replacement only; the bench request does not automatically belong to that agreement.]] is skirting replacement only. A built-in bench would be a separate item rather than part of the existing task.
Amara | I understand it is more work. I was not sure whether it could simply be added while you are already here with the materials.
Jules | It is [[additional work::Additional work describes the bench beyond the existing skirting task, even though both would be in the same bedroom.]], and we need a defined proposal for it. Being on site does not establish the dimensions, the price, or when it could be completed.
Amara | Could you get it priced, then? I would like to know what is involved before deciding whether to go ahead with the idea.
Jules | I can arrange a [[separate quotation::Separate quotation is the available route for pricing the bench request; it is not an accepted price or permission to begin.]]. Asking for that quote does not mean you have approved the bench or agreed to pay an amount we have not supplied.
Amara | Good. I have not settled how long or deep it should be. Please do not assume the full length of the wall just because I pointed there.
Jules | I will keep the [[bench dimensions::Bench dimensions are not agreed; a pointing gesture does not establish length, depth, height, or a final design.]] unresolved. The handoff will describe a built-in bench request without turning your gesture into a fixed length or depth.
Amara | Would painting be part of it? I know the current job is carpentry, but I want to understand whether the new idea changes the decorating arrangement.
Jules | The current [[scope exclusion::Scope exclusion keeps decorating outside the existing booking; the bench discussion does not silently add painting or other finishing work.]] remains decorating. The bench request does not add painting to today's agreement, and any proposed finish would need to be stated in its own quotation.
Amara | That is useful. I would rather see exactly what a price includes than have a lower figure that leaves us disagreeing about the finish later.
Jules | A clear [[quotation scope::Quotation scope identifies what a proposed price covers, including any stated finish requirements, rather than relying on an unstated assumption.]] matters. We should not promise a finish, a design, or a service that has not been defined in the proposal.
Amara | Do you have an idea of when it could be ready? I am interested, but I do not want to make room arrangements around a guessed date.
Jules | No [[completion commitment::Completion commitment for the bench is absent; interest in the idea and a quotation referral do not establish a finish date.]] has been made for the bench. I cannot give you a confirmed date before the proposed work and arrangements are agreed.
Amara | Understood. Please keep the skirting replacement as the existing job. I do not want this question to sound like I have replaced that task with the bench.
Jules | I will preserve the [[existing contract::Existing contract continues to cover the skirting replacement; discussing a bench does not cancel or replace that task.]] scope. The skirting remains the agreed task, and the bench will be recorded as a separate request for pricing.
Amara | If I like the quote later, I can confirm the details through the normal process. For now, we are only taking the idea to the next stage.
Jules | Correct. [[Change authorization::Change authorization has not been given; a future decision would need to establish the additional work through the relevant process.]] has not happened in this conversation. I will not describe your interest as approval to start building or to choose measurements for you.
Amara | Please send the request with those open points. I want the bench considered, but I have not agreed dimensions, a price, or a completion date.
Jules | I will make that [[scope handoff::Scope handoff transfers the bench request with its unresolved dimensions, price, and timing while preserving the skirting-only agreement.]] clearly. The note will keep the bench proposal separate, preserve the decorating exclusion, and leave the unagreed details open for the quotation process.''',
    transfer_title='Keep an extra request separate',
    transfer_setup='Complete the client exchange about the bedroom work. Preserve the original task, excluded decorating, separate quotation, and unresolved bench dimensions.',
    transfer='''Carpenter: "The agreed task is replacing the ___." | skirting | Skirting replacement is the only work included in the current agreement.
Client: "Decorating remains ___." | excluded | The current booking excludes decorating, even after the bench question.
Carpenter: "I can arrange a separate ___ for the bench." | quotation | A quotation can be arranged without approving or pricing the work now.
Client: "The bench dimensions are not yet ___." | agreed | No bench measurements have been established or accepted during the conversation.''',
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
unreleased room | Area not yet handed over for the proposed work. | flag the unreleased room
purpose-specific access | Permission limited to a named activity. | respect purpose-specific access
hallway | Passage connecting rooms or areas. | identify the hallway
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
    dialogue='''Farah | Can you give me the study joinery update? I have a delivery note and a review time, but I want to know which arrangements are actually confirmed.
Ben | The [[delivery slot::Delivery slot is Tuesday morning for the joinery; it does not establish room access, storage permission, or installation readiness.]] is confirmed for Tuesday morning. The study, however, has not been released by the decorator for carpentry access.
Farah | So I should not put the room down as ready just because the supplier is coming. Do we have a release time from the decorator?
Ben | No confirmed [[access release::Access release for the study has not been given, and no release time is supplied in the case.]] time is available. I want that dependency kept visible rather than treated as settled in the delivery update.
Farah | What about the hallway at 11:00? I saw that on the notes and wondered whether it gave the crew somewhere to put the joinery temporarily.
Ben | The hallway is available for a [[trim review::Trim review is the specific activity allowed in the hallway at 11:00; it is not a material-storage arrangement.]] at 11:00. That is a separate activity, and the hallway is not available for material storage.
Farah | Thank you. I will not turn the review arrangement into a holding area. Is another place for the materials confirmed in the information you have?
Ben | No alternative [[storage location::Storage location is not confirmed elsewhere, and the hallway is explicitly excluded from material storage.]] is confirmed here. I should not invent one or assume that a room available for a discussion can receive the delivery.
Farah | Understood. I need to coordinate the access issue, but I do not want to tell the team you have moved the delivery without an actual arrangement.
Ben | I have not changed the [[confirmed delivery::Confirmed delivery remains Tuesday morning; reporting the access conflict does not itself reschedule the supplier.]]. Tuesday morning is still the stated slot. The update flags the mismatch without claiming that a replacement plan exists.
Farah | Is there any basis for saying installation starts immediately after delivery? That is how someone might read a short note if we leave access out.
Ben | No. [[Installation access::Installation access is unresolved because the study has not been released; a delivered product does not authorize fitting work there.]] remains unresolved. Delivery, room release, and the start of fitting work should not be compressed into one promise.
Farah | I also want to avoid blaming the decorator. We know the room has not been released, but the note does not tell us why or when that changes.
Ben | That is the right [[logistics update::Logistics update reports the actual arrangements and unresolved dependency without inventing a cause or blaming another trade.]] to give. I am reporting the current release status, not a reason for it or a claim that another trade has missed a deadline.
Farah | Please give me the four-point summary once more. I will use it when I coordinate with the people responsible for the room and the delivery.
Ben | Here is the [[status readback::Status readback repeats delivery, access, review, and storage separately so no permission is lost or expanded in the handoff.]]: Tuesday-morning delivery confirmed; study unreleased; hallway trim review at 11:00; no material storage in the hallway.
Farah | That makes the open question clear. I need to coordinate study access and any related arrangements without treating the hallway review as a solution to everything.
Ben | Yes. The [[schedule dependency::Schedule dependency is the unresolved study access, which remains distinct from the already confirmed delivery and review arrangements.]] is still the study release. No alternative storage, changed delivery slot, or installation start has been established in this update.
Farah | I will carry that into the coordination discussion. The team needs an accurate list of arrangements and restrictions, not a general statement that everything is ready.
Ben | Exactly. [[Purpose-specific access::Purpose-specific access limits the hallway arrangement to the trim review; it does not authorize storage or substitute for study access.]] is the key point for the hallway. I will keep the review permission and the storage restriction together whenever I pass the update on.''',
    transfer_title='Keep four arrangements separate',
    transfer_setup='Complete the coordinator update. Preserve the confirmed delivery, unreleased study, hallway review time, and storage restriction.',
    transfer='''Carpenter: "Delivery is confirmed for ___ morning." | Tuesday | Tuesday morning is the delivery slot, not a confirmed installation start.
Coordinator: "The study has not been ___ for carpentry access." | released | The decorator has not released the study for the intended work.
Carpenter: "The hallway trim review is at ___." | 11:00 | Eleven o'clock is the separate trim-review time supplied in the case.
Coordinator: "The hallway is not available for material ___." | storage | Storage is explicitly excluded even though the hallway review is allowed.''',
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
verification | Check establishing whether a claim or result is accurate. | complete verification
closeout status | Whether review and required follow-up are complete. | preserve the closeout status''',
    precision='Luis must withdraw all fronts are flush because D3 provides a specific exception. The observation is a projecting left edge relative to the neighboring front. It does not establish the projection amount, applicable tolerance, underlying cause, or correct remedy.',
    precision_extra='Record the component identifier, side, and comparison surface so follow-up is specific. Do not convert projects into a claim that the drawer is broken, or a possible adjustment into an agreed repair. The item remains open pending the appropriate assessment.',
    phrases='''Correct the earlier statement | I need to correct what I said about all the fronts being flush.\nAcknowledge the exception | You are right to point out D3.\nName the component | The observation concerns drawer D3.\nLocate the edge | Its left edge projects beyond the neighboring front.\nAvoid a guessed measurement | I have not established the amount of the offset.\nAvoid a tolerance claim | I have not checked the applicable tolerance.\nKeep the cause open | The cause has not been assessed.\nKeep the remedy open | I have not determined the appropriate remedy.\nAvoid blaming hardware | I cannot call the runner defective from this observation alone.\nRecord the follow-up | I will add the specific item to the snagging list.\nPreserve the comparison | The neighboring front is the reference in this observation.\nAvoid minimizing | I will not dismiss it as acceptable without checking.\nAvoid a repair promise | No repair method or completion time is agreed.\nLimit the finding | This identifies D3, not every drawer in the wardrobe.\nRead back the item | D3 left edge projects; cause and remedy unassessed.\nClose honestly | The earlier overall claim is corrected and this item remains open.''',
    notes='''All | A universal claim contradicted by even one verified exception.\nProjects beyond | Describes relative position without supplying a measured amount.\nLeft edge | Makes the observation more useful than saying the drawer looks wrong.\nUnassessed | Keeps an observation separate from a technical conclusion.\nCorrect what I said | Directly withdraws an inaccurate statement rather than quietly changing the subject.\nOpen item | Acknowledgement and recording do not establish that correction is complete.''',
    d='''Which opening corrects the earlier claim? | I need to correct that: D3's left edge is not flush with the neighboring front. | I said all, but I meant most, so nothing needs changing. | You must be looking at the wrong wardrobe. | The runner is definitely broken. | The opening explicitly withdraws the inaccurate overall claim and identifies the exception.
Which snag entry is precise? | D3 left edge projects beyond neighboring front; cause and remedy unassessed. | All drawers broken and replacement approved. | Wardrobe fine; no follow-up. | Five-millimeter failure repaired. | The entry preserves the component, side, reference surface, and unassessed cause and remedy.
Which conclusion is unsupported? | A replacement runner is definitely required. | D3 needs follow-up. | The left edge projects. | The earlier all-fronts claim needs correction. | No assessment establishes that the runner caused the projection or needs replacement.
What remains open after recording the item? | Cause, remedy, and any completion arrangement | Whether Luis made the earlier claim | Whether Priya identified D3 | Which edge is described | Recording the observation does not determine the cause, repair, or completion timing.''',
    dialogue='''Priya | You said all the fronts were flush, but look at D3. The left edge sits forward of the neighboring front, which does not match that description.
Luis | You are right. I need a [[correction of record::Correction of record explicitly withdraws the inaccurate claim that all fronts are flush in light of the D3 observation.]] here: my statement about all the fronts being flush was too broad. D3 is a specific exception.
Priya | Thank you. I want the exact drawer recorded, because a general note saying check the wardrobe could miss the point when someone comes back.
Luis | I will identify the [[drawer front::Drawer front is D3's visible face, the specific component Priya wants recorded rather than a vague whole-wardrobe concern.]] as D3 and state that its left edge projects beyond the neighboring front. That preserves the location and comparison.
Priya | Is it an adjustment issue, or is something wrong with the runner? I am asking because I do not know what makes one side project like that.
Luis | I have not assessed the [[root cause::Root cause remains unassessed; the visible projection does not establish a runner defect or another explanation.]]. I should not call the runner defective or promise an adjustment before the reason for the position is checked.
Priya | Have you measured how far it projects? I can see the difference, but I do not want a guessed number written down as if it was measured.
Luis | I have not established the [[offset::Offset is the amount of displacement between the fronts; no measured value is supplied by the visible observation alone.]]. The record can describe the visible projection without inventing a measurement or claiming a particular amount.
Priya | Then please do not dismiss it as within tolerance yet either. That would sound like a decision made before the relevant detail has been checked.
Luis | Agreed. I have not checked the applicable [[tolerance::Tolerance is the permitted variation under the relevant specification; no comparison with that requirement has been completed here.]]. I will not label it acceptable or unacceptable against a limit that has not been assessed.
Priya | What will you put on the follow-up list? I want the issue acknowledged without the note saying every drawer in the wardrobe has the same problem.
Luis | The [[snagging list::Snagging list records the specific D3 item for follow-up; it does not establish that every drawer has the same condition.]] entry will name D3, the left edge, and the neighboring front as the reference. It will not generalize to every drawer.
Priya | And the earlier statement will be corrected, rather than left above the new note? Otherwise someone could read the two entries and think the item is already resolved.
Luis | Yes. The original [[quality claim::Quality claim that all fronts were flush must be corrected rather than retained as a conflicting statement beside the new observation.]] needs correction. I will not leave an unqualified all-fronts statement standing as though this exception had not been identified.
Priya | Can you tell me when it will be put right? I would like to plan, but I understand you have not established what needs doing.
Luis | I do not have an agreed [[remedy::Remedy is the corrective action, which has not been determined; therefore no method or completion time can be promised here.]] or completion time. Recording the concern is the next step, not confirmation of a particular repair or return arrangement.
Priya | Please read the entry back. I want it specific enough for someone else to find the same edge without needing me to repeat this whole conversation.
Luis | The [[follow-up item::Follow-up item is the precise D3 left-edge projection, with cause and remedy left unassessed for the next review.]] is: drawer D3, left edge projects beyond neighboring front; cause and remedy unassessed; earlier claim that all fronts are flush corrected.
Priya | That is accurate. It acknowledges what we can see and leaves the technical explanation open, without turning the issue into a claim that all the work is wrong.
Luis | Correct. The [[closeout status::Closeout status remains open for D3 because recording the observation and correcting a statement do not complete the necessary follow-up.]] for D3 remains open. We have corrected the statement and recorded the observation, but we have not completed the assessment or the follow-up work.''',
    transfer_title='Correct and record the exception',
    transfer_setup='Complete the review exchange. Correct the universal claim, identify the projecting edge, and leave the cause and remedy unresolved.',
    transfer='''Carpenter: "I need to correct my claim that all fronts are ___." | flush | Flush was the inaccurate overall claim contradicted by D3's projecting edge.
Client: "The specific drawer is ___." | D3 | D3 identifies the drawer that needs the recorded follow-up.
Carpenter: "Its ___ edge projects beyond the neighboring front." | left | Left identifies the side of the visible projection in the case.
Client: "The cause and remedy remain ___." | unassessed | Neither cause nor remedy has been determined by the observation alone.''',
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
    dialogue='''Daniel | I have the cabinet drawings and the care sheet. Before we finish the handover, can we confirm what is still open and who is following it up?
Mina | Yes. The [[handover pack::Handover pack includes the cabinet drawings and correct finish care sheet already received; the replacement cover remains a separate open item.]] documents are with you, including the correct sheet for the finish. The replacement shelf pin cover is still outstanding.
Daniel | Is the cover already here waiting to be fitted, or are we waiting for it to arrive? I want to record the right stage.
Mina | We are waiting for [[part receipt::Part receipt has not occurred because the replacement shelf pin cover is due but has not been delivered.]]. The cover is due, but it has not been delivered. I should not describe it as here or ready to fit.
Daniel | Who will contact the supplier about it? I do not want each person to assume someone else is checking while the item remains open.
Mina | I accept the [[supplier follow-up::Supplier follow-up is Mina's accepted responsibility for the outstanding cover, rather than an unassigned action for someone else.]]. I will contact the supplier about the cover, and the record should name me as the person responsible.
Daniel | Thank you. When will I hear from you? A clear update time would help even if the delivery arrangement is not settled yet.
Mina | I will call you on Friday. That is my [[callback commitment::Callback commitment is Mina's explicit promise to call Friday, distinct from a request or a confirmed delivery arrangement.]], so you have a definite contact point rather than an open-ended note to wait for news.
Daniel | Does Friday also mean you will return to fit the cover, or is that only the call? I need to know whether to arrange access.
Mina | It is the call, not [[appointment confirmation::Appointment confirmation for a return visit has not been given; Friday identifies the promised call only.]]. No return-visit date is confirmed, and I do not have a confirmed arrival date for the part to give you.
Daniel | All right. I will not keep Friday free for a visit on that basis. Please make that distinction clear if another person reads the handover record.
Mina | I will preserve the [[commitment boundary::Commitment boundary limits the Friday promise to a call, without expanding it into delivery or physical attendance.]]. The entry will show supplier follow-up with Mina and a Friday call, with the return visit still unconfirmed.
Daniel | One other question: does anything you have said today change the warranty? I have the document, but I do not want two different versions of the terms.
Mina | The [[warranty document::Warranty document remains the source of the applicable terms; Mina does not add or remove coverage through this handover conversation.]] remains the reference. I am not adding broader coverage verbally or changing the terms supplied with your records.
Daniel | Good. I will use that document for the terms and the care sheet for the finish instructions, rather than treat the outstanding cover note as either one.
Mina | Exactly. The [[care sheet::Care sheet contains the relevant finish-care information and is already received; it is distinct from warranty terms and the open-part record.]] and warranty document have different purposes. Receiving them does not establish that the replacement cover has arrived or been fitted.
Daniel | Could you read the final record back? I want the documents acknowledged without the whole handover being marked complete while the cover is still missing.
Mina | The [[handover record::Handover record must distinguish received documents from the undelivered cover and preserve Mina's follow-up and Friday-call commitment.]] says drawings and correct care sheet received; replacement cover outstanding; supplier follow-up owned by Mina; Friday callback committed; return date unconfirmed.
Daniel | That is clear. Please keep the cover on the open list until its actual outcome is confirmed. The Friday call will give us the next communication point.
Mina | I will retain it in the [[open-item tracker::Open-item tracker keeps the replacement cover unresolved until the actual outcome supports closure, rather than closing it because documents were supplied.]]. We can acknowledge the documents received while keeping the part, its follow-up, and any later attendance arrangement visible.''',
    transfer_title='Confirm the promise without expanding it',
    transfer_setup='Complete the handover exchange. Distinguish received documents, the undelivered cover, Mina as owner, and the Friday callback.',
    transfer='''Owner: "The drawings and correct care sheet are ___." | received | The case confirms that both documents have reached the owner.
Lead: "The replacement cover has not been ___." | delivered | The cover is due but has not arrived, so it remains outstanding.
Owner: "___ owns the supplier follow-up." | Mina | Mina explicitly accepts responsibility for contacting the supplier about the cover.
Lead: "I will call ___; the return visit is not confirmed." | Friday | Friday is the committed call date, not an agreed return visit.''',
))
