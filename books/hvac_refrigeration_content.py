"""Original HVAC and Refrigeration English learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='hvac-refrigeration', title='HVAC & Refrigeration English',
    cover_label='ENGLISH FOR BUILDING COMFORT AND REFRIGERATION TEAMS',
    cover_title='HVAC &\nRefrigeration', cover_size=35,
    tagline='Clear readings. Reliable handovers.',
    audience='For heating, ventilation, air-conditioning, and refrigeration staff communicating with clients, facilities teams, and project partners.',
    map_intro='Eight conversations develop precise reporting and coordination: clarify a thermostat value, reconcile equipment labels, explain supply and return air, compare ratings, report moisture, escalate a cabinet alarm, discuss a grille move, and hand over unfinished commissioning items.',
    notes_title='Keep the reading attached to its meaning.',
    notes_intro='Technical English in this field depends on what a number measures, which component a label identifies, and what a record actually establishes. Practice explaining those distinctions to colleagues and customers.',
    field_notes=[
        ('Name the value before interpreting it', 'A thermostat setpoint is a target, not automatically the measured room temperature. Cooling capacity and electrical input can both use kilowatts but describe different quantities. Keep the quantity name and unit together.', '"The 22 degrees Celsius is the setpoint; no ambient reading has been supplied."'),
        ('Preserve component identity', 'Similar suffixes on an outdoor unit and an air handler do not prove a verified pairing. Use the project register and confirmed references rather than treating a familiar shorthand label as the whole system.', '"CU-4 and AH-4 appear in separate records; their relationship needs confirmation."'),
        ('Separate history, findings, and decisions', 'A past moisture report can coexist with a dry floor during a later visit. A cabinet display and a defrost entry do not establish food temperatures or release food for service. Name the evidence and the responsible decision route.', '"The display recorded 8 degrees Celsius; product temperatures and event duration are not supplied."'),
        ('Keep unfinished handover items visible', 'Receiving a commissioning report does not complete a deferred check. Correct documents, scheduling responsibility, and update dates need separate entries. A named document owner does not automatically own every outstanding action.', '"Nia owns document correction; responsibility for scheduling the seasonal check remains open."'),
    ],
    scope_note='The projects, products, values, and records are fictional. This book teaches English, not equipment operation, diagnosis, installation, refrigerant handling, food-safety decisions, or compliance. Follow actual training, authorization, manufacturer instructions, site procedures, and applicable requirements. No dialogue authorizes roof access, testing, adjustment, refrigerant work, food release, or a system alteration. Equipment readings and document receipt do not establish safety or overall performance.',
    sources=[
        dict(title='US Department of Energy. Weatherization Training Glossary.',
             url='https://www.energy.gov/sites/prod/files/2016/06/f32/glossary.pdf',
             note='Background terminology for air distribution, temperature, humidity, and building systems. Historical program rules and technical procedures are not taught here.', checked='1 October 2026'),
        dict(title='Carrier. Return Air Vent System.',
             url='https://www.carrier.com/us/en/residential/hvac-resources/return-air-vent/',
             note='Reference for distinguishing supply and return airflow. No airflow targets, maintenance intervals, adjustments, or product recommendations are adopted.', checked='1 October 2026'),
        dict(title='US Environmental Protection Agency. Section 608 Technician Certification.',
             url='https://www.epa.gov/section608/section-608-technician-certification',
             note='Context for professional boundaries around refrigerant work. The book does not teach certification requirements or authorize servicing.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Refrigerator Thermometers: Cold Facts about Food Safety.',
             url='https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety',
             note='Background for treating temperature information carefully. The fictional cabinet case supplies no food-release decision or substitute for site procedures.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying comfort complaints and thermostat readings',
    scene='Twenty-two is the target, not the finding',
    skill='Separate a thermostat setpoint from a measured room temperature while preserving the time and location of a comfort complaint.',
    brief='Office manager Asha tells service coordinator Ben that the meeting room is 22 degrees Celsius. The number is actually the thermostat setpoint, not a confirmed ambient-temperature reading. Staff report feeling warm there after 14:00. No cause or equipment fault has been established. Ben needs to clarify the value, keep the staff report attributed, and record the afternoon pattern. The conversation uses existing information and gives no instruction to adjust or test the equipment.',
    cast='Asha | Office manager\nBen | Service coordinator',
    culture=('Correct the number label without dismissing the people', 'A setpoint can be accurate while a comfort complaint is still meaningful. Ask what the displayed value represents before treating it as a measurement. Acknowledge the occupants and preserve their reported pattern without diagnosing a fault or prescribing a control change.'),
    a='''What does 22 degrees Celsius represent? | The thermostat setpoint | A verified ambient-temperature reading | A supply-air measurement | An outdoor temperature | The brief identifies the number as the target setting rather than a measured room condition.
When do staff report feeling warm? | After 14:00 | Only before 08:00 | Exactly at a confirmed failure time | Throughout every day without exception | The supplied pattern is an afternoon report beginning after 14:00.
What is established about the equipment? | No cause or fault has been established | The thermostat sensor has failed | The cooling capacity is inadequate | The system is confirmed fault-free | The complaint and setpoint do not establish a cause or equipment condition.''',
    vocabulary='''HVAC | Heating, ventilation, and air conditioning. | discuss the HVAC system
thermostat | Control associated with maintaining a selected temperature. | identify the thermostat
setpoint | Target value used by a control system. | distinguish the setpoint
ambient temperature | Temperature of the surrounding air at the relevant location. | record ambient temperature
temperature reading | Value reported by a temperature-measuring device. | identify the temperature reading
degrees Celsius | Temperature unit used in the supplied report. | state the value in degrees Celsius
comfort complaint | Occupant report that environmental conditions feel uncomfortable. | log a comfort complaint
occupant feedback | Account supplied by people using the space. | preserve occupant feedback
meeting room | Room used for group meetings. | identify the meeting room
afternoon pattern | Reported tendency occurring later in the day. | record the afternoon pattern
sensor | Device responding to a physical condition for measurement or control. | identify the relevant sensor
measured value | Quantity established by a measurement. | distinguish the measured value
displayed value | Number shown by a device or interface. | clarify the displayed value
target temperature | Temperature the control is intended to seek. | state the target temperature
actual condition | State present at the relevant place and time. | establish the actual condition
relative humidity | Water-vapor level relative to saturation at the same temperature. | report relative humidity
occupancy | Use of a space by people. | describe room occupancy
control schedule | Timing arrangement for control settings or operation. | review the control schedule
zone | Defined area treated as a control or service region. | identify the relevant zone
heat gain | Heat added to a space from its surroundings or internal sources. | assess heat gain
equipment fault | Established malfunction of a system component. | avoid assuming an equipment fault
reported period | Time span described in an account. | preserve the reported period
service description | Concise account used to request relevant attention. | clarify the service description
attributed report | Statement linked to the person or group who supplied it. | retain an attributed report''',
    precision='Twenty-two degrees Celsius is the setpoint in this case. It must not be relabeled as ambient temperature. The complaint concerns staff feeling warm in the meeting room after 14:00, not a verified temperature or fault.',
    precision_extra='A comfort report is useful even without a confirmed ambient reading. Retain the people, place, and afternoon pattern. Do not diagnose a sensor failure, prescribe a setting change, or claim normal performance from the target alone.',
    phrases='''Ask what the number means | Is 22 the setpoint or a measured room temperature?
Name the target | The thermostat is set to 22 degrees Celsius.
Preserve the missing reading | No confirmed ambient reading has been supplied.
Acknowledge the people | Staff report feeling warm in the meeting room.
Keep the time pattern | The reports concern the period after 14:00.
Avoid a contradiction | A target setting does not disprove a comfort complaint.
Separate the evidence | We have a setpoint and an occupant report, not a diagnosis.
Avoid assigning a failed part | No sensor fault has been established.
Ask about existing information | What does the current record identify that value as?
Keep the location | Please keep meeting room in the service description.
Use the correct unit | The value is stated in degrees Celsius.
Avoid prescribing an adjustment | This clarification does not specify a new setting.
Retain the account | I will record what the staff have reported.
Avoid inventing a measured excess | We do not have a measured temperature above the target.
Read back the distinction | Setpoint 22; staff feel warm after 14:00; ambient reading unavailable.
Close with an accurate request | I will pass on that description for the relevant assessment.''',
    notes='''Set to | Describes a target, not necessarily a measured condition.
Report feeling | Attributes a subjective experience without dismissing it.
After 14:00 | Preserves the reported period without inventing an exact onset.
Not supplied | Means information is absent from the account, not that measurement is impossible.
Does not disprove | Allows the setpoint and occupant experience to coexist.
No fault established | Avoids both a diagnosis and an unsupported fault-free assurance.''',
    d='''Which wording accurately uses the number? | The thermostat setpoint is 22 degrees Celsius | The room was measured at exactly 22 | Supply air is confirmed at 22 | The outdoor temperature caused the problem at 22 | The value identifies a target setting, not any of the proposed measurements.
Which summary preserves the complaint? | Staff feel warm in the meeting room after 14:00; ambient reading not supplied | Staff are mistaken because the setting is 22 | Every room overheats all day | A sensor fault begins at 14:00 | The summary keeps attribution, place, period, and missing measurement intact.
What should Ben avoid inferring? | A particular equipment fault | The value's unit | The reported room | The afternoon pattern | No diagnostic evidence establishes a component failure in the supplied facts.
Which question best clarifies the displayed value? | Does the record label 22 as the target or the measured room temperature? | Why is the compressor broken? | Which new setting should we choose immediately? | Can the client test the equipment now? | The bounded question identifies the value using existing information without assuming a fault.''',
    dialogue='''Asha | The meeting room is twenty-two degrees, but people still say it feels warm in the afternoon. I am not sure how to describe that to the service team.
Ben | Before I record it, is twenty-two the [[setpoint::Setpoint identifies the target setting, which must not be mistaken for a room measurement.]], or is it a separate measured room-temperature value? Those mean different things in a service request.
Asha | It is the setting on the thermostat. I do not have a separate room reading in the information I was given by the office team.
Ben | Then we should not call it the [[ambient temperature::Ambient temperature is the surrounding-air condition, for which no confirmed reading is supplied.]]. We can record the target and the staff account without treating the setting as proof of the room condition.
Asha | The complaint is specifically about the meeting room. Staff say they feel warm there after two in the afternoon, rather than making a claim about every room.
Ben | That is a useful [[afternoon pattern::Afternoon pattern preserves the reported period after 14:00 without inventing continuous discomfort or exact onset.]]. I will retain the meeting-room location and after 14:00, so the request does not become a whole-office complaint.
Asha | Will mentioning the setting make it sound as though the staff must be mistaken? I do not want their experience dismissed because of one number.
Ben | No. We can preserve the [[occupant feedback::Occupant feedback records the staff experience alongside the target rather than treating one as a contradiction.]] and clarify the number at the same time. A target does not establish what everyone in the room actually experiences.
Asha | Good. I had started to write that the sensor must be wrong. That is probably another step beyond the information we have.
Ben | It is. No [[equipment fault::Equipment fault has not been established by the setpoint or the comfort report.]] has been established. We should not name a failed sensor or another component simply to give the complaint a technical-sounding cause.
Asha | The twenty-two is in Celsius, not Fahrenheit. Please keep that in the record too, because our overseas office sometimes uses a different scale.
Ben | Certainly. I will state [[degrees Celsius::Degrees Celsius supplies the unit attached to the stated target value.]] explicitly. A number without its unit and its meaning can become misleading when the message is forwarded.
Asha | Is it enough to say no measured value was supplied, rather than suggesting nobody has ever measured the room or could measure it?
Ben | Yes. The missing [[temperature reading::Temperature reading is absent from this account; that does not assert that no measurement ever exists.]] is a limit of this information. It does not establish the history of every measurement or the condition of the equipment.
Asha | I also do not want the message to ask the occupants to change settings or try tests. We are only passing on what is already known.
Ben | Agreed. We are clarifying a [[service description::Service description communicates the known complaint without prescribing tests or a control adjustment.]], not issuing control instructions. Any assessment belongs with the relevant team and its actual procedures.
Asha | Please read the short version so I can use the same wording when the facilities manager asks what we reported.
Ben | Here is the [[attributed report::Attributed report links the comfort account to staff and keeps the target and missing reading separate.]]: staff feel warm in the meeting room after 14:00; thermostat setpoint 22 degrees Celsius; no confirmed ambient reading supplied; cause unestablished.
Asha | That is clear. It preserves the complaint, explains the twenty-two, and does not invent a temperature above the target or a failed component.
Ben | I will pass on that record. It distinguishes the [[target temperature::Target temperature is the intended control value, not proof of actual room conditions or performance.]] from the actual condition that still needs assessment, while keeping the staff's reported experience visible.''',
    transfer_title='Label the value correctly',
    transfer_setup='Complete the service report using the target, time pattern, and missing measurement. Do not add a diagnosis.',
    transfer='''Manager: "The thermostat ___ is 22 degrees Celsius." | setpoint | Setpoint correctly identifies the target rather than a measured ambient temperature.
Coordinator: "Staff feel warm after ___." | 14:00 | The time preserves the supplied afternoon complaint without inventing another period.
Manager: "No confirmed ___ reading is supplied." | ambient | Ambient identifies the actual surrounding-air measurement that is missing from the account.
Coordinator: "The cause remains ___." | unestablished | Neither the setpoint nor the report establishes a technical cause.'''
))


BOOK['units'].append(unit(
    title='Identifying equipment and linked components',
    scene='AC-4, CU-4, and AH-4 are not yet a pairing',
    skill='Reconcile conflicting equipment references using existing records and preserve an unverified relationship between components.',
    brief='A school service request calls the system AC-4. The roof plan labels an outdoor unit CU-4, while the indoor equipment register identifies air handler AH-4. Their relationship is not confirmed. Facilities manager Mira has the equipment register and discusses the request with service coordinator Owen. They need to preserve the three source references and seek confirmation through the records process. Neither person needs to access the roof or inspect equipment to clarify the existing documents.',
    cast='Mira | Facilities manager\nOwen | Service coordinator',
    culture=('Treat a familiar label as a starting point', 'Site shorthand may name a whole system while formal documents identify separate components. Similar numbering can suggest a question, but it is not proof of connection. Cite each label with its source so the next person can reconcile the records without silently merging them.'),
    a='''Which label appears in the service request? | AC-4 | CU-4 only | AH-4 only | A verified combined asset number | AC-4 is the request label, distinct from the plan and register references.
What does the register identify as AH-4? | An indoor air handler | A confirmed outdoor condenser | A roof-access permit | A room thermostat setting | The indoor equipment register explicitly identifies an air handler as AH-4.
What is unresolved? | The relationship between CU-4 and AH-4 | Whether Mira has the register | Whether the request uses AC-4 | Whether the roof plan contains CU-4 | The supplied documents do not confirm how the two components are related.''',
    vocabulary='''equipment register | Record identifying equipment and relevant asset information. | consult the equipment register
asset tag | Assigned identifier used to distinguish an equipment item. | preserve the asset tag
system reference | Label used to identify an overall system. | clarify the system reference
component reference | Label identifying a particular part of a system. | retain the component reference
air handler | Equipment that moves and may condition air in a building system. | identify the air handler
outdoor unit | Equipment assembly located outside the served interior. | identify the outdoor unit
condensing unit | Assembly associated with refrigerant compression and heat rejection in relevant systems. | verify the condensing-unit reference
indoor unit | Equipment assembly located within the building or served space. | identify the indoor unit
equipment pairing | Confirmed relationship between components intended to operate together. | verify the equipment pairing
served area | Space associated with the service from an identified system. | confirm the served area
roof plan | Drawing showing relevant roof-level features and equipment. | cite the roof plan
record source | Document or system from which information was obtained. | identify the record source
cross-reference | Link connecting corresponding entries in different records. | establish a cross-reference
label discrepancy | Difference between identifiers in related information. | record the label discrepancy
model number | Manufacturer identifier for a product design or version. | confirm the model number
serial number | Identifier distinguishing an individual manufactured unit. | record the serial number
nameplate | Manufacturer label carrying equipment identification or ratings. | use recorded nameplate information
asset hierarchy | Organized relationship between systems and their components. | clarify the asset hierarchy
service request | Record asking for attention to an identified issue or system. | reconcile the service request
records reconciliation | Process of resolving differences between documented information. | complete records reconciliation
unverified link | Relationship that has not been confirmed. | retain an unverified link
identification query | Request to clarify which equipment is meant. | raise an identification query
record custodian | Person responsible for maintaining or providing a record. | identify the record custodian
confirmed mapping | Verified correspondence between identifiers or components. | obtain confirmed mapping''',
    precision='AC-4 appears in the request, CU-4 on the roof plan, and AH-4 in the indoor register. Keep all three with their sources. A shared numeral does not confirm a component pairing or served area.',
    precision_extra='Mira already has the equipment register. The next step is records reconciliation through the responsible process, not asking someone to reach a roof or inspect a nameplate. Recorded information must still be verified in context.',
    phrases='''Quote the request | The service request calls the system AC-4.
Quote the plan | The roof plan labels an outdoor unit CU-4.
Quote the register | The indoor register identifies air handler AH-4.
Preserve source attribution | Each label should stay attached to its source.
Avoid a number shortcut | The shared four does not prove that the components are paired.
Name the unresolved link | The relationship between CU-4 and AH-4 is unverified.
Use existing records | You already have the equipment register.
Request reconciliation | We need a confirmed cross-reference between these entries.
Separate system and component | A system label may not be the identifier of one physical unit.
Avoid assumed renaming | I will not replace AC-4 with CU-4 by guesswork.
Keep the served area open | We have not confirmed the served area from these labels.
Distinguish identifiers | A model number and a serial number identify different things.
Keep the request precise | Please retain all three references in the query.
Avoid directing access | This is a document query, not a request for roof access.
Read back the gap | The records name the items but do not confirm their relationship.
Close with the needed result | We need confirmed mapping before merging the references.''',
    notes='''Labels versus connects | A label names an item; it does not establish the item's relationship to another.
Appears in | Attributes an identifier to a particular source.
May not | Warns against assuming equivalence without declaring the records wrong.
By guesswork | Identifies an unsupported substitution of one label for another.
Already have | Directs attention to available information rather than new physical access.
Before merging | Makes verification a condition of consolidating records.''',
    d='''Which summary is accurate? | Request AC-4; roof plan CU-4; register AH-4; relationship unverified | AC-4 is definitely another name for CU-4 | AH-4 and CU-4 are paired because both end in four | All three labels identify one physical item | The summary preserves the separate source labels and unresolved relationship.
What should Owen ask Mira to provide? | The relevant existing register information for reconciliation | A roof inspection performed during the call | A guessed replacement label | A test of the refrigerant circuit | The case calls for existing records, not physical access or testing.
Why is the numeral four insufficient? | Similar numbering does not establish verified component relationships | Numbers can never be used in asset labels | All outdoor units must have different numerals | AH always means the entire outdoor system | An identifier pattern is not evidence that the recorded components form a confirmed pairing.
What should remain visible until clarified? | The source of each label and the unverified link | Only the shortest label | A presumed served area | An invented nameplate reading | Keeping sources and uncertainty supports accurate reconciliation without losing original information.''',
    dialogue='''Mira | The school request says AC-4, but I have found different labels in the project documents. I do not want the service team sent with the wrong reference.
Owen | Let us keep the [[record source::Record source identifies where each label comes from instead of treating the labels as interchangeable.]] attached to each label. What does the roof plan call the outdoor item, and what does the indoor register list?
Mira | The roof plan shows CU-4 for an outdoor unit. The indoor register lists AH-4 as an air handler. The request itself just says AC-4.
Owen | Thank you. An [[air handler::Air handler is the indoor item named AH-4 in the register, not a confirmed synonym for CU-4.]] is a component reference here, while AC-4 may be a broader system label. We should not collapse those descriptions into one item.
Mira | The matching four makes me think they belong together, but I cannot find a confirmed link in the information I have in front of me.
Owen | Then the [[equipment pairing::Equipment pairing is the relationship that remains unverified despite the shared numeral.]] remains unverified. Similar numbering is a reason to ask the question, not a sufficient answer to it.
Mira | I have the equipment register available. Would it help to send the relevant entries with the roof-plan reference rather than asking someone to go up there?
Owen | Yes. Use the existing [[equipment register::Equipment register is already available to Mira and can support the document reconciliation.]] and the plan reference. This conversation is about reconciling records, not arranging roof access or directing anyone to inspect equipment.
Mira | Should I change the original request from AC-4 to CU-4 in the meantime? That would at least match one of the drawings.
Owen | No, not by assumption. Preserve the [[service request::Service request retains the original AC-4 wording while its relationship to other labels is clarified.]] wording and add the other references as unresolved identification information. Replacing it could erase the original meaning before we know what was intended.
Mira | That makes sense. A request about a whole system might otherwise become a request about only the outdoor component because I changed the label.
Owen | Exactly. We need to distinguish the [[system reference::System reference may identify the overall arrangement rather than one physical component.]] from each component identifier. The next person should see both the naming difference and the missing confirmation.
Mira | The register may also contain model and serial information. I will keep those fields separate rather than treating them as another version of the asset tag.
Owen | Good. A [[model number::Model number identifies a product design or version, unlike the individual-unit serial number.]] identifies a product design or version; a serial number distinguishes an individual unit. Those fields help only when kept with the right recorded item.
Mira | We have not confirmed which rooms these entries serve either. I should not add the meeting-room location just because it appears in another recent request.
Owen | Correct. The [[served area::Served area must be established for the identified system rather than borrowed from another request.]] needs its own confirmation. We should not fill an information gap with a location from an unrelated service record.
Mira | I will send all three labels and their sources. Can you phrase the question so it asks for the relationship rather than accusing one document of being wrong?
Owen | Please confirm the [[cross-reference::Cross-reference asks how the documented labels correspond without presuming that any one record is wrong.]] between request AC-4, outdoor unit CU-4 on the roof plan, and air handler AH-4 in the register, including their verified relationship.
Mira | That is clear. It leaves the original labels intact and gives the record owner a specific issue to resolve through the proper process.
Owen | Once we receive [[confirmed mapping::Confirmed mapping supplies verified correspondence before labels are merged or the request is relabeled.]], the service reference can be clarified accordingly. Until then, keep the three source labels and the unverified link visible in the record.''',
    transfer_title='Keep all three references',
    transfer_setup='Complete the identification exchange using the three labels and the unresolved relationship. Use existing records only.',
    transfer='''Manager: "The request says ___." | AC-4 | AC-4 is the original request label and must remain traceable.
Coordinator: "The roof plan identifies the outdoor unit as ___." | CU-4 | CU-4 belongs to the outdoor item on the roof plan.
Manager: "The register identifies the air handler as ___." | AH-4 | AH-4 is the indoor air-handler reference in the register.
Coordinator: "Their relationship remains ___." | unverified | Similar numbering does not establish a confirmed link between the recorded components.'''
))


BOOK['units'].append(unit(
    title='Explaining airflow and distribution reports',
    scene='Two ceiling openings, two functions',
    skill='Translate supply and return labels into plain language while preserving the difference between a comfort report and an airflow measurement.',
    brief='Client Tomas calls both ceiling openings air-conditioning outlets. The current drawing identifies S3 as supply air and R2 as return air. He reports discomfort below S3 but supplies no airflow measurements. Technician Leila explains the labels and records the location of the complaint. The drawing establishes the stated functions, not measured performance. No cause, balancing result, or adjustment is supplied, and the conversation must not prescribe changes to grilles or controls.',
    cast='Tomas | Client\nLeila | Technician',
    culture=('Translate the function, then return to the complaint', 'An everyday label can conceal an important functional difference. Explain the direction of airflow simply, then repeat the actual complaint. Technical vocabulary should improve the report, not overwhelm the customer or imply a diagnosis that the measurements do not support.'),
    a='''Which opening does the drawing identify as supply? | S3 | R2 | Both openings | Neither opening | The current drawing explicitly labels S3 as supply air.
Where does Tomas report discomfort? | Below S3 | Below R2 only | In every room | At an identified outdoor unit | The client names the area below S3 as the complaint location.
What is missing? | Airflow measurements | The drawing labels | The existence of two openings | The client's location description | No measured airflow data are supplied with the discomfort report.''',
    vocabulary='''supply air | Air delivered into a served space through the distribution system. | identify supply air
return air | Air drawn from a space back toward the air-handling system. | identify return air
supply grille | Grille associated with delivery of air into the space. | locate the supply grille
return grille | Grille associated with air returning from the space. | identify the return grille
diffuser | Air-distribution device designed to spread delivered air. | identify the diffuser
register | Grille assembly that may include an airflow-control damper. | distinguish the register
duct | Passage used to convey air. | identify the duct
ductwork | Network of ducts and associated components. | review the ductwork
air distribution | Delivery and movement of air within a served area. | describe air distribution
airflow rate | Volume of air passing a point per unit time. | report the airflow rate
cubic feet per minute | Volume-flow unit commonly abbreviated CFM. | state cubic feet per minute
liters per second | Volume-flow unit used for air or liquid movement. | record liters per second
air velocity | Speed of air movement at a stated position. | distinguish air velocity
volume flow | Quantity of air volume moving per unit time. | specify volume flow
draft | Air movement perceived as unwanted by an occupant. | describe a reported draft
occupied zone | Part of a room normally used by people. | identify the occupied zone
throw | Distance associated with a defined air jet under stated conditions. | review diffuser throw
spread | Lateral extent of a delivered air stream under defined conditions. | distinguish spread from throw
damper | Component used to regulate or control airflow in a system. | identify the damper
balancing | Technical adjustment and verification of distribution to meet specified requirements. | distinguish balancing from explanation
design airflow | Airflow value specified by the design. | compare design airflow
measured airflow | Airflow established through the relevant measurement. | record measured airflow
distribution report | Account describing air delivery or related comfort observations. | clarify the distribution report
performance finding | Supported conclusion about how a system functions. | distinguish a performance finding''',
    precision='S3 is labeled supply and R2 return on the current drawing. This tells the reader their stated functions. It does not establish actual flow rate, velocity, balance, or the cause of the discomfort.',
    precision_extra='The report concerns discomfort below S3. Preserve that location without changing it to a measured excess or deficit of airflow. Explanation of the labels is not an instruction to adjust a grille, damper, or control.',
    phrases='''Name the two functions | S3 is supply air; R2 is return air.
Explain supply | Supply air is delivered into the room.
Explain return | Return air goes back toward the air-handling system.
Attribute the labels | Those are the functions shown on the current drawing.
Keep the complaint location | You report discomfort below S3.
Avoid converting experience into measurement | We do not have an airflow measurement for that location.
Separate rate and speed | Airflow rate and air velocity are different quantities.
Name common units | Volume flow may be stated in cubic feet per minute or liters per second.
Avoid a balance claim | The labels do not establish that the system is balanced.
Keep cause open | The cause of the discomfort has not been established.
Clarify the everyday term | Calling both openings outlets hides their different functions.
Retain the customer's words | I will record the discomfort without inventing a measured excess.
Avoid prescribing a change | This explanation does not specify an adjustment.
Ask for the existing reference | Please keep S3 attached to the reported location.
Distinguish design from result | A design value is not automatically a measured result.
Close with a precise report | Discomfort below supply S3; airflow data not supplied; cause unresolved.''',
    notes='''Shown on the drawing | Attributes the stated function without verifying installed performance.
Into versus back toward | Gives the customer a simple directional contrast.
Below S3 | Preserves the complaint location rather than generalizing to the whole system.
Not automatically | Blocks an unsupported equivalence between design and measurement.
Reported discomfort | Records the experience without assigning a technical cause.
Does not specify | Keeps an explanation separate from an operating instruction.''',
    d='''Which explanation is accurate? | Supply delivers air into the room; return carries air back toward the system | Both openings must deliver air into the room | Return means outdoor exhaust in every system | Supply means measured excess airflow | The directional distinction explains the stated functions without changing them into performance findings.
What can the drawing labels establish here? | The stated functions of S3 and R2 | A verified airflow rate | The cause of the discomfort | The correct damper adjustment | The supplied drawing labels identify functions, not measured operating conditions.
Which report invents a measurement? | S3 delivers too many liters per second | Tomas reports discomfort below S3 | R2 is labeled return | No airflow data were supplied | No airflow measurements support a quantified excess at S3.
What is the proper scope of Leila's response? | Explain labels and preserve the complaint for assessment | Prescribe a grille adjustment | Declare the system balanced | Reject the complaint because S3 is supply | The case supports explanation and accurate reporting, not adjustment or performance conclusions.''',
    dialogue='''Tomas | I have two air-conditioning outlets in the ceiling. The one above this part of the room is uncomfortable to sit under, and the drawing calls it S3.
Leila | The drawing identifies S3 as [[supply air::Supply air is the stated delivery function of S3 on the current drawing.]]. The other opening, R2, has a different function, so calling both outlets can make the description less precise.
Tomas | What is different about R2? I had assumed that both openings did the same thing because they look like parts of the same system.
Leila | R2 is labeled [[return air::Return air describes the flow back toward the system rather than delivery into the room.]]. In plain language, supply delivers air into the room, while return carries air back toward the air-handling system.
Tomas | That helps. My complaint is below S3, the supply location, rather than below the return opening. I want the service record to identify the right place.
Leila | I will keep that location in the [[distribution report::Distribution report records the air-related complaint and its location without adding measurements.]]. The complaint is discomfort below S3; the drawing gives us its label, but it does not supply an airflow measurement.
Tomas | I have no measured figures. I was going to say too much air comes through it, but that would be my impression rather than a measured quantity.
Leila | Exactly. A [[measured airflow::Measured airflow would require relevant measurement data, which Tomas has not supplied.]] value is different from an occupant description. We can retain what you experience without inventing a numerical excess or a diagnosis.
Tomas | I have seen CFM on another report. Is that a speed, or does it describe something different about the air moving through the system?
Leila | CFM means [[cubic feet per minute::Cubic feet per minute is a volume-flow unit, not an air-speed unit.]], a unit of volume flow. It tells how much air volume moves per unit time, rather than directly stating the air speed.
Tomas | So the feeling of moving air near a seat cannot simply be relabeled as a particular CFM result, especially when we have no measurement.
Leila | Correct. [[Air velocity::Air velocity is the speed of air movement and must not be confused with volume flow.]] describes speed at a location. It is a different quantity from volume flow, and neither has been measured in the information you have given me.
Tomas | Does identifying the return opening tell us the system is balanced, or is that another conclusion the drawing cannot establish by itself?
Leila | It cannot establish [[balancing::Balancing involves technical distribution work and verification, not merely identifying supply and return labels.]]. We have identified the stated functions, not verified that the distribution meets its requirements or determined why your seat feels uncomfortable.
Tomas | Then please do not put an adjustment instruction in the record on my behalf. I am asking for the complaint to be assessed, not choosing a technical change.
Leila | Understood. I will not prescribe a [[damper::Damper is an airflow-control component; no adjustment to it is supported by this conversation.]] adjustment or a grille change. The appropriate assessment must establish what is happening before a remedy is selected.
Tomas | The distinction is clearer now: S3 supplies, R2 returns, and the concern remains the experience below S3, with no figures attached.
Leila | Yes. That preserves the [[occupied zone::Occupied zone is the area used by people, helping locate the comfort issue rather than diagnose equipment.]] concern while avoiding a performance claim. We know where you report discomfort, not a confirmed cause or measured flow problem.
Tomas | Please read the short note back so I can use the same description when I speak to our facilities manager.
Leila | Discomfort reported below supply S3; R2 labeled return on the current drawing; no airflow measurements supplied. No [[performance finding::Performance finding would require supporting evidence beyond the labels and discomfort account.]] or cause has been established. That is the account I will pass on for assessment.''',
    transfer_title='Explain supply and return',
    transfer_setup='Complete the client summary. Identify each function and keep the missing measurement visible.',
    transfer='''Technician: "S3 is labeled ___ air." | supply | Supply is the stated function assigned to S3 by the drawing.
Client: "R2 is labeled ___ air." | return | Return distinguishes R2 from the supply opening named in the complaint.
Technician: "The discomfort is reported below ___." | S3 | S3 is the specific location identified by the client.
Client: "No airflow ___ have been supplied." | measurements | The complaint includes no measured airflow data to support a performance conclusion.'''
))


BOOK['units'].append(unit(
    title='Checking equipment ratings and refrigerant references',
    scene='Five kilowatts of what?',
    skill='Compare like quantities, request missing equipment data, and distinguish refrigerant identification from approval to select or service a system.',
    brief='Client Jules compares two fictional proposals with estimator Farah. Both show 5 kilowatts, but proposal A labels the value cooling capacity while proposal B labels it electrical input. Jules calls them equal-size systems. Full data sheets and equipment pairings are not supplied, and no selection is approved. Farah must explain why the matching numbers are not enough, request complete specifications, and keep refrigerant references tied to the actual equipment without recommending handling or substitution.',
    cast='Jules | Client\nFarah | Estimator',
    culture=('Ask what a familiar number measures', 'Customers often compare the largest printed number in a proposal. Name the quantity before comparing the value. Explain what information is missing and why it matters, without turning a partial specification into a product recommendation or an efficiency claim.'),
    a='''What does proposal A's 5 kilowatts describe? | Cooling capacity | Electrical input | Stored electrical energy | A refrigerant charge | Proposal A explicitly labels the value as cooling capacity.
What does proposal B's 5 kilowatts describe? | Electrical input | Confirmed equal cooling capacity | A measured room temperature | A maintenance interval | Proposal B labels the value electrical input, which is a different quantity.
What conclusion is supported? | The numbers alone cannot establish equivalent systems | Both systems have identical capacity | Both have identical efficiency | Proposal B is approved | The matching unit and value do not make the two differently labeled quantities equivalent.''',
    vocabulary='''cooling capacity | Rate at which a system can remove heat under stated conditions. | compare cooling capacity
electrical input | Electrical power required by the equipment under stated conditions. | identify electrical input
kilowatt | Unit of power equal to one thousand watts. | state the rating in kilowatts
kilowatt-hour | Unit of energy representing one kilowatt over one hour. | distinguish a kilowatt-hour
rating condition | Defined condition under which a performance value is stated. | check the rating conditions
data sheet | Manufacturer document listing relevant product characteristics. | obtain the complete data sheet
equipment combination | Particular set of components proposed to work together. | verify the equipment combination
matched system | Component arrangement confirmed as suitable together by the relevant specifications. | identify the matched system
nominal capacity | Stated classification or approximate rating rather than every operating output. | distinguish nominal capacity
operating condition | Relevant environmental or system state during operation. | state the operating conditions
efficiency | Relationship between useful output and required input under defined conditions. | compare efficiency on a consistent basis
coefficient of performance | Ratio of useful heating or cooling output to input power on a defined basis. | interpret the coefficient of performance
refrigerant | Working fluid used to transfer heat in a refrigeration system. | identify the specified refrigerant
refrigerant designation | Identifier naming a particular refrigerant or blend. | preserve the refrigerant designation
refrigerant charge | Quantity of refrigerant specified or present in a system. | distinguish refrigerant charge
blend | Refrigerant made from more than one component substance. | identify a refrigerant blend
compatibility | Suitability of materials or components for use together. | verify compatibility
manufacturer specification | Product requirement or attribute stated by its manufacturer. | consult the manufacturer specification
technical submittal | Product information submitted for project review. | review the technical submittal
selection basis | Information and criteria supporting an equipment choice. | establish the selection basis
like-for-like comparison | Comparison of matching quantities on a consistent basis. | make a like-for-like comparison
input-output distinction | Difference between energy supplied and useful effect produced. | preserve the input-output distinction
approved selection | Equipment choice accepted through the relevant process. | confirm the approved selection
substitution review | Evaluation of a proposed replacement for a specified item. | request a substitution review''',
    precision='Both proposals state 5 kilowatts, but A describes cooling output and B electrical input. The unit can express either quantity. It does not follow that the systems have equal cooling capacities or equal efficiencies.',
    precision_extra='The complete data sheets and component pairings are missing. A refrigerant designation must stay tied to the actual equipment specification; a familiar refrigerant name does not approve a substitution, determine compatibility, or authorize servicing.',
    phrases='''Ask the key question | Five kilowatts of which quantity?
Read proposal A | A lists 5 kilowatts of cooling capacity.
Read proposal B | B lists 5 kilowatts of electrical input.
Name the distinction | Cooling output and electrical input are different.
Reject the false equivalence | Matching numbers do not establish equal-size systems here.
Ask for complete data | We need the full data sheets for both proposals.
Include the combination | The proposed component pairings also need to be identified.
Keep conditions attached | Compare ratings under the relevant stated conditions.
Avoid inventing efficiency | We cannot calculate a supported efficiency comparison from these two entries.
Distinguish power and energy | Kilowatts and kilowatt-hours are different units.
Keep refrigerant information specific | Use the refrigerant designation from the actual equipment specification.
Avoid treating a name as approval | A refrigerant reference does not approve a substitution.
Keep charge separate | Refrigerant type and refrigerant quantity are different information.
Name the review task | We need a like-for-like comparison.
State the selection limit | No equipment selection has been approved.
Close with the request | Please supply complete ratings and equipment combinations for review.''',
    notes='''Of which quantity? | Forces a value to be connected to what it describes.
Both ... but | Acknowledges the shared number while exposing the important difference.
Under stated conditions | Prevents ratings from being treated as universal operating results.
Cannot calculate from these entries | Limits a conclusion to the information actually available.
Type versus quantity | Separates refrigerant identity from charge amount.
No selection approved | Keeps information gathering distinct from a purchase or installation decision.''',
    d='''Which comparison is valid from the supplied entries? | A's value is cooling capacity; B's is electrical input | Both values prove equal cooling output | Both values prove identical energy consumption | B must be more efficient than A | Only the differently labeled quantities can be identified; performance equivalence is not established.
What additional information is needed? | Full data sheets, rating conditions, and component pairings | Only which proposal has a shorter title | An assumed refrigerant substitution | A guessed efficiency value | The missing specifications are needed to compare matching quantities and equipment combinations.
Which conclusion exceeds the evidence? | The systems have equal efficiency | A is labeled cooling capacity | B is labeled electrical input | No selection is approved | The two entries do not provide the corresponding output and input data needed for that claim.
What does a refrigerant designation provide? | Identification to be checked against the actual equipment specification | Automatic approval to substitute fluids | A complete compatibility assessment | Permission for untrained servicing | The designation identifies the fluid but does not establish compatibility or authorization.''',
    dialogue='''Jules | These two proposals both say five kilowatts. I have been calling them equal-size systems, so I thought we could compare their prices directly.
Farah | We need to read the quantity labels first. Proposal A gives [[cooling capacity::Cooling capacity identifies A's heat-removal output rating, not its electrical power input.]], while proposal B labels its five-kilowatt figure as something different.
Jules | You are right; B says electrical input. I had treated the unit as though it always described how much cooling a system could deliver.
Farah | [[Electrical input::Electrical input is the power required by the equipment, not the useful cooling output.]] describes the power required by the equipment. Cooling capacity describes heat removal under stated conditions, so the matching numbers do not establish matching performance.
Jules | Does that mean one is definitely less efficient, or are we missing the other half of the information needed for that comparison?
Farah | We are missing information. A supported [[efficiency::Efficiency comparison needs corresponding output and input information on a consistent basis.]] comparison needs corresponding output and input values on an appropriate basis, not one quantity from A and a different quantity from B.
Jules | I should ask for the full documents, then, rather than only another summary sentence saying each system is five kilowatts.
Farah | Yes. We need each complete [[data sheet::Data sheet supplies product characteristics beyond the two incomplete proposal entries.]] and the proposed component combination. The ratings also need their conditions, because a stated output is not a promise for every operating situation.
Jules | I have not been given the indoor and outdoor pairings. Would comparing a single component's sheet still leave an important gap?
Farah | It would. The [[equipment combination::Equipment combination identifies the components whose joint specifications are relevant to the proposal.]] must be clear. We should not assume that information for one item describes any indoor and outdoor units someone happens to pair with it.
Jules | There is a refrigerant name in one of the short descriptions. Can we use that to decide whether the alternative is an equivalent replacement?
Farah | A [[refrigerant designation::Refrigerant designation identifies the specified fluid but does not establish system equivalence or replacement approval.]] identifies a fluid or blend; it does not by itself prove equivalent equipment or approve a replacement. It must match the actual equipment specification.
Jules | So even a familiar refrigerant reference should not become an instruction to use another fluid or a shortcut around checking the manufacturer's information.
Farah | Correct. Any [[substitution review::Substitution review evaluates a proposed replacement and is not bypassed by a familiar refrigerant name.]] needs the relevant technical process. This comparison does not authorize refrigerant handling, servicing, or an assumed change to the specified system.
Jules | One more terminology question: if I see a quantity of refrigerant beside the name, that is not another cooling-capacity rating, is it?
Farah | No. [[Refrigerant charge::Refrigerant charge concerns the quantity of working fluid, distinct from capacity and refrigerant identity.]] refers to the quantity specified or present. Type, quantity, cooling output, and electrical input are separate information and should not be substituted for one another.
Jules | Then the next request should ask for matching rating information and the actual components, with no approved choice implied by our discussion.
Farah | Exactly. We need a [[like-for-like comparison::Like-for-like comparison uses matching quantities and conditions instead of the superficially matching five-kilowatt figures.]] before the proposals can be assessed meaningfully. The shared number has helped us find an ambiguity, not resolve the selection.
Jules | I will stop describing them as equal-size systems. I will request full data sheets, the pairings, and the conditions attached to the ratings.
Farah | Thank you. That establishes the next step toward a sound [[selection basis::Selection basis is the supporting information still needed before an equipment choice can be approved.]]. No selection is approved, and we have made no unsupported claim about equal capacity, efficiency, or refrigerant compatibility.''',
    transfer_title='Keep input and output apart',
    transfer_setup='Complete the proposal comparison. Preserve the different quantity labels and the missing approval.',
    transfer='''Client: "A gives 5 kilowatts of cooling ___." | capacity | Capacity identifies the cooling-output quantity stated in proposal A.
Estimator: "B gives 5 kilowatts of electrical ___." | input | Input identifies power required by the equipment, not cooling output.
Client: "We need complete data ___ and pairings." | sheets | Full data sheets and component pairings are missing from the supplied proposals.
Estimator: "No selection is yet ___." | approved | The comparison does not establish an accepted equipment choice or authorization.'''
))


BOOK['units'].append(unit(
    title='Reporting moisture, symptoms, and service findings',
    scene='Yesterday wet, today dry, source still unknown',
    skill='Reconcile a historical report with a later observation and avoid treating an earlier maintenance concern as a proven cause.',
    brief="Client Elena reported water near air handler AH-6 at 15:00 yesterday. Today's visit note states that the nearby floor is dry and the source was not identified. An earlier service log mentions a drain-pan concern but does not establish a link to the reported water. Coordinator Kai must preserve the chronology, distinguish each source, and summarize the unresolved issue. The exercise supplies records only; no equipment inspection or diagnostic procedure is requested.",
    cast='Elena | Client\nKai | Service coordinator',
    culture=('Keep two times visible in one account', 'A later observation need not contradict an earlier report. Use time markers and source attribution rather than choosing one account and deleting the other. A prior concern can remain relevant history without becoming the confirmed cause of a new symptom.'),
    a='''What did Elena report yesterday? | Water near AH-6 at 15:00 | A verified drain-pan failure | A completed repair | A dry floor throughout the day | Elena's account concerns observed water near AH-6 at the stated time.
What does today's visit note establish? | The nearby floor was dry and the source was not identified | The earlier report was false | The drain pan caused the water | Every component was repaired | The note records a later surface condition and an unresolved source.
What does the earlier drain-pan entry prove? | Only that a concern was recorded, not a causal link | That the pan caused yesterday's water | That the concern has been repaired | That the current system is fault-free | The historical concern is not linked to the water by the supplied evidence.''',
    vocabulary='''condensate | Liquid formed when water vapor condenses. | identify a condensate reference
drain pan | Component intended to collect relevant drainage or condensate in equipment. | record a drain-pan concern
condensate line | Pipe or tube associated with carrying condensate away. | identify the condensate line
moisture report | Account describing water or dampness at a location. | retain the moisture report
service log | Chronological record of service-related information. | consult the service log
visit note | Record of observations or actions during an attendance. | quote the visit note
historical entry | Record created before the current event. | distinguish a historical entry
chronology | Ordered sequence of events and observations. | preserve the chronology
reported water | Water described in an account before its cause is established. | locate the reported water
nearby floor | Floor surface close to the referenced equipment. | describe the nearby floor
source identification | Establishing where the reported water originated. | keep source identification open
causal link | Supported connection between a condition and its cause. | establish a causal link
unresolved concern | Issue that has not been confirmed as corrected or closed. | retain an unresolved concern
dry observation | Record that the visible surface was dry at the stated time. | qualify the dry observation
intermittent symptom | Condition that may appear at some times and not others. | describe an intermittent symptom
recurrence history | Record of repeated appearances of a condition. | verify recurrence history
drainage path | Route intended for the relevant liquid to travel. | identify the drainage path
overflow | Liquid exceeding the capacity or boundary of its intended containment. | distinguish a reported overflow
leakage | Unintended escape of a fluid. | avoid assuming leakage source
condensation | Formation of liquid from vapor under relevant conditions. | distinguish condensation from a diagnosis
finding | Observation or conclusion established through the relevant assessment. | state the actual finding
repair status | Whether corrective work is proposed, underway, or completed. | verify repair status
evidence boundary | Limit of what the information supports. | preserve the evidence boundary
record reconciliation | Bringing separate accounts together without erasing their distinctions. | complete record reconciliation''',
    precision='Yesterday at 15:00, Elena reported water near AH-6. Today, the floor is recorded as dry. Those observations concern different times; the later note does not disprove the earlier report or establish a repair.',
    precision_extra='The earlier drain-pan concern is history, not a verified cause. Do not change near AH-6 to from AH-6, or concern to failure, without evidence. The source remains unidentified in the supplied visit note.',
    phrases='''State yesterday's account | The client reported water near AH-6 at 15:00 yesterday.
State today's observation | The visit note records the nearby floor as dry today.
Keep both times | Those accounts refer to different observations at different times.
Name the unresolved issue | The source was not identified.
Attribute the history | An earlier service-log entry mentions a drain-pan concern.
Avoid converting history into cause | That entry does not establish a link to yesterday's water.
Distinguish near from from | Near AH-6 gives a location, not a proven origin.
Avoid changing concern to failure | The record says concern, not confirmed failure.
Keep repair separate | No completed repair is established by the dry-floor note.
Preserve the client report | The later observation does not cancel your account.
Use the exact equipment reference | Please retain AH-6 in the summary.
Avoid an invented recurrence pattern | We have not established how often this happens.
Name the three sources | Client report, visit note, and earlier log remain distinct.
Limit the finding | We can report the surface condition without diagnosing the source.
Give a balanced summary | Water reported yesterday; floor dry today; cause unresolved.
Close with accurate status | The source question remains open for the relevant assessment.''',
    notes='''Yesterday versus today | Prevents observations at different times from being treated as a contradiction.
Near versus from | Distinguishes location from origin.
Mentions | Records what a document says without upgrading it to a verified diagnosis.
Does not establish a link | Keeps a plausible history item from becoming a proven cause.
Recorded as | Attributes an observation to the supplied note.
Remains open | Preserves an unresolved matter without inventing an outcome.''',
    d='''Which summary preserves chronology? | Water near AH-6 yesterday at 15:00; floor dry today; source unidentified | The floor has always been dry | The drain pan failed at 15:00 and was repaired | The visit disproves the client's account | The summary combines the different times while retaining the unresolved source.
Which wording improperly asserts origin? | Water came from AH-6 | Water was reported near AH-6 | The nearby floor was dry today | The source was not identified | The supplied report gives proximity, not proof that AH-6 produced the water.
How should the drain-pan entry be handled? | Retain it as history with no established causal link | Treat it as the final diagnosis | Delete it because the floor is dry | Relabel it as a completed repair | Relevant history can be preserved without asserting a cause or resolution.
What can the dry-floor note establish about repair? | No completed repair by itself | Every possible leak was fixed | The earlier concern was resolved | A drainage component was replaced | A surface observation is not evidence that corrective work occurred.''',
    dialogue='''Elena | I reported water near AH-6 at three yesterday afternoon. Today's note says the floor is dry, and I am worried that my report will be treated as mistaken.
Kai | We can preserve the [[chronology::Chronology keeps yesterday's report and today's observation separate instead of treating them as simultaneous claims.]]. Your account and today's note refer to different times, so a dry floor now does not cancel the water you reported yesterday.
Elena | Please keep three o'clock with yesterday's report. Otherwise the summary may make it sound as though the service team saw water during today's visit.
Kai | I will. The [[visit note::Visit note is the source for today's dry-floor observation, not yesterday's client report.]] records today's nearby floor as dry and says the source was not identified. That is a separate observation with its own limits.
Elena | There is an older entry about the drain pan. Someone suggested we could simply name that as the explanation for the water.
Kai | We should retain the [[drain-pan concern::Drain-pan concern is historical information, not a confirmed cause of the later water report.]] as history, but the entry does not establish a connection to yesterday's report. It is not enough to name the pan as the proven source.
Elena | The wording near the air handler matters too, then. I saw the water near it; I did not identify the point it came from.
Kai | Exactly. That is an [[evidence boundary::Evidence boundary limits the account to observed location rather than asserting origin from AH-6.]]. Changing near AH-6 to from AH-6 would turn a location description into an unsupported statement about origin.
Elena | Would calling the old entry a drain-pan failure make the record stronger, or would that change what the earlier person actually wrote?
Kai | It would change it. The [[historical entry::Historical entry must retain its recorded status as a concern rather than being upgraded to confirmed failure.]] says concern, not confirmed failure. We need to preserve that distinction even if the topic appears relevant to the current question.
Elena | Understood. I would rather have a precise unresolved record than a confident explanation that nobody has actually established.
Kai | Then the [[source identification::Source identification remains unresolved because today's note explicitly says the source was not identified.]] stays open. We can report the facts and the earlier concern without claiming that the relationship between them has been verified.
Elena | Does the dry floor tell us a repair must have worked overnight? I do not have a record of corrective work, but someone asked that.
Kai | No. The [[repair status::Repair status cannot be inferred from a later dry surface when no corrective work is documented.]] cannot be inferred from the dry-floor observation. Nothing in these records establishes that a repair was completed between your report and the visit.
Elena | We also should not call it a recurring problem unless there are actual records showing repeated events, correct? One older concern is not the same thing.
Kai | Correct. A [[recurrence history::Recurrence history requires evidence of repeated events, not merely an earlier concern about a component.]] would need supporting information. We should not invent a frequency or treat every earlier note as another occurrence of the same water event.
Elena | Please give me a short summary that includes my report, today's visit, and the older log without mixing the three together.
Kai | Client reported water near AH-6 at 15:00 yesterday. Today's floor was dry; source unidentified. Earlier log notes a drain-pan concern, with no established [[causal link::Causal link is the missing connection between the earlier concern and the reported water.]] to the water.
Elena | That is accurate. It does not dismiss my observation, promise the issue is resolved, or make the earlier note say more than it does.
Kai | I will use that [[record reconciliation::Record reconciliation combines the three sources while preserving time, attribution, and uncertainty.]] in the handoff. The next assessment can address the source question with the original accounts intact, rather than starting from an assumed diagnosis.''',
    transfer_title='Preserve the three records',
    transfer_setup='Complete the service summary. Keep yesterday, today, and the earlier concern distinct.',
    transfer='''Client: "Water was reported near AH-6 at ___ yesterday." | 15:00 | The time belongs to Elena's report on the previous day.
Coordinator: "Today the nearby floor was recorded as ___." | dry | Dry describes the surface observed during the later visit.
Client: "The earlier log mentions a drain-pan ___." | concern | Concern preserves the historical wording without upgrading it to a confirmed failure.
Coordinator: "The source was not ___." | identified | The visit note leaves the origin of the reported water unresolved.'''
))


BOOK['units'].append(unit(
    title='Discussing refrigeration alarms and temperature records',
    scene='An alarm, a display value, and missing product data',
    skill='Report an alarm chronology accurately, distinguish cabinet and product information, and route a food-safety question to the responsible lead.',
    brief='Cafe manager Noah discusses a refrigeration record with technician Imani. A cabinet display recorded 8 degrees Celsius at 06:10. Product temperatures are not supplied. An alarm-history entry and a scheduled-defrost entry have the same time, but event cause and duration are unconfirmed. Noah asks whether the food is safe. The responsible food-safety lead must decide under the site procedures. The display value and coincident entries do not authorize food release or establish a harmless defrost event.',
    cast='Noah | Cafe manager\nImani | Refrigeration technician',
    culture=('Give the record, not an improvised release decision', 'Operational pressure can turn a request for information into a request for reassurance. Identify exactly what the record contains and what is missing. Refer the product decision to the responsible food-safety lead while preserving the technical event as unresolved.'),
    a='''What was recorded at 06:10? | A cabinet display value of 8 degrees Celsius | Verified temperatures for every food item | A confirmed harmless alarm cause | The end of a measured exposure period | The record supplies a cabinet display value, not product temperatures or duration.
What do the matching timestamps establish? | The two entries share a recorded time | Defrost definitely caused the alarm | The alarm lasted one minute | Every food item remained safe | Coincident timestamps do not establish cause, duration, or product safety.
Who must decide the food-safety question? | The responsible food-safety lead under site procedures | The display value alone | The technician by assuming defrost | The customer waiting at the counter | The scenario assigns that decision to the responsible lead using the site's procedures.''',
    vocabulary='''refrigerated cabinet | Enclosed equipment used to hold products under cooled conditions. | identify the refrigerated cabinet
cabinet display | Interface showing a value or status from refrigeration equipment. | quote the cabinet display
product temperature | Temperature of the actual stored product. | distinguish product temperature
display value | Number shown by the equipment interface. | record the display value
alarm history | Log of recorded equipment alarm events. | review the alarm history
timestamp | Recorded date or time associated with an entry. | preserve the timestamp
defrost | Process intended to remove frost from relevant equipment surfaces. | identify the defrost entry
scheduled defrost | Defrost event listed in the control schedule or record. | distinguish scheduled defrost
event duration | Length of time an event continued. | establish event duration
coincident entries | Records appearing at the same stated time. | compare coincident entries
causation | Relationship in which one event produces another. | avoid assuming causation
temperature excursion | Departure from a defined temperature range or limit. | assess a recorded temperature excursion
exposure history | Record of conditions experienced by the product over time. | establish exposure history
data gap | Missing information needed for an assessment. | identify the data gap
food-safety lead | Person assigned responsibility for the relevant food-safety decision. | notify the food-safety lead
site procedure | Established process applicable at the premises. | follow the site procedure
release decision | Authorization to make a product available for its intended use. | refer the release decision
product disposition | Decision about how affected products will be handled. | determine product disposition
alarm acknowledgment | Record that an alarm has been noticed or accepted by an operator. | distinguish alarm acknowledgment
alarm clearance | Change in alarm status that does not alone establish product safety. | distinguish alarm clearance
trend record | Series of values showing change over time. | review the trend record
sensor location | Position associated with a particular measurement device. | identify the sensor location
technical cause | Established equipment or process explanation for an event. | keep the technical cause open
escalation summary | Concise information passed to the responsible decision-maker. | give an escalation summary''',
    precision='The record gives a display value of 8 degrees Celsius at 06:10. Product temperatures are absent. No safe holding period or release decision can be inferred from this isolated display value and timestamp.',
    precision_extra='The alarm and scheduled-defrost entries coincide, but cause and duration remain unconfirmed. Do not call the event harmless or assume defrost explains it. Follow the site food-safety escalation process; the responsible lead decides product disposition.',
    phrases='''Quote the actual record | The cabinet display recorded 8 degrees Celsius at 06:10.
Name the missing information | Product temperatures have not been supplied.
Keep the record type clear | That is a display value, not a verified food-temperature record.
Identify the coincident entries | The alarm and scheduled-defrost entries share a timestamp.
Avoid a causal shortcut | The matching time does not establish that defrost caused the alarm.
Preserve duration uncertainty | The event duration is unconfirmed.
Reject premature reassurance | I cannot declare the food safe from these records.
Name the decision route | The responsible food-safety lead must decide under the site procedures.
Keep technical status open | The cause of the event still needs confirmation.
Avoid equating clearance with safety | Alarm clearance would not itself release the food.
Preserve the data gap | The product exposure history is not established.
Escalate accurately | Please pass the display record and the missing data to the lead.
Keep disposition separate | Product disposition is separate from explaining the equipment entry.
Avoid a guessed threshold | We should not invent an allowable exposure period.
Read back the essentials | 8 degrees at 06:10; product data absent; cause and duration unconfirmed.
Close without releasing product | This technical discussion does not authorize food release.''',
    notes='''Recorded | Attributes the number to the equipment record without changing what it measures.
Same time versus because | Separates coincidence from a causal explanation.
Unconfirmed duration | Prevents a timestamp from being read as a complete event interval.
Must decide under | Names both the responsible role and the governing site process.
Would not itself | Limits what an alarm-status change can establish.
Separate from | Keeps equipment assessment and product disposition as distinct questions.''',
    d='''Which summary belongs in the escalation? | Display 8 degrees Celsius at 06:10; product data absent; cause and duration unconfirmed | Food definitely safe because defrost was scheduled | Every product was measured at 8 degrees | Alarm lasted only until 06:11 | The summary preserves the actual value and all material information limits.
Why is defrost caused it unsupported? | The shared timestamp does not establish causation | Defrost can never appear in a schedule | The display has no number | Product temperatures are all confirmed | Temporal coincidence alone does not prove the explanation for the alarm.
Who should receive the food-release question? | The responsible food-safety lead using site procedures | Whoever recognizes the cabinet brand | The person who wants service to resume fastest | The alarm display as sole authority | Product decisions require the assigned responsible process rather than an improvised technical assurance.
Which statement improperly fills a data gap? | The food was warm for only one minute | The display value was recorded at 06:10 | Product temperatures were not supplied | The duration remains unconfirmed | No event duration or product exposure period is established by the record.''',
    dialogue='''Noah | The cabinet display recorded eight degrees at 06:10, and there is an alarm entry. We open soon; can you tell me whether the food is safe?
Imani | I cannot make that release decision from the [[display value::Display value is equipment information and does not supply the missing product temperatures or exposure history.]] alone. We need to keep the equipment record separate from the actual product information.
Noah | The value is in Celsius. I have not been given any temperatures for the food itself, only the number from the cabinet display.
Imani | Then [[product temperature::Product temperature concerns the food itself and is absent from the information supplied.]] is a missing piece of information. The display record must not be rewritten as though every item was measured at eight degrees.
Noah | The alarm history and the scheduled-defrost entry both show 06:10. Could that mean the alarm was simply part of a harmless defrost period?
Imani | The [[timestamp::Timestamp establishes the recorded time shared by the entries, not why the alarm occurred.]] tells us the entries coincide, but it does not establish that defrost caused the alarm or that the event was harmless.
Noah | We do not have the length of the event either. The record gives that one time, not a confirmed start and finish.
Imani | Then the [[event duration::Event duration remains unknown because one timestamp does not establish a complete interval.]] remains unconfirmed. We should not turn 06:10 into a one-minute event or another guessed exposure period.
Noah | I understand. I need to give our food-safety lead the facts now, rather than asking you to infer a release decision from the equipment screen.
Imani | Yes. The [[food-safety lead::Food-safety lead is the assigned decision-maker for product safety under the site's procedures.]] must decide under your site procedures. I can help describe the technical records accurately, but this conversation does not authorize serving the food.
Noah | Please help me separate what we know from what we are only wondering about. I do not want the scheduled entry to become a diagnosis in the handoff.
Imani | We know there is a [[scheduled defrost::Scheduled defrost is a recorded event sharing the time, not a proven explanation for the alarm.]] entry at the same time as the alarm. The causal relationship is unconfirmed, and product-temperature information has not been supplied.
Noah | Even if somebody later tells us the alarm is no longer showing, that would not by itself settle what happened to the products earlier, would it?
Imani | Correct. [[Alarm clearance::Alarm clearance concerns equipment alarm status and does not establish product safety or past exposure.]] would not establish the products' temperature history or make a release decision. The equipment status and the food decision remain different matters.
Noah | I will not invent a holding period or tell the staff everything is fine because the entries share a time. The lead needs the unresolved points.
Imani | Exactly. The [[exposure history::Exposure history describes conditions experienced by the products over time, which these isolated records do not establish.]] is not established here. Keep that gap visible along with the unknown event duration and cause, rather than substituting a reassuring guess.
Noah | Here is my summary: display eight degrees Celsius at 06:10; no product readings; alarm and defrost entries coincide; cause and duration unconfirmed.
Imani | That is an accurate [[escalation summary::Escalation summary passes the actual records and missing information to the responsible lead without authorizing release.]]. Send it through the site process to the responsible lead, and keep the technical cause question open separately.
Noah | I will do that. Any decision about using, retaining, or otherwise handling the products will come from the responsible process, not this call.
Imani | Yes. [[Product disposition::Product disposition is the responsible decision about the food, distinct from interpreting the equipment records.]] must follow that process. We have clarified the information for the decision-maker; we have not declared the food safe or resolved the equipment event.''',
    transfer_title='Escalate the record without a safety claim',
    transfer_setup='Complete the handoff to the responsible lead. Preserve the display record and the missing product information.',
    transfer='''Manager: "The display recorded ___ degrees Celsius." | 8 | Eight is the cabinet display value, not a verified product temperature.
Technician: "The timestamp was ___." | 06:10 | The timestamp records one time and does not establish event duration.
Manager: "Product temperatures were not ___." | supplied | The absence of product readings is a material limit on the information.
Technician: "The responsible food-safety ___ must decide under site procedures." | lead | The assigned lead makes the product decision rather than the equipment display alone.'''
))


BOOK['units'].append(unit(
    title='Coordinating ductwork, access, and changes',
    scene='Moving a grille is a coordinated change',
    skill='Acknowledge an appearance preference, explain unassessed consequences, and present two bounded choices without promising price or timing.',
    brief='Office client Priya asks project coordinator Daniel to move a supply grille because it visually conflicts with a pendant light. The proposal has not assessed ductwork, ceiling restoration, service access, price, or timing. Priya may retain the current reviewed layout or request a coordinated change proposal. Daniel must explain the choice without treating a small visible move as a minor technical task or guaranteeing unchanged cost and completion.',
    cast='Priya | Office client\nDaniel | Project coordinator',
    culture=('Make the choice clear without minimizing the work', 'A visible component can be connected to less visible work above the ceiling. Acknowledge the design preference, list the specific unassessed matters, and offer the stated choices. A request to assess a move is not approval to install it or an agreement to absorb its cost.'),
    a='''Why does Priya want the grille moved? | It visually conflicts with a pendant light | A measured airflow failure is established | A new layout has already been accepted | A maintenance inspection ordered the move | The request concerns appearance, not an established system fault.
Which consequences have been assessed? | None of the listed change effects | Ductwork and price only | Service access and timing only | All effects with a fixed quote | Ductwork, restoration, access, price, and timing remain unassessed.
What are the stated choices? | Retain the reviewed layout or request a coordinated change proposal | Move it immediately or cancel the whole project | Accept a guessed price or waive review | Change the refrigerant or replace the system | The brief supplies two bounded options without authorizing an immediate alteration.''',
    vocabulary='''supply grille relocation | Proposed change to the position of a supply-air grille. | assess a supply grille relocation
pendant light | Light fitting suspended from the ceiling. | coordinate the pendant light
visual conflict | Appearance issue between elements in the same view. | describe the visual conflict
reflected ceiling plan | Drawing of ceiling elements represented as viewed in reflection from below. | review the reflected ceiling plan
ceiling void | Space above the visible ceiling and below the structure above. | coordinate the ceiling void
branch duct | Duct section branching from a larger distribution route. | review the branch duct
duct connection | Interface joining a duct to another component. | assess the duct connection
flexible duct | Air-conveying duct with a flexible construction. | identify the flexible duct
rigid duct | Air-conveying duct with a relatively fixed form. | distinguish rigid duct
service clearance | Space required for relevant maintenance or access. | preserve service clearance
ceiling restoration | Reinstatement of ceiling finishes after defined work. | assess ceiling restoration
access provision | Means included in the design for reaching services. | review the access provision
reviewed layout | Arrangement that has undergone the stated project review. | retain the reviewed layout
change proposal | Defined suggestion for altering the existing arrangement. | request a change proposal
coordination review | Evaluation of the change across affected elements and trades. | arrange a coordination review
scope impact | Effect of a change on the work required. | identify the scope impact
cost impact | Effect of a change on price or expenditure. | assess the cost impact
schedule impact | Effect of a change on timing. | assess the schedule impact
design preference | Client choice concerning the desired arrangement or appearance. | record the design preference
technical feasibility | Whether the proposed arrangement can satisfy relevant technical conditions. | establish technical feasibility
revised layout | Updated arrangement proposed or accepted after a change. | review the revised layout
unassessed consequence | Effect not yet evaluated. | keep unassessed consequences visible
instruction to proceed | Direction authorizing agreed work to begin. | distinguish an instruction to proceed
decision record | Record of the option selected and its conditions. | confirm the decision record''',
    precision='The visible conflict concerns the grille and pendant light. No performance fault is established. Ductwork, restoration, access, price, and timing all need assessment before the proposed move can be treated as a defined change.',
    precision_extra='The two available decisions are to retain the reviewed layout or request a coordinated proposal. Choosing assessment does not approve a new location, authorize installation, or guarantee that the original cost and schedule will remain unchanged.',
    phrases='''Acknowledge the preference | I understand why you want the grille clear of the pendant light.
Name the request | You are asking to relocate the supply grille.
Avoid minimizing hidden work | The visible move may involve work above the ceiling.
Identify the unassessed items | Ductwork, restoration, access, price, and timing still need assessment.
Separate appearance and fault | The concern is visual, not a confirmed performance defect.
State the first option | You can retain the current reviewed layout.
State the second option | You can request a coordinated change proposal.
Keep the choice bounded | Those are the two decisions available at this stage.
Avoid a price promise | I cannot confirm unchanged cost before review.
Avoid a timing promise | The schedule effect has not been established.
Keep access in scope | The proposal must account for service access.
Clarify the request status | Asking for a proposal does not authorize the relocation.
Preserve technical review | The new position needs the relevant coordination.
Name restoration explicitly | Ceiling restoration must be included in the assessment.
Read back the decision | You are requesting assessment, not approving installation.
Close with the next deliverable | We will bring back a defined proposal with its consequences.''',
    notes='''May involve | Acknowledges possible hidden work without inventing a specific construction requirement.
Still need assessment | Keeps every listed consequence open.
Retain or request | Presents two concrete choices instead of an unbounded design task.
Before review | Makes evidence a condition of a price or timing commitment.
Not a confirmed defect | Distinguishes an appearance preference from a performance finding.
With its consequences | Requires the proposal to show related effects, not merely a new dot on a plan.''',
    d='''Which response explains the choice accurately? | Retain the reviewed layout or request a coordinated proposal with impacts assessed | The move is free because it is visually small | The move is already approved because the client prefers it | Only the grille position matters; access can be ignored | The response offers the two supplied options and preserves the need to assess consequences.
Which item must not disappear from review? | Service access | A guessed refrigerant change | An invented system failure | A promised unchanged date | Service access is explicitly one of the unassessed matters in the brief.
What does requesting a proposal authorize here? | Assessment of the change, not its installation | Immediate relocation | Automatic acceptance of any price | Waiving ceiling restoration | A request for review does not equal agreement to carry out the proposed work.
Which phrase overstates certainty? | We can move it with no cost or timing effect | We need to assess the ductwork | The conflict is visual | You can retain the current layout | Cost and timing effects remain unknown, so a no-impact promise is unsupported.''',
    dialogue='''Priya | The supply grille sits awkwardly beside the pendant light. I would like it moved so the ceiling looks more deliberate. Is that a small change?
Daniel | It is a [[design preference::Design preference identifies the appearance concern without claiming a performance fault.]] we can record, but the visible size of the move does not tell us the amount of work involved above the ceiling.
Priya | I am not reporting a cooling problem. It is the way the grille and light look together that bothers me in the current arrangement.
Daniel | Understood. We should call it a [[visual conflict::Visual conflict describes the relationship in appearance between the grille and pendant light.]], not an established performance defect. That keeps the reason for the request accurate when it reaches the design team.
Priya | What would need review beyond drawing the grille in a different position? I want to understand the practical issues before choosing the next step.
Daniel | The [[ductwork::Ductwork is one of the hidden systems whose changes have not been assessed for the proposed move.]] has not been assessed, nor have ceiling restoration, service access, price, or timing. A revised drawing must be supported by review of those related effects.
Priya | I had only thought about the visible ceiling opening. The work needed to restore the original position would need a clear scope too.
Daniel | Yes. [[Ceiling restoration::Ceiling restoration concerns reinstating affected finishes and remains part of the unassessed change scope.]] must be assessed rather than treated as automatically included or unnecessary. We should not give you a price for only part of the actual change.
Priya | And access above the ceiling cannot simply be ignored because the new position looks better from the room below, correct?
Daniel | Correct. The [[access provision::Access provision concerns how the relevant services remain reachable after a proposed layout change.]] needs review with the other requirements. Appearance is important, but it does not by itself establish whether a revised arrangement is technically acceptable.
Priya | What can I decide today without having to invent the new technical solution myself? I would prefer a clear choice about how to proceed.
Daniel | You can retain the current [[reviewed layout::Reviewed layout is the existing arrangement available as the first stated option.]], or request a coordinated change proposal. Those are the two options at this stage; neither requires you to specify a duct route.
Priya | I would like the proposal, provided that asking for it does not mean I have already approved installation or accepted an unknown extra price.
Daniel | It does not. A [[change proposal::Change proposal is the requested assessed alternative, not authorization to install or acceptance of its terms.]] will define the alternative and its consequences for review. Requesting it is separate from accepting the resulting work and commercial terms.
Priya | Can you guarantee the original finish date while that is being assessed? The office move-in planning depends on the overall schedule.
Daniel | I cannot confirm that yet. The [[schedule impact::Schedule impact remains unassessed, so unchanged completion cannot be guaranteed.]] is one of the open questions, along with cost. Your timing concern should be recorded without being mistaken for a promise that no effect exists.
Priya | Please also avoid describing the move as free or minor in the meeting notes. I want the assessment to be clear before anyone makes that assumption.
Daniel | Agreed. The [[cost impact::Cost impact must be assessed with the defined work rather than assumed absent because the visible move seems small.]] will need a defined scope. We will include ductwork, access, restoration, and timing in the coordinated review rather than price only the visible grille.
Priya | Then record that I am requesting a proposal, not directing the team to move the grille now. I will review the actual consequences before agreeing.
Daniel | That is the [[decision record::Decision record preserves the selected assessment step without turning it into an instruction to proceed.]]: coordinated proposal requested; relocation not authorized. The current reviewed arrangement is not replaced by an assumed new position during this conversation.''',
    transfer_title='Offer two clear paths',
    transfer_setup='Complete the choice discussion. Keep the existing layout and the request for assessment separate from installation approval.',
    transfer='''Coordinator: "You can retain the reviewed ___." | layout | Layout refers to the existing reviewed arrangement available as the first option.
Client: "Or request a coordinated change ___." | proposal | Proposal is the assessed alternative the client may request before deciding.
Coordinator: "Cost and timing still need ___." | assessment | The effects on price and schedule have not yet been evaluated.
Client: "This request does not authorize ___." | relocation | Requesting a proposal does not approve moving the supply grille.'''
))


BOOK['units'].append(unit(
    title='Handing over commissioning and maintenance information',
    scene='Report received, seasonal check still open',
    skill='Separate document receipt from completed verification and distinguish assigned correction work from an unassigned scheduling responsibility.',
    brief='Client Ben receives a commissioning report for a fictional office system. It lists a deferred seasonal check, and the maintenance sheet names the wrong model. Coordinator Nia accepts responsibility for document correction and will update Ben on Friday. The seasonal-check date is not booked, and responsibility for scheduling it has not been confirmed. The handover must preserve that ownership gap. No overall performance conclusion, completed seasonal result, or change to warranty terms is supplied.',
    cast='Ben | Client\nNia | Coordinator',
    culture=('Do not let one named owner hide a different unassigned task', 'A coordinator can own a document correction without owning every remaining technical action. A useful handover names the received records, the unresolved checks, and who is responsible for each. State an ownership gap directly rather than letting a polite promise to update imply it is settled.'),
    a='''What does the commissioning report list? | A deferred seasonal check | A completed seasonal result | A confirmed Friday test booking | No outstanding verification | The report explicitly identifies a check that has been deferred rather than completed.
What responsibility does Nia accept? | Document correction and a Friday update | Confirmed ownership of scheduling every check | A guaranteed system-performance result | An automatic warranty extension | Nia's commitment is to document correction and communication, not the unassigned scheduling task.
What remains unresolved about the seasonal check? | Both the date and the scheduling owner | Only the spelling of Friday | Whether any report was received | Whether Nia agreed to correct the sheet | The check is unbooked and responsibility for arranging it is not confirmed.''',
    vocabulary='''commissioning | Process of verifying and documenting system performance against relevant project requirements. | distinguish commissioning from document delivery
commissioning report | Record of commissioning activities, results, and outstanding matters. | receive the commissioning report
deferred check | Verification postponed until a later appropriate time or condition. | record the deferred check
seasonal check | Verification associated with relevant seasonal operating conditions. | schedule the seasonal check
maintenance sheet | Document describing relevant maintenance information for equipment. | correct the maintenance sheet
model-specific guidance | Information applicable to the actual identified product model. | obtain model-specific guidance
document mismatch | Difference between supplied information and the relevant equipment. | identify the document mismatch
correction owner | Person responsible for resolving a record error. | name the correction owner
scheduling owner | Person responsible for arranging the required attendance or check. | confirm the scheduling owner
ownership gap | Task for which responsibility has not been confirmed. | preserve the ownership gap
unbooked check | Required verification with no confirmed appointment. | retain the unbooked check
update commitment | Promise to provide further information at a stated time. | honor the update commitment
outstanding verification | Check not yet completed or accepted. | track outstanding verification
handover register | Record of delivered information and remaining handover matters. | update the handover register
operating record | Documented information about actual operation. | retain the operating record
performance result | Established outcome from relevant measurement or verification. | distinguish a performance result
acceptance criterion | Requirement used to judge whether an outcome meets the agreed standard. | identify the acceptance criterion
test condition | Defined state under which a verification is carried out. | record the test condition
deferral reason | Explanation for postponing an activity. | preserve the deferral reason
closeout status | Current position of remaining completion matters. | state the closeout status
maintenance requirement | Relevant action or condition specified for upkeep. | verify the maintenance requirement
warranty terms | Actual conditions and coverage stated in the relevant warranty. | preserve warranty terms
document receipt | Confirmation that information has been delivered. | acknowledge document receipt
responsibility readback | Repetition of assigned and unassigned tasks for clarity. | give a responsibility readback''',
    precision='The report has been received, but the seasonal check is deferred. The wrong-model maintenance sheet needs correction. Neither delivery nor a corrected document would itself establish a completed seasonal result or overall system performance.',
    precision_extra='Nia owns document correction and promises a Friday update. The seasonal check has no booked date and no confirmed scheduling owner. Preserve both gaps instead of silently assigning the check to Nia or treating Friday as its appointment.',
    phrases='''Acknowledge the report | You have received the commissioning report.
Name the exception | The report lists a deferred seasonal check.
Identify the document error | The maintenance sheet names the wrong model.
Accept a specific task | I will take responsibility for document correction.
Commit to an update | I will update you on Friday.
Keep the date limited | Friday is an update date, not a booked seasonal check.
State the booking gap | The seasonal-check date is not booked.
State the ownership gap | Responsibility for arranging that check is not confirmed.
Avoid implied ownership | My document task does not settle who schedules the check.
Preserve model specificity | The replacement sheet must match the actual model.
Separate receipt and verification | Receiving the report does not complete the deferred check.
Avoid an overall assurance | We have no overall performance conclusion to add here.
Keep warranty separate | This discussion does not change the actual warranty terms.
Name the next coordination issue | We still need a confirmed scheduling owner and date.
Read back responsibilities | Nia owns correction; seasonal scheduling ownership remains open.
Close with accurate status | Documents are received, corrections and deferred verification remain visible.''',
    notes='''Lists a deferred check | Describes a recorded exception rather than a completed result.
Will update | Commits to communication without guaranteeing an unresolved outcome.
Responsibility not confirmed | Makes an ownership gap explicit.
Does not settle | Prevents one accepted task from silently resolving another.
Must match | Connects the maintenance document to the relevant equipment model.
Remain visible | Keeps unfinished items in the handover instead of hiding them in a general completion claim.''',
    d='''Which summary preserves all responsibilities? | Nia corrects documents and updates Friday; seasonal-check owner and date remain open | Nia has booked every check for Friday | Report receipt proves full performance | The client automatically owns the seasonal check | The summary keeps Nia's accepted task distinct from the unresolved scheduling responsibility.
What does Friday identify? | Nia's promised update | A confirmed seasonal test date | A warranty start date supplied by this case | Completion of every open item | The only Friday commitment is communication about follow-up.
Which inference is unsupported? | Correcting the maintenance sheet completes the seasonal check | The sheet names the wrong model | The report was received | Scheduling ownership is unconfirmed | A document correction is not performance of the deferred verification.
What should the handover keep open? | Correct model guidance, deferred verification, scheduling owner, and date | Only a general statement saying all complete | A guessed successful test result | An automatic warranty extension | The remaining matters must be separately visible rather than replaced by an unsupported closure claim.''',
    dialogue='''Ben | I have received the commissioning report, but it lists a seasonal check as deferred. The maintenance sheet also seems to name a different model from our system.
Nia | Those are two distinct handover matters. I accept the [[document mismatch::Document mismatch identifies the wrong-model maintenance sheet as a correction task.]] on the maintenance sheet and will take responsibility for correcting that information.
Ben | Thank you. Before we close the handover discussion, I also need to know whether receiving the report means the remaining seasonal check is treated as complete.
Nia | No. The [[deferred check::Deferred check remains outstanding even though its existence is recorded in the delivered report.]] is still outstanding. The report records its status; delivery of that report does not carry out the verification or supply its result.
Ben | Can you confirm who is arranging that check and when it will take place? I cannot find a booked date in the information I received.
Nia | The [[scheduling owner::Scheduling owner has not been confirmed, so the arranging responsibility remains open.]] has not been confirmed, and no date is booked. I should not imply that my document-correction task resolves either of those questions.
Ben | That distinction matters. I might otherwise assume that because you own the wrong-sheet correction, you also own arranging all the remaining technical work.
Nia | Exactly. We need to preserve the [[ownership gap::Ownership gap names the unassigned scheduling responsibility rather than silently giving it to Nia.]] for the seasonal check. It needs an explicit assignment, not an assumption based on who is speaking at handover.
Ben | What commitment can you give me today about the documents, so I have a clear next contact point even while the other responsibility remains open?
Nia | I will correct the document information and make an [[update commitment::Update commitment is Nia's promise to communicate on Friday, not a promised technical-check result.]] for Friday. That gives you a communication date without presenting an unbooked seasonal check as scheduled.
Ben | Please make sure the corrected maintenance sheet is for the actual model. A similar-looking product document would leave us with the same uncertainty.
Nia | Agreed. We need [[model-specific guidance::Model-specific guidance links the corrected maintenance information to the actual equipment rather than a similar model.]] for the actual equipment. Correcting the sheet is a defined records task; it is not evidence that the seasonal verification has occurred.
Ben | Would it be accurate to say the system has passed every operating condition because the commissioning report is now in our hands?
Nia | No. We have no overall [[performance result::Performance result cannot be generalized to all conditions when a seasonal check is still deferred.]] to add from these facts. The deferred item remains part of the record, and we should not invent a successful result for it.
Ben | I also want to avoid changing the warranty language in our summary. We should keep the actual warranty terms separate from this follow-up discussion.
Nia | Correct. The [[warranty terms::Warranty terms retain their actual meaning and are not revised by the document update or deferred-check discussion.]] are not changed by this conversation. Neither an update date nor an outstanding check creates a new warranty promise here.
Ben | Let me read the responsibilities back: you own the document correction and Friday update. The seasonal check is unbooked, and its scheduling owner is still unconfirmed.
Nia | That [[responsibility readback::Responsibility readback distinguishes the assigned document task from the unassigned seasonal scheduling task.]] is accurate. It makes the commitment and both remaining scheduling questions visible instead of assigning the whole handover to one person by implication.
Ben | Then I will record receipt of the report without marking every item complete. Friday will be listed as an update, not a test appointment.
Nia | Thank you. The [[handover register::Handover register should record receipt alongside corrections and outstanding verification without claiming full completion.]] should preserve the report receipt, wrong-model correction, deferred check, and open scheduling responsibility and date. That is a clear close to today's conversation, with the unfinished work still visible.''',
    transfer_title='Assign only the responsibility actually accepted',
    transfer_setup='Complete the handover readback. Keep the document owner, update date, and unassigned seasonal-check task distinct.',
    transfer='''Client: "___ owns document correction." | Nia | Nia accepts the correction task, not confirmed ownership of arranging the seasonal check.
Coordinator: "The update is promised for ___." | Friday | Friday is the communication commitment rather than a booked technical appointment.
Client: "The seasonal check is still ___." | unbooked | No confirmed date has been supplied for the deferred seasonal verification.
Coordinator: "Its scheduling owner is not yet ___." | confirmed | The responsibility for arranging the check remains an explicit open question.'''
))
