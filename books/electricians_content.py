"""Original Electricians' Workplace English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='electricians',
    title="Electricians' Workplace English",
    cover_label='ENGLISH FOR ELECTRICAL PROJECTS AND CLIENT COMMUNICATION',
    cover_title="Electricians'\nWorkplace",
    cover_size=38,
    tagline='Specific reports. Clear status.',
    audience='For electricians, electrical project staff, service coordinators, and specialists communicating with clients and other trades.',
    map_intro='Eight electrical-work conversations: define a service report, distinguish lumens and color temperature, clarify a device datum, coordinate ceiling routes, correct an outage notice, report uncertainty, assess added equipment, and hand over an unverified directory entry.',
    notes_title='Say exactly what the information establishes.',
    notes_intro='Precise electrical-work English separates client reports from verified conditions, lighting attributes from one another, and proposals from authorization. Practice accurate questions, comparisons, corrections, and handovers.',
    field_notes=[
        ('Keep a reported condition attributed', 'A client saying sockets are dead describes their experience; it is not verified electrical status. Capture the exact devices, location, and observation time without expanding the report to unassessed areas.', '"The client reports two desk receptacles in Room 204, first noticed at 08:30."'),
        ('Keep quantities attached to their units', 'Lumens describe light output, while kelvins describe color temperature. A mounting dimension also needs a reference point. A precise number alone does not settle a product comparison or an installation position.', '"Both are listed at 1,200 lumens; the 3,000 K and 4,000 K values describe color temperature."'),
        ('Separate proposals, approvals, and status', 'A requested outage window is not an approved outage or proof of isolation. Shared drawing review is not approval of a revised route. Use the exact stage established by the information.', '"The proposed window is 18:00-19:00 for reception lighting only; facilities approval is pending."'),
        ('Do not turn missing evidence into reassurance', 'A symptom not seen during one visit does not establish that a fault is absent. An outdated room label needs verification before identification is changed. State the limit and the named next step.', '"Flickering was not observed during the visit; the cause is not established and report review is pending."'),
    ],
    scope_note='The cases and products are fictional. This book teaches English, not electrical testing, switching, isolation, diagnosis, installation, circuit identification, or code compliance. Follow actual training, authorization, procedures, manufacturer information, and applicable requirements. Client descriptions, labels, outage plans, and handover records do not prove equipment is de-energized or safe to use or work on. These dialogues authorize no electrical operation, relabeling, routing change, substitution, or added load.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Electricians.',
             url='https://www.bls.gov/ooh/construction-and-extraction/electricians.htm',
             note='Occupational context for drawings, electrical systems, and coordination. The scenarios provide no installation or testing procedures.', checked='1 October 2026'),
        dict(title='Occupational Safety and Health Administration. Electrical Glossary.',
             url='https://www.osha.gov/electrical/glossary',
             note='Terminology for devices, raceways, ratings, and qualified roles. Learner definitions do not replace standards or safety procedures.', checked='1 October 2026'),
        dict(title='US Department of Energy. Purchasing Energy-Efficient Light Bulbs.',
             url='https://www.energy.gov/cmei/femp/purchasing-energy-efficient-light-bulbs',
             note='Reference for distinguishing lumen output, power input, and correlated color temperature. Procurement rules, historical prices, efficiency thresholds, and product recommendations are not taught here.', checked='1 October 2026'),
        dict(title='US Department of Energy. LED Basics.',
             url='https://www.energy.gov/cmei/ssl/led-basics',
             note='Background for lighting-system attributes, color appearance, color rendering, and product compatibility questions. No performance forecast, lifetime guarantee, or installation decision is inferred.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Taking a precise electrical service request',
    scene='Which sockets, where, and since when?',
    skill='Narrow a broad client description to named devices, location, and observation time without inferring technical status or requesting tests.',
    brief='Client Rosa tells electrician Kai that the office sockets are dead. Her account concerns two desk receptacles in Room 204, noticed at 08:30. Other areas have not been assessed. A panel-directory entry says office, but its accuracy has not been verified. Kai must clarify the request from the information Rosa already has. He must not ask her to test or operate anything, expand the report to the whole office, or treat dead as proof of safe electrical status.',
    cast='Rosa | Client\nKai | Electrician',
    culture=('Translate broad wording into a precise report', 'Clients often use a general room name and an everyday word for a problem. Ask neutral questions about what they already observed. Keep their report attributed, preserve unassessed areas as unknown, and avoid turning an informal description into a technical finding.'),
    a='''What does Rosa's account actually cover? | Two desk receptacles in Room 204 | Every circuit in the building | A verified whole-office outage | A confirmed isolated panel | The specific account concerns two desk receptacles in Room 204, not the whole office.
What does 08:30 represent? | When Rosa noticed the problem | A verified fault start time | A completed test time | A guaranteed repair appointment | The time records Rosa's observation, not the exact onset or an assessment result.
What is the status of the panel-directory entry? | It says office, but accuracy is unverified | It proves the relevant circuit identity | It authorizes the client to operate equipment | It confirms the area is safe | The label's wording is known, but its identification accuracy has not been verified.''',
    vocabulary='''receptacle | Device providing contacts for a plug connection. | identify the reported receptacles
socket | Common term for a receptacle or plug-in connection point. | clarify which sockets are reported
outlet | Point where electrical energy is supplied to utilization equipment. | identify the outlet location
desk receptacle | Receptacle serving or located at a desk position. | specify the desk receptacle
service request | Report asking for attention to a stated issue. | clarify the service request
client account | Description supplied by the customer. | preserve the client account
reported symptom | Problem described by a person rather than established by a technical finding. | record the reported symptom
observation time | When a person noticed the described condition. | record the observation time
onset | Time when a condition began, if established. | distinguish observation from onset
affected location | Area named in the report as experiencing the issue. | specify the affected location
unassessed area | Location whose condition has not been evaluated. | identify unassessed areas
panel directory | List identifying circuits or areas associated with a panel. | verify the panel directory
directory entry | Individual item in a panel or circuit list. | quote the directory entry
circuit identification | Establishing which circuit corresponds to a device or area. | refer circuit identification for verification
circuit | Electrical path or connected arrangement through which current may flow. | distinguish the circuit from the room name
distribution panel | Assembly distributing electrical supply to outgoing circuits. | identify the distribution panel
device count | Number of devices included in a report. | confirm the device count
room reference | Identifier locating a room in the building. | include the room reference
verified status | Condition established through the appropriate authorized process. | distinguish verified status
de-energized | In a state without energization, requiring appropriate verification before reliance. | avoid an unsupported de-energized claim
isolation status | Established state of separation from relevant energy sources under the actual procedure. | report only verified isolation status
technical finding | Conclusion supported by the relevant professional assessment. | distinguish a technical finding
scope of report | Extent of the issue actually described by the reporting person. | limit the scope of report
readback | Repetition of important information to confirm accuracy. | give a precise readback''',
    precision="Dead is Rosa's informal description, not verified de-energized or isolated status. Her account identifies two desk receptacles in Room 204. Other areas are unassessed, so they must not be described as either working normally or affected.",
    precision_extra='08:30 is the time the issue was noticed, not a proven onset time. The directory says office, but its accuracy is unverified. Clarify the report from known observations without asking the client to operate, open, switch, reset, or test any equipment.',
    phrases='''Acknowledge the report | I will record what you have already observed.\nNarrow the location | Which room does your report concern?\nConfirm the devices | You mean the two desk receptacles in Room 204.\nClarify the time | Is 08:30 when you first noticed the issue?\nAvoid an onset claim | We have not established exactly when it began.\nKeep attribution | The client reports that those two receptacles are not working as expected.\nPreserve unknown areas | Other areas have not been assessed.\nAvoid a whole-office claim | I will not describe this as a verified office-wide outage.\nQuote the label accurately | The directory entry says office.\nKeep identification open | The directory's accuracy has not been verified.\nSeparate wording and status | Dead is your description, not verified electrical status.\nAvoid a safety inference | I cannot infer that equipment is de-energized or safe from this report.\nUse existing observations | You do not need to test or operate anything for this clarification.\nKeep the count visible | The report concerns two devices, not an unspecified number.\nRead back the request | Two desk receptacles, Room 204, noticed at 08:30, other areas unassessed.\nClose the intake | I will preserve the unverified directory entry separately from your device report.''',
    notes='''The client reports | Attributes information rather than presenting it as a verified finding.\nNoticed at | Describes observation time without proving when the issue began.\nTwo | Limits the device count instead of generalizing to a whole room or floor.\nDead | Informal wording that must not become a technical statement of de-energization.\nUnassessed | Means unknown, not unaffected and not necessarily faulty.\nSays versus verifies | A directory label provides wording, not proof of correct circuit identification.''',
    d='''Which service summary is accurate? | Client reports two desk receptacles in Room 204, noticed at 08:30; other areas unassessed. | Entire office verified dead since exactly 08:30. | Panel isolated and safe because its label says office. | All other areas confirmed normal. | The summary preserves the attributed devices, location, observation time, and unassessed areas.
Which question is appropriate? | Which room does your existing report concern? | Can you open the panel and test the circuit? | Can you reset devices until something changes? | Can you operate equipment to prove the label? | The question clarifies known information without asking the client to perform an electrical action.
What does the label office establish? | Only the wording of an unverified directory entry | Verified circuit identity for the two devices | Safe isolation of all office equipment | A completed technical assessment | The entry's wording is known, but its accuracy and associated electrical status are not.
Which statement wrongly upgrades the evidence? | The receptacles are confirmed de-energized because the client called them dead. | The client used the word dead. | The report concerns Room 204. | The directory needs verification. | An informal symptom description does not establish de-energization, isolation, or safety.''',
    dialogue='''Rosa | The office sockets are dead. I need to report it, but I am not sure how much detail you want before someone looks at the issue.
Kai | Let us clarify the [[service request::Service request captures Rosa's existing observations without requiring her to operate or test electrical equipment.]] using what you already know. Which room and which connection points does your report concern? You do not need to test or operate anything.
Rosa | It is Room 204, specifically the two receptacles at the desks. I used office because that is how we refer to that room.
Kai | I will use the [[room reference::Room reference is Room 204, which is more precise than treating the word office as the entire office area.]] of 204 and name the two desk receptacles. I will not expand that to every connection point in the office.
Rosa | I noticed the issue at 08:30. I cannot say exactly when it started, because that was when I first became aware of it.
Kai | Then 08:30 is the [[observation time::Observation time records when Rosa noticed the issue, not a proven start time for the underlying condition.]]. I will keep that distinction and avoid saying the fault definitely began at that exact time.
Rosa | Nobody has assessed the other rooms as part of this report. I do not want my broad wording to make it sound as though they have.
Kai | I will describe those as [[unassessed areas::Unassessed areas remain unknown; the report does not establish that they are either affected or working normally.]]. That means their status is unknown here, not that they are definitely affected or definitely working normally.
Rosa | The panel directory has an entry saying office. I have that wording in the information we already hold, but I do not know whether it is accurate.
Kai | I will record the [[directory entry::Directory entry supplies the word office, but its accuracy and relationship to the reported devices remain unverified.]] separately. Its wording is useful information, but it does not verify which circuit serves the devices in your report.
Rosa | Should I call them outlets or receptacles? I have heard both terms, and I want the person reading the request to recognize the same two points.
Kai | We can specify two desk [[receptacles::Receptacles identifies the two plug-connection devices in Rosa's account and keeps the device description specific.]]. The important detail is the exact devices and room, not replacing your wording with a broader claim about the electrical installation.
Rosa | And when I say dead, I only mean they were not working as I expected. I am not giving a technical statement about their condition.
Kai | I will preserve that as a [[reported symptom::Reported symptom attributes the informal description to Rosa without treating it as a verified electrical condition.]]. Dead in a client account is not proof that equipment is de-energized, isolated, or safe to use or work on.
Rosa | Thank you. I would prefer the report to keep that limit explicit rather than have someone assume a check has already taken place because the wording sounds confident.
Kai | There is no [[verified status::Verified status is not supplied by this intake conversation, so no assessment or safety conclusion can be claimed.]] established by this conversation. I am clarifying the information for the request, not reporting a completed electrical assessment.
Rosa | Could you read the description back before it goes further? The room, the two devices, and the time are the details I can confirm.
Kai | The [[readback::Readback confirms the two devices, Room 204, and the 08:30 observation while retaining unknown conditions elsewhere.]] is: client reports two desk receptacles in Room 204, noticed at 08:30; exact onset unknown; other areas unassessed; directory wording unverified.
Rosa | That is accurate. Please keep the directory wording attached as unverified information, not as proof that the circuit has already been identified.
Kai | I will. [[Circuit identification::Circuit identification remains unverified; the office label is not proof of which circuit serves the reported receptacles.]] remains open for the appropriate process. The request will preserve your observations without asking you to carry out any electrical action or adding a technical finding.''',
    transfer_title='Keep the report attributed and specific',
    transfer_setup='Complete the intake readback from the client information. Do not turn the word dead or an unverified label into a technical conclusion.',
    transfer='''Electrician: "Your report concerns ___ desk receptacles." | two | Two is the device count in the client's specific account.
Client: "They are in Room ___." | 204 | Room 204 identifies the reported location without including the whole office.
Electrician: "You noticed the issue at ___." | 08:30 | This records the observation time rather than a verified onset time.
Client: "The directory entry remains ___." | unverified | The word office appears in the directory, but its accuracy is unconfirmed.''',
))

BOOK['units'].append(unit(
    title='Clarifying lighting specifications',
    scene='More kelvins does not mean more light',
    skill='Explain the difference between light output and color temperature while preserving unresolved compatibility and substitution decisions.',
    brief='Client Ben has selected two fictional luminaires for comparison with electrician Asha. Both are listed at 1,200 lumens. One is 3,000 kelvins and the other 4,000 kelvins. Ben assumes the larger kelvin number means more light. No substitution is approved, and driver compatibility remains for specialist review. Asha must explain the two attributes without promising identical illumination at a work surface or treating equal lumen output as proof that the products are interchangeable.',
    cast='Ben | Client\nAsha | Electrician',
    culture=('Correct the comparison without making the client feel foolish', 'Lighting labels place several numbers close together, and a larger figure can seem like a simple improvement. Name what each unit describes, compare the supplied values, and keep separate questions such as distribution, compatibility, and approval visible.'),
    a='''What do both products list? | 1,200 lumens | The same color temperature | Confirmed driver compatibility | An approved substitution | Both luminaires list the same light output of 1,200 lumens.
What differs between them? | The 3,000 K and 4,000 K color-temperature values | The listed lumen output | A confirmed installation position | A supplied warranty duration | The kelvin values differ, while the listed lumen values are equal.
What remains for specialist review? | Driver compatibility | Whether 4,000 is greater than 3,000 | Whether both labels say 1,200 lumens | Whether Ben asked a question | Driver compatibility has not been established by the supplied product comparison.''',
    vocabulary='''luminaire | Complete lighting unit with its relevant light source and supporting components. | compare the luminaires
lumen | Unit of luminous flux, describing visible light output. | compare lumen output
luminous flux | Total visible light output weighted for human visual sensitivity. | specify luminous flux
kelvin | Unit used to state correlated color temperature. | read the kelvin value
correlated color temperature | Description of a light source's color appearance relative to a reference, abbreviated CCT. | compare correlated color temperature
warm white | Description commonly used for a warmer white-light appearance. | describe warm-white light
cool white | Description commonly used for a cooler white-light appearance. | compare cool-white appearance
light output | Amount of light emitted, commonly stated in lumens. | distinguish light output
illuminance | Amount of light arriving on a surface per unit area. | assess illuminance at the work surface
lux | Unit of illuminance equal to one lumen per square meter. | state illuminance in lux
light distribution | Pattern in which a luminaire sends light into a space. | compare light distribution
beam angle | Angular spread used to describe a light beam under a stated convention. | check the beam angle
LED | Light-emitting diode, a semiconductor light source. | identify the LED product
driver | Device supplying and regulating electrical power for an LED system. | review the driver specification
driver compatibility | Suitability of a driver for the specified lighting and control arrangement. | verify driver compatibility
dimming | Adjustment of light output through a compatible control arrangement. | review dimming requirements
control interface | Connection or protocol through which a lighting system is controlled. | identify the control interface
watt | Unit of power, distinct from a measure of light output. | compare input power in watts
efficacy | Light output per unit of input power, commonly lumens per watt. | distinguish efficacy from color temperature
color rendering | Effect of a light source on the appearance of object colors. | compare color rendering
color rendering index | Metric describing color fidelity relative to a reference, abbreviated CRI. | check the color rendering index
product data sheet | Document describing specified product attributes. | compare the product data sheets
substitution | Proposed replacement of a specified product with another. | review a proposed substitution
specialist review | Assessment by a person with relevant technical competence. | refer compatibility for specialist review''',
    precision='Both luminaires are listed at 1,200 lumens, so the supplied light-output figures are equal. The 4,000 K product has a cooler color appearance than the 3,000 K product. The larger kelvin number does not establish a greater lumen output.',
    precision_extra='Equal listed lumens do not guarantee identical light levels at a desk, because distribution and installation conditions matter. No substitution is approved, and driver compatibility remains unresolved. Do not infer wattage, efficiency, dimming behavior, or technical interchangeability from these two numbers.',
    phrases='''Name the two attributes | Lumens and kelvins describe different things.\nExplain output | Lumens describe the listed light output.\nExplain color | Kelvins describe the color temperature.\nCompare the given output | Both products are listed at 1,200 lumens.\nCompare the color | The 4,000 K option has a cooler appearance than the 3,000 K option.\nCorrect the assumption | A larger kelvin number does not mean more lumen output.\nPreserve the exact claim | Their listed outputs match; that is not a promise of identical desk illumination.\nSeparate distribution | We also need to consider how the light is distributed.\nAvoid a wattage inference | The supplied figures do not tell us their input power.\nAvoid an efficiency inference | We cannot rank efficiency from color temperature alone.\nKeep compatibility open | Driver compatibility still needs specialist review.\nKeep approval open | No product substitution is approved.\nDistinguish comparison and replacement | Comparing them does not authorize swapping one for the other.\nRefer the data | The specialist needs the relevant product and driver information.\nAvoid a control promise | We have not established dimming compatibility.\nRead back the result | Same listed lumens, different color temperature, and compatibility still unresolved.''',
    notes='''Listed at | Attributes the value to the supplied product information, not a site measurement.\nCooler | Describes white-light color appearance rather than physical temperature or greater output.\nSame output | Refers to the stated lumens, not every lighting characteristic.\nAt the surface | Introduces illuminance, which is distinct from source output.\nCompatible | Requires relevant technical assessment beyond matching two label numbers.\nApproved substitution | A decision status that is separate from a comparison of specifications.''',
    d='''Which correction is accurate? | Both list 1,200 lumens; 4,000 K describes a cooler color appearance, not more listed output. | 4,000 K means 4,000 lumens. | 3,000 K always uses less electricity. | Equal lumens prove identical drivers. | The correction distinguishes the equal listed output from the differing color-temperature values.
Which claim is not supported by equal lumens? | Both will provide identical illumination at every desk. | Their listed light-output values match. | Each is listed at 1,200 lumens. | The lumen figures do not differ in this comparison. | Surface illumination also depends on distribution and installation conditions not supplied in the case.
What should happen with driver compatibility? | Refer it for specialist review using the relevant information | Assume compatibility because both list 1,200 lumens | Ask the client to try connecting them | Treat the higher kelvin value as approval | Matching light-output figures do not establish electrical or control compatibility.
What is the substitution status? | Not approved | Automatically approved by the color comparison | Approved because the client mentioned both products | Completed and tested | The scenario explicitly states that no product substitution has been approved.''',
    dialogue='''Ben | I picked these two fittings to compare. The 4,000 K one gives more light than the 3,000 K one, so it should make the desk brighter, correct?
Asha | The larger number is the [[correlated color temperature::Correlated color temperature describes color appearance, not the amount of light emitted by the luminaire.]], not the light-output figure. Both products are listed at 1,200 lumens, so their stated outputs are equal.
Ben | I had treated all the numbers as variations on brightness. Could you explain which one I should use when comparing the amount of light?
Asha | Compare the [[lumen::Lumen is the unit for visible light output; both supplied product figures are 1,200 lumens.]] values for the listed output. In this comparison, each says 1,200. The kelvin values describe another attribute and should not replace that comparison.
Ben | Then what would I notice about the difference between 3,000 and 4,000 K? I want the wording right when I discuss the options with our designer.
Asha | The 4,000 K option has a cooler [[color appearance::Color appearance is cooler at 4,000 K than at 3,000 K; this is separate from the equal listed lumen output.]] than the 3,000 K option. That describes the character of the white light, not an increase from 1,200 lumens.
Ben | If the listed output is the same, can I assume either one gives exactly the same light level on the desk after installation?
Asha | Not from that figure alone. [[Illuminance::Illuminance concerns light reaching a surface, which is not determined by the listed lumen output alone.]] at the desk is a different question. Distribution and installation conditions affect how much of the emitted light reaches that surface.
Ben | So two fittings can have the same total output and send it into the room differently. We would need more than these two numbers to compare that.
Asha | Yes. Their [[light distribution::Light distribution describes where emitted light goes and can affect surface illumination even when listed outputs match.]] matters. I will not turn matching lumen figures into a guarantee that every point in the room receives the same light.
Ben | What about electricity use? Does the higher kelvin number mean the fitting needs more power, or is that another separate part of the data?
Asha | Input power is stated in [[watts::Watts measure power, which is distinct from lumens and color temperature; no wattage comparison is supplied.]]. We do not have those figures here, so neither the kelvin difference nor the matching lumens establishes which uses more power.
Ben | Understood. I also saw a driver mentioned in the product information. Can we assume the one planned for the first fitting will suit the second?
Asha | No. [[Driver compatibility::Driver compatibility remains for specialist review and cannot be inferred from matching lumen values or a color-temperature comparison.]] still needs specialist review. Matching output figures do not establish that the electrical and control arrangements are suitable for both products.
Ben | I am only comparing options at this stage. Please do not treat my question about the second fitting as approval to substitute it in the order.
Asha | I will keep [[substitution::Substitution is not approved; discussing the alternative does not authorize replacing a specified product.]] approval separate. No replacement product is approved in this conversation, and the outstanding compatibility question remains visible.
Ben | Could the specialist review the relevant product and driver details before anyone tells me that changing the fitting is straightforward? I would rather know the actual requirements.
Asha | The relevant [[product data sheet::Product data sheet provides product-specific information for review; a brief comparison does not establish all compatibility requirements.]] and driver information should support that review. We have not established dimming behavior or interchangeability from the supplied figures.
Ben | My summary is that both list 1,200 lumens, while 3,000 and 4,000 K describe different color appearances. The comparison does not settle the technical replacement question.
Asha | Correct. The [[specialist review::Specialist review remains the next step for compatibility; neither equal output nor a cooler appearance resolves the substitution decision.]] remains outstanding. We can explain the labels accurately while leaving compatibility and any substitution decision open until the appropriate information is assessed.''',
    transfer_title='Keep light output and color separate',
    transfer_setup='Complete the client explanation using the supplied values. Do not infer a different output, identical desk illumination, or approved compatibility.',
    transfer='''Electrician: "Both products list 1,200 ___." | lumens | Lumens describe the equal light-output figures supplied for the two products.
Client: "The 3,000 and 4,000 values are in ___." | kelvins | Kelvins identify the color-temperature values rather than the output figures.
Electrician: "The 4,000 K option has a ___ appearance." | cooler | Cooler compares the white-light appearance with that of the 3,000 K option.
Client: "Driver compatibility still needs specialist ___." | review | Compatibility remains unresolved and requires the stated specialist review.''',
))

BOOK['units'].append(unit(
    title='Agreeing device positions and drawing references',
    scene='Centerline or lower edge?',
    skill='Clarify the datum and device reference behind a mounting dimension without treating another trade drawing as installation approval.',
    brief='Electrician Leila and joinery coordinator Omar review a reception elevation showing a device at 1,100 millimeters above finished floor level. The electrical note does not identify whether the figure refers to the device centerline or lower edge. The joinery drawing uses a centerline. No position has been approved for installation. Leila needs the responsible designer to clarify the intended reference rather than silently import the joinery convention into the electrical detail.',
    cast='Omar | Joinery coordinator\nLeila | Electrician',
    culture=('Shared numbers still need shared reference points', 'Two trades may use the same dimension while measuring to different parts of a component. Name the datum and endpoint separately. Another drawing can reveal a question to resolve, but its convention does not automatically answer an unclear note in a different discipline.'),
    a='''What is stated on the reception elevation? | 1,100 millimeters above finished floor level, with the device reference unclear | An approved lower-edge position | A verified centerline instruction for installation | A dimension from the unfinished slab | The elevation states the height and floor datum but not the device endpoint.
What convention does the joinery drawing use? | Centerline | Lower edge only | Top edge only | No reference at all | The joinery drawing uses a centerline, but that does not resolve the electrical note.
What is the installation status? | No device position is approved | Centerline approved automatically | Lower edge approved automatically | Installation already completed | The case explicitly leaves installation position unapproved pending clarification.''',
    vocabulary='''finished floor level | Level of the completed floor surface, commonly abbreviated FFL. | confirm finished floor level
above finished floor | Dimension measured upward from the completed floor, commonly abbreviated AFF. | state the height above finished floor
centerline | Reference line through the specified center of a component. | identify the centerline
lower edge | Bottom boundary of the specified device or component. | locate the lower edge
upper edge | Top boundary of the specified device or component. | distinguish the upper edge
mounting height | Specified height for locating a mounted device. | clarify the mounting height
device position | Intended location of a specified component. | confirm the device position
reception elevation | Drawing view showing the reception face and its details. | review the reception elevation
datum level | Reference level from which a height is measured. | verify the datum level
dimension endpoint | Point or edge to which a dimension extends. | identify the dimension endpoint
set-out | Defined positioning information for locating work. | clarify the set-out information
joinery interface | Point where electrical work and fitted woodwork must coordinate. | review the joinery interface
drawing convention | Agreed or customary way information is represented on a drawing. | clarify the drawing convention
reference ambiguity | Uncertainty about what a dimension or note refers to. | flag the reference ambiguity
faceplate | Visible plate associated with an electrical accessory or device. | identify the faceplate
back box | Enclosure behind a device or accessory. | distinguish the back box
device schedule | List identifying specified devices and their attributes. | check the device schedule
horizontal alignment | Relative positioning along a horizontal direction. | coordinate horizontal alignment
vertical alignment | Relative positioning along a vertical direction. | confirm vertical alignment
approved location | Position explicitly accepted through the relevant process. | verify the approved location
design clarification | Explanation resolving uncertain design information. | request design clarification
coordination mark-up | Annotated drawing used to communicate coordination questions. | prepare a coordination mark-up
installation instruction | Authorized direction for fitting the specified equipment. | distinguish an installation instruction
reference readback | Repetition of the datum and endpoint to verify shared understanding. | give a reference readback''',
    precision='The floor datum is stated: finished floor level. The missing information is the endpoint on the device, centerline or lower edge. The joinery centerline convention highlights the need to coordinate, but does not authorize applying that convention to the electrical note.',
    precision_extra='No device dimensions are supplied, so no centerline-to-edge conversion can be calculated here. No position is approved for installation. The next step is design clarification of the intended reference, with both drawings included in the coordination question.',
    phrases='''Read the stated height | The elevation shows 1,100 millimeters above finished floor level.\nIdentify the known datum | The reference level is the completed floor surface.\nIdentify the missing endpoint | The note does not say centerline or lower edge.\nCite the other drawing | The joinery drawing uses a centerline.\nAvoid importing a convention | That does not automatically settle the electrical reference.\nAsk a precise question | Does 1,100 refer to the device centerline or its lower edge?\nKeep the datum unchanged | I am not asking to change the finished-floor reference.\nKeep the value unchanged | The query concerns the endpoint, not a new height.\nAvoid a guessed conversion | We do not have the device dimensions needed for a conversion.\nPreserve approval status | No installation position has been approved.\nRequest coordinated review | Please review the reception elevation with the joinery drawing.\nDistinguish a mark-up from approval | A coordination note is not an installation instruction.\nName the interface | This is a device-position question at the joinery interface.\nAsk for explicit clarification | The reply should state the datum and the device reference.\nRead back the known facts | 1,100 above finished floor, endpoint unclear, joinery centerline shown.\nClose without setting a position | We need clarification before presenting either interpretation as approved.''',
    notes='''Above finished floor | Defines the vertical origin of the measurement, not its endpoint on the device.\nCenterline versus edge | Different references that can produce different positions from the same stated number.\nUses | Describes the other drawing's convention without transferring its authority.\nClarify versus change | Resolving meaning does not necessarily request a different design.\nShown versus approved | A displayed dimension and an accepted installation position are distinct statuses.\nBoth drawings | Keeps the interface visible for coordinated interpretation.''',
    d='''Which question addresses the ambiguity? | Is the 1,100-millimeter height to the centerline or lower edge of the device? | Why is the lower edge already approved? | Can we assume the unfinished slab is the datum? | Which installed device has failed? | The question targets the missing endpoint while preserving the stated height and floor datum.
Which fact is already known? | The datum is finished floor level | The electrical endpoint is definitely centerline | The lower edge is approved | The device height needed for conversion | The elevation names finished floor level even though the device reference remains unclear.
Which inference is unsupported? | The joinery centerline automatically approves the electrical centerline position. | The joinery drawing uses a centerline. | The electrical note needs clarification. | No installation position is approved. | A convention on another drawing does not resolve or authorize the ambiguous electrical detail.
What should the clarification preserve? | Both drawing references, the stated height, the floor datum, and the unanswered endpoint | A guessed device height | An invented installation approval | A substituted floor reference | These details define the actual coordination question without adding dimensions or permission.''',
    dialogue='''Omar | The reception elevation says 1,100 above finished floor. Our joinery drawing uses a centerline, so can we treat the electrical device position as matching that?
Leila | Not yet. The [[mounting height::Mounting height is stated as 1,100 millimeters, but the point on the device to which it applies remains unclear.]] is shown, but the electrical note does not say whether it refers to the centerline or the lower edge.
Omar | I see. We know the level from which the height starts, but not exactly where it ends on the device. Is that the distinction?
Leila | Yes. [[Finished floor level::Finished floor level is the stated datum; the ambiguity concerns the device endpoint rather than the floor reference.]] is the stated datum. The missing part is the reference on the device, and we should keep those two questions separate.
Omar | I can include the joinery detail in the query. It shows why I expected a centerline, but I do not want it treated as a decision for your drawing.
Leila | That will help explain the [[joinery interface::Joinery interface identifies the coordination point between the device and fitted woodwork without authorizing a position.]]. The other drawing is relevant evidence for the question, not permission to fill in the missing electrical reference ourselves.
Omar | Should we ask whether the dimension is to the faceplate, the box, or some other feature? I want the reply to remove the ambiguity rather than repeat the number.
Leila | We need an explicit [[dimension endpoint::Dimension endpoint is the particular point or edge being measured to, which must be clarified instead of merely repeating 1,100.]]. The reply should identify the intended device reference, including whether the note means centerline or lower edge.
Omar | Could we calculate the difference between those positions now? That might show the team why the same number does not necessarily put the device in the same place.
Leila | We do not have the device dimensions for that calculation. A [[reference ambiguity::Reference ambiguity cannot be resolved by a guessed conversion when the device dimensions and intended endpoint are not established.]] is not solved by inventing an offset or assuming a particular faceplate size.
Omar | Fair point. I will keep the question about interpretation, not turn it into a proposal to raise or lower the device by a guessed amount.
Leila | Exactly. The [[design clarification::Design clarification asks what the current note means; it does not automatically request a new height or authorize a position.]] concerns what the existing note means. We are not asking to change the 1,100-millimeter value or the finished-floor datum without a design decision.
Omar | No position has been approved for installation, correct? I want the review note to make that explicit before it reaches the site team.
Leila | Correct. There is no [[approved location::Approved location has not been established, so neither centerline nor lower-edge interpretation can be presented as ready for installation.]] from this conversation. Neither interpretation should be presented as an authorized installation position while the reference remains unresolved.
Omar | I can prepare a marked-up comparison showing the reception elevation and the joinery centerline. That should make the question easier to locate.
Leila | A [[coordination mark-up::Coordination mark-up communicates the unresolved interface question and is not itself an instruction or approval to install.]] is useful for the review. It should identify the uncertainty clearly, not look like an instruction to install at the position you have assumed.
Omar | Please give me the wording you want in the query. I want the responsible designer to answer the specific issue rather than comment generally on reception.
Leila | Use this [[reference readback::Reference readback preserves the 1,100-millimeter height, finished-floor datum, and unresolved device endpoint together.]]: 1,100 millimeters above finished floor level; electrical endpoint unclear; joinery uses centerline; please confirm the intended device reference with both drawings reviewed together.
Omar | That is precise. I will keep the current value and the unapproved status visible, and avoid using the mark-up as if the designer had already answered.
Leila | Thank you. The clarification is not an [[installation instruction::Installation instruction is not supplied by the unresolved query; the team still needs the intended reference and appropriate approval.]] until the relevant process establishes what is intended and approved. For now, the endpoint remains open and no position is authorized here.''',
    transfer_title='Name both ends of the dimension',
    transfer_setup='Complete the coordination query. Preserve the height, known floor datum, unclear endpoint, and lack of installation approval.',
    transfer='''Electrician: "The stated height is ___ millimeters." | 1,100 | The numerical height remains 1,100; the query does not replace it.
Coordinator: "It is measured above finished ___ level." | floor | Finished floor level is the stated datum for the dimension.
Electrician: "The device reference could be centerline or lower ___." | edge | Lower edge is the alternative endpoint that the note leaves unclear.
Coordinator: "No installation position is ___ yet." | approved | The position remains unapproved until the relevant clarification and approval process.''',
))

BOOK['units'].append(unit(
    title='Coordinating containment and shared work areas',
    scene='A tray and a duct in bay C3',
    skill='Describe a cross-trade drawing conflict, request joint review, and preserve the distinction between a meeting and an approved route.',
    brief='Electrical drawing E6 places a cable tray in ceiling bay C3. The mechanical layout shows a duct in the same space. Electrician Dev reports the conflict to ceiling coordinator Elena before the coordination meeting at 13:00. Neither trade has agreed a revised route. Dev needs both drawings reviewed together. He must not announce an invented offset, assume one trade has priority, or treat the meeting time as authorization to install a changed route.',
    cast='Elena | Ceiling coordinator\nDev | Electrician',
    culture=('Describe the interface without turning it into a contest', 'A shared-space conflict needs a coordinated answer, not a claim that one trade must move because the other spoke first. Name the components, location, and drawing sources, then state the unresolved route and the agreed review point.'),
    a='''What occupies the same drawn space? | A cable tray on E6 and a duct on the mechanical layout in bay C3 | Two approved routes in separate rooms | A completed installation and an unrelated floor finish | A tray with a confirmed revised offset | The electrical tray and mechanical duct conflict in the same ceiling bay.
What is scheduled for 13:00? | The ceiling coordination meeting | Guaranteed route approval | Completion of the reroute | A confirmed installation start | The supplied time is the meeting time, not approval or completion.
What is the revised-route status? | Neither trade has agreed one | Electrical has automatic priority | Mechanical has accepted a specific offset | Both routes are installed and accepted | No revised route is agreed by either trade in the supplied facts.''',
    vocabulary='''cable tray | Support system used to carry cables along a route. | identify the cable tray
containment | Systems supporting or enclosing cables along their route. | coordinate cable containment
conduit | Tube or pipe used as an electrical raceway. | distinguish conduit from cable tray
trunking | Enclosed channel used to contain cables in relevant terminology. | identify the trunking route
raceway | Channel designed to contain electrical conductors or cables. | specify the raceway
duct | Passage or enclosure conveying air in a mechanical system. | locate the mechanical duct
ceiling bay | Defined section of ceiling space used as a location reference. | identify ceiling bay C3
ceiling void | Space above a ceiling surface. | coordinate work in the ceiling void
mechanical layout | Drawing showing the arrangement of mechanical services. | compare the mechanical layout
electrical layout | Drawing showing the arrangement of electrical work. | review the electrical layout
route conflict | Incompatibility between proposed paths or occupied spaces. | flag a route conflict
spatial clash | Overlap or incompatible use of physical space. | report a spatial clash
clearance requirement | Space needed around a component for the relevant purpose. | verify clearance requirements
maintenance access | Space or route needed for inspection or servicing. | preserve maintenance access
support arrangement | Specified way a component is held in place. | review the support arrangement
coordinated drawing | Drawing incorporating agreed interfaces among relevant disciplines. | issue a coordinated drawing
revised route | Changed path proposed or agreed for a service. | review a revised route
proposed offset | Suggested displacement from a stated route or position. | assess a proposed offset
trade priority | Claimed or agreed precedence between work disciplines. | avoid assuming trade priority
joint review | Assessment involving the relevant parties together. | request a joint review
coordination meeting | Discussion intended to resolve interfaces and arrangements. | attend the coordination meeting
route approval | Acceptance of a specified routing arrangement. | confirm route approval
drawing overlay | Combined view of related drawings for comparison. | use a drawing overlay
unresolved interface | Cross-discipline connection or conflict not yet settled. | record an unresolved interface''',
    precision='E6 places a cable tray in ceiling bay C3 where the mechanical layout shows a duct. The conflict is between the drawn arrangements; the case does not establish completed installation. No revised route or priority rule is agreed.',
    precision_extra='The meeting at 13:00 is a review point, not a route approval or installation start. Both drawings need joint review. No alternative route, offset, clearance, support detail, or maintenance-access solution is supplied for students to invent.',
    phrases='''Locate the conflict | The clash is in ceiling bay C3.\nCite the electrical source | E6 shows the cable tray in that space.\nCite the mechanical source | The mechanical layout shows a duct there.\nState the interface | The two drawn routes occupy the same space.\nRequest joint review | We need both drawings reviewed together.\nPreserve the current status | Neither trade has agreed a revised route.\nAvoid priority assumptions | I am not assuming that one trade automatically takes priority.\nAvoid an invented offset | No offset has been proposed and approved here.\nState the meeting time | The ceiling coordination meeting is at 13:00.\nSeparate meeting and approval | The meeting time does not authorize a routing change.\nKeep related requirements open | Clearances and access would need review for any proposed solution.\nAvoid an installation claim | I am describing the drawings, not a completed site installation.\nKeep the record specific | Cable tray and duct conflict at C3, with route revision unresolved.\nAsk for an explicit outcome | The review needs to identify the agreed arrangement through the project process.\nPreserve both sources | Please keep E6 and the mechanical layout attached to the query.\nClose with the open issue | The interface remains unresolved pending coordinated review.''',
    notes='''Shows | Attributes the position to a drawing rather than claiming it is installed.\nSame space | Defines the conflict between the two arrangements.\nNeither | Makes clear that no trade has agreed the revised route.\nTogether | Calls for coordinated review rather than separate assumptions.\nAt 13:00 | Identifies the meeting, not the time a technical solution becomes approved.\nProposed versus agreed | A possible change and an accepted route are different stages.''',
    d='''Which report identifies the conflict precisely? | E6 cable tray and mechanical-layout duct share ceiling bay C3; revised route unresolved. | The ceiling is wrong somewhere. | Mechanical must move because electrical has priority. | A new offset is already approved. | The report names both components, sources, location, and unresolved route status.
What does Dev need at the meeting? | Both drawings reviewed together | Only E6 treated as automatically authoritative | A guessed offset presented as agreed | Confirmation of a completed reroute that never occurred | Joint review is needed to resolve the cross-trade conflict without unilateral assumptions.
Which statement overstates the 13:00 arrangement? | The new route is approved for installation at 13:00. | The coordinator meeting is at 13:00. | The route remains unresolved. | Neither trade has agreed a revision. | The meeting time establishes no route approval or installation authorization.
What must remain open for a proposed solution? | The actual route and relevant technical coordination requirements | Whether E6 shows a tray | Whether C3 is the identified bay | Whether the mechanical layout shows a duct | No alternative route or supporting technical details have been established in the case.''',
    dialogue='''Elena | What needs to come into the ceiling meeting at 13:00? I want each issue tied to a location so we can review the relevant drawings together.
Dev | There is a [[route conflict::Route conflict is the cable tray and duct occupying the same drawn space in ceiling bay C3.]] in bay C3. Electrical drawing E6 places a cable tray where the mechanical layout shows a duct.
Elena | Is that a conflict on the drawings, or are you reporting that both services have already been installed in the same area?
Dev | I am reporting the [[electrical layout::Electrical layout E6 shows the proposed tray position; the case does not establish that either service is already installed.]] against the mechanical layout. I am not saying the components are already installed or that a site alteration has been authorized.
Elena | Thank you. Has either trade agreed to a revised path, perhaps in a separate discussion that has not reached the coordination record?
Dev | Neither trade has agreed a [[revised route::Revised route remains unagreed by both trades, so no changed path can be presented as a settled arrangement.]]. I do not have an accepted alternative to bring to the team, only the conflict and the two drawing sources.
Elena | Then we should show both views rather than ask one trade to solve its route in isolation. The shared space is the point we need to address.
Dev | Exactly. A [[joint review::Joint review brings both drawing arrangements into the same discussion instead of assuming either trade can resolve the interface alone.]] is needed. Looking only at E6 would hide the duct, while looking only at the mechanical layout would hide the tray requirement.
Elena | Can we state that one service has priority? Sometimes people arrive with that assumption, even when the project has not made a decision about the interface.
Dev | No [[trade priority::Trade priority is not established in the case, so neither electrical nor mechanical can be assumed to take precedence automatically.]] is supplied here. I should not tell the mechanical team it must move, or promise that electrical will move, before the coordinated review.
Elena | Agreed. We also need to avoid a sketch that looks like an approved solution when it is only a way of showing the clash.
Dev | I can identify the [[ceiling bay::Ceiling bay C3 is the precise shared-space reference, not an approved route or technical solution.]] as C3 and preserve both positions. No offset is agreed, so the query should not draw an invented change as though it has been accepted.
Elena | If a route is proposed during review, the team will need the relevant clearances and access considered. We do not have those details in this issue note yet.
Dev | Correct. [[Maintenance access::Maintenance access is one relevant coordination question for any solution; no access or clearance arrangement is supplied here.]] and other requirements cannot be assumed from a simple line moved on a drawing. The current report does not settle them.
Elena | Please keep the 13:00 time in the message, but make clear that it is the meeting. I do not want it copied as an installation start.
Dev | I will label it as the [[coordination meeting::Coordination meeting identifies the 13:00 review point and does not authorize installation or guarantee a completed solution.]]. It is a review point, not permission to install a new route or a promise that the conflict will be resolved by then.
Elena | Read the issue back once before you send it. I want the two sources and the unagreed status in the same short summary.
Dev | E6 cable tray and mechanical-layout duct share bay C3; [[route approval::Route approval is absent because neither trade has agreed a revised path; the query must preserve that status.]] is not established; both drawings need review at the 13:00 ceiling meeting. No alternative route is agreed.
Elena | That gives the team the question without assigning blame or inventing the answer. I will keep both drawings with the issue for the joint discussion.
Dev | Thank you. I will retain it as an [[unresolved interface::Unresolved interface keeps the cross-trade conflict open until the actual project process establishes an agreed arrangement.]] until the project process records an agreed arrangement. The meeting and the query do not themselves authorize a routing change.''',
    transfer_title='Bring both drawings to the review',
    transfer_setup='Complete the coordination summary. Include the electrical source, shared bay, meeting time, and unresolved route status.',
    transfer='''Electrician: "The cable tray is shown on drawing ___." | E6 | E6 is the electrical drawing that shows the cable-tray route.
Coordinator: "The shared ceiling bay is ___." | C3 | C3 is the location where the tray and duct drawings conflict.
Electrician: "The coordination meeting is at ___." | 13:00 | Thirteen hundred is the meeting time, not an installation approval.
Coordinator: "Neither trade has ___ a revised route." | agreed | No revised route has been agreed by either relevant trade.''',
))

BOOK['units'].append(unit(
    title='Communicating outage plans and status',
    scene='Correcting the proposed outage notice',
    skill='Preserve the proposed scope and time window, correct an overstated notice, and distinguish facilities approval from electrical status.',
    brief='Electrician Imani reviews an outage request with facilities coordinator Joel. The request proposes 18:00-19:00 for reception lighting only. Facilities has not approved it. A draft tenant notice incorrectly says the whole floor will be unavailable. No isolation status is supplied. Imani and Joel need to correct the notice scope and its proposed status without presenting the window as confirmed or giving operational instructions.',
    cast='Joel | Facilities coordinator\nImani | Electrician',
    culture=('Correct scope and status together', 'A notice can mislead through both its area description and its level of certainty. Correcting whole floor to reception lighting is not enough if the notice still presents an unapproved request as confirmed. Keep proposal, approval, communication, and verified operational status separate.'),
    a='''What does the request propose? | Reception lighting only, 18:00-19:00 | The whole floor all day | A confirmed outage for every service | An already completed isolation | The proposed request covers only reception lighting within the stated one-hour window.
What is wrong with the tenant notice? | It says the whole floor will be unavailable | It correctly limits the proposal to reception lighting | It establishes verified isolation | It confirms facilities approval already received | The notice expands the impact beyond the reception-lighting scope of the request.
What remains unapproved? | The outage request | The existence of the draft notice | The fact that the requested window is 18:00-19:00 | The wording reception lighting only in the request | Facilities has not approved the proposed outage arrangement.''',
    vocabulary='''outage request | Proposal for an interruption of a defined service. | submit an outage request
proposed window | Suggested period not yet approved or confirmed. | state the proposed window
reception lighting | Lighting serving the reception area. | identify the reception-lighting scope
affected service | Particular function covered by the proposed interruption. | name the affected service
impact scope | Extent of the service or area affected as described. | correct the impact scope
tenant notice | Communication informing occupants of a relevant building arrangement. | review the tenant notice
draft notice | Preliminary communication not yet treated as final. | correct the draft notice
facilities approval | Acceptance through the responsible facilities process. | await facilities approval
approval status | Whether a proposal is accepted, pending, or rejected. | state the approval status
confirmed window | Time period explicitly agreed through the relevant process. | distinguish a confirmed window
planned interruption | Intended break in service delivery. | describe the planned interruption
isolation | Separation from relevant energy sources through the applicable authorized process. | distinguish isolation from a planned outage
isolation status | Verified state under the applicable electrical procedure. | avoid inferring isolation status
operational instruction | Direction to perform an equipment or system action. | distinguish a notice from an operational instruction
notice correction | Amendment of inaccurate communication. | make a notice correction
whole-floor impact | Claim that an entire floor is affected. | avoid an unsupported whole-floor impact
service boundary | Limit of the functions included in the request. | preserve the service boundary
time range | Stated beginning and end of a period. | confirm the time range
pending approval | Awaiting a decision rather than accepted. | mark the request pending approval
communication release | Authorization or controlled action to issue a notice. | confirm the communication release
scope readback | Repetition of the exact extent of a proposal. | give a scope readback
status qualifier | Wording showing the level of certainty or approval. | preserve the status qualifier
authorization | Permission for a specified action through the relevant process. | distinguish authorization from discussion
revision record | Note showing how a communication or document changed. | maintain a revision record''',
    precision='The proposal is 18:00-19:00 for reception lighting only. Facilities approval is pending. The notice wrongly expands the scope to the whole floor. Correct both the affected service and the unapproved status; do not call the request a confirmed outage.',
    precision_extra='No isolation status is given. An outage request, even if later approved, is not proof of safe electrical status. The exercise concerns accurate communication, not switching, testing, isolation, restoration, or instructions for staff to operate equipment.',
    phrases='''State the proposal | The request proposes 18:00-19:00.\nName the exact service | The scope is reception lighting only.\nState the approval limit | Facilities has not approved the request.\nFlag the wording error | The draft notice incorrectly says the whole floor will be unavailable.\nCorrect the scope | Replace that impact claim with reception lighting only.\nCorrect the certainty | Keep the window labeled proposed, not confirmed.\nSeparate two checks | We need accurate scope and accurate approval status.\nAvoid an all-services claim | The request does not include every service on the floor.\nPreserve the time range | The proposed start is 18:00 and the proposed end is 19:00.\nAvoid a safety inference | The request gives no verified isolation status.\nSeparate planning and operation | A notice is not an electrical operating instruction.\nAvoid premature release | This discussion does not authorize issuing a final notice.\nUse a status qualifier | Proposed window, pending facilities approval.\nRead back the correction | Reception lighting only, 18:00-19:00, approval pending.\nPreserve the review route | The corrected wording still needs the relevant review and release process.\nClose with the unresolved status | No confirmed outage or operational clearance is established here.''',
    notes='''Proposes | Marks an arrangement as requested rather than accepted.\nOnly | Limits the service scope to reception lighting.\nWill be unavailable | Can incorrectly present a proposal as a definite future event.\nPending | Indicates no approval decision has yet been supplied.\nNotice versus instruction | Occupant information does not direct electrical operations.\nNo status supplied | Prevents assumptions about energization or isolation from planning paperwork.''',
    d='''Which wording preserves scope and status? | Proposed reception-lighting interruption, 18:00-19:00, pending facilities approval. | Whole floor confirmed unavailable all evening. | Reception lighting safely isolated now. | All services approved for shutdown. | The wording retains the limited service, proposed window, and pending approval without an operational claim.
Why is changing whole floor alone insufficient? | The notice must also stop presenting the unapproved window as confirmed. | The time range must be invented again. | Every service must be added instead. | A corrected area automatically verifies isolation. | Accurate area wording does not fix an inaccurate claim of approval or certainty.
What does the request establish about isolation? | No verified isolation status is supplied | All equipment is safe to work on | Reception lighting is already isolated | The floor has been tested | Planning information supplies no verified electrical status or safety clearance.
What is the purpose of this review? | Correct the communication and preserve the unresolved approval | Instruct tenants to operate equipment | Authorize switching without the actual procedure | Announce restoration already complete | The task is a communication review, not authorization or instructions for electrical operation.''',
    dialogue='''Joel | The draft tenant notice says the whole floor will be unavailable from 18:00 to 19:00. Is that the scope you put in the outage request?
Imani | No. The [[affected service::Affected service is reception lighting only; the request does not cover every service or the whole floor.]] is reception lighting only. The notice has expanded the impact beyond the request, and that needs to be corrected.
Joel | I will change the area description. Can the notice then say the reception lighting will be unavailable during that hour, or is there another status issue?
Imani | There is another issue: [[facilities approval::Facilities approval has not been given, so the proposed window cannot be presented as a confirmed outage.]] has not been given. The window is proposed, not confirmed, so the wording must preserve that as well.
Joel | Then we have two errors to avoid: an impact that is too broad and a definite statement about a window that has not been accepted.
Imani | Exactly. Correcting the [[impact scope::Impact scope limits the proposal to reception lighting, but correcting it does not resolve the separate pending-approval issue.]] alone would not make the notice accurate. It also needs to describe the pending approval rather than promise an outage.
Joel | Please confirm the requested times. I want to preserve the actual proposal while changing the inaccurate wording, not introduce a different window by mistake.
Imani | The [[proposed window::Proposed window is 18:00-19:00, with neither endpoint constituting a confirmed operational arrangement.]] is 18:00-19:00. Both times belong to the request, and neither should be treated as a confirmed operational arrangement in this review.
Joel | Could the notice simply say proposed reception-lighting interruption, pending facilities approval? That would make its present status visible to whoever reviews the wording next.
Imani | Yes, that [[status qualifier::Status qualifier makes the proposal and pending approval explicit, preventing the wording from implying a settled arrangement.]] preserves the distinction. Include the proposed time range and keep reception lighting only attached to it, rather than saying all services.
Joel | Does an outage request tell us anything about isolation? I do not want the notice to imply that the lighting has already been made safe for work.
Imani | No [[isolation status::Isolation status is not supplied by the request or this conversation, so no de-energization or safety conclusion can be inferred.]] is supplied. Planning paperwork is not proof that equipment is de-energized or safe, and the notice should not make that claim.
Joel | Understood. We are correcting information about a proposal, not giving tenants or the site team instructions to switch, test, or restore anything.
Imani | Correct. This is a [[notice correction::Notice correction amends scope and certainty in the communication; it does not direct an electrical operation.]], not an operating procedure. No electrical action is authorized by the revised sentence or by our discussion.
Joel | What should the record say about issuing the notice? I do not want a wording review to be taken as permission to release a final confirmed message.
Imani | Keep [[communication release::Communication release remains subject to the actual review process; correcting a draft does not authorize issuing a final notice.]] separate. The corrected wording still needs the relevant review and release process, and facilities approval of the outage remains pending.
Joel | Please give me a final readback that I can compare with the request. It should include the exact service, the hour, and the missing approval.
Imani | The [[scope readback::Scope readback preserves reception lighting only, the proposed 18:00-19:00 window, and pending facilities approval together.]] is: reception lighting only; proposed window 18:00-19:00; facilities approval pending. No whole-floor impact or verified isolation status is established.
Joel | That is clear. I will preserve those facts in the review record and remove the unsupported whole-floor statement without presenting the proposal as confirmed.
Imani | Thank you. The [[authorization::Authorization for the outage or electrical operation is not created by this notice review; the actual approval processes still apply.]] status remains unchanged by this wording discussion. We have identified the corrections, not approved the outage or established operational clearance.''',
    transfer_title='Correct scope and certainty',
    transfer_setup='Complete the notice-review exchange. Retain the exact service and proposed time range, while making the approval limit explicit.',
    transfer='''Coordinator: "The request covers reception ___ only." | lighting | Lighting is the specified reception service, not every service on the floor.
Electrician: "The proposed window starts at ___." | 18:00 | Eighteen hundred is the proposed start, not a confirmed switching instruction.
Coordinator: "It ends at ___." | 19:00 | Nineteen hundred is the proposed endpoint in the request.
Electrician: "Facilities approval is still ___." | pending | Facilities has not approved the proposal, so it remains pending.''',
))

BOOK['units'].append(unit(
    title='Reporting findings and uncertainty',
    scene='Not seen today is not fault-free',
    skill='Distinguish a reported intermittent symptom from a limited visit observation and avoid turning a pending report into an unsupported assurance.',
    brief='Client Mira reported occasional flickering in display bay 2. Electrician Ellis has a visit note stating that flickering was not observed during the visit. No cause is established, and the technical report is pending review. Mira asks whether the installation is now fault-free. Ellis must explain the limited finding without dismissing the earlier report, inventing a repair, or asserting that the installation is safe or free of defects.',
    cast='Mira | Client\nEllis | Electrician',
    culture=('Acknowledge both accounts without forcing them to agree', 'An intermittent symptom may be absent during a visit. The client report and the visit observation can therefore coexist. Explain the observation period and the unresolved cause, rather than treating the client as mistaken or upgrading limited evidence into complete reassurance.'),
    a='''What did Mira report? | Occasional flickering in display bay 2 | A verified cause already identified | Flickering in every area at all times | A completed repair | Mira reports an occasional symptom in a specific display bay.
What does the visit note state? | Flickering was not observed during the visit | The installation is fault-free | The client report was false | A component was replaced successfully | The note describes what was not observed during that visit, not a diagnosis or repair.
What is the report status? | Pending review, with no cause established | Final and approved as defect-free | Withdrawn because the client was wrong | Proof of operational clearance | The technical report is still awaiting review and no cause has been established.''',
    vocabulary='''flickering | Visible variation in light output perceived as fluctuating light. | report occasional flickering
intermittent symptom | Problem that appears at intervals rather than continuously. | describe an intermittent symptom
display bay | Defined display area within a premises. | identify display bay 2
visit note | Record of information from a particular attendance. | quote the visit note
observation period | Time during which a condition was observed or monitored. | define the observation period
not observed | Wording stating that a condition was not seen during the specified period. | preserve not-observed wording
reported history | Earlier account of events or symptoms. | retain the reported history
technical report | Document recording the relevant professional information and findings. | submit the technical report
pending review | Awaiting examination or approval through the relevant process. | state pending-review status
established cause | Explanation supported by the relevant assessment. | distinguish an established cause
fault-free claim | Assertion that no faults are present. | avoid an unsupported fault-free claim
evidence limit | Boundary of what the available information supports. | explain the evidence limit
repeat occurrence | Another instance of a previously reported symptom. | record a repeat occurrence
observation finding | Statement about what was seen during an examination or visit. | report the observation finding
diagnostic conclusion | Conclusion identifying a technical problem or its cause. | distinguish a diagnostic conclusion
repair record | Documentation of work actually carried out to correct an issue. | verify the repair record
defect | Condition that fails an applicable requirement or expected function. | assess a reported defect
operational clearance | Authorization or verified status for use under the actual process. | avoid inferring operational clearance
qualified statement | Claim limited to the scope supported by the evidence. | give a qualified statement
absence of evidence | Lack of a finding, not automatically proof that a condition is absent. | explain absence of evidence
symptom frequency | How often the reported condition occurs. | clarify symptom frequency
review outcome | Result of the relevant report assessment. | await the review outcome
case status | Current stage of the reported issue and its follow-up. | report the case status
unsupported reassurance | Comforting claim not established by the available evidence. | avoid unsupported reassurance''',
    precision='Mira reported occasional flickering, while the visit note says none was observed during that attendance. Those statements do not contradict each other. The note does not prove that the symptom never occurs, that a cause has been identified, or that a repair has been completed.',
    precision_extra='No cause is established, and technical-report review is pending. Keep fault-free and safe-to-use claims out of the summary unless the actual authorized process establishes them. This language exercise gives no diagnostic procedure, testing instruction, or operational clearance.',
    phrases='''Acknowledge the history | You reported occasional flickering in display bay 2.\nQuote the limited finding | Flickering was not observed during the visit.\nKeep the time boundary | That statement applies to the visit observation period.\nExplain coexistence | An occasional symptom may not appear during every visit.\nAvoid dismissing the client | The note does not show that your earlier report was wrong.\nKeep cause open | No cause has been established.\nKeep report status open | The technical report is pending review.\nReject an overbroad conclusion | I cannot turn that note into a fault-free claim.\nAvoid inventing work | No completed repair is established by this information.\nSeparate finding and diagnosis | Not observed is an observation statement, not a diagnosis.\nAvoid a safety inference | The note does not establish operational clearance.\nPreserve the location | The reported symptom concerns display bay 2.\nUse qualified wording | No flickering observed during this visit; cause unresolved.\nAvoid an exact frequency claim | Occasional does not provide a precise interval.\nRead back the status | Your report remains recorded, the visit observation is limited, and review is pending.\nClose without false certainty | I can explain the record, but I cannot promise the issue is absent.''',
    notes='''Occasional | Indicates intermittent occurrence without specifying a precise frequency.\nDuring the visit | Limits the observation to a particular attendance period.\nNot observed versus absent | A missing observation does not prove the condition never occurs.\nPending review | A report stage, not a completed technical conclusion.\nNow fault-free | A stronger claim than the supplied visit note supports.\nEstablished | Requires supporting assessment, not a plausible guess.''',
    d='''Which explanation reconciles the two accounts? | Occasional flickering may not appear during a particular visit. | The client must have invented the issue. | No observation proves a successful repair. | Every intermittent symptom is harmless. | The reported intermittent history can coexist with no flickering observed during one attendance.
Which summary is supported? | No flickering observed during the visit; cause unestablished; report review pending. | Installation now guaranteed fault-free. | Driver failure confirmed and repaired. | All areas cleared for unrestricted use. | The summary preserves the actual observation, unresolved cause, and report stage.
Which statement invents a repair? | The issue is fixed because it did not flicker while we were there. | The visit note records no observed flickering. | The client reported an occasional symptom. | The technical report awaits review. | No repair or verified correction is supplied, so symptom absence during the visit cannot prove a fix.
What should remain in the record? | Both Mira's reported history and the limited visit observation | Only a declaration that the client was mistaken | A guessed cause presented as fact | A universal fault-free certificate | Keeping both accounts preserves the history and the actual limits of the visit evidence.''',
    dialogue='''Mira | Your visit note says no flickering was observed. Does that mean the installation is fault-free now, and I can tell our manager the issue is finished?
Ellis | The note records the [[observation period::Observation period limits the finding to the visit, not every time the installation has operated.]] of that visit. It does not establish a fault-free installation, and no cause has been identified in the information we have.
Mira | I reported it because the lights flicker occasionally in display bay 2, not because they do it continuously. I would not expect it every minute.
Ellis | That is an [[intermittent symptom::Intermittent symptom describes occasional flickering, which may not appear during a particular attendance.]], so your report and the visit note can both be accurate. Not seeing it during one attendance does not invalidate what you previously reported.
Mira | Thank you. I was concerned that the wording might be taken to mean I had described the wrong area or imagined the problem.
Ellis | I will retain the [[reported history::Reported history preserves Mira's earlier account instead of replacing it with a claim that she was mistaken.]] of occasional flickering in display bay 2. The note does not establish that your account was wrong or that every other area was assessed.
Mira | Has the visit established a likely component or cause? I would rather distinguish a possibility from something the technical team has actually concluded.
Ellis | There is no [[established cause::Established cause is absent; the supplied information does not support naming a failed component or a diagnosis.]]. I should not name a component or give you a diagnosis when the report has not established one.
Mira | And is the technical report final, or does someone still need to review it before its conclusions are communicated as accepted findings?
Ellis | It is [[pending review::Pending review describes the current report stage and does not imply an approved technical conclusion.]]. That status matters. I can explain the visit note, but I should not present the report as finalized or approved.
Mira | Then I should not say a repair has fixed the problem either. There is nothing in this information telling me a corrective repair was completed.
Ellis | Correct. No [[repair record::Repair record confirming completed corrective work is not supplied; absence of observed flickering is not proof of repair.]] is established here. The absence of flickering during the visit does not prove a repair happened or that a correction has been verified.
Mira | What wording would accurately describe the position to our manager? I need a short summary that does not either dismiss the issue or exaggerate the findings.
Ellis | Use a [[qualified statement::Qualified statement limits the summary to the actual visit observation, unresolved cause, and pending report review.]]: occasional flickering reported in display bay 2; none observed during the visit; cause not established; technical report awaiting review.
Mira | That makes the difference clear. It preserves the earlier report without claiming the electrician saw the flickering or found a particular explanation.
Ellis | Exactly. The [[evidence limit::Evidence limit prevents a visit-specific observation from becoming a universal fault-free assurance or a technical diagnosis.]] is important. We can state what was observed, and what was not, without adding a universal assurance about the installation.
Mira | Could someone read that summary as permission to use or work on equipment? I want to avoid wording that sounds like a safety clearance.
Ellis | It gives no [[operational clearance::Operational clearance is not established by the visit note or language summary; the actual authorized process still governs use and work.]]. This conversation and the note do not authorize an electrical action or establish safe status. The actual authorized process governs those questions.
Mira | Understood. I will say that review is pending and the cause remains unresolved, rather than announce that the installation is now fault-free or repaired.
Ellis | That preserves the [[case status::Case status remains unresolved with review pending; the client report and limited observation both stay in the record.]]. Your report stays recorded alongside the limited visit observation. We have clarified the information, not closed the issue with a diagnosis or a repair claim.''',
    transfer_title='Keep the observation within its limits',
    transfer_setup='Complete the client summary. Retain the intermittent history, the visit-specific observation, the unknown cause, and pending review.',
    transfer='''Client: "I reported occasional ___ in display bay 2." | flickering | Flickering is the reported intermittent symptom in the specified display area.
Electrician: "It was not ___ during the visit." | observed | Not observed limits the finding to that visit rather than proving permanent absence.
Client: "No cause is ___." | established | No assessment result in the case identifies the cause.
Electrician: "The technical report is pending ___." | review | Review remains pending, so the report is not presented as finalized.''',
))

BOOK['units'].append(unit(
    title='Assessing added equipment and substitutions',
    scene='A second machine changes the question',
    skill='Request missing equipment information and explain the need for revised assessment and quotation without confirming capacity, price, or timing.',
    brief='After electrical scope is agreed for a café, owner Hana adds a second espresso machine and asks electrician Luis to include it at the original price and completion date. Equipment data for the added machine are unavailable. Luis can request the data and arrange a revised assessment and quotation. Electrical capacity and installation requirements are not established. The discussion must not assume the new machine matches the first, fits the existing provision, or can be added without cost or schedule effects.',
    cast='Hana | Café owner\nLuis | Electrician',
    culture=('Treat an added appliance as a defined change request', 'A client may see an extra machine as a simple addition to a familiar plan. Explain which information is missing and how it affects the assessment route. Preserve the commercial request without accepting it or inventing the technical answer.'),
    a='''What changed after scope agreement? | A second espresso machine was added | The original scope was already defined for two machines | A completed capacity assessment approved the addition | The second machine was removed | Hana adds the second machine after the electrical scope has been agreed.
What information is missing? | Equipment data for the added machine | The fact that Hana wants the original price | The fact that timing matters | The existence of the extra request | The case states that the additional machine's equipment data are unavailable.
What can Luis offer? | Request data and arrange revised assessment and quotation | Guarantee unchanged price and completion | Confirm spare capacity from the machine name | Authorize immediate connection | The supported route is data collection and revised review, not technical or commercial approval.''',
    vocabulary='''equipment data | Product-specific technical information needed for assessment. | request the equipment data
espresso machine | Coffee-making equipment forming the added request in this case. | identify the second espresso machine
additional load | Extra electrical demand associated with added equipment. | assess the additional load
rated input | Manufacturer-stated input requirement under specified conditions. | confirm the rated input
nameplate | Product marking showing identification and relevant ratings. | obtain recorded nameplate information
manufacturer specification | Technical requirements or attributes supplied by the manufacturer. | review the manufacturer specification
supply requirement | Electrical supply characteristics required by the equipment. | establish the supply requirement
capacity assessment | Evaluation of whether the relevant provision can meet the proposed demand. | arrange a capacity assessment
existing provision | Electrical arrangement already included or available for the project. | review the existing provision
installation requirement | Condition or detail needed for the specified installation. | establish installation requirements
revised assessment | Updated review accounting for changed information or scope. | request a revised assessment
revised quotation | Updated price proposal for the changed defined work. | prepare a revised quotation
original scope | Work included before the new request. | preserve the original scope
scope addition | Extra item proposed after the agreed scope. | record the scope addition
commercial request | Client request about price, timing, or other business terms. | separate the commercial request
price commitment | Agreed promise about cost. | avoid an unsupported price commitment
schedule impact | Effect of a change on timing. | assess the schedule impact
technical suitability | Whether the proposed arrangement meets relevant technical needs. | verify technical suitability
product substitution | Replacement of a specified item with a different product. | review a product substitution
like-for-like claim | Assertion that a replacement or addition has equivalent relevant characteristics. | verify a like-for-like claim
data gap | Missing information necessary for a review. | identify the data gap
approval boundary | Limit of what has actually been authorized. | preserve the approval boundary
change request | Proposal to alter the agreed work or requirements. | submit a change request
assessment outcome | Result reached after the required review. | await the assessment outcome''',
    precision='The second machine is a scope addition, not an already assessed part of the original work. Equipment data are missing, so capacity and installation requirements remain unknown. The machine category alone does not establish that it matches the first unit.',
    precision_extra='Hana requests the original price and completion date, but Luis has not accepted those terms for the addition. Request the relevant data through the actual process and arrange revised assessment and quotation. Do not ask the client to test, connect, or operate equipment.',
    phrases='''Acknowledge the addition | You want to add a second espresso machine.\nName the scope change | That machine was added after the electrical scope was agreed.\nIdentify the missing information | We do not have the equipment data for the added unit.\nRequest the data | Please provide the relevant product information through the usual project process.\nAvoid assuming equivalence | I cannot assume it has the same requirements as the first machine.\nKeep capacity open | Available capacity has not been established for the addition.\nKeep installation open | The installation requirements still need assessment.\nOffer the review route | I can arrange a revised assessment and quotation.\nPreserve the price request | I understand you want to keep the original price.\nAvoid accepting the price | I cannot confirm unchanged cost for the added machine.\nPreserve the timing request | I understand the original completion date matters to you.\nAvoid accepting the date | I cannot promise the same date before the change is assessed.\nSeparate two decisions | Technical suitability and commercial terms both remain open.\nAvoid operational instructions | This information request does not authorize connection or testing.\nRead back the change | Second machine requested; data missing; capacity, requirements, price, and timing unresolved.\nClose with the next step | We need the data for the revised assessment and quotation.''',
    notes='''Added after | Establishes why the extra machine is outside the already agreed scope.\nSame kind of machine | Does not establish identical ratings or requirements.\nRequest versus commitment | Asking for the original price or date does not mean those terms are accepted.\nRevised | Indicates that the review must account for changed scope.\nNot established | Leaves the answer open rather than predicting failure or approval.\nBoth remain open | Keeps technical assessment and commercial agreement distinct.''',
    d='''Which response preserves the facts? | We need the added machine's data for revised assessment and quotation before confirming terms. | The same appliance name proves spare capacity. | The original price automatically includes any extra machine. | The completion date is guaranteed unchanged. | Missing data and changed scope require review before technical or commercial commitments can be established.
Which assumption is unsupported? | The second machine has the same requirements as the first. | A second machine has been requested. | Equipment data are unavailable. | Revised assessment can be arranged. | No product-specific information establishes equivalence between the two machines.
What is the status of unchanged price and date? | Requested by Hana but not committed by Luis | Already accepted for the extra work | Technically proven by the machine category | Irrelevant because extra work is always free | Hana's commercial preference remains a request while the additional work is unassessed.
What should the next handoff contain? | Added machine, missing data, requested terms, and need for revised assessment and quotation | A guessed load rating and connection instruction | A completed capacity approval | An invented revised price | The handoff preserves the actual change and unresolved questions without technical or commercial invention.''',
    dialogue='''Hana | We are adding a second espresso machine to the café. Can you include it in the electrical work at the original price and still finish on the agreed date?
Luis | I understand the request, but it is a [[scope addition::Scope addition identifies the second machine as new work introduced after the original electrical agreement.]]. The second machine was added after we agreed the electrical scope, and its equipment data are not available yet.
Hana | It is another espresso machine, so I assumed the requirements would be similar to the first. Is the type of machine enough information for an initial decision?
Luis | The category does not establish the [[supply requirement::Supply requirement depends on the specific equipment information, not simply on both appliances being called espresso machines.]]. I cannot assume the added unit has the same relevant characteristics or that the existing provision is suitable.
Hana | What information do you need from the project team? I want to give you the right documents rather than ask someone to guess from a product description.
Luis | We need the relevant [[equipment data::Equipment data are the missing product-specific information required for the revised review, not guessed ratings or client testing.]] for the added unit through the usual project process. This is an information request, not a request for you to test or connect anything.
Hana | Understood. Once the information is available, is the next question whether the existing electrical arrangement can support the additional equipment?
Luis | A [[capacity assessment::Capacity assessment remains necessary for the addition; the conversation does not establish available capacity or a suitable arrangement.]] forms part of the revised review. At present, capacity and installation requirements are not established, so I cannot give a yes-or-no technical approval.
Hana | I am also trying to control costs. I would like the original figure to remain the same, but I understand that is a request from me, not a quote.
Luis | Correct. There is no unchanged [[price commitment::Price commitment for the extra machine has not been made; Hana's wish to retain the original price remains a request.]] for the addition. We can preserve your preference without recording it as something we have already accepted.
Hana | The original completion date matters because we have other work coordinated around it. Please include that constraint when the added machine is reviewed.
Luis | I will include it, but the [[schedule impact::Schedule impact of the added equipment remains unassessed, so the original completion date cannot be guaranteed for the change.]] remains open. I cannot promise the same completion date for changed work before the requirements and arrangements have been assessed.
Hana | Then the review needs to address both the technical information and the commercial terms. A technical answer alone would not tell me the final price or timing.
Luis | Exactly. I can arrange a [[revised quotation::Revised quotation will address defined changed work after the necessary review; no new or unchanged price is established now.]] alongside the revised assessment process. Neither the technical outcome nor the commercial terms has been settled in this discussion.
Hana | Please do not call the new machine a like-for-like addition in the note. We have not checked that, and the phrase might make the change sound already accepted.
Luis | I will avoid that [[like-for-like claim::Like-for-like claim is unsupported because the added machine's relevant data have not been supplied or compared.]]. The note will identify a second machine with missing data, not an equivalent unit whose requirements we already know.
Hana | What should I tell the project coordinator today? I need a clear next step without making it sound as though you have rejected the idea outright.
Luis | Say the [[change request::Change request remains open for data collection and revised review, rather than being automatically accepted or rejected.]] needs product information, revised assessment, and quotation. Capacity, installation requirements, cost, and completion timing are still to be established.
Hana | That is fair. I will ask the team for the relevant documents and keep my request about the original price and date separate from any agreement.
Luis | Thank you. The [[approval boundary::Approval boundary keeps the added machine unapproved until the relevant technical and commercial process establishes what is acceptable.]] remains clear: this conversation records the request and the next review steps, not approval to add equipment or a promise of unchanged terms.''',
    transfer_title='Request data before confirming terms',
    transfer_setup='Complete the café update. Keep the missing information, changed scope, review route, and unresolved commercial terms visible.',
    transfer='''Owner: "The second machine was added after scope ___." | agreement | The timing makes the second machine a new scope request.
Electrician: "Its equipment ___ are not available." | data | Product-specific data are missing and needed for the revised review.
Owner: "We need revised assessment and a ___." | quotation | The added work needs pricing through a revised quotation process.
Electrician: "Capacity, price, and timing are not yet ___." | established | None of these outcomes has been determined for the unassessed addition.''',
))

BOOK['units'].append(unit(
    title='Handing over electrical records',
    scene='An old room name needs verification',
    skill='Confirm document receipt, record an identification discrepancy, and assign a dated follow-up without relabeling or implying operational clearance.',
    brief='At an office handover, facilities contact Ben receives the as-built drawings from electrical lead Priya. One circuit-directory entry still says old store, although the room is now called archive. The associated circuit identification needs verification; the room-name change does not justify relabeling by assumption. Priya accepts follow-up and will report Thursday. No operational clearance is inferred from the handover, and no verification result or corrected entry is supplied.',
    cast='Ben | Facilities contact\nPriya | Electrical lead',
    culture=('Document receipt is not verification of every detail', 'A handover may contain received records and a remaining identification question. Acknowledge the documents, preserve the exact discrepancy, and name the owner and reporting date. Do not let a familiar room name substitute for verification of the electrical identification.'),
    a='''What has Ben received? | The as-built drawings | A verified corrected directory entry | A new operational clearance | A completed circuit-identification result | The as-built drawings are received, while the directory question remains unresolved.
What discrepancy remains? | The directory says old store while the room is now archive | The drawings were never delivered | Every circuit is verified incorrect | A corrected entry has already been approved | The mismatch concerns the old directory wording and the current room name.
What does Priya accept? | Follow-up and a Thursday report, without an invented verification outcome | Immediate relabeling based on the name alone | Guaranteed operational clearance Thursday | A completed correction already recorded | Priya owns the follow-up and report, but no verified identification or correction is established.''',
    vocabulary='''as-built drawing | Record drawing intended to represent the installed arrangement, subject to its actual verification status. | receive the as-built drawings
document handover | Transfer of project records to the receiving party. | complete the document handover
circuit directory | List intended to identify circuits and the areas or equipment they serve. | verify the circuit directory
room designation | Name or identifier assigned to a room. | confirm the current room designation
legacy label | Older wording retained in a current record or label. | identify a legacy label
identification discrepancy | Mismatch or uncertainty in how an item or circuit is identified. | record an identification discrepancy
verification task | Defined check needed to establish the relevant information. | assign the verification task
relabeling | Changing identification wording on a label or record. | avoid relabeling by assumption
record correction | Amendment based on verified information and the actual process. | arrange a record correction
document receipt | Confirmation that records have been supplied to the recipient. | acknowledge document receipt
follow-up owner | Person responsible for the next action on an open item. | name the follow-up owner
reporting date | Day committed for an update or report. | confirm the reporting date
verification outcome | Result of the relevant identification check. | await the verification outcome
operational clearance | Authorization or verified status for use under the actual process. | distinguish operational clearance
handover exception | Open item retained when other handover elements are complete. | list a handover exception
record accuracy | Correctness of the information contained in a document or label. | verify record accuracy
installed arrangement | Actual configuration of the relevant equipment or system. | distinguish the installed arrangement
document title | Name describing a record, not proof of every entry's accuracy. | distinguish document title from verification
location name | Words identifying a space. | preserve the current location name
circuit identity | Verified correspondence between a circuit and what it serves. | establish circuit identity
update commitment | Promise to provide further information at a stated time. | make an update commitment
open-item record | List or note preserving unresolved matters. | maintain the open-item record
approved amendment | Change accepted through the applicable process. | confirm an approved amendment
handover readback | Repetition of received records and unresolved items to confirm understanding. | give a handover readback''',
    precision='The room is now called archive, and the directory entry says old store. That wording difference does not verify which circuit serves the room. Priya must follow up through the appropriate process; no relabeling is authorized simply by matching room names.',
    precision_extra='The as-built drawings are received, but their receipt does not close the identification question or establish operational clearance. Thursday is the committed reporting date, not a guaranteed verification outcome, correction date, or authorization to operate equipment.',
    phrases='''Acknowledge the records | You have received the as-built drawings.\nName the remaining issue | One circuit-directory entry still says old store.\nState the current room name | The room is now called archive.\nPreserve the uncertainty | The circuit identification still needs verification.\nAvoid a naming shortcut | A room-name change does not prove the circuit identity.\nAvoid premature relabeling | We should not relabel the entry by assumption.\nAccept follow-up | I will take responsibility for the follow-up.\nName the owner | Priya owns the identification follow-up.\nState the commitment | I will report on Thursday.\nKeep the outcome open | I cannot state the verification result before it is established.\nSeparate receipt and accuracy | Receiving the drawings does not verify every directory entry.\nKeep the exception visible | The identification discrepancy remains an open handover item.\nAvoid operational inference | This handover does not establish operational clearance.\nPreserve the actual process | Any correction needs verified information and the relevant approval process.\nRead back the handover | Drawings received; old-store entry unresolved; Priya follows up and reports Thursday.\nClose with the right limit | The reporting date is committed, but no corrected identity is supplied here.''',
    notes='''As-built | A record-document description, not a reason to ignore an identified discrepancy.\nStill says | Flags older wording without proving the correct electrical identity.\nNow called | Establishes the current room name, not the circuit correspondence.\nWill report Thursday | Commits to communication, not a predetermined technical result.\nBy assumption | Describes the shortcut the dialogue must avoid.\nReceived versus verified | Receipt of records and verification of their contents are separate facts.''',
    d='''Which handover statement is accurate? | Drawings received; directory wording differs from the room name; identification needs verification. | Every circuit verified because drawings were delivered. | Archive can be substituted immediately without checking. | Operational clearance is automatic at handover. | The statement preserves document receipt and the separate unresolved identification question.
Why is immediate relabeling unsupported? | The current room name does not establish circuit identity. | The word archive can never be used. | All old labels are definitely correct. | Receiving drawings forbids any later correction. | Verification is required because matching a name does not prove the circuit correspondence.
What does Thursday identify? | Priya's committed reporting date | Guaranteed completion of a label change | Permission to operate equipment | A verified circuit identity | Priya promises to report Thursday without promising an unestablished technical outcome.
What belongs in the open-item record? | Old-store entry, current archive name, verification needed, Priya as owner, Thursday report | A guessed corrected circuit and automatic clearance | A claim that no follow-up remains | An invented completed verification | These details preserve the discrepancy, required review, responsible person, and communication commitment.''',
    dialogue='''Ben | I have received the as-built drawings. Before we close the handover discussion, one circuit-directory entry still says old store, but that room is now called archive.
Priya | I will keep that [[identification discrepancy::Identification discrepancy is the old-store directory wording against the current archive name, with circuit correspondence still unverified.]] open. The room name has changed, but the associated circuit identification still needs verification rather than a label change based on the name alone.
Ben | I was going to ask whether we could simply replace the words. I see that would assume the existing entry actually refers to the room we mean.
Priya | Exactly. The [[circuit identity::Circuit identity requires verification; the room-name change does not establish which circuit serves the archive.]] is the unresolved point. We should not treat a familiar location name as proof of the electrical correspondence.
Ben | Does receiving the as-built set mean the directory has already been checked as part of that document package? I do not want to confuse the two statuses.
Priya | [[Document receipt::Document receipt confirms the as-built drawings reached Ben, not that every directory entry or circuit identity has been verified.]] confirms that you have the drawings. It does not establish that this directory entry is verified or that the discrepancy has been resolved.
Ben | Then please retain the old wording exactly in the note, as well as the current room name. That will help the follow-up refer to the same entry.
Priya | I will record the [[legacy label::Legacy label is the exact wording old store, retained alongside archive so the specific entry can be followed up.]] as old store and the current designation as archive. The record will not silently replace one with the other as though verification were complete.
Ben | Who is taking responsibility for the follow-up? I want someone named so the item does not remain between facilities and the electrical team.
Priya | I accept it as the [[follow-up owner::Follow-up owner is Priya, who explicitly accepts responsibility for the unresolved identification issue.]]. Please record Priya against the item. That identifies who is responsible without pretending the check has already produced a result.
Ben | When will you report back? We need a communication point, even if the record still has an unresolved detail at that stage.
Priya | I will report Thursday. That is the [[reporting date::Reporting date is Thursday for Priya's update, not a guaranteed correction or a predetermined verification result.]] I am committing to, not a promise that a particular circuit identity or amendment has already been established.
Ben | Understood. I will not tell anyone the entry is corrected now or that Thursday automatically becomes an instruction to use equipment under a new identification.
Priya | Correct. No [[operational clearance::Operational clearance is not established by receiving drawings, discussing names, or assigning a reporting date.]] is inferred from this handover. The records discussion does not authorize operating equipment or relying on an unverified label.
Ben | Once the relevant information is verified, any correction can follow the actual project process. Until then, the open note needs to stay separate from completed document delivery.
Priya | Yes. A [[record correction::Record correction needs verified information and the applicable process; it is not authorized by a room-name assumption.]] should reflect verified information and the relevant approval process. It should not be a guessed amendment made just to make the wording look current.
Ben | Could you read back the whole handover status? I want to make sure the received drawings, the remaining entry, and your commitment are all visible.
Priya | The [[handover readback::Handover readback combines received drawings, the unresolved label discrepancy, Priya's ownership, and the Thursday report without adding clearance.]] is: as-built drawings received; old-store entry differs from current archive designation; identification needs verification; Priya owns follow-up and will report Thursday.
Ben | That is accurate. We can acknowledge the documents without closing the identification question, and the reporting commitment gives us a clear next contact point.
Priya | I will retain the [[handover exception::Handover exception keeps the unverified directory entry open while allowing receipt of the drawings to be acknowledged separately.]] until the actual outcome supports closure. No corrected circuit identity, relabeling approval, or operational status is established by this conversation.''',
    transfer_title='Separate receipt from verification',
    transfer_setup='Complete the handover record. Retain the current and old names, the verification need, the owner, and the committed report date.',
    transfer='''Facilities: "The room is now called ___." | archive | Archive is the current room designation, not a verified circuit identity.
Lead: "The old-store entry needs ___ before any assumed correction." | verification | The identification must be checked rather than changed from the name alone.
Facilities: "___ owns the follow-up." | Priya | Priya explicitly accepts responsibility for the unresolved identification item.
Lead: "I will report ___; no operational clearance is inferred." | Thursday | Thursday is the committed reporting date, without a guaranteed technical outcome.''',
))
