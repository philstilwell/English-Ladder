"""Original semiconductor workplace conversations and structured practice."""
from books.authoring import unit

BOOK = dict(
    slug='semiconductor', title='Semiconductor English',
    cover_label='Fab / metrology / qualification / foundry',
    cover_title='Semiconductor', cover_size=32,
    tagline='Name the layer. Qualify the result. Align the handoff.',
    audience='For process, integration, equipment, yield, product, test, and foundry-facing teams.',
    map_intro='Eight semiconductor conversations connecting process context, measurement, yield, qualification, and delivery commitments.',
    notes_title='A number needs its process context.',
    notes_intro='Semiconductor discussions compress complex evidence into phrases such as CD shift, yield gain, matched tool, and tape-out ready. Useful communication restores the missing context: layer, stage, lot, measurement recipe, test coverage, or decision status. These cases practice precise technical questions and concise updates that help different specialties work from the same facts.',
    field_notes=[
        ('Locate the observation', 'Identify the layer, process stage, lot or wafer, tool, and time relevant to the claim. A change after etch is not automatically the same as a change measured in developed resist.', '"The reported shift is on M2 after etch; the measurement recipe also changed."'),
        ('Keep the denominator visible', 'Yield and defect figures depend on what was counted, sampled, and compared. State the population and measurement basis before interpreting the difference.', '"The pilot result is 92 passing die out of 100 tested, with a different product mix."'),
        ('Separate settings from performance', 'Identical recipe names do not prove tools behave alike. Compare the evidence against a defined matching criterion and distinguish availability from qualification.', '"Both means are within specification, but the pair misses our matching limit."'),
        ('Do not compress pending into complete', 'A finished test, a submitted layout, and a possible capacity slot each have a limited meaning. Name the remaining checks and who can authorize the next step.', '"One qualification test passed; two required tests remain open."')],
    scope_note='Original fictional English practice, not a fabrication recipe, equipment procedure, product qualification, design sign-off, or production authorization. Numbers, lots, organizations, and schedules are invented. Real work must follow approved process documents, safety rules, applicable standards, customer requirements, and authorized engineering decisions.',
    sources=[
        dict(title='ASML. How Microchips Are Made.', url='https://www.asml.com/en/technology/all-about-microchips/how-microchips-are-made', note='Background on wafer processing, layers, lithography, and industry roles. The cases do not specify an actual fabrication flow or reproduce an equipment recipe.', checked='30 September 2026'),
        dict(title='NIST/SEMATECH. Engineering Statistics Handbook, Section 6.3.1: What Are Control Charts?', url='https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm', note='Background on monitoring process behavior. The yield comparisons use invented data and do not claim a completed statistical process study.', checked='30 September 2026'),
        dict(title='Texas Instruments. Reliability.', url='https://www.ti.com/quality-reliability/reliability.html', note='An industry example of reliability and qualification practice. The fictional three-test plan is not asserted as a universal qualification requirement.', checked='30 September 2026'),
        dict(title='SkyWater SKY130 PDK Documentation. Process Design Rules.', url='https://skywater-pdk.readthedocs.io/en/main/rules.html', note='An open example of process-specific design rules, layer definitions, and physical verification terminology. The tape-out case does not use or approve a real design.', checked='30 September 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Wafer Fabrication Flow and Process Integration',
    scene='Back-end does not always mean packaging',
    skill='Explain the current process stage and ownership without confusing wafer interconnect fabrication with package assembly.',
    brief='New product coordinator Eric describes lot L24 as being in packaging because the status says BEOL. Integration engineer Min explains that this lot is still in wafer fabrication, building on-wafer interconnect layers. Its current operation concerns metal layer M2. In this fictional route, an inspection review must be completed before the next authorized operation. Packaging has not started, and the lot is on hold pending that review. Eric must correct the customer update without inventing a shipping date.',
    cast='Eric | Product coordinator\nMin | Process integration engineer',
    culture=('Expand the abbreviation at a handoff', 'Back-end can refer to different stages in different teams. Use the full process name when crossing organizational boundaries, then identify the actual operation and lot status. Familiar shorthand is efficient only when the receiver shares its meaning.'),
    a='''Where is L24 now? | In wafer fabrication at an M2-related operation | In completed package assembly | In final shipment inspection | In customer field qualification | The briefing places L24 in wafer fabrication, not the packaging stage Eric inferred.
What does BEOL mean in this case? | Back end of line, forming on-wafer interconnects | Completed assembly and final test | A confirmed customer delivery date | A shipping release status | The integration engineer uses BEOL for on-wafer interconnect fabrication.
What prevents the next operation? | A pending inspection review and lot hold | A completed packaging qualification | A customer order cancellation | A recorded shipment approval | The lot remains on hold until the stated inspection review and authorized disposition.''',
    vocabulary='''wafer | A semiconductor substrate on which many devices are fabricated. | process a wafer
die | An individual circuit area or chip separated from a wafer. | identify the die
fab | A semiconductor fabrication facility. | move material through the fab
wafer fabrication | Processes that form devices and interconnects on wafers. | track wafer fabrication
process flow | The defined sequence of manufacturing operations. | review the process flow
process integration | Coordination of process steps into a functioning device flow. | assess process integration
FEOL | Front end of line, principally the formation of active devices. | complete FEOL processing
MOL | Middle of line, connecting devices to the interconnect structure. | review MOL interfaces
BEOL | Back end of line, forming the on-wafer interconnect structure. | track BEOL progress
interconnect | A conductive structure connecting circuit elements. | form an interconnect
metal layer | A defined level of conductive routing in a chip. | identify the metal layer
via | A conductive connection between interconnect levels. | inspect a via
dielectric | An electrically insulating material used between conductors. | deposit a dielectric
process module | A related group of operations within the fabrication flow. | qualify a process module
lot | A tracked group of wafers or units processed under defined identity. | identify the lot
wafer ID | The identifier assigned to an individual wafer. | confirm the wafer ID
route | The controlled sequence assigned to a tracked product or lot. | follow the approved route
traveler | A record accompanying material through its required operations. | update the traveler
WIP | Work in process: material not yet through the defined manufacturing flow. | report WIP status
lot hold | A restriction preventing a lot from proceeding without disposition. | place a lot on hold
disposition | An authorized decision about the next treatment or status of material. | obtain lot disposition
wafer sort | Electrical testing of individual die while on the wafer. | schedule wafer sort
dicing | Separating individual die from a wafer. | complete wafer dicing
package assembly | Integrating and protecting die in the intended package structure. | begin package assembly''',
    precision='BEOL is still part of wafer fabrication in this conversation. It is not interchangeable with package assembly, although some organizations also use back-end for assembly and test. Expand the term and state the actual operation before communicating status.',
    precision_extra='A lot at a later fabrication stage is not necessarily ready to ship. L24 remains on hold for inspection review. Its next move depends on the approved route and authorized disposition; no packaging start or delivery commitment is supplied.',
    phrases='''Clarify the abbreviation | Here BEOL means back end of line.
Locate the work | The lot is still in wafer fabrication.
Name the layer | The current operation concerns metal layer M2.
Separate the stages | On-wafer interconnect formation is not package assembly.
Explain integration | We need to preserve compatibility between successive process modules.
Identify the material | Which lot and wafer IDs does the update cover?
Check the route | What is the next operation on the approved route?
State the hold | L24 is on hold pending inspection review.
Keep authority explicit | The next move needs authorized disposition.
Avoid a shipping inference | This stage does not establish a shipment date.
Distinguish the tests | Wafer sort and final packaged-device test are different steps.
Confirm the handoff | Which team owns the inspection review?
Correct the update | Packaging has not started for this lot.
Preserve traceability | Keep the traveler linked to the lot and operation.
Ask for the status basis | Does completed mean processed, inspected, or released?
Close precisely | Report the stage, hold reason, owner, and next decision.''',
    notes='''Back-end | May mean BEOL or assembly and test; clarify context.
Complete | Specify the operation and whether inspection or release is included.
Lot | A tracking group, not necessarily one die or one finished package.
Next | Must follow the approved route and current restrictions.
Ready | Needs a named next step and its prerequisites.
Released | Means a specific authorized status change, not merely elapsed time.''',
    d='''Which customer update is accurate? | L24 remains in wafer fabrication at M2, on hold for inspection review; packaging has not started. | L24 has completed the interconnect stack and awaits wafer sort. | L24 is in package assembly with final electrical test pending. | L24 is at M2 and can move while the inspection report is being completed. | M2 identifies the current fabrication work, not completion of the stack or assembly. The hold still prevents an unapproved next move.
Why expand BEOL for the coordinator? | Different teams can use back-end for different parts of the manufacturing chain. | BEOL always means package assembly in every organization. | Acronyms eliminate the need to name an operation. | The lot ID alone reveals its full status. | Expanding the term prevents a cross-team ambiguity that already caused an inaccurate update.
What is the appropriate next-step wording? | The lot awaits inspection review and authorized disposition under its route. | Move the lot because M2 is usually near completion. | Skip the review because packaging has not started. | Promise shipment before checking the remaining flow. | The stated hold and route control what may happen next, not a generic assumption about progress.
Which distinction is correct? | Wafer sort tests die on the wafer; package assembly integrates die into packages. | Wafer sort separates die mechanically; dicing classifies their electrical performance. | BEOL joins die to package substrates; package assembly forms on-wafer metal layers. | FEOL forms package connections; BEOL forms the active transistor devices. | Wafer sort is electrical testing, dicing is physical separation, FEOL principally forms devices, and BEOL forms on-wafer interconnects.''',
    dialogue='''Eric | I wrote that L24 is in packaging because the status says BEOL. The customer wants to know whether that means finished parts will be ready soon.
Min | Here [[BEOL::BEOL refers to the on-wafer interconnect stage in this case, not to completed package assembly.]] means back end of line. We are building the interconnect structure on the wafer, so your update places the lot at a later stage than the record supports.
Eric | That explains the confusion. The assembly team also calls its work back-end, so I assumed both groups meant the same stage.
Min | Use [[wafer fabrication::Wafer fabrication locates the current work on the wafer before the package assembly stage described in the mistaken update.]] in the customer message, then name the actual operation. Expanding the term is especially useful when the reader does not share our process shorthand.
Eric | I will name M2 in the update. Does that identify the current layer, rather than mean the full interconnect stack is finished?
Min | Correct. M2 is the relevant [[metal layer::The metal layer identifies the specific interconnect level involved in the current operation.]]. A layer name locates the work, but it does not by itself tell you that inspection, disposition, or later stages have finished.
Eric | Can you explain how that fits with the earlier device work? I need enough context to brief the customer without reciting every operation in the fab.
Min | [[FEOL::FEOL principally forms active devices, distinct from the later on-wafer interconnect work now involving L24.]] principally forms the active devices, while later interconnect work connects them. The exact flow is technology-specific, so use our product route for the actual sequence and status.
Eric | I also see that inspection review is pending. The lot cannot simply move to its next listed operation because someone has already processed the current step.
Min | It is on a [[lot hold::A lot hold restricts further movement until the required review and authorized disposition occur.]]. That restriction remains in place until the required review and authorized decision. Processed, inspected, and released are different status claims.
Eric | Then the update should identify what must happen before the next move, not describe the hold as if it were just a routine scheduling delay.
Min | Yes. We need [[disposition::Disposition is the authorized decision about how the lot may proceed after review, not an assumption based on its position in the flow.]] under the approved process. The review owner can explain the decision basis; we should not predict the outcome before that evidence is assessed.
Eric | I will confirm the owner and preserve the lot reference. We should also keep the record connected to the individual wafers where the inspection information requires that detail.
Min | Keep the [[traveler::The traveler connects the material with its operation history and required next steps, supporting traceable status communication.]] and relevant wafer IDs aligned with the update. Otherwise two teams may discuss different material while assuming they are referring to the same issue.
Eric | What later stages should I distinguish in the message? I need to explain why an M2 status does not yet give the customer a finished-product date.
Min | Exactly. [[Wafer sort::Wafer sort is electrical testing of die on the wafer and is distinct from package assembly or shipment.]], dicing, assembly, and subsequent checks have their own place in the approved route. Their timing is not established by the M2 entry alone.
Eric | I will correct the packaging statement now, before the customer plans around a stage the lot has not reached.
Min | Say that [[package assembly::Package assembly is the later integration of die into packages, which has not started for L24.]] has not started for this lot. You can give a precise current status without inventing dates for the remaining operations.
Eric | The revised message will locate L24 in wafer fabrication at M2, explain the inspection hold, and identify the next review. It will leave shipment timing uncommitted.
Min | That reflects the [[process flow::The process flow connects the current stage and authorized next steps without collapsing fabrication, testing, and assembly into one label.]] accurately. The customer gets a clear explanation of progress and the pending decision instead of an optimistic interpretation of an abbreviation.''',
    rehearsal=[
        'Check the dialogue answers. Read Eric and Min aloud, expanding BEOL and FEOL when they appear.',
        'Switch roles. Read turns 9-20 again, stressing the hold, required decision, and stage not yet started.',
        'Complete the transfer and check its key. Read the corrected update without adding a shipping date.'],
    transfer_title='Name the stage before the date',
    transfer_setup='Lot N6 is forming on-wafer interconnects. It is on hold for inspection review. Package assembly has not started, and no shipping date is confirmed.',
    transfer='''Coordinator: "I will correct the update: this on-wafer interconnect work is still ___." | BEOL | BEOL names the on-wafer interconnect stage, not package assembly.
Engineer: "Keep the restriction visible too; the record still shows a ___." | lot hold | A lot hold restricts movement while the required review and decision remain open.
Coordinator: "Then I should not tell the customer we have started ___." | package assembly | Package assembly is distinct from the current on-wafer work and has not begun here.
Engineer: "Correct. Ask the review owner for the authorized ___ before discussing the next move." | disposition | Disposition is the authorized material decision, not a date inferred from the process stage.'''))

BOOK['units'].append(unit(
    title='Lithography, Reticles, and Critical Dimensions',
    scene='A three-nanometer shift without a common basis',
    skill='Clarify a reported dimension change by identifying the layer, process stage, sampling, and measurement recipe before attributing a cause.',
    brief='Lithography engineer Lina reviews a reported critical-dimension increase with metrology engineer Theo. The summary initially omits the layer and stage. The records show M2 after etch, with means of 86 nm and 89 nm. However, the two measurements used different CD-SEM recipes and different sampling sites. No comparable remeasurement, specification assessment, or cause investigation is complete. Lina must report the apparent 3 nm difference without treating it as a confirmed lithography shift or changing an exposure setting.',
    cast='Lina | Lithography engineer\nTheo | Metrology engineer',
    culture=('Ask which dimension was measured', 'CD shift sounds specific but can conceal different features, stages, or measurement settings. A useful challenge asks for the measurement basis before debating process causes. Do not assume that a post-etch result isolates lithography or that a changed mean proves a specification violation.'),
    a='''Which layer and stage do the records identify? | M2 after etch | Unspecified resist before exposure | Final package thickness | M2 before every fabrication step | The recovered records specifically locate the two means on M2 after etch.
What is the reported numerical difference? | An increase of 3 nm | A decrease of 3 nm | An increase of 89 nm | No numerical difference | Subtracting the first mean, 86 nm, from the second, 89 nm, gives a 3 nm increase.
Why is a direct process attribution premature? | The measurement recipes and sampling sites differ. | Both figures use nanometers. | The layer is now identified. | Every post-etch result can only originate in lithography. | Changed measurement and sampling conditions prevent the difference from isolating a process cause.''',
    vocabulary='''lithography | Pattern formation using exposure of a sensitive layer. | review lithography performance
reticle | A patterned optical element used in lithographic exposure. | identify the reticle
photoresist | A radiation-sensitive material used to form a pattern. | coat the photoresist
exposure dose | The delivered exposure energy per unit area. | record exposure dose
focus offset | A displacement from a defined best-focus reference. | evaluate focus offset
critical dimension | A feature dimension important to process or device performance, abbreviated CD. | measure critical dimension
CD-SEM | A scanning electron microscope used for critical-dimension measurement. | verify the CD-SEM recipe
measurement recipe | The controlled settings and analysis used to obtain a measurement. | confirm the measurement recipe
sampling site | A specified location selected for measurement. | align sampling sites
post-develop | Measured or occurring after resist development. | review post-develop CD
post-etch | Measured or occurring after an etch operation. | compare post-etch measurements
etch bias | A dimensional difference associated with pattern transfer through etch. | evaluate etch bias
overlay | Alignment accuracy between patterned layers. | measure overlay
alignment mark | A feature used to position a layer or measurement. | inspect alignment marks
line-edge roughness | Variation of a patterned line edge from its intended shape. | assess line-edge roughness
line-width roughness | Variation in the width of a patterned line. | assess line-width roughness
pitch | The repeat distance between corresponding features. | specify feature pitch
pattern fidelity | Agreement between the intended and produced pattern. | assess pattern fidelity
optical proximity correction | Layout adjustments compensating for imaging effects, abbreviated OPC. | review optical proximity correction
focus-exposure matrix | A test pattern set spanning selected focus and dose conditions. | analyze a focus-exposure matrix
depth of focus | A usable focus range under a defined imaging criterion. | assess depth of focus
exposure latitude | A usable dose range under a defined imaging criterion. | estimate exposure latitude
measurement bias | A systematic measurement difference relative to a reference. | assess measurement bias
remeasurement | A repeated measurement under identified conditions. | request comparable remeasurement''',
    precision='The arithmetic difference is 3 nm. That does not prove a 3 nm physical process shift because the recipes and sampled sites differ. A post-etch CD combines the history of pattern formation and transfer; it does not identify exposure as the sole cause.',
    precision_extra='CD and overlay measure different properties: feature size and layer alignment. Neither should be substituted for the other. A specification judgment also needs the applicable limits and measurement basis, which are not supplied as resolved facts in this case.',
    phrases='''Locate the dimension | Which layer and feature does the CD refer to?
Identify the stage | These measurements are from M2 after etch.
State the numbers | The reported means are 86 and 89 nm.
Qualify the difference | The apparent difference is 3 nm.
Ask about measurement | Did both datasets use the same CD-SEM recipe?
Check sampling | Were the same types of sites sampled?
Avoid a causal shortcut | Post-etch CD does not isolate exposure performance.
Separate metrics | Overlay is not another name for critical dimension.
Request comparability | Remeasure on an agreed, traceable basis.
Preserve the originals | Keep both original recipes with their datasets.
Avoid an unsupported adjustment | Do not infer an exposure change from this comparison alone.
Ask for limits | Which specification applies to this feature and stage?
Distinguish variation | A mean shift and within-wafer variation are different questions.
Clarify reticle identity | Which reticle revision was used for the layer?
Describe the next check | Resolve the measurement difference before attributing the process cause.
Close the report | State the apparent shift and the comparability limitation together.''',
    notes='''Shift | Specify whether apparent, confirmed, or attributed.
CD | Identify feature, layer, stage, and measurement method.
Post-etch | Describes a stage, not proof of which earlier step caused a change.
Same recipe | Confirm the actual revision, not only the displayed name.
Out of spec | Needs the applicable limit and a valid measurement basis.
Adjust | Requires an authorized technical decision, not a language exercise inference.''',
    d='''Which report sentence is justified? | The means differ by 3 nm, but recipe and site changes limit comparability. | Exposure drift has been confirmed at exactly 3 nm. | Both datasets prove the same physical result because they use nanometers. | M2 is out of specification without any stated limit. | The sentence reports the arithmetic while preserving the unresolved measurement basis.
Which comparison best helps investigate the apparent change? | Comparable measurements on identified sites using an agreed recipe basis | Repeating both datasets with their different original recipes and locations | Increasing sample counts while leaving recipe and site differences uncontrolled | Comparing the post-etch mean with a post-develop mean as though the stages were identical | An agreed measurement basis addresses the changed recipes and sampling. More data alone does not remove those differences, and different stages answer different questions.
Why is post-etch important? | The result follows pattern transfer and does not isolate lithography alone. | It means no etch process has occurred. | It establishes that every cause is in the reticle. | It makes the sampling locations irrelevant. | The measurement stage affects interpretation because more than the exposure step contributes to the resulting feature.
Which distinction is accurate? | CD concerns feature size; overlay concerns layer alignment. | CD measures layer alignment; overlay measures a line's width. | Pitch measures line-edge variation; line-edge roughness measures repeat distance. | Etch bias is the exposure energy; exposure dose is the post-etch dimensional change. | CD and overlay separate size from alignment. Pitch is repeat distance, roughness is edge variation, dose is exposure energy per area, and etch bias concerns dimensional transfer.''',
    dialogue='''Lina | The review slide says CD shifted, but it does not identify the layer or the measurement stage. I cannot tell which process team should investigate first.
Theo | The records identify [[post-etch::Post-etch locates the measurement after pattern transfer, which matters when interpreting possible causes.]] M2 measurements. The two means are eighty-six and eighty-nine nanometers, so the reported numerical increase is three nanometers.
Lina | That locates the result, but I still need to know whether the two measurements were obtained on a comparable basis before calling it a physical process shift.
Theo | The [[measurement recipe::The measurement recipe defines settings and analysis that can affect the reported CD and differs between these datasets.]] changed between datasets. Both used CD-SEM, but sharing the instrument type does not mean their settings and analysis were identical.
Lina | Were the same locations measured? A different selection across the wafer could also change the average without establishing the process explanation stated in the meeting.
Theo | The [[sampling site::A sampling site is a selected measurement location; different site selections can affect the reported average.]] selection changed too. We need the location records alongside the recipes, rather than treating the two mean values as a controlled before-and-after comparison.
Lina | I will keep the three-nanometer difference and remove the exposure-drift conclusion. Can we show the changed recipe and sites beside the two means?
Theo | Correct. The [[critical dimension::Critical dimension is the relevant feature size, but its reported change does not alone establish the physical cause.]] result is important, but the present comparison does not separate process behavior from measurement and sampling effects.
Lina | Because this is after etch, the final feature can reflect both the earlier resist pattern and the transfer step. It is not a direct exposure-only measurement.
Theo | Exactly. [[Etch bias::Etch bias concerns the dimensional change associated with pattern transfer and is one reason post-etch CD does not isolate exposure.]] is a separate consideration in the investigation. Naming it does not establish that etch caused this case, but it prevents an unjustified shortcut to lithography.
Lina | The review also asks whether this is an alignment problem. Can we clarify that separately? I do not want the CD figure copied into an overlay conclusion.
Theo | [[Overlay::Overlay describes alignment between layers, whereas CD describes a feature dimension.]] concerns alignment between layers. It is not another name for feature width, so this CD comparison cannot be relabeled as an overlay finding.
Lina | Our next request should identify the relevant feature, layer, stage, locations, and agreed measurement settings. Then the engineers can compare results with a traceable basis.
Theo | Request comparable [[remeasurement::Remeasurement on an agreed basis can help determine whether the apparent difference persists under comparable conditions.]] through the approved process. Preserve the original datasets too, because their recipes and locations are part of the explanation for what was initially reported.
Lina | If the difference persists, the team can investigate possible process causes with better evidence. If it does not, we still need to explain the original discrepancy.
Theo | Yes. Assess [[measurement bias::Measurement bias is a systematic difference in measurement relative to a reference and is distinct from an assumed process shift.]] and other relevant effects rather than force either outcome. The aim is a supported interpretation, not a preferred conclusion that the process changed or stayed identical.
Lina | I will include the reticle revision in the context record as well. That gives the investigation the configuration information without implying the reticle has been found defective.
Theo | Good. The [[reticle::The reticle carries the lithographic pattern; identifying its revision provides context without proving it caused the observation.]] identity belongs with the layer history. Configuration details help evaluate hypotheses, but listing a component does not make it the cause.
Lina | The revised slide will keep the two means and the three-nanometer difference, state the changed measurement basis, and leave the cause and specification assessment open.
Theo | That protects [[pattern fidelity::Pattern fidelity concerns how well the produced pattern matches its intent; assessing it requires more than an unexplained mean difference.]] discussions from unsupported conclusions. We can plan the next evidence review without treating this comparison as permission to change exposure settings.''',
    rehearsal=[
        'Check the answers. Read 86 nm and 89 nm as complete spoken measurements.',
        'Switch roles for turns 7-16. Stress apparent difference, post-etch, and the changed measurement basis.',
        'Check and read the transfer twice. Keep feature size distinct from alignment.'],
    transfer_title='Same units, different measurement basis',
    transfer_setup='A layer has reported means of 120 and 124 nm after etch. Different measurement recipes and sampling sites were used. The cause is not established.',
    transfer='''Engineer: "Check that both reports refer to the same ___." | critical dimension | Critical dimension refers to feature size, not the settings or locations used to measure it.
Reviewer: "Send the settings and analysis from each ___." | measurement recipe | The recipe defines the settings and analysis that differ between the datasets.
Engineer: "I will attach a wafer map of both sets of ___." | sampling sites | Sampling sites identify the measurement locations, which also differed in this case.
Reviewer: "Good. An alignment claim would need separate ___ evidence." | overlay | Overlay addresses alignment rather than the reported feature-size difference of four nanometers.'''))


BOOK['units'].append(unit(
    title='Deposition, Etch, CMP, and Process Windows',
    scene='A better center point is not a wider window',
    skill='Describe a process trial improvement without extending it to untested conditions or overlooking downstream integration effects.',
    brief='Deposition engineer Yuki and integration engineer Sam review a trial film process. At the nominal setting, a defined thickness-nonuniformity metric falls from 5% to 3%; lower is better on this unchanged measurement basis. Only that center condition has been tested. The proposed low and high settings remain untested, and effects on subsequent etch and chemical mechanical planarization are not assessed. The new recipe is not released. A summary nevertheless says the complete process window is validated.',
    cast='Yuki | Deposition engineer\nSam | Integration engineer',
    culture=('Celebrate a bounded improvement', 'An encouraging center-point result is worth reporting. State the metric and tested condition, then identify the untested range and integration questions. This lets colleagues recognize progress without confusing a promising experiment with a released process window.'),
    a='''What improved in the supplied trial? | The stated nonuniformity metric fell from 5% to 3% at the nominal setting. | Every condition in the proposed range was tested. | Etch and planarization were fully qualified. | The new recipe received production release. | The only reported improvement concerns the unchanged metric at one tested condition.
What is the absolute change in that percentage metric? | A decrease of 2 percentage points | A decrease of 2 relative percent | An increase of 3 percentage points | A decrease of 5 percentage points | Five percent minus three percent equals two percentage points on the stated metric.
Which conclusion is premature? | The complete process window is validated. | The nominal-setting result improved on the stated metric. | The low and high settings remain untested. | Downstream integration effects remain open. | The broader range and downstream behavior were not assessed, so full-window validation is unsupported.''',
    vocabulary='''deposition | Formation of a material film on a surface. | qualify a deposition step
thin film | A material layer with a small controlled thickness. | characterize the thin film
CVD | Chemical vapor deposition, forming a film through chemical reactions of vapor precursors. | evaluate CVD film properties
PVD | Physical vapor deposition, forming a film from material vaporized by methods such as sputtering or evaporation. | review PVD performance
ALD | Atomic layer deposition, using successive self-limiting surface reactions. | assess ALD conformality
precursor | A starting substance used in a film-forming reaction. | qualify the precursor
conformality | How consistently a film coats different surface orientations or features. | assess film conformality
step coverage | Film thickness on a specified feature relative to thickness on a reference surface. | evaluate step coverage
film stress | Internal stress within a deposited film. | measure film stress
thickness nonuniformity | Variation in film thickness under a defined metric. | report thickness nonuniformity
etch selectivity | Relative removal rates of different materials in an etch process. | assess etch selectivity
anisotropy | Direction-dependent behavior, such as preferential vertical removal. | evaluate etch anisotropy
endpoint detection | Monitoring used to identify a process completion condition. | verify endpoint detection
overetch | Additional etching beyond a defined clearing or endpoint condition. | assess overetch effects
CMP | Chemical mechanical planarization, combining chemical and mechanical surface removal. | evaluate CMP compatibility
slurry | A polishing fluid mixture supplying chemical action and often suspended abrasive particles in CMP. | qualify the CMP slurry
dishing | Local depression of a material surface during planarization. | measure dishing
erosion | Excess regional material removal during planarization. | assess erosion
process window | A range of conditions meeting defined process requirements. | establish the process window
nominal setting | The chosen central or reference process setting. | test the nominal setting
corner condition | A selected limiting combination in an evaluation range. | evaluate corner conditions
process interaction | An effect arising from the relationship between process steps or factors. | investigate process interactions
integration trade-off | An exchange between benefits and effects across process steps. | explain the integration trade-off
recipe release | Authorization of a controlled process recipe for defined use. | obtain recipe release''',
    precision='The metric improves by 2 percentage points, a 40% relative reduction from its initial 5% value. Neither calculation establishes the proposed window. The same measurement definition is used here; other nonuniformity formulas must not be mixed into the comparison.',
    precision_extra='A deposition improvement can affect later etch and planarization behavior. The case supplies no result for those steps. Describe their assessment as pending, not as either a guaranteed benefit or a demonstrated new failure.',
    phrases='''Identify the metric | The defined thickness-nonuniformity metric fell from 5% to 3%.
Keep the basis fixed | Both values use the same measurement definition.
State the condition | The result applies to the nominal setting only.
Separate changes | That is two percentage points, or a 40% relative reduction.
Limit the claim | One center point does not establish a process window.
Name the missing tests | The proposed low and high settings are untested.
Check interactions | What does the film change mean for the subsequent etch?
Ask about planarization | Has compatibility with the CMP step been assessed?
Avoid a causal leap | Better uniformity does not prove every film property improved.
Identify trade-offs | We still need the integration trade-off assessment.
Qualify maturity | This is a trial result, not a released recipe.
Ask for criteria | Which responses must meet limits across the range?
Preserve configuration | Keep the trial recipe revision with the measurement record.
Request bounded follow-up | Assess the planned range and the identified downstream effects.
Avoid declaring failure | Untested corners are unresolved, not failed.
Close the summary | Report the center-point result and the remaining validation scope.''',
    notes='''Uniformity | State the formula or metric, not only a percentage.
Window | A range meeting requirements, not one successful setting.
Corner | A defined edge or combination in the evaluation plan.
Better | Name the response that improved and what was not assessed.
Integrated | Requires consideration of connected process steps.
Released | An authorization status, not a synonym for promising.''',
    d='''Which summary preserves the evidence boundary? | The nominal-setting metric improved; the range and downstream effects remain untested. | The metric improved at nominal, so the same reduction applies at the low and high settings. | A lower nonuniformity metric establishes improved film stress and conformality too. | The trial establishes the window, with etch and CMP review needed only after release. | The observed improvement concerns one response at one setting. Untested settings, other film properties, integration, and release remain separate questions.
What is the relative reduction from 5% to 3%? | 40% | 2% | 60% | 3% | The decrease of two divided by the original five equals forty percent.
Why review downstream etch and CMP? | A film change may alter later process behavior. | The deposition metric already establishes the etch selectivity. | An unchanged CMP recipe proves the new film polishes identically. | Lower thickness variation removes the need to assess other film properties. | A changed film can interact differently with later processes. A shared recipe or one improved response does not establish selectivity, polishing behavior, or all material properties.
Which status should remain separate from trial success? | Recipe release | The reported nominal-setting value of 3% | The unchanged metric definition | The recorded original value of 5% | Recipe release is an authorized decision that has not occurred in this case.''',
    dialogue='''Yuki | The nominal-setting trial reduced our thickness-nonuniformity metric from five percent to three percent. The summary now says the full process window is validated, which seems too broad.
Sam | It is too broad. A [[process window::A process window is a range satisfying defined requirements, not a single successful nominal setting.]] covers a range of conditions meeting defined requirements. We have one encouraging center-point result, not evidence for the entire proposed range.
Yuki | Both values use the same measurement definition, and lower is better for this metric. I want to report that improvement clearly without losing the limitation.
Sam | Name [[thickness nonuniformity::Thickness nonuniformity is the specific response that improved; it does not stand for all film or integration properties.]] explicitly. Saying the process improved could imply that every relevant response was assessed, while the supplied result addresses only this defined metric.
Yuki | The absolute decrease is two percentage points. Relative to the original five percent, the decrease is forty percent, not merely two percent.
Sam | Keep that arithmetic tied to the [[nominal setting::The nominal setting is the only process condition tested, so the measured improvement must remain limited to it.]]. Neither way of expressing the improvement extends the evidence to settings that have not been run.
Yuki | I will mark the low and high settings untested. What evidence does the approved plan require before we can make a claim about that range?
Sam | Correct. Each planned [[corner condition::A corner condition is a defined limiting setting or combination that requires its own evidence in the evaluation plan.]] needs its own assessment under the approved plan. An untested condition is unresolved, not a favorable result or a demonstrated defect.
Yuki | The deposition change may also affect other film characteristics. A lower thickness-variation metric does not tell us that stress, coverage, or later pattern transfer remained acceptable.
Sam | That is an [[integration trade-off::An integration trade-off concerns benefits and consequences across related steps that a single improved deposition metric cannot settle.]] question. We need to assess the relevant responses and interactions rather than optimize one number in isolation from the product flow.
Yuki | For the subsequent etch, the team has not yet checked how the changed film behaves relative to the neighboring materials. That could affect the interpretation of the trial.
Sam | Review [[etch selectivity::Etch selectivity compares material removal rates and may be affected by a film change; no result is supplied here.]] where it matters to the approved integration assessment. Naming the concern identifies a question to investigate, not a result we can claim already occurred.
Yuki | The planarization team also needs the proposed film information. Their review has not started, so I should not imply that the next surface-finishing step is already covered.
Sam | State that [[CMP::CMP is chemical mechanical planarization, a downstream process whose compatibility with the changed film remains unassessed.]] compatibility remains open. The deposition result does not establish that planarization behavior, surface effects, or related requirements are unchanged.
Yuki | We can identify the relevant responses in the evaluation plan without improvising operating settings during this review. The process owners should define the approved technical work.
Sam | Yes. Capture each [[process interaction::A process interaction is a relationship between factors or steps that can change the overall result and needs explicit assessment.]] question and its owner. That makes the remaining work specific enough to schedule and review without treating the meeting as recipe authorization.
Yuki | Please keep trial revision on the summary. Planning is asking about routine use, and I do not want this result mistaken for a production release.
Sam | Keep [[recipe release::Recipe release is the controlled authorization for defined use, separate from a promising experimental result.]] separate from the experiment. A favorable metric can support the review, but the required scope and approvals still need to be completed.
Yuki | I will revise the summary to report the center-point improvement, the unchanged metric basis, and the untested range. I will list the etch and planarization reviews as pending.
Sam | That presents the [[deposition::Deposition is the film-forming step actually assessed; the statement should not imply the entire integrated flow was validated.]] result accurately. The team can recognize progress while seeing exactly what evidence is still needed before making a broader process claim.''',
    rehearsal=[
        'Check the answers. Read the opening six turns, distinguishing two percentage points from forty percent.',
        'Switch roles. Read the etch and CMP exchanges while keeping both assessments pending.',
        'Complete and check the transfer. Read nominal setting, process window, and release as separate claims.'],
    transfer_title='An improved metric with a limited range',
    transfer_setup='At one nominal setting, an unchanged nonuniformity metric falls from 8% to 6%. Lower is better. Edge settings and downstream etch remain untested; the recipe is not released.',
    transfer='''Engineer: "The metric fell from eight to six percent, but only at the ___." | nominal setting | The nominal setting is the single tested condition, not the full range.
Reviewer: "Keep the low and high settings open; we have not established the ___." | process window | A process window requires evidence across the relevant range, which is missing here.
Engineer: "I will also list the untested effect on the later etch as an ___." | integration question | The film change may affect a later step, so downstream compatibility remains an integration question.
Reviewer: "And keep routine production use pending the authorized ___." | recipe release | A favorable trial result does not itself authorize the recipe for production use.'''))

BOOK['units'].append(unit(
    title='Metrology, SPC, and Yield Learning',
    scene='Two percentage points, not a proven process gain',
    skill='Report yield with counts and comparison limits, and distinguish product acceptance from evidence about process stability.',
    brief='Yield engineer Ravi presents a pilot lot with 92 passing die out of 100 tested, compared with a reference lot with 900 passing die out of 1,000 tested. The product mixes differ, and no controlled comparison or statistical significance assessment has been completed. Manager Elena wants to announce that a process change caused a two-percent yield improvement. The team also has no time-ordered control-chart analysis supporting a stability claim. Ravi must preserve the useful observations while correcting the causal, percentage, and stability language.',
    cast='Elena | Yield program manager\nRavi | Yield engineer',
    culture=('Give the counts before the conclusion', 'A favorable yield difference can start an investigation without ending it. State the passing and tested counts, identify changed product mix, and distinguish an absolute percentage-point difference from a relative percentage change. Avoid using the words significant or stable as casual substitutes for better.'),
    a='''What is the pilot yield? | 92% from 92 of 100 tested die | 90% from 900 of 1,000 die | 2% from two lots | 100% because the pilot completed | Ninety-two passing die divided by one hundred tested gives a 92% observed yield.
What is the absolute difference between the observed yields? | 2 percentage points | 2 passing die | Exactly 2 relative percent | 20 percentage points | The observed yields are 92% and 90%, a difference of two percentage points.
Which factor limits the causal comparison? | The product mixes differ. | Both yields have denominators. | The pilot is called a pilot. | The reference contains more passing die in absolute number. | Different product mixes can affect yield, so the process change is not isolated by this comparison.''',
    vocabulary='''metrology | The science and practice of measurement. | review metrology consistency
electrical yield | The proportion meeting defined electrical test criteria. | report electrical yield
pass count | The number of tested items meeting the stated criteria. | preserve the pass count
tested population | The set of items included in a reported test result. | define the tested population
denominator | The total used as the base of a fraction or percentage. | state the denominator
product mix | The composition of different products in a dataset. | adjust for product mix
pilot lot | A limited production lot used to evaluate a process or product. | evaluate a pilot lot
reference lot | A lot used as a stated comparison basis. | identify the reference lot
percentage point | A unit for the absolute difference between percentages. | report percentage-point change
relative change | A change divided by its specified starting value. | calculate relative change
confounding factor | A factor that prevents clean attribution of an observed relationship. | identify a confounding factor
stratification | Separating data into relevant comparable groups. | stratify by product
SPC | Statistical process control, using data to monitor process behavior. | apply SPC
control chart | A time-ordered chart with a defined process-monitoring method. | review the control chart
control limit | A monitoring boundary derived under a stated process model or method. | distinguish control limits
specification limit | A defined product or process acceptance boundary. | check specification limits
common-cause variation | Variation inherent in the currently defined process system. | characterize common-cause variation
special-cause variation | Variation associated with a nonroutine identifiable influence. | investigate special-cause variation
control signal | A result meeting a defined rule for investigation on a control chart. | respond to a control signal
process stability | Consistent statistical behavior under the defined monitoring basis. | assess process stability
subgroup | A defined set of observations grouped for process analysis. | define rational subgroups
measurement system | The instruments, methods, people, and conditions producing measurements. | assess the measurement system
yield learning | Investigation that improves understanding of yield losses and drivers. | support yield learning
causal attribution | Assigning an observed effect to a particular cause. | qualify causal attribution''',
    precision='The pilot has 92% yield and the reference 90%. The difference is 2 percentage points, or about 2.22% relative to 90%. Different product mixes and sample sizes mean this observation alone does not establish a causal improvement or statistical significance.',
    precision_extra='Control limits describe expected process behavior under a defined monitoring method; specification limits express acceptance requirements. Passing a specification does not establish stability, and a control signal does not automatically identify either the cause or the disposition of every unit.',
    phrases='''Give the pilot counts | The pilot passed 92 of 100 tested die.
Give the reference counts | The reference passed 900 of 1,000 tested die.
Name the absolute change | The observed difference is two percentage points.
Name the relative basis | Relative to 90%, that is approximately 2.22%.
Expose the mix | The two lots have different product mixes.
Avoid causality by timing | The process change is not isolated by this comparison.
Qualify significance | Statistical significance has not been assessed.
Request like-for-like data | Compare relevant product groups on a consistent basis.
Separate limits | Control limits and specification limits serve different purposes.
Ask for time order | Which time-ordered evidence supports the stability claim?
Keep the method visible | State the subgrouping and monitoring rules.
Avoid dismissing a signal | A control signal warrants investigation under the defined procedure.
Avoid invented diagnosis | The signal does not identify its own cause.
Preserve useful progress | The pilot result is encouraging but limited.
Check measurement consistency | Confirm the measurement and test basis before combining data.
Close the finding | Report the counts, observed difference, limitations, and next analysis.''',
    notes='''Improvement | Can describe an observation or an established effect; specify which.
Significant | Distinguish business importance from statistical evidence.
Stable | Needs a defined time-ordered process assessment.
Yield | Attach the test stage, criteria, and denominator.
In spec | An acceptance statement, not proof of statistical control.
Caused | Stronger than followed or coincided with.''',
    d='''Which announcement is supported? | The pilot observed 92% versus 90% yield, with different product mixes and no causal conclusion. | The process change is proven to improve every product by two relative percent. | The pilot proves the process is statistically stable. | Different denominators make both observed percentages meaningless. | The counts support descriptive percentages, but the comparison does not isolate cause or establish stability.
What is the approximate relative increase from 90% to 92%? | 2.22% | 2.00% | 20.00% | 92.00% | The two-point increase divided by the 90% starting value is approximately 2.22%.
Which next analysis addresses the product-mix problem? | Separate comparable product groups and review consistent test bases. | Pool both lots into one aggregate percentage and omit the product breakdown. | Equalize lot sample sizes while retaining their different product compositions. | Compare only the absolute pass counts without the tested populations. | Stratification examines comparable product groups. Equal sample sizes, pooled totals, or pass counts alone do not remove a difference in product composition.
Which statement distinguishes control and specification limits? | Control limits monitor behavior; specification limits define acceptance boundaries. | Control limits are customer acceptance boundaries; specification limits summarize observed variation. | A process within its specification limits necessarily has stable statistical behavior. | A process within its control limits necessarily meets all product requirements. | Statistical stability and conformity are different questions. A stable process may miss specifications, and in-spec observations do not establish statistical control.''',
    dialogue='''Elena | The pilot reached ninety-two percent against ninety percent in the reference lot. Can we announce that the process change caused a two-percent yield improvement?
Ravi | Begin with the [[pass count::The pass count identifies the actual successes behind the percentage, preserving the scale of the evidence.]] and denominator. The pilot passed ninety-two of one hundred tested die; the reference passed nine hundred of one thousand.
Elena | Put both counts beside the percentages. A reader needs to see that one result comes from a hundred die and the other from a thousand.
Ravi | Correct. Also state the [[product mix::Product mix differs between the lots and may affect observed yield independently of the process change.]]. The lots contain different product compositions, so the two percentages are not a controlled comparison of the process change alone.
Elena | The wording about two percent needs correction too. The absolute difference between ninety and ninety-two percent is two percentage points.
Ravi | Yes, use [[percentage point::Percentage point measures the absolute difference between the two yield percentages, here 92 minus 90.]] for that absolute change. Relative to the ninety-percent starting value, the increase is approximately two point two two percent.
Elena | I want the team to see the pilot as useful progress without overstating what caused the result. The change happened before the pilot, but timing is not enough.
Ravi | Avoid unsupported [[causal attribution::Causal attribution assigns the observed yield difference to the process change, which this mixed comparison does not isolate.]]. The result can guide further investigation while the product mix and other relevant differences remain visible.
Elena | Can you break the results down by product and confirm the test basis? I want to see whether the mix is driving the overall difference.
Ravi | Use [[stratification::Stratification separates the data into comparable product groups to examine the mix effect more directly.]] to examine the appropriate groups. It will not automatically prove causality, but it addresses one important weakness in the aggregate comparison.
Elena | The draft also says the pilot demonstrates stable production. We have not presented a time-ordered analysis, only these two lot summaries.
Ravi | Then remove that [[process stability::Process stability concerns statistical behavior over time under a defined monitoring method, not two favorable aggregate yields.]] claim. A favorable summary percentage does not establish how the process behaves over time or whether a monitoring rule has signaled a change.
Elena | We have acceptance criteria for individual test results. Some colleagues are treating those limits as though they were the same as the chart's monitoring boundaries.
Ravi | A [[specification limit::A specification limit defines acceptance requirements and is distinct from a statistically based process-monitoring boundary.]] defines an acceptance boundary. A control limit has a different purpose, so passing the specification is not proof that the process is in statistical control.
Elena | If a monitoring rule signals something unusual, the team needs to investigate. But the signal itself does not identify which tool or material caused it.
Ravi | Exactly. A [[control signal::A control signal triggers investigation under the monitoring method; it does not provide its own causal diagnosis.]] is a prompt for the defined investigation process. Do not convert it directly into a root-cause statement or an automatic disposition for every unit.
Elena | We also need to make sure the measurements and test criteria are consistent before combining records. Otherwise the next comparison could carry a different hidden change.
Ravi | Check the [[measurement system::The measurement system includes methods and conditions that affect whether the collected results can be compared consistently.]] and test basis. Clear denominators are essential, but they do not solve inconsistencies in how observations were produced or classified.
Elena | The revised update will report the counts, the two-point difference, and the changed product mix. It will leave significance, stability, and causality unclaimed pending the appropriate analysis.
Ravi | That supports [[yield learning::Yield learning uses the observations to investigate losses and drivers without claiming an effect before the evidence supports it.]]. The pilot remains informative, and the team gets a precise next question instead of a success claim that the present data cannot establish.''',
    rehearsal=[
        'Check the answers. Read both pass counts and denominators before reading their percentages.',
        'Switch roles. Read turns 5-16, emphasizing percentage points, product mix, and the two types of limits.',
        'Complete and check the transfer. Read the corrected exchange without turning the observed difference into a causal claim.'],
    transfer_title='Percentage points need a denominator',
    transfer_setup='A trial passes 48 of 50 tested die, or 96%. A reference passes 450 of 500, or 90%. Product mixes differ, and no causal analysis is complete.',
    transfer='''Engineer: "Put 48 passing die over the trial's 50-die ___." | denominator | The tested total is the denominator; the 48 passing die form the numerator.
Reviewer: "Then show the changed ___ beside the reference comparison, not in a separate appendix." | product mix | Product mix differs between the trial and reference and may affect the observed yields.
Engineer: "I will report the difference as six ___, not six relative percent." | percentage points | Ninety-six percent minus ninety percent is six percentage points, not six relative percent.
Reviewer: "Good. Leave the claim that the process caused it open until we have supported ___." | causal attribution | Causal attribution needs evidence isolating the process effect, which the supplied comparison lacks.'''))


BOOK['units'].append(unit(
    title='Defect Density and Cleanroom Contamination',
    scene='Twenty-four detections are not a confirmed source',
    skill='Describe inspection findings with location, area, timing, and classification while avoiding premature contamination-source claims.',
    brief='Inspection engineer Hana and contamination-control engineer Oscar review a note saying cleanroom problem. The underlying record contains 24 particle-like detections over 200 square centimeters inspected on wafers from lot P8 after tool C2 between 9 and 10 a.m. The map shows an edge cluster. No comparable pre-process scan exists, defect review is incomplete, and no source is confirmed. The lot is held under the local procedure. The team must distinguish detections, confirmed defects, added defects, and airborne particle measurements.',
    cast='Hana | Inspection engineer\nOscar | Contamination-control engineer',
    culture=('Describe the pattern before naming the source', 'A location pattern can focus an investigation without proving where contamination originated. State the observation and its limits, then request traceable process and inspection records. Avoid turning a vague cleanroom label into blame for a team, operator, or tool before the evidence supports it.'),
    a='''What does the inspection record contain? | 24 particle-like detections over 200 square centimeters | 24 confirmed electrical failures on every wafer | An airborne count per cubic meter | A measured increase of 24 defects from a matched pre-scan | The record describes surface inspection detections and inspected area, not confirmed failure or added-defect counts.
What does the map show? | An edge cluster | Uniform distribution across every layer | A confirmed cleanroom air source | A completed source elimination study | The supplied observation is a spatial edge cluster, without an established source.
Why cannot the 24 detections be called 24 added defects? | No comparable pre-process scan exists, and review is incomplete. | The inspected area is known. | The lot has an identifier. | Surface maps always measure airborne particles. | Added defects require a valid before-and-after basis, and the detections are not all confirmed defects.''',
    vocabulary='''inspection detection | A feature flagged by an inspection method for assessment. | review inspection detections
defect review | Examination used to classify and interpret detected features. | complete defect review
defect density | Defects per unit area on a stated counting and inspection basis. | report defect density
inspected area | The surface area included in an inspection result. | state the inspected area
particle-like signature | An observed appearance consistent with a particle, pending review. | classify a particle-like signature
nuisance detection | A flagged feature not relevant to the defect concern being assessed. | filter nuisance detections
killer defect | A defect that causes functional failure in its particular context. | assess killer-defect relevance
defect classification | Assignment of detected features to defined categories. | refine defect classification
wafer map | A spatial representation of results on a wafer. | examine the wafer map
edge cluster | A concentration of observations near a wafer's edge. | investigate an edge cluster
spatial signature | A location pattern in measured or inspected results. | compare spatial signatures
added defect | A defect introduced between comparable inspection points. | quantify added defects
pre-process scan | Inspection performed before a specified process step. | preserve the pre-process scan
post-process scan | Inspection performed after a specified process step. | compare post-process scans
airborne particle count | A count of particles in a defined air sample or volume. | review airborne particle counts
surface contamination | Unwanted material present on a surface. | investigate surface contamination
cross-contamination | Transfer of unwanted material between areas, items, or processes. | prevent cross-contamination
contamination source | The origin of unwanted material. | identify the contamination source
particle excursion | An unusual particle-related result under defined monitoring rules. | investigate a particle excursion
inspection sensitivity | The ability of an inspection method to detect specified features. | confirm inspection sensitivity
size threshold | The size boundary used for counting or classifying features. | state the size threshold
exposure history | The record of relevant environments and handling encountered. | reconstruct exposure history
suspect interval | A defined period being examined for possible affected material. | bound the suspect interval
containment scope | The material or operations covered by a temporary restriction. | define containment scope''',
    precision='The observed detection density is 24 divided by 200, or 0.12 detections per square centimeter. Do not call it a confirmed killer-defect density. Classification is incomplete, and no comparable pre-scan establishes how many detections were introduced by C2.',
    precision_extra='A surface result per square centimeter is not an airborne count per cubic meter. Measurement type, inspected area or air volume, size threshold, and sensitivity belong with the number. Similar timing or spatial patterns guide investigation but do not prove a source.',
    phrases='''Replace the vague label | The record shows particle-like surface detections, not a confirmed cleanroom source.
Give the count and area | There were 24 detections over 200 square centimeters inspected.
Name the density basis | That is 0.12 detections per square centimeter.
Locate the pattern | The wafer map shows an edge cluster.
Bound the interval | These records follow C2 between 9 and 10 a.m.
Preserve the uncertainty | Defect classification remains incomplete.
Avoid an added-defect claim | We lack a comparable pre-process scan.
Separate measurement types | Surface detections are not airborne particle counts.
Ask about sensitivity | Were the inspection settings and size threshold consistent?
Avoid premature blame | The spatial signature does not confirm the source.
Trace the material | Link the map to the lot, wafers, and process history.
Keep the restriction clear | P8 remains held under the local procedure.
Define the next review | Review the detections and relevant exposure history.
Avoid automatic yield claims | Not every flagged feature is a confirmed killer defect.
Ask about scope | Which material is included in the current containment?
Close the note | Report observations, limits, containment status, and investigation ownership.''',
    notes='''Particle-like | An appearance classification, not necessarily a confirmed material identity.
Added | Needs comparable before-and-after evidence.
Density | Requires a count definition and area or volume denominator.
Source | A causal conclusion, not merely the last tool visited.
Cluster | A spatial pattern that can guide but not finish an investigation.
Cleanroom problem | Too broad to locate the evidence or assign a justified cause.''',
    d='''What is the observed detection density? | 0.12 detections per square centimeter | 12 detections per square centimeter | 8.33 detections per square centimeter | 0.12 particles per cubic meter of air | Twenty-four detections divided by two hundred square centimeters equals 0.12 on a surface-area basis.
Which conclusion is unsupported? | C2 introduced all 24 detections. | The records are after C2. | The map shows an edge cluster. | Defect review is incomplete. | Timing after C2 does not establish introduction by C2 without the needed comparison and investigation.
Which next record is useful for the investigation? | Traceable wafer, inspection-setting, timing, and exposure information | A count from another layer using a different threshold, treated as a matched pre-scan | A whole-fab monthly total used to assign the source for this lot | A surface map converted to an airborne count without an air sample | The traceable records preserve the actual material and measurement context. Unmatched layers, aggregate totals, and unsupported conversions cannot replace that evidence.
Which distinction is correct? | Surface detection density and airborne particle counts use different measurement bases. | A post-process detection count equals an added-defect count without a pre-scan. | An inspection's flagged-feature count is already the confirmed killer-defect count. | An edge pattern identifies the contamination source without further review. | Surface and air results have different bases. Detection is not confirmed classification, timing is not proof of introduction, and a pattern alone does not identify a source.''',
    dialogue='''Hana | The review note says cleanroom problem, but that label is much broader than the evidence. We have twenty-four particle-like detections on the inspected surfaces from P8.
Oscar | Start with the [[inspected area::The inspected area provides the denominator for the surface detection density rather than leaving the count without scale.]]. The record covers two hundred square centimeters, so the number can be interpreted on a defined surface basis rather than as an unexplained total.
Hana | That gives zero point one two detections per square centimeter. I should keep the word detections because the detailed classification has not been completed.
Oscar | Correct. [[Defect review::Defect review determines how flagged features should be classified before they are treated as confirmed relevant defects.]] is still open. A flagged feature is not automatically a confirmed defect of the relevant type, much less a demonstrated electrical failure.
Hana | The map clusters near the edge. I will send the wafer IDs and coordinates so the team can examine the pattern without guessing its source.
Oscar | Call it an [[edge cluster::An edge cluster describes the spatial concentration actually observed without claiming its origin has been established.]]. Describe where it appears and connect the map to the wafer IDs, rather than turn the pattern into an immediate diagnosis of the cleanroom.
Hana | The records follow C2 between nine and ten a.m. Someone has rewritten that as C2 added twenty-four particles, although we do not have a comparable earlier scan.
Oscar | We cannot claim an [[added defect::An added defect requires evidence that it appeared between comparable inspection points, which is missing here.]] count on that basis. After C2 establishes the recorded sequence, not proof that C2 introduced every detected feature.
Hana | A matched earlier inspection would help distinguish what was already present from what appeared later. We would also need to check the inspection basis before comparing counts.
Oscar | Exactly. A [[pre-process scan::A pre-process scan provides the earlier observation needed for a valid before-and-after comparison when methods are comparable.]] must be comparable with the later scan. Different sensitivity, locations, or thresholds could otherwise make a count difference look like process-added contamination.
Hana | Facilities sent an air-monitoring result too. I will keep it separate from these surface counts; the units and measurement methods are different.
Oscar | An [[airborne particle count::An airborne particle count concerns a defined air sample or volume, unlike the surface-area-based detections here.]] is a different measurement. A value per air volume cannot be treated as the same quantity as detections per inspected surface area.
Hana | I will include the inspection recipe and threshold with the maps. That will let reviewers see whether the method was capable of detecting the features being discussed.
Oscar | Keep [[inspection sensitivity::Inspection sensitivity affects which features are detected and must be considered when comparing inspection results.]] visible. A tool finding more features after a settings change does not by itself prove that the process produced more contamination.
Hana | P8 remains on hold under the local procedure. The investigation team needs to say which material and time interval are included, rather than leave the restriction implicit.
Oscar | Define the [[containment scope::Containment scope identifies which material or operations are restricted while the investigation remains open.]] through the authorized process. A precise scope supports coordination without turning this discussion into permission to release or extend the hold arbitrarily.
Hana | We can reconstruct the lot's recent handling and process history alongside the spatial pattern. That should help distinguish possible explanations and identify useful follow-up evidence.
Oscar | Review the [[exposure history::Exposure history connects the wafers to relevant handling and environments that may help evaluate possible contamination origins.]]. It can guide source investigation, but a shared tool or time interval is not enough on its own to establish the origin.
Hana | The corrected note will give the count, area, edge pattern, interval, and incomplete classification. It will state that introduction by C2 and an airborne source are unconfirmed.
Oscar | That keeps the [[contamination source::The contamination source is the origin to be established by investigation, not assumed from the latest process step or vague label.]] question open on an accurate basis. We can investigate efficiently while preserving the distinction between an observation, a hypothesis, and a confirmed cause.''',
    rehearsal=[
        'Check the answers. Read 24 detections over 200 square centimeters and the resulting density aloud.',
        'Switch roles for turns 5-14. Keep the edge pattern, possible source, and surface-versus-air distinction explicit.',
        'Complete and check the transfer. Read the evidence requests without naming an unconfirmed contamination source.'],
    transfer_title='Count the detections, not an invented cause',
    transfer_setup='A post-process scan flags 12 features over 100 square centimeters. Classification is pending, and no comparable pre-process scan exists. No contamination source is confirmed.',
    transfer='''Engineer: "Keep 100 square centimeters beside the count as the ___." | inspected area | Inspected area supplies the surface basis for the 12 detections, giving a density of 0.12.
Reviewer: "And leave the twelve flagged features unclassified pending ___." | defect review | Defect review determines how inspection detections should be classified; it remains incomplete.
Engineer: "I will request a comparable ___ before reporting any process-added count." | pre-process scan | A comparable pre-process scan is needed to assess what was introduced between inspection points.
Reviewer: "Thank you. Do not name the last tool as the ___ without supporting investigation." | contamination source | The source is an origin to investigate, not a conclusion established by the post-process count.'''))

BOOK['units'].append(unit(
    title='Equipment Uptime, Recipes, and Tool Matching',
    scene='Same recipe, different means',
    skill='Distinguish recipe identity, specification performance, tool matching, and equipment availability in a transfer discussion.',
    brief='Equipment engineer Victor and process engineer Asha compare tools A and B using the same identified R7 recipe and an agreed comparable measurement basis. Their film-thickness sample means are 98 nm and 102 nm. The local mean specification is 95 to 105 nm, but the tool-matching criterion requires the means to differ by no more than 2 nm. Tool B was available for 900 of a defined 1,000-minute window. A colleague uses the identical recipe and 90% availability to claim B is an approved interchangeable backup. No transfer approval is recorded.',
    cast='Victor | Equipment engineer\nAsha | Process engineer',
    culture=('Name which readiness question you answered', 'Available, in specification, matched, and released describe different conditions. A tool may satisfy one and not another. Give each claim its own evidence and criterion so production planning does not convert equipment uptime into process-transfer approval.'),
    a='''How far apart are the sample means? | 4 nm | 2 nm | 7 nm | 200 nm | The difference between 102 nm and 98 nm is four nanometers.
Do the means meet the stated matching criterion? | No; 4 nm exceeds the allowed 2 nm difference. | Yes; both means are within the mean specification. | Yes; both tools use R7. | The availability percentage automatically settles matching. | The matching criterion applies to the difference between means, not merely each mean's specification status.
What does 90% describe here? | Availability for 900 of the defined 1,000 minutes | The proportion of wafers passing final test | A 90% probability that the tools are interchangeable | A recorded production transfer approval | The supplied time ratio concerns equipment availability and establishes no product-yield or approval claim.''',
    vocabulary='''tool matching | Demonstrating comparable tool performance against defined criteria. | assess tool matching
chamber matching | Demonstrating comparable performance between process chambers. | verify chamber matching
recipe revision | The identified version of a process recipe. | confirm the recipe revision
setpoint | A commanded target value for a controlled variable. | record the setpoint
actual value | The measured or achieved value rather than the commanded target. | compare setpoint and actual value
equipment state | The recorded operational condition of a tool. | report equipment state
availability | The share of a defined time basis during which equipment is available. | calculate equipment availability
utilization | The share of a stated time basis during which equipment is used. | state the utilization denominator
scheduled downtime | Planned time when equipment is unavailable for the defined use. | plan scheduled downtime
unscheduled downtime | Unplanned time when equipment is unavailable. | investigate unscheduled downtime
preventive maintenance | Planned work intended to reduce equipment failures or deterioration. | schedule preventive maintenance
corrective maintenance | Work to restore equipment after a fault or failure. | complete corrective maintenance
MTBF | Mean time between failures under a stated operating and event definition. | report MTBF
MTTR | Mean time to repair or restore under the stated local definition. | define the MTTR basis
chamber condition | The physical and operating state of a process chamber. | assess chamber condition
seasoning | Controlled processing used to establish a required chamber condition. | verify seasoning status
calibration status | The current documented state of required measurement calibration. | check calibration status
qualification wafer | A wafer used to assess a specified tool or process condition. | evaluate a qualification wafer
monitor wafer | A wafer used to track selected process or tool behavior. | review monitor-wafer results
matching criterion | A defined limit for acceptable performance difference. | apply the matching criterion
process transfer | Moving a defined process to another tool or location. | approve process transfer
backup tool | An alternative tool intended for use under defined conditions. | qualify a backup tool
release status | Whether the required authorization for a specified use is in place. | confirm release status
offset correction | A controlled adjustment addressing a measured systematic difference. | assess offset correction''',
    precision='Both sample means meet the local 95-to-105 nm mean specification. Their difference is 4 nm, so they fail the separate 2 nm matching criterion. This does not establish the status of every individual wafer, whose measurements are not supplied.',
    precision_extra='Availability is 900 divided by 1,000, or 90%, on this stated basis. It does not measure process matching, output yield, or production-use approval. Availability and utilization definitions vary, so keep the time denominator explicit.',
    phrases='''Confirm the recipe | Both tools used the identified R7 revision.
Separate inputs from outputs | Identical setpoints do not prove identical performance.
State the means | A measured 98 nm and B measured 102 nm.
Give the difference | The means are 4 nm apart.
Apply the right criterion | Matching allows no more than a 2 nm difference.
Separate the specifications | Both means are in spec, but the pair is not matched.
Bound the evidence | These are sample means, not every individual wafer result.
Ask about chamber state | Were the relevant chamber conditions documented?
Check measurement status | Confirm the calibration and measurement basis.
State availability | B was available for 900 of the defined 1,000 minutes.
Keep the percentage limited | That 90% figure is availability, not yield.
Avoid automatic substitution | Backup status needs the required qualification and approval.
Route the investigation | Review the observed offset before proposing a correction.
Preserve authorization | Do not change the recipe from this comparison alone.
Clarify the transfer | Which process, product, and tool combination is proposed?
Close the status | Report specification, matching, availability, and release separately.''',
    notes='''Same | Identify whether recipe, settings, product, or measured outcome is the same.
Available | Describes a time or operational state, not qualification.
In spec | Specify the metric; a passing mean does not prove every unit passed.
Matched | Requires an actual matching criterion and supporting evidence.
Backup | A planning role that does not automatically authorize production use.
Offset | A measured difference to investigate, not an instruction to adjust settings.''',
    d='''Which status report is accurate? | Both means meet the mean specification; their 4 nm difference fails the 2 nm matching limit. | Both tools are matched because 98 and 102 lie within 95 to 105. | Tool B is approved because its availability is 90%. | Every wafer from both tools is proven in specification. | The specification and matching tests use different criteria, and individual results are not supplied.
What does using the same recipe establish? | The identified recipe input is shared, not that output performance is interchangeable. | The two tools have equivalent physical chamber conditions throughout the run. | The same nominal setpoints remove the need to compare actual results. | A matching recipe revision substitutes for product-specific transfer approval. | Shared commanded inputs do not establish identical physical conditions, equivalent output, or authorization to transfer the process.
Which calculation matches the availability basis? | 900 divided by 1,000 equals 90%. | 900 divided by the 100 unavailable minutes equals the availability fraction. | 100 unavailable minutes divided by 1,000 gives 10% availability. | The available-time count alone establishes utilization without a used-time count. | Availability is available time over the defined window. Ten percent is the unavailable fraction, and utilization needs its own use-time data and basis.
What remains necessary before calling B an approved interchangeable backup? | The required matching or qualification evidence and transfer approval | Only a repeated statement that R7 is installed | Only a higher availability percentage | Only a passing sample mean against the broad mean specification | The case lacks matching acceptance and transfer approval, neither of which is replaced by uptime.''',
    dialogue='''Victor | Tool B has the same R7 recipe as A and was available for ninety percent of the window. The planning note calls it an interchangeable backup.
Asha | That combines different questions. [[Tool matching::Tool matching requires measured performance against a defined comparison criterion, not simply a shared recipe or uptime figure.]] depends on the measured outcomes and our criterion, not only the recipe name or the amount of time the tool was available.
Victor | We confirmed the same recipe revision and an agreed measurement basis. A's sample mean was ninety-eight nanometers, while B's was one hundred two.
Asha | The [[matching criterion::The matching criterion allows no more than two nanometers between means; the observed difference is four.]] allows a difference of no more than two nanometers. These means differ by four, so this comparison does not establish an acceptable match.
Victor | Both means are within the local mean specification of ninety-five to one hundred five. That explains why someone thought the comparison had passed.
Asha | The [[actual value::Actual value concerns the measured outcome; passing the mean specification does not remove the separate difference between tools.]] has to be assessed against the correct question. Each mean passes that specification, but the pair fails the separate matching limit.
Victor | I will say both sample means meet that limit. We have not reviewed every individual measurement, so I cannot extend that claim to every wafer.
Asha | Agreed. Confirm the [[recipe revision::The recipe revision identifies the shared controlled input, but cannot stand in for unsupplied individual wafer evidence.]] and report the evidence at its actual level. Do not let a summary mean or a shared input become a claim about every processed unit.
Victor | The observed difference needs investigation. Chamber history and maintenance condition may be relevant, but neither has been established as the cause from these numbers.
Asha | Review [[chamber condition::Chamber condition is a possible contributor to tool behavior that must be assessed rather than assumed from the recipe.]] and the other appropriate records. Identical commanded settings do not guarantee identical physical conditions or measurement behavior.
Victor | I will bring the calibration and monitor records. Can we review those before anyone suggests changing R7 to remove the offset?
Asha | Check [[calibration status::Calibration status concerns the documented measurement basis and is relevant to interpreting the observed tool difference.]] through the approved process. We should not prescribe a recipe adjustment before the team understands the relevant evidence and authorization requirements.
Victor | For the uptime figure, B was available for nine hundred minutes out of a defined one-thousand-minute window. That calculation gives ninety percent.
Asha | Label it [[availability::Availability is the available-time fraction on the stated basis, not a measure of matching, yield, or approval.]] and retain the denominator. It does not mean ninety percent yield or ninety percent confidence that the tool can substitute for A.
Victor | We also have no usage-time figure here, so we should not relabel availability as utilization. The two measures can use different time bases and answer different questions.
Asha | Correct. The [[equipment state::Equipment state records the tool's operational condition; an available state does not establish qualified process performance.]] record helps explain the time measure, but an available tool is not automatically qualified for this product and process combination.
Victor | The backup proposal remains useful because capacity is constrained, but it needs the appropriate technical assessment and approval before production relies on it.
Asha | Treat it as a [[process transfer::Process transfer moves a defined process to another tool and requires its own relevant assessment and approval.]] decision. The defined scope, matching evidence, and required authorization must be clear instead of being inferred from the existence of an alternative tool.
Victor | I will revise the planning note to separate the passing means, failed matching comparison, ninety-percent availability, and missing approval. It will no longer call B interchangeable.
Asha | That preserves the [[release status::Release status records authorization for the intended use, which remains absent despite the tool's availability and passing means.]] accurately. We can pursue the backup option while making its unresolved requirements visible to the people planning production.''',
    rehearsal=[
        'Check the answers. Read the 98 nm and 102 nm means, then the separate specification and matching limits.',
        'Switch roles. Read the availability exchange without replacing availability with yield or utilization.',
        'Complete and check the transfer. Read each claim with its own criterion and keep approval pending.'],
    transfer_title='Two different limits',
    transfer_setup='Two tools have sample means of 50 and 53 nm. Both meet a mean specification of 48 to 55 nm. Matching allows at most 1 nm difference. Transfer approval is pending.',
    transfer='''Engineer: "Both means meet the 48-to-55 nm ___." | specification | The specification applies to each sample mean, and both 50 and 53 fall within it.
Reviewer: "But their three-nanometer gap misses our one-nanometer ___." | matching criterion | The matching criterion applies to the three-nanometer difference, which exceeds the permitted one.
Engineer: "Then moving this process to the other tool remains a proposed ___." | process transfer | Process transfer is the move between tools and requires its own assessment and authorization.
Reviewer: "Correct. Keep approval pending in the ___ field." | release status | Release status concerns authorization; passing individual means does not establish that approval.'''))


BOOK['units'].append(unit(
    title='Packaging, Test, and Reliability Qualification',
    scene='One completed test is not complete qualification',
    skill='Explain qualification status test by test, preserve configuration scope, and correct an overbroad customer claim.',
    brief='Product engineer Diego and reliability engineer Mei review package Q7. Its approved fictional qualification plan requires temperature cycling, high-temperature operating life testing, a highly accelerated stress test, and final review of the evidence. Temperature cycling has passed under its protocol. Operating-life testing is running, and the accelerated stress test has not started. No final approval or accepted substitution is recorded. A customer slide nevertheless says qualification complete. The team must replace that headline with a precise status without describing open tests as failures.',
    cast='Diego | Product engineer\nMei | Reliability engineer',
    culture=('Give progress without collapsing the plan', 'A customer may prefer a short headline, but complete must refer to the required plan and configuration. Name the finished test, the open work, and the pending decision. Do not imply that a test still running has passed, or that a test not yet started has failed.'),
    a='''Which test has passed? | Temperature cycling | High-temperature operating life | The highly accelerated stress test | Every required test and final review | The briefing identifies temperature cycling as the only completed passing test.
What is the operating-life test status? | Running | Passed and approved | Not required by the plan | Replaced by an accepted substitution | The supplied plan still includes the test, and its stated status is running.
Why is qualification complete unsupported? | Two required tests and final review remain open. | Every package test is optional. | A running test is automatically a failure. | The package identifier proves approval. | The defined plan requires evidence and final review that have not all been completed.''',
    vocabulary='''package substrate | The package structure carrying connections between die and external interfaces. | specify the package substrate
wire bonding | Forming electrical connections using fine wires. | qualify wire bonding
flip-chip attachment | Connecting a die face-down through conductive bumps or pillars. | evaluate flip-chip attachment
underfill | Material placed around interconnections to support a package assembly. | assess underfill integrity
mold compound | Encapsulating material used in many semiconductor packages. | qualify the mold compound
solder joint | A soldered electrical and mechanical connection. | inspect solder joints
BGA | Ball grid array, a package connection format using an array of solder balls. | assess BGA assembly
QFN | Quad flat no-lead, a package format with exposed connection lands. | review the QFN package
SiP | System in package, integrating multiple functions or components in one package. | evaluate a SiP design
TSV | Through-silicon via, a conductive connection passing through silicon. | characterize TSV connections
package construction | The materials and structural arrangement of a package. | identify package construction
moisture sensitivity | Susceptibility to moisture-related effects under stated handling or stress conditions. | assess moisture sensitivity
delamination | Separation between bonded material layers. | inspect for delamination
thermal cycling | Repeated temperature changes under a specified test profile. | complete thermal cycling
HTOL | High-temperature operating life, an operating stress test under defined conditions. | report HTOL status
HAST | Highly accelerated stress test, a defined accelerated humidity-related stress test. | schedule HAST
preconditioning | Defined preparation before a test to represent relevant handling or assembly stresses. | document preconditioning
qualification plan | The defined tests, evidence, scope, and approval requirements for qualification. | follow the qualification plan
qualification vehicle | The selected device or structure used to support qualification evidence. | identify the qualification vehicle
test coverage | The requirements or failure concerns addressed by the performed tests. | assess qualification test coverage
failure analysis | Investigation of failed samples and their causes. | initiate failure analysis
qualification by similarity | Use of justified related evidence under an accepted qualification approach. | assess qualification by similarity
final test | Electrical testing at the defined final product stage. | complete final test
qualification approval | Authorized acceptance of the required qualification evidence. | obtain qualification approval''',
    precision='This case uses a specific fictional plan, not a universal mandatory three-test list. One passing test supports its defined result. It does not complete the two open tests or the final review, and it does not establish every application-specific reliability claim.',
    precision_extra='Related package evidence may sometimes support qualification through an accepted similarity rationale. No such substitution is accepted here. Similar appearance, a shared package name, or a convenient schedule cannot silently change the approved evidence requirements.',
    phrases='''Name the completed result | Q7 passed temperature cycling under the stated protocol.
State ongoing work | HTOL is still running.
State unstarted work | HAST has not started.
Keep the plan visible | The approved plan requires all three tests and final review.
Correct the headline | Qualification is in progress, not complete.
Avoid treating pending as failed | No result is available for the unstarted test.
Preserve configuration | Which package construction does the evidence cover?
Ask about the vehicle | Is this the approved qualification vehicle?
Check preparation | Are the required preconditioning records included?
Separate production test | Final test is not a substitute for every reliability stress.
Qualify related evidence | Similarity needs an accepted technical rationale.
Avoid a schedule shortcut | A desired customer date does not remove a required test.
State the approval gap | Final qualification approval is not recorded.
Describe coverage | Identify what each completed test actually addresses.
Commit to the next update | The next report will distinguish completed, running, and unstarted tests.
Close accurately | Keep release decisions with the authorized review process.''',
    notes='''Qualified | Specify product, package, construction, scope, and approval.
Passed | Applies to a defined test result, not automatically the entire plan.
Running | A current activity status, not a completed result.
Not started | Does not mean failed or waived.
Similar | Needs a justified and accepted relevance argument.
Complete | Includes the required evidence review, not only laboratory scheduling.''',
    d='''Which customer headline is supported? | Qualification in progress: temperature cycling passed; HTOL running; HAST not started. | Q7 is fully qualified because temperature cycling passed. | Q7 failed HAST because HAST has not started. | Q7 is approved by similarity despite no accepted substitution. | The headline accurately separates each test's status without inventing a result or approval.
What does the passing temperature-cycle result establish? | The stated test result under its protocol and scope | Completion of the operating-life test because both involve temperature | Completion of HAST because both are accelerated stress tests | Qualification of every package variant sharing the Q7 marketing name | Temperature cycling, operating-life testing, and humidity-related stress address different test conditions. A shared name also does not establish equivalent package construction or scope.
When could related evidence replace a required test in this case? | Only through the applicable accepted change or similarity process, which has not occurred | When the related package has the same outside dimensions, without a construction review | When the older report is newer than the current plan, without an applicability assessment | When final electrical test passes, without assessing the reliability evidence gap | Related evidence requires an accepted relevance and authorization basis. Dimensions, document age, and a different passing test do not by themselves justify substitution.
What should final review examine? | Required evidence, scope, configuration, open items, and approval conditions | Only whether the slide uses the word complete | Only the date the first test started | A presumed pass for all tests without final results | Qualification approval depends on the required evidence and scope, not a favorable summary label.''',
    dialogue='''Diego | The customer slide says Q7 qualification is complete because temperature cycling passed. We still have two other tests in the plan, so I need a more accurate headline.
Mei | Start from the [[qualification plan::The qualification plan defines all required tests and final review, so one passing test cannot complete it.]]. Our approved plan requires all three tests and final evidence review. We have completed one part, not the entire qualification decision.
Diego | The completed test followed its protocol and passed. I want to preserve that positive result rather than make the update sound as though nothing has been achieved.
Mei | Report the [[thermal cycling::Thermal cycling is the completed temperature-change stress test; its passing result remains valid within its defined protocol.]] result clearly. Its value is not diminished by stating the other work accurately, and it should not be expanded beyond its protocol and scope.
Diego | The operating-life test is still running. The lab has not supplied its final result, so the customer should not read the current status as a pass.
Mei | Label [[HTOL::HTOL is high-temperature operating life testing, which is currently running rather than completed in this case.]] as running. If a progress checkpoint is available, identify it as interim information without treating it as the completed test outcome.
Diego | The accelerated humidity-related stress test has not started. That is a schedule and evidence gap, but it is not a failed result.
Mei | Exactly. [[HAST::HAST is the highly accelerated stress test that has not started; absence of a result is not a pass or failure.]] remains unstarted in this plan. Use that status rather than either a reassuring green result or an unsupported failure label.
Diego | Which package construction should I name on the slide? Q7 alone may cover variants with different materials or assembly details.
Mei | Keep the [[package construction::Package construction identifies the materials and structure covered by the evidence, preventing unsupported extension to other variants.]] linked to the evidence. Qualification scope should not silently expand to a different variant simply because the marketing name is similar.
Diego | We should confirm the tested device or structure as well. Otherwise reviewers may not know how the selected samples relate to the configuration being discussed.
Mei | Identify the [[qualification vehicle::The qualification vehicle is the selected device or structure whose results support the defined qualification scope.]] and its approved rationale. Traceability makes it possible to review applicability rather than assume that any available sample represents every product.
Diego | The assembly preparation records also belong in the package. I do not want the final review to discover that important preparation details were omitted from the summary.
Mei | Include the required [[preconditioning::Preconditioning records show the defined preparation used before testing and form part of interpreting the evidence.]] records where the plan calls for them. A passing result needs the relevant preparation and test context to be interpreted correctly.
Diego | Sales wants to reuse results from an older package. I will refer that request for review; we have no accepted substitution for the open tests.
Mei | [[Qualification by similarity::Qualification by similarity requires an accepted technical rationale; no such substitution is established in this case.]] needs an accepted basis under the applicable process. A related package or a desired delivery date does not automatically change the approved requirements.
Diego | We also have final electrical test records, but those should not be presented as though they address every stress-related concern in the qualification plan.
Mei | Correct. [[Test coverage::Test coverage identifies which requirements or concerns the available tests address; final electrical testing does not replace every reliability stress.]] differs between production checks and reliability assessments. Each result needs to be connected to what it actually evaluates, not treated as interchangeable evidence.
Diego | I will change the headline to qualification in progress, list the three statuses, and keep the configuration and outstanding review visible. We will not announce release from this slide.
Mei | That preserves [[qualification approval::Qualification approval is the authorized acceptance of the required evidence, which remains pending while tests and review are incomplete.]] as a separate decision. The next update can show genuine progress while keeping the unresolved tests and final review clear.''',
    rehearsal=[
        'Check the answers. Read the three test statuses, expanding HTOL and HAST using the vocabulary pages.',
        'Switch roles for turns 9-20. Keep construction, preparation, related evidence, and final approval distinct.',
        'Complete and check the transfer. Read the pending work without changing it into either a pass or a failure.'],
    transfer_title='Pending is neither passed nor failed',
    transfer_setup='A fictional package plan requires tests A, B, and C plus final review. A passed, B is running, and C has not started. No substitution or final approval is recorded.',
    transfer='''Engineer: "Keep A's passing result as test ___, not a claim that every requirement is complete." | evidence | The passing result is evidence for its defined test, not completion of the whole plan.
Reviewer: "B and C are still required by the approved ___." | plan | The approved qualification plan still requires these tests; neither has an accepted replacement.
Engineer: "We would need an accepted technical ___ before substituting related results." | rationale | A justified and accepted rationale is necessary for a relevant substitution; none exists here.
Reviewer: "Until the tests and final review are complete, do not announce qualification ___." | approval | Qualification approval remains pending while required tests and final review are incomplete.'''))

BOOK['units'].append(unit(
    title='Foundry, Tape-Out, PDK, and Capacity Communication',
    scene='A possible slot is not tape-out readiness',
    skill='Negotiate a requested date by separating design sign-off, data delivery, foundry acceptance, and capacity confirmation.',
    brief='Customer design lead Sofia asks foundry liaison Ken to move a planned October 15 tape-out to October 8. Four design-rule-check findings and one layout-versus-schematic mismatch remain unresolved in the agreed fictional PDK revision P3. The foundry has mentioned a possible earlier slot but has not reserved or accepted it. No complete sign-off package is available, and no waiver is approved. Ken must communicate the blockers and conditional next steps without promising a wafer start, finished samples, or shipment.',
    cast='Sofia | Customer design lead\nKen | Foundry liaison',
    culture=('Separate the milestones under date pressure', 'Tape-out, foundry data acceptance, wafer start, and finished samples are related but distinct milestones. State which date is requested and which prerequisites remain open. A possible capacity opportunity should trigger a feasibility discussion, not erase design checks or become a shipment promise.'),
    a='''Which earlier date is requested? | October 8 tape-out | October 8 finished samples | October 15 shipment | October 15 completed wafer sort | Sofia asks to move tape-out from October 15 to October 8, not to deliver finished devices then.
What remains unresolved in the design checks? | Four DRC findings and one LVS mismatch | A completed sign-off package with no open items | Only a customer shipping address | An approved waiver for all findings | The briefing explicitly lists four design-rule findings and one layout-versus-schematic mismatch.
What is the capacity status? | A possible earlier slot, not reserved or accepted | A confirmed wafer start | A guaranteed sample delivery | An approved bypass of design sign-off | A mentioned opportunity is not a recorded capacity commitment or approval.''',
    vocabulary='''foundry | A manufacturer producing semiconductor devices for other companies. | coordinate with the foundry
fabless company | A chip-design company that contracts out fabrication. | support a fabless customer
IDM | Integrated device manufacturer, combining chip design and manufacturing. | work with an IDM
PDK | Process design kit: process-specific models, rules, and design resources. | confirm the PDK revision
design rule | A process-specific constraint governing layout features or relationships. | check design rules
DRC | Design rule checking, testing layout against applicable rule definitions. | resolve DRC findings
LVS | Layout versus schematic checking, comparing extracted layout connectivity with the schematic. | close an LVS mismatch
rule deck | The implemented rules used by a physical-verification tool. | identify the rule deck
sign-off | The required formal completion and approval of defined checks. | complete design sign-off
tape-out | Release of the approved design dataset for the intended fabrication handoff. | plan the tape-out
GDSII | A widely used layout-data format for integrated circuit design. | deliver a GDSII dataset
OASIS | A compact integrated-circuit layout interchange format. | verify the OASIS file
mask data preparation | Processing layout data for mask manufacture. | schedule mask data preparation
mask set | The collection of masks needed for a defined fabrication flow. | release the mask set
engineering change order | A controlled record authorizing a defined engineering change, abbreviated ECO. | approve an engineering change order
waiver | An authorized exception to a specific requirement under an applicable process. | request a defined waiver
data acceptance | Confirmation that a delivered dataset meets the receiving process's requirements. | obtain foundry data acceptance
capacity reservation | A confirmed allocation of manufacturing capacity. | confirm capacity reservation
wafer start | Entry of a wafer lot into the defined fabrication flow. | confirm the wafer start
cycle time | Elapsed time through a defined manufacturing flow or stage. | state fabrication cycle time
engineering lot | A lot used for development or engineering evaluation. | plan an engineering lot
risk production | Production begun before all defined qualification or maturity conditions are complete. | assess risk-production approval
respin | A revised design iteration requiring another fabrication cycle. | evaluate the need for a respin
delivery commitment | An agreed promise about a specified deliverable and date. | qualify the delivery commitment''',
    precision='October 8 is a requested tape-out date, not an accepted slot or a finished-sample date. The open DRC and LVS items remain blockers to the stated sign-off package. The case does not provide an approved waiver or permission to bypass checks.',
    precision_extra='PDK and rule-deck versions affect what physical verification means. Keep results connected to the agreed revision. A clean check run also has a defined scope; it does not guarantee first-silicon performance, complete qualification, or a confirmed manufacturing schedule.',
    phrases='''Name the requested milestone | You are requesting October 8 tape-out.
Separate later dates | That is not a wafer-start or sample-delivery commitment.
State the open checks | Four DRC findings and one LVS mismatch remain open.
Confirm the basis | The checks use the agreed PDK revision P3.
Avoid silent version changes | Keep the rule deck and design dataset identified.
Qualify the slot | The foundry mentioned a possibility, not a reservation.
Ask about acceptance | What is required for the foundry to accept the dataset?
Keep sign-off visible | The complete sign-off package is not yet available.
Bound the exception | No waiver is approved for these findings.
Preserve the decision route | Any exception must follow the applicable authorization process.
Request a feasible sequence | Align check closure, data review, and capacity confirmation.
Avoid a downstream promise | We cannot infer finished samples from a tape-out target.
Clarify ownership | Who owns each open check and the next status update?
Record the dependency | The earlier request depends on both technical readiness and capacity.
State the next update | We will report check status and slot confirmation separately.
Close conditionally | October 8 remains a request pending the required evidence and acceptance.''',
    notes='''Slot | Clarify whether possible, held, reserved, or confirmed.
Ready | Identify which handoff and its required checks.
Tape-out | Not interchangeable with wafer start or finished-device delivery.
Clean | State the check scope, version, and remaining exceptions.
Waived | Requires an actual authorized exception, not a schedule preference.
Committed | Name the deliverable, date, dependencies, and accepting party.''',
    d='''Which reply to the earlier-date request is supported? | October 8 remains conditional on check closure, the required handoff, and capacity confirmation. | October 8 guarantees finished samples because a slot was mentioned. | The unresolved findings disappear if the customer accepts schedule risk. | The foundry has already reserved capacity by discussing it. | The reply preserves the separate technical and capacity prerequisites without inventing acceptance.
What does an LVS mismatch concern? | A difference between extracted layout connectivity and the schematic | A minimum geometric spacing violation against a design-rule deck | A negative setup-slack result in a required timing scenario | An offset between patterned wafer layers measured as overlay | LVS compares the layout-derived circuit with the schematic. Spacing rules, timing slack, and overlay belong to different verification or measurement questions.
Why retain the PDK and rule-deck versions with results? | The check result depends on the process-specific definitions actually used. | A clean result from one revision automatically clears later rule changes. | The design filename alone identifies every rule and model used. | The latest available deck replaces the agreed deck without an impact review. | Traceable versions identify the actual basis of the result. A filename is insufficient, and neither a later release nor an earlier clean run establishes unchanged applicability.
Which statement about tape-out is accurate? | It is a design-data handoff milestone, not proof of wafer start or sample availability. | It means every package has completed reliability qualification. | It always occurs on the same day as customer shipment. | It guarantees that no respin can be needed. | Fabrication, test, qualification, and delivery remain distinct activities after the design-data handoff.''',
    dialogue='''Sofia | Can we move tape-out from October fifteenth to October eighth? The foundry mentioned an earlier slot, and the customer is asking whether that means samples can arrive sooner.
Ken | Separate the [[tape-out::Tape-out is the design-data release milestone being requested, not a confirmed wafer start or finished-sample date.]] request from the later milestones. An earlier data handoff may matter to the plan, but it does not itself establish a wafer start or sample-delivery date.
Sofia | We still have four design-rule findings and one layout-versus-schematic mismatch. I want to know whether those can remain open while we secure the opportunity.
Ken | The [[sign-off::Sign-off is the required completion and approval of the defined checks; the complete package is not yet available here.]] package is not complete. No waiver is approved, so we cannot describe the design as ready by treating the open checks as an informal schedule exception.
Sofia | The verification team is working against P3, the agreed kit revision. We should preserve that basis when reporting progress rather than mix results from different revisions.
Ken | Keep the [[PDK::The PDK supplies process-specific design resources; its agreed revision must remain connected to the verification results.]] revision with the dataset and check results. The design rules and supported flow are process-specific, so version identity is part of the evidence.
Sofia | Please list the owner and status for each of the four findings. A falling count is not useful if the items were only relabeled.
Ken | Report each [[DRC::DRC checks the layout against applicable design rules; its open findings need documented resolution rather than a changed headline.]] finding with its status under the agreed process. Do not call the run clean while unresolved findings or required decisions remain outside the summary.
Sofia | The connectivity mismatch is a separate issue. I do not want the customer to hear that all five items are the same kind of geometric spacing check.
Ken | Correct. [[LVS::LVS compares extracted layout connectivity with the schematic and therefore addresses a different verification question from geometric rule checks.]] addresses layout versus schematic consistency. Keep that distinction clear when assigning ownership and explaining why the complete sign-off package is not yet available.
Sofia | On capacity, the foundry said a slot might become available. We have no written confirmation that it is allocated to this design.
Ken | Then there is no confirmed [[capacity reservation::Capacity reservation is an actual allocation; a possible earlier slot has not been reserved or accepted in this case.]]. We can discuss feasibility, but a mentioned opportunity must not be reported as an accepted manufacturing commitment.
Sofia | Who confirms that the foundry has accepted the data package? I do not want a file-transfer receipt reported as acceptance of the design handoff.
Ken | Exactly. [[Data acceptance::Data acceptance confirms the receiving process's requirements have been met; transmitting files alone does not establish it.]] is a separate handoff status. Record what the foundry needs and who confirms it, rather than assume a sent dataset has cleared the receiving review.
Sofia | Could a formal exception be considered if one finding remains? I want to ask through the correct route, not imply that my request already authorizes it.
Ken | A [[waiver::A waiver is an authorized exception to a specific requirement; none is approved for the open findings here.]] would need the applicable technical assessment and authorization. We cannot assume it is available or accepted simply because the earlier date is commercially attractive.
Sofia | I will avoid calling October eighth a fabrication start. The manufacturing schedule also depends on accepted data and actual capacity arrangements beyond our requested handoff.
Ken | Correct. A [[wafer start::A wafer start is the lot's entry into fabrication and is distinct from the earlier design-data handoff milestone.]] is a different milestone. Its timing and the subsequent flow must be confirmed on their own basis before anyone promises finished samples.
Sofia | The next update will separate check closure from slot confirmation. It will identify owners and show what remains conditional rather than announce the earlier date as secured.
Ken | That protects the [[delivery commitment::A delivery commitment must identify an accepted deliverable and date; neither a requested tape-out nor a possible slot guarantees finished samples.]]. We can pursue the opportunity actively while making clear which evidence, acceptance, and manufacturing decisions still stand between a request and a confirmed outcome.''',
    rehearsal=[
        'Check the answers. Read the requested tape-out date separately from wafer start and finished samples.',
        'Switch roles for turns 5-16. Expand PDK, DRC, and LVS using the vocabulary pages and preserve each open status.',
        'Complete and check the transfer. Read the four milestones without converting a possible slot into a commitment.'],
    transfer_title='A requested handoff is not a shipment',
    transfer_setup='A team requests tape-out on November 3. Two DRC items remain open. The foundry has mentioned a possible slot but has not reserved it. No waiver or sample-delivery date is approved.',
    transfer='''Designer: "Keep November third attached to the requested design-data handoff: ___." | tape-out | Tape-out identifies the requested design-data handoff, not a later manufacturing or delivery event.
Liaison: "The possible slot is not yet an allocated ___." | capacity reservation | Capacity reservation requires a confirmed allocation; a possible slot has not reached that status.
Designer: "I will not tell the customer that fabrication begins then; we have no confirmed ___." | wafer start | A wafer start is distinct from the requested design-data handoff and is not confirmed here.
Liaison: "And discussing a slot does not establish a finished-sample ___." | delivery commitment | A delivery commitment needs an accepted deliverable and date, neither of which follows from discussing a slot.'''))
