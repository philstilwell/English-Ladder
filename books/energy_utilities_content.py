"""Original learner-book content for energy and utility workplaces."""
from books.authoring import unit

BOOK = dict(
    slug='energy-utilities',
    title='Energy and Utilities English',
    cover_label='ENGLISH FOR ENERGY AND UTILITY TEAMS',
    cover_title='Energy\nand Utilities',
    cover_size=34,
    tagline='Explain the status. Name the uncertainty. Make the measure clear.',
    audience='For utility operations, customer communication, project, program, and asset-management teams.',
    map_intro='Eight utility exchanges: correct an outage update, escalate an identifier conflict, explain a rate proposal, report an interconnection review, compare asset costs, hand over storm resources, qualify efficiency claims, and interpret reliability measures.',
    notes_title='Translate the system without changing its meaning',
    notes_intro='Utility conversations move between specialist records and decisions that affect customers. Translate jargon into clear language while preserving the difference between an estimate, an authorization, a measured result, and an unresolved question.',
    field_notes=[
        ('Put status beside the number', 'A time may refer to restoration, a crew arrival, or the next information update. Name what it measures and whether it is verified, estimated, requested, or still unavailable.', '"The next update is at 16:40; that is not a restoration estimate."'),
        ('Make identifiers exact', 'Similar equipment labels are not interchangeable. Raise a mismatch through the authorized process and keep the operational restriction explicit; a plausible correction is not verification.', '"The work package says Q27; the switching request says Q72. The discrepancy remains unresolved."'),
        ('Show the comparison basis', 'Purchase price, energy use, and interruption counts answer different questions. State the period, units, included costs or events, and assumptions before drawing a conclusion.', '"This is a ten-year purchase-and-maintenance comparison, not the complete life-cycle cost."'),
        ('Translate without overpromising', 'Plain language should make a technical boundary easier to understand, not remove it. A queued application is not an approved connection, and a lower meter reading is not by itself verified program savings.', '"The application is in review; permission to operate has not been issued."')],
    scope_note='All organizations, projects, figures, equipment identifiers, and local processes are fictional. This is English-language practice, not electrical, emergency, financial, regulatory, or engineering instruction. Only qualified personnel using applicable authorized procedures may make operational decisions. No dialogue authorizes switching, access, energization, or restoration.',
    sources=[
        dict(title='U.S. Energy Information Administration. Reliability metrics, Electric Power Annual, Table 11.3.', url='https://www.eia.gov/electricity/annual/html/epa_11_03.html', note='Background for SAIDI, SAIFI, CAIDI, reporting scope, and major-event distinctions. All reliability figures in this book are invented teaching examples, not reported utility performance.', checked='1 October 2026'),
        dict(title='U.S. Department of Energy. Measurement and Verification Options for Federal Energy- and Water-Saving Projects.', url='https://www.energy.gov/cmei/femp/measurement-and-verification-options-federal-energy-and-water-saving-projects', note='Background for measurement, baseline adjustments, weather, and occupancy. The book does not prescribe an actual savings-verification method or certify program results.', checked='1 October 2026'),
        dict(title='U.S. Department of Energy. Solar Energy Guide for Homebuilders.', url='https://www.energy.gov/cmei/systems/solar-energy-guide-homebuilders', note='Background for separating applications, interconnection arrangements, and permission to operate. Actual requirements vary by utility, project, and jurisdiction.', checked='1 October 2026'),
        dict(title='California Public Utilities Commission. Understanding How the CPUC Processes a General Rate Case.', url='https://www.cpuc.ca.gov/news-and-updates/all-news/understanding-how-the-cpuc-processes-a-general-rate-case', note='A jurisdiction-specific example of reviewing utility proposals and customer impacts. The fictional rate case does not reproduce California rates, procedures, or a real customer bill.', checked='1 October 2026')],
    units=[])

BOOK['units'].append(unit(
    title='Grid Reliability and Outage Response',
    scene='An update time is not a restoration promise',
    skill='Give a useful outage message while distinguishing affected scope, assessment status, and the next update.',
    brief='At 16:10 local time, a verified operations update lists 420 affected service points in the Oak district. The cause and estimated restoration time remain under assessment. A crew is assigned, but its arrival has not been confirmed. A draft public message promises restoration by 18:00, although that figure is an unverified internal planning assumption. Communications officer Nia and operations liaison Paul must correct the draft. Paul will provide the next verified status at 16:40 local time, even if no restoration estimate is available. The affected count is a snapshot, not a prediction of the final scope.',
    cast='Nia | Communications officer\nPaul | Operations liaison',
    culture=('Uncertainty needs a useful next step', 'Customers can hear we do not know as abandonment if the message stops there. Give the confirmed scope, explain what remains under assessment, and state the next update commitment. Do not manufacture confidence by converting a planning assumption into a promise.'),
    a='''What is verified at 16:10? | 420 affected service points in the Oak district | Restoration by 18:00 | A confirmed equipment failure | Crew arrival at every affected location | The supplied operations update verifies the affected count and area, not cause or restoration time.
What does 16:40 represent? | The next status update | Guaranteed restoration | Confirmed crew arrival | The start of the outage | Paul commits to another verified status update, even if restoration timing remains unavailable.
Which crew statement is accurate? | A crew is assigned; arrival is unconfirmed. | A crew has completed the repair. | Every crew is on site. | No crew has been assigned. | Assignment is confirmed, but the brief explicitly leaves crew arrival unconfirmed.''',
    vocabulary='''electric grid | The interconnected infrastructure delivering electricity from sources to users. | maintain the electric grid
transmission | Bulk movement of electricity over the relevant high-voltage network. | coordinate transmission operations
distribution | Delivery of electricity through the network serving end users. | restore distribution service
feeder | A circuit supplying a section of the distribution network. | identify the affected feeder
substation | A facility connecting, transforming, or controlling parts of an electrical network. | identify the supplying substation
service point | A defined point at which service is supplied or measured. | count affected service points
outage | A loss or unavailability of electricity service or equipment function. | report an outage
outage footprint | The area or set of service points affected by an outage. | verify the outage footprint
estimated restoration time (ERT) | The current estimate of when interrupted service may be restored. | update the estimated restoration time
damage assessment | Evaluation of damage and relevant conditions following an event. | coordinate damage assessment
crew assignment | Allocation of a crew to an identified task or response. | confirm the crew assignment
crew arrival | The crew reaching the relevant location, distinct from being assigned. | verify crew arrival
dispatch | Coordination and direction of resources or operating activity. | contact dispatch
outage management system (OMS) | A system supporting outage tracking, analysis, and response coordination. | update the outage management system
supervisory control and data acquisition (SCADA) | Systems used to monitor and control relevant industrial processes. | interpret SCADA information
telemetry | Measurements or status information transmitted from remote equipment. | verify telemetry status
load | Electrical demand placed on the system or equipment. | monitor system load
peak demand | The highest demand over a specified period and measurement basis. | assess peak demand
kilowatt (kW) | A unit of power equal to one thousand watts. | state demand in kilowatts
kilowatt-hour (kWh) | A unit of energy equal to one kilowatt sustained for one hour. | measure energy in kilowatt-hours
restoration sequence | The authorized order of activities or service recovery during restoration. | communicate the restoration sequence
status snapshot | A report of conditions as known at a stated time. | timestamp the status snapshot
planning assumption | An unverified condition or estimate used in developing a plan. | label a planning assumption
update commitment | A promise to provide new status information at a specified point. | keep the update commitment''',
    precision='A service-point count is not necessarily a count of individual people. The 420 figure describes the verified snapshot at 16:10. Do not turn it into a final impact total or silently change the population being counted.',
    precision_extra='The 16:40 commitment concerns information. It is not a crew-arrival or restoration time. Also, a customer outage report does not establish that equipment is electrically safe; operational status requires authorized verification.',
    phrases='''Timestamp the message | This is the verified status as of 16:10 local time.
Name the scope | The update lists 420 affected service points in the Oak district.
Limit the count | That is the current snapshot, not a final impact total.
State the assessment | The cause remains under assessment.
Separate the estimate | A restoration estimate is not yet available.
Correct unsupported certainty | We cannot publish 18:00 as a confirmed restoration time.
Explain the source | That figure was an unverified planning assumption.
Describe crew status | A crew is assigned; arrival is not yet confirmed.
Make a clear commitment | Our next status update will be at 16:40 local time.
Preserve the distinction | The update time is not a promise of restored service.
Acknowledge disruption | I understand that the uncertainty makes planning difficult.
Avoid a guessed cause | We will not name a cause before it is verified.
Coordinate the channels | Correct the website and customer-service message together.
Keep the clock basis | Use local time consistently in the public update.
Maintain contact | We will update you even if the estimate remains unavailable.
Close accurately | Share the confirmed facts and the questions still under assessment.''',
    notes='''As of | Connects a count or status to its timestamp.
Affected service points | Names the measured unit without equating it to individual people.
Assigned versus arrived | Separates allocation from physical arrival.
Not yet available | Preserves uncertainty without implying that no work is happening.
By 18:00 | Creates a latest-time promise that is unsupported here.
Next update | Identifies a communication commitment, not an operational outcome.''',
    d='''Which public update matches the record? | At 16:10, 420 service points are affected; restoration timing is under assessment; next update 16:40. | All 420 people will have power at 18:00. | Crews have arrived everywhere; repair is complete. | The cause is known because a crew is assigned. | The accurate update preserves the count, timestamp, unresolved estimate, and communication commitment.
Which phrase wrongly strengthens the crew status? | Crews are on site. | A crew is assigned. | Arrival is unconfirmed. | We are checking the arrival status. | On site claims arrival, which the supplied facts do not confirm.
What should happen if no estimate exists at 16:40? | Provide the promised update and state that timing remains under assessment. | Cancel all communication without explanation. | Invent a restoration time to meet the commitment. | Repeat 18:00 as if it had been verified. | The commitment is to provide status information, not to produce a certainty that does not exist.
What does the 420 figure count? | Service points in the verified snapshot | Every person experiencing disruption | Every network asset needing replacement | The guaranteed final number affected | The supplied unit is affected service points, and the figure is limited to a timestamped snapshot.''',
    dialogue='''Nia | The draft promises restoration by eighteen hundred. Before publishing, can you confirm that time's source and whether it is verified?
Paul | It is a [[planning assumption::A planning assumption is an unverified basis for a plan, not a confirmed restoration estimate suitable for a promise.]], not a confirmed estimate. Remove the promise. As of sixteen ten local time, operations still has the cause and restoration timing under assessment.
Nia | What can I say confidently? The draft also mentions the Oak district and four hundred twenty affected service points, but I want the exact scope.
Paul | Those are the verified figures in the [[status snapshot::The status snapshot describes known conditions at a stated time, not a final total or prediction of the outage's full scope.]]. Keep the timestamp attached. The number may change as information improves, and it is not a count of individual people.
Nia | I will retain service points rather than replace that with residents. Customers also want to know whether anybody is working on the problem right now.
Paul | We can confirm the [[crew assignment::Crew assignment means a crew has been allocated; it does not establish arrival, repair progress, or restoration.]]. Arrival has not been verified, so do not say crews are on site. Assignment and physical arrival are different stages in the response.
Nia | Customer service is already saying on site. I will ask them to change that to assigned, with arrival unconfirmed.
Paul | Exactly. The [[outage management system::The outage management system supports tracking the incident, but communications must preserve the actual verified status recorded through operations.]] supports tracking, but we still need to communicate the actual verified status. A populated field does not justify a stronger statement than its source.
Nia | Can we at least promise another update? Saying the estimate is unavailable without a next contact point sounds as though we have nothing further to offer.
Paul | Yes. Make an [[update commitment::An update commitment promises further information at a specified time, not restoration or a completed assessment by that time.]] for sixteen forty local time. I will provide the verified position then, even if the restoration estimate remains unavailable and we need to say so.
Nia | I will put the update time on its own line and label it clearly. It must not look like a deadline for the lights to come back on.
Paul | Keep it separate from [[estimated restoration time::Estimated restoration time concerns when service may return; the next communication time is not a substitute for that operational estimate.]]. Customers may scan only the number. The label must make clear that sixteen forty is our next communication, not an expected restoration or crew arrival.
Nia | The draft also guesses that a failed transformer caused the outage. Our record does not verify that cause.
Paul | Remove that diagnosis. [[Damage assessment::Damage assessment evaluates actual damage and conditions; an unverified guess about equipment failure must not replace its findings.]] and other relevant checks remain with qualified operations personnel. We should not turn a plausible equipment explanation into a finding because it sounds more informative.
Nia | I will correct the website and customer-service script together. Leaving the eighteen hundred promise in either channel would continue the confusion.
Paul | Agreed. Describe the [[outage footprint::The outage footprint is the verified affected area or service-point set; here it is the Oak district snapshot, not an invented wider impact.]] consistently as well. We have a verified Oak district snapshot, not evidence that every nearby district or every person in that area is affected.
Nia | The draft also says the affected equipment is safe because service is off. I will remove that; the outage record does not establish safety.
Paul | Preserve that boundary without improvising instructions. The [[restoration sequence::The restoration sequence is an authorized operational matter; a public communications update does not direct switching or establish electrical safety.]] and equipment safety remain governed by authorized procedures. This message reports customer-service status; it does not authorize anyone to approach or operate equipment.
Nia | The revised message will give the timestamp, affected service points, unresolved cause and timing, assigned crew with arrival unconfirmed, and the sixteen forty update.
Paul | That is accurate. If [[crew arrival::Crew arrival is a distinct verified event that can be reported when confirmed, without automatically implying repair completion or restoration.]] or restoration information is confirmed before the next update, we can communicate the verified change. Until then, keep the difference between known status and expectation visible.''',
    rehearsal=['Read the corrected dialogue, keeping 420 service points distinct from a count of people.', 'Switch roles; emphasize assigned versus arrived and 16:40 as an information update, not restoration.', 'Read the checked Pine exchange twice with 180 service points and a 09:50 update, without adding a restoration promise.'],
    transfer_title='Correct a second outage message',
    transfer_setup='At 09:20 local time, 180 service points are affected in Pine district. Restoration timing is under assessment. The next information update is 09:50.',
    transfer='''Officer: "The verified affected count is ___ service points." | 180 | One hundred eighty is the supplied service-point count for this snapshot.
Liaison: "The affected district is ___." | Pine | Pine is the named district in the separate outage case.
Officer: "The next information update is at ___." | 09:50 | Nine fifty is the stated communication time, not a restoration estimate.
Liaison: "Restoration timing remains under ___." | assessment | The brief explicitly leaves restoration timing under assessment rather than confirmed.'''))

BOOK['units'].append(unit(
    title='Safety, Field Work, and Switching',
    scene='Two identifiers must not be treated as interchangeable',
    skill='Escalate conflicting equipment references and use exact repeat-back without creating an operational instruction.',
    brief='A fictional field work package identifies equipment Q27, while its associated switching request identifies Q72. The team has not established which identifier is correct. Field lead Luis has placed the affected task on hold under the local process; no operational action is authorized from these conflicting documents. System operator Farah will coordinate reconciliation through the authorized document and operating procedures. Neither identifier is to be silently corrected, and neither the equipment state nor a safe work condition can be inferred from this dialogue. The language task is to communicate the discrepancy, hold, owner, and next review accurately.',
    cast='Luis | Field lead\nFarah | System operator',
    culture=('Exact repetition can prevent a dangerous assumption', 'Similar numbers can sound like a small administrative mistake. Treat the discrepancy as unresolved until the authorized process establishes the correct reference. A respectful repeat-back confirms the message; it does not verify the physical asset or authorize work.'),
    a='''Which identifiers conflict? | Q27 and Q72 | Q27 and Q27 | Two confirmed names for the same asset | Two approved replacement instructions | The work package identifies Q27 while the switching request identifies Q72.
Which identifier is correct from the supplied facts? | It has not been established. | Q27 because it appears first | Q72 because it sounds more familiar | Both, because the digits match | The case provides no verified basis for selecting either conflicting identifier.
What does a repeat-back establish? | That the discrepancy and current hold were understood | That equipment is deenergized | That a switching action is authorized | That the physical asset has been verified | Repeating the message confirms communication, not the equipment condition or operating authority.''',
    vocabulary='''equipment identifier | The exact reference used to identify a particular item of equipment. | verify the equipment identifier
asset tag | A label or code assigned to an asset for identification. | reconcile the asset tag
work package | The documents and information governing a defined work task. | review the work package
switching request | A request for specified switching activity through the authorized process. | check the switching request
switching order | An authorized sequence or instruction for switching under the applicable process. | verify the switching order
single-line diagram | A simplified diagram representing electrical connections with single lines. | consult the current single-line diagram
system operator | An authorized person responsible for specified system-operating functions. | contact the system operator
field lead | The person leading the relevant field team or task. | notify the field lead
energized | Connected to an electrical energy source or otherwise carrying electrical potential as applicable. | verify energized status
deenergized | Without connection to an electrical potential source, stored charge, or voltage relative to earth; not synonymous with safe to work. | establish deenergized status
isolation | Separation from relevant energy sources under the applicable authorized process. | verify isolation requirements
backfeed | Electrical energy supplied from an unexpected or alternative direction or source. | assess backfeed hazards
grounding | Establishing the required electrical connection to ground under applicable procedures. | follow authorized grounding requirements
induced voltage | Voltage produced by electromagnetic influence from another source. | assess induced-voltage hazards
arc flash | A hazardous release of energy associated with an electrical arc. | assess arc-flash hazards
minimum approach distance | A required separation from electrical hazards under applicable conditions and rules. | observe the applicable minimum approach distance
qualified worker | A worker with the required training and competence for the specified task. | verify qualified-worker status
operating authority | The assigned authority to make or direct specified operational decisions. | preserve operating authority
clearance | A formal authorization or controlled status with a defined meaning under the operating procedure. | verify the clearance conditions
lockout/tagout | Procedures using locks and tags within the applicable hazardous-energy control process. | follow applicable lockout/tagout procedures
read-back | Repetition of a received message to check its accuracy. | perform an exact read-back
hold point | A boundary beyond which the affected activity must not proceed until requirements are met. | maintain the hold point
document reconciliation | Resolving conflicting information through the authorized review and record process. | complete document reconciliation
revision control | Management of document versions and their applicable status. | maintain revision control''',
    precision='Q27 and Q72 contain the same digits in a different order. That resemblance does not prove a harmless typo or identify the correct asset. Keep both references intact in the discrepancy report until authorized reconciliation is complete.',
    precision_extra='Read-back confirms what was communicated. It does not establish equipment identity, isolation, deenergized status, or authorization. No operation, testing sequence, distance, or protective-equipment selection is taught by this dialogue.',
    phrases='''State the discrepancy | The work package says Q27; the switching request says Q72.
Keep the hold explicit | The affected task remains on hold.
Avoid choosing by appearance | We have not established which identifier is correct.
Repeat the digits | I read Q two seven in the work package.
Contrast the other reference | The switching request reads Q seven two.
Preserve the documents | Do not silently change either reference.
Name the review owner | Farah will coordinate the authorized reconciliation.
Keep authority separate | This conversation does not authorize an operational action.
Check receipt | Please read back the discrepancy and task status.
Limit the repeat-back | That confirms the message, not the physical asset.
Avoid a state assumption | We cannot infer the equipment's electrical state from these labels.
Check the applicable issue | Reconcile the current documents through revision control.
Maintain role boundaries | Only the relevant authorized personnel can change the operating status.
Avoid an improvised shortcut | Familiarity with the site is not a substitute for verification.
State the next condition | The conflict must be resolved through the required process.
Close accurately | Keep the task on hold until the applicable requirements and authorization are satisfied.''',
    notes='''Two seven versus seven two | Read each digit distinctly to expose the mismatch.
Which is correct | An unresolved question, not an invitation to guess.
Remain | Preserves the existing hold instead of implying a new permission.
Coordinate | Describes responsibility for review, not automatic approval.
Does not authorize | Keeps a communication exercise outside operational instruction.
Current | Must be established through revision control, not assumed from a file name.''',
    d='''Which message preserves the discrepancy? | Work package Q27; switching request Q72; correct reference unresolved; task on hold. | Q27 is correct because it was typed first. | Q72 is correct because the numbers look familiar. | Both references mean the same equipment, so proceed. | The accurate message gives both exact identifiers and preserves the unresolved status and hold.
What should happen to the conflicting records? | Preserve them and use the authorized reconciliation process. | Quietly edit one until both match. | Delete the less convenient reference. | Replace both with a guessed asset name. | Traceable reconciliation preserves the evidence and avoids inventing a correct identifier.
Which conclusion is not supported by a read-back? | The equipment is safe to work on. | The listener heard Q27 and Q72. | The listener understood the task is on hold. | The listener knows who coordinates the review. | Communication accuracy does not establish electrical state, work safety, or operating authorization.
Which response to schedule pressure is appropriate? | The identifier conflict remains unresolved; the task stays on hold under the local process. | Proceed using whichever asset is closer. | Assume a familiar label removes the conflict. | Use the dialogue as the switching instruction. | The local hold cannot be replaced by an unverified choice or a language-practice script.''',
    dialogue='''Luis | The affected task is on hold. Our work package identifies Q two seven, but the switching request identifies Q seven two. We have not established the correct reference.
Farah | I have the [[equipment identifier::The equipment identifier distinguishes the actual asset; Q27 and Q72 cannot be treated as equivalent.]] discrepancy. Keep both references exactly as recorded while I coordinate the authorized review. This conversation does not authorize any operational action.
Luis | A colleague thinks the digits were simply transposed and wants to correct the request. That may be plausible, but we do not have a verified basis.
Farah | Do not substitute plausibility for [[document reconciliation::Document reconciliation resolves conflicting references through authorized review, not silent editing to match an assumption.]]. We need the applicable process to establish the correct information and its relationship to the physical asset, not merely make two documents look consistent.
Luis | I will preserve both documents and report the mismatch. The team knows the site well, but familiarity does not tell us which record is wrong.
Farah | Correct. The [[work package::The work package contains task information, but its identifier is not automatically correct merely because it appears first.]] may contain the error, or the associated request may. We must not give either one automatic priority just because it was the first document someone read.
Luis | Let me read the distinction again: Q two seven in the package; Q seven two in the request. The affected task remains on hold.
Farah | That [[read-back::Read-back confirms the received identifiers and task status; it does not verify the asset or provide operating permission.]] confirms the message accurately. It does not verify the physical equipment, establish its electrical state, or satisfy the separate requirements for an authorized operating decision.
Luis | I will tell the incoming lead you received the mismatch but have not released the task. Both identifiers will stay in the handover.
Farah | Keep the [[hold point::The hold point prevents the affected activity from proceeding until the specified review and authorization requirements have been satisfied.]] visible in the handover. My acknowledgement means I received the discrepancy. It is not a release, a clearance, or an instruction to perform switching.
Luis | Should I label the equipment deenergized? The public outage map shows customers without supply nearby, but that is a different source.
Farah | Do not infer [[deenergized::Deenergized status requires the applicable hazardous-energy process; an outage map or uncertain label does not establish it.]] status from an outage map or these records. The applicable hazardous-energy procedures and qualified verification govern that determination, not a communications summary.
Luis | I will leave the equipment state unconfirmed. We need to communicate the document problem, not create our own technical work sequence.
Farah | Exactly. [[Operating authority::Operating authority belongs to the people assigned the relevant decisions under the actual procedure; this dialogue does not confer it.]] remains with the relevant authorized personnel under the actual procedures. Neither our discussion nor a corrected label alone establishes every condition required for the work.
Luis | Who coordinates the next review? The incoming lead needs a named contact and a clear statement that the discrepancy remains unresolved.
Farah | I will coordinate it as the [[system operator::The system operator is the named coordinator here; accepting that role does not itself resolve the discrepancy or release the task.]] for this exchange, through the authorized process. Keep the current hold and unresolved reference in the handover, and identify any later verified decision by its record.
Luis | If a replacement file arrives, where will its authorized revision status be recorded? I do not want the crew relying on the filename alone.
Farah | Use the required [[revision control::Revision control establishes the applicable document issue and status; a newer-looking file name alone is not sufficient evidence.]] process. The relevant records must be reconciled and distributed correctly, with any operational authorization handled under its own requirements rather than implied by an attachment.
Luis | My summary is Q27 in the package, Q72 in the request, correct identifier unresolved, task on hold, and you coordinating the authorized review.
Farah | That is the right boundary. A [[switching request::A switching request asks for activity; it is not itself a verified authorized instruction to perform that activity.]] is not permission to improvise an operation. Keep the discrepancy and hold explicit until the actual procedure establishes the information and authorization required.''',
    rehearsal=['Read the corrected dialogue with Q two seven and Q seven two spoken distinctly.', 'Switch roles for turns 11-20. Keep a correct read-back separate from equipment verification or operating permission.', 'Read the checked R18/R81 exchange twice, retaining Ema as coordinator and the task hold.'],
    transfer_title='Read back another identifier conflict',
    transfer_setup='A work package says R18; its associated request says R81. The correct reference is unresolved. Coordinator Ema owns the review, and the affected task remains on hold.',
    transfer='''Lead: "The work package identifies ___." | R18 | R18 is the identifier printed in the supplied work package.
Operator: "The associated request identifies ___." | R81 | R81 is the conflicting identifier in the supplied request.
Lead: "The review coordinator is ___." | Ema | Ema is the named person coordinating this separate review.
Operator: "The affected task remains on ___." | hold | The brief preserves the task hold while the correct reference remains unresolved.'''))


BOOK['units'].append(unit(
    title='Regulatory Affairs and Rate Cases',
    scene='A proposed rate is mistaken for the current bill',
    skill='Explain a rate proposal and calculate a conditional bill example without implying approval.',
    brief='A fictional notice proposes increasing an energy charge from $0.10 to $0.105 per kWh, a 5% increase in that component. The monthly fixed charge would remain $20. The proposal is under review; neither approval nor an effective date is established. Customer adviser Hana uses a simplified 500 kWh monthly example with no taxes, credits, or other charges. At the current rates the example totals $70; under the proposal it would total $72.50 at the same usage. Customer Mr Diaz assumes his entire bill has already risen 5%. His actual account has not been reviewed.',
    cast='Hana | Customer adviser\nMr Diaz | Customer',
    culture=('Explain the number the customer will actually interpret', 'A notice may accurately describe a percentage change in one component while a reader hears a change in the whole bill. Identify the component first, then show the conditional total. Do not dismiss the misunderstanding as a failure to read carefully.'),
    a='''What is the proposal's current status? | Under review, with no approval or effective date established | Already effective for every customer | Rejected permanently | Applied only because a notice was mailed | The supplied notice describes an unapproved proposal with no established effective date.
What does the 5% figure describe? | The energy-charge rate increase from $0.10 to $0.105 per kWh | The increase in every total bill | The change in monthly usage | An increase in the fixed charge | The percentage applies to the energy rate component, while the fixed charge remains unchanged.
What is the current simplified bill at 500 kWh? | $70 | $50 | $72.50 | $73.50 | Five hundred times $0.10 is $50, plus the $20 fixed charge gives $70.''',
    vocabulary='''tariff | The applicable schedule of rates, terms, and conditions for service. | consult the current tariff
rate case | A regulatory proceeding concerning utility revenues, rates, or their allocation. | explain the rate case
public utilities commission | A regulatory body overseeing specified utility matters in its jurisdiction. | identify the public utilities commission
revenue requirement | The revenue amount considered necessary under the applicable regulatory determination. | review the revenue requirement
cost of service | Costs allocated to providing utility service under the relevant analysis. | assess cost of service
rate base | The investment value used in the applicable regulatory return calculation. | determine the rate base
rate of return | The return rate considered or allowed on the relevant investment basis. | explain the rate of return
customer class | A grouping of customers used for service or rate treatment. | identify the customer class
fixed charge | A charge not directly varying with the measured usage in the stated example. | distinguish the fixed charge
volumetric charge | A charge based on the quantity consumed or delivered. | calculate the volumetric charge
demand charge | A charge based on measured or specified demand under the applicable tariff. | explain a demand charge
ratepayer | A customer paying the regulated utility's rates. | communicate with ratepayers
filing | A formal submission to the relevant authority or proceeding. | review a regulatory filing
docket | The official record or identifier for a proceeding. | locate the docket
hearing | A formal session for evidence, argument, or public participation. | attend a regulatory hearing
effective date | The date on which an approved or applicable provision begins to operate. | verify the effective date
proposed rate | A rate submitted for consideration rather than established as current. | distinguish the proposed rate
approved rate | A rate accepted through the relevant regulatory process. | verify the approved rate
bill impact | The effect of rates and usage on a customer's total charge. | illustrate the bill impact
test year | A period used as a basis for the relevant rate-case analysis. | identify the test year
rate design | The structure by which charges are assigned and recovered from customers. | explain the rate design
rate rider | A separate adjustment or provision attached to the relevant rate structure. | identify a rate rider
intervenor | A party participating in a proceeding under its applicable rules. | identify an intervenor
usage assumption | The stated consumption level used in a calculation or example. | state the usage assumption''',
    precision='The example energy charge rises from $50 to $52.50. With the unchanged $20 fixed charge, the total rises from $70 to $72.50: $2.50, or about 3.57%, not 5%. All proposed figures are conditional.',
    precision_extra='The example holds usage at 500 kWh and excludes other charges. It does not predict the actual bill for Mr Diaz. A rate proposal, an approved rate, and a rate in effect are different statuses that must remain distinct.',
    phrases='''Name the status first | The notice describes a proposal that is still under review.
Avoid implied approval | No approval or effective date is established in this case.
Identify the component | The five percent refers to the energy-charge rate.
State the current rate | The current example rate is ten cents per kilowatt-hour.
State the proposed rate | The proposed rate is ten and a half cents per kilowatt-hour.
Keep the fixed charge | The monthly twenty-dollar fixed charge would remain unchanged.
Give the usage basis | This example holds monthly usage at five hundred kilowatt-hours.
Calculate the current component | The current energy charge is fifty dollars.
Calculate the proposed component | Under the proposal, the energy charge would be fifty-two dollars fifty.
Add the components | The example total would move from seventy dollars to seventy-two dollars fifty.
Distinguish percentage bases | That is about a 3.57 percent increase in this example total.
Preserve the condition | These figures apply only if the proposal is approved as described.
Limit the illustration | Taxes, credits, and other charges are excluded from this simplified example.
Avoid account assumptions | We have not reviewed your actual account or usage.
Offer the relevant record | The official notice and proceeding record show the proposal's status.
Close with a check | The proposal changes one rate component, not every bill by the same percentage.''',
    notes='''Would | Keeps proposed charges conditional rather than current.
Per kilowatt-hour | Identifies the usage-based unit in the rate.
At the same usage | Prevents a rate comparison from silently changing consumption.
Percentage of what | Identifies the denominator behind a percentage claim.
In this example | Limits the calculation to its supplied charges and assumptions.
Under review | Neither approved nor necessarily rejected.''',
    d='''What would the proposed energy charge be at 500 kWh? | $52.50 | $50 | $72.50 | $105 | Five hundred multiplied by $0.105 per kWh gives $52.50 before the fixed charge.
What would the simplified total be? | $72.50 | $52.50 | $73.50 | $75 | The proposed $52.50 energy charge plus the unchanged $20 fixed charge totals $72.50.
Which percentage statement is accurate? | The energy rate rises 5%; this example total rises about 3.57%. | Every total bill rises exactly 5%. | The fixed charge rises 5%. | Usage necessarily rises 5%. | The unchanged fixed charge means the total's percentage increase differs from the energy-rate increase.
Which customer statement preserves the status? | This is a conditional illustration, not an approved change to your account. | Your bill has already risen because the notice was published. | The example determines every future bill. | The proposal takes effect automatically when discussed. | The proposal remains unapproved and the actual account has not been reviewed.''',
    dialogue='''Mr Diaz | I received the notice about a five percent increase. Does that mean my whole electricity bill has already gone up by five percent this month?
Hana | The [[proposed rate::The proposed rate is under consideration; the notice does not establish approval or a current change to the customer's account.]] is still under review. No approval or effective date is established here, so the notice does not mean this change has already reached your bill.
Mr Diaz | I still want to understand the five percent figure. The notice has several numbers, and I assumed that percentage described my total.
Hana | It describes the [[volumetric charge::The volumetric charge depends on consumption; the proposed percentage increase concerns its per-kWh rate, not every component of the total bill.]] rate, from ten cents to ten and a half cents per kilowatt-hour. The separate monthly fixed charge would remain twenty dollars.
Mr Diaz | Could you show a simple example of how the energy rate combines with the other charge on a bill?
Hana | Let's use a [[usage assumption::The usage assumption fixes consumption at 500 kWh so the example isolates the proposed rate change rather than changing both rate and usage.]] of five hundred kilowatt-hours for the month. We will hold that constant and exclude taxes, credits, and other charges so the comparison is clear.
Mr Diaz | At ten cents for each of five hundred kilowatt-hours, the current energy part is fifty dollars. Then I still add the twenty-dollar monthly charge.
Hana | Correct. Including the [[fixed charge::The fixed charge is the unchanged $20 component in this example; it must be added to the energy charge to obtain the total.]], the current example totals seventy dollars. Under the proposal, the energy part would be fifty-two dollars fifty, before that same twenty dollars.
Mr Diaz | So the proposed example total would be seventy-two dollars fifty. That is two dollars fifty more than seventy, not five percent of the whole amount.
Hana | Exactly. The [[bill impact::Bill impact concerns the total charge; the example's $2.50 increase on $70 is about 3.57%, not the component rate's 5%.]] in this illustration is about three point five seven percent. The energy rate rises five percent, but the unchanged fixed charge makes the total's percentage different.
Mr Diaz | My usage is not always five hundred, and my bill has a credit line. Can we check my own account before you estimate my total?
Hana | Yes. Your [[customer class::Customer class can determine applicable rate treatment; the simplified example does not establish the terms governing Mr Diaz's actual account.]] and actual applicable terms also matter. We have not reviewed your account, so I should not present this simplified calculation as your personal bill forecast.
Mr Diaz | Where can I see whether the proposal changes or is accepted? I would prefer the official information rather than a social-media summary of the notice.
Hana | The official notice and [[docket::The docket is the proceeding's official record or identifier, allowing the customer to locate the proposal and relevant decisions.]] provide the relevant proceeding information. Follow the stated official channels; this fictional example does not supply a real filing number or a participation deadline.
Mr Diaz | And if a decision is eventually issued, I should still check what it actually approves rather than assume every part of the original request was accepted.
Hana | Correct. An [[approved rate::An approved rate is the outcome accepted through the relevant process; it need not be identical to the original proposal.]] may differ from what was proposed. The decision and applicable tariff information determine the resulting terms, not the version of the notice first circulated.
Mr Diaz | If it is approved later, how will I know which bill first uses the new rate? Is that date part of the decision?
Hana | Check the [[effective date::The effective date identifies when a provision begins to operate; the supplied case establishes neither that date nor an approval.]] rather than infer one. Here, neither approval nor that date is established, so the proposed numbers remain conditional throughout our explanation.
Mr Diaz | I can now explain it accurately: a five percent proposal for one energy-rate component, with a different percentage effect on the simplified total, and no approved change yet.
Hana | That captures the [[rate design::Rate design is the structure of charges; separating its components explains why a component-rate percentage differs from the total-bill effect.]] distinction. Keep the usage and exclusions beside the example, and use would rather than has when describing the proposal's possible effect.''',
    rehearsal=['Read the corrected exchange with the 500 kWh assumption and unchanged $20 fixed charge.', 'Switch roles; stress would for $72.50 and distinguish the 5 percent component change from the 3.57 percent total change.', 'Read the checked transfer twice using $60 current, $42 proposed energy, and $62 proposed total, still unapproved.'],
    transfer_title='Calculate another conditional example',
    transfer_setup='At 400 kWh, a simplified current bill uses $0.10 per kWh plus a $20 fixed charge. An unapproved proposal would change the energy rate to $0.105. Other charges are excluded.',
    transfer='''Adviser: "The current total is $___." | 60 | Four hundred times ten cents is forty dollars, plus twenty gives sixty.
Customer: "The proposed energy component would be $___." | 42 | Four hundred multiplied by $0.105 gives a forty-two-dollar energy charge.
Adviser: "The proposed total would be $___." | 62 | Forty-two dollars plus the unchanged twenty-dollar charge gives sixty-two.
Customer: "The proposal remains ___." | unapproved | The supplied case explicitly labels the proposed rate as unapproved.'''))

BOOK['units'].append(unit(
    title='Renewables Integration and Interconnection',
    scene='In the queue does not mean connected',
    skill='Explain renewable-project review status without confusing capacity, application progress, and operating permission.',
    brief='A fictional 120 kW rooftop solar project has submitted interconnection application Q314 and received an acknowledgement. It is in the review queue, but inverter data remain incomplete and the metering review is open. No connection approval, permission to operate, confirmed upgrade cost, or operating date has been issued. Developer Elena finds a presentation saying connection secured. Utility coordinator Amir must help replace that claim with the actual status. The 120 kW figure is proposed nameplate power, not annual energy output or a guaranteed export allowance. Applicable utility and jurisdictional requirements govern the real process.',
    cast='Elena | Project developer\nAmir | Utility interconnection coordinator',
    culture=('A milestone label can outrun the evidence', 'A project team may shorten a long status into secured to sound decisive. State the completed administrative step and the open technical questions separately. This allows a positive report of progress without implying a permission or commercial certainty that does not exist.'),
    a='''What has the project received? | An acknowledgement of application Q314 | Permission to operate | A guaranteed export allowance | A final upgrade invoice | The case establishes submission and acknowledgement, while the substantive reviews remain open.
What does 120 kW describe? | Proposed nameplate power | Annual energy in kWh | A confirmed export entitlement | The approved upgrade price | Kilowatts measure power, and the brief labels this figure as proposed nameplate capacity.
Which status is supported? | Application acknowledged; inverter data incomplete; metering review open | Connection secured with a fixed operating date | Every technical review passed | No application exists | The accurate status preserves both the completed administrative step and the unresolved reviews.''',
    vocabulary='''interconnection | The arrangement and process for connecting a generating resource to an electrical network. | review the interconnection
distributed energy resource (DER) | A generation, storage, or controllable resource connected at the distribution or customer level. | assess a distributed energy resource
photovoltaic (PV) | Relating to conversion of sunlight into electricity. | develop a photovoltaic project
nameplate capacity | The rated power capacity stated for equipment or a system on its specified basis. | state nameplate capacity
inverter | Equipment converting direct-current electricity to alternating-current electricity in the relevant application. | submit inverter data
application acknowledgement | Confirmation that a submitted application has been received. | distinguish application acknowledgement
review queue | The sequence or grouping of applications awaiting relevant review. | track the review queue
queue position | The application's place under the applicable queue rules. | confirm queue position
feasibility study | A preliminary assessment of whether and under what conditions a proposed connection may be feasible. | review a feasibility study
system impact study | Analysis of a proposed connection's effects on the electrical system. | assess the system impact study
facilities study | Review of the facilities and associated work needed for a proposed connection. | review the facilities study
hosting capacity | The ability of a network area to accommodate additional resources under defined conditions. | assess hosting capacity
export limit | A limit on the power a resource may send to the network under applicable terms. | verify the export limit
non-export arrangement | An arrangement intended to prevent export to the network under its specified controls and terms. | review a non-export arrangement
protection settings | Parameters governing relevant protective equipment behavior. | verify protection settings
metering arrangement | The equipment and terms used to measure relevant flows or usage. | confirm the metering arrangement
network upgrade | A change to network facilities required or proposed for a connection or other need. | assess network upgrades
cost allocation | Assignment of costs to the relevant parties under the applicable basis. | clarify cost allocation
interconnection agreement | The applicable agreement defining the terms of a connection. | review the interconnection agreement
permission to operate (PTO) | The required authorization to operate under the relevant utility process. | verify permission to operate
commissioning | Verification and documentation of installed-system performance under the relevant process. | coordinate commissioning
curtailment | Reduction of output below otherwise available generation under specified conditions. | explain curtailment risk
power quality | Characteristics of electrical supply or output relevant to acceptable performance. | assess power quality
reactive power | Power associated with alternating-current energy exchange in inductive or capacitive elements. | assess reactive-power requirements''',
    precision='Kilowatts describe power; kilowatt-hours describe energy over time. Proposed nameplate power does not establish annual output, hosting capacity, approved export, or permission to operate. Each needs its own basis and, where relevant, decision.',
    precision_extra='An acknowledgement records receipt. A queue position describes an administrative status under applicable rules. Neither supplies the missing inverter data, closes metering review, fixes upgrade costs, or authorizes operation.',
    phrases='''Report the completed step | Application Q314 has been submitted and acknowledged.
State the current stage | The application is in the review queue.
Correct the slide | Connection secured overstates the current status.
Name the first open item | Inverter data remain incomplete.
Name the second open item | The metering review is still open.
Separate operating permission | No permission to operate has been issued.
Define the capacity figure | The 120 kW figure is proposed nameplate power.
Avoid an energy claim | It is not annual energy output in kilowatt-hours.
Avoid an export assumption | Nameplate capacity does not establish the permitted export limit.
Keep costs qualified | Upgrade costs and their allocation are not confirmed.
Preserve timing uncertainty | No operating date has been issued.
Ask for the applicable route | Which current utility requirements govern this application?
Limit queue language | Queue status does not itself reserve an approved connection.
Coordinate the missing input | We will submit the required inverter information for review.
Avoid automatic completion | Supplying one missing document does not close every review.
Close with separate statuses | Report receipt, technical review, commercial terms, and operating permission separately.''',
    notes='''Acknowledged | Means received, not technically approved.
Secured | Can imply a completed right or commitment and is too strong here.
Remain incomplete | Identifies an unresolved information gap.
Nameplate | Describes rated power on its stated basis, not actual energy production.
Not confirmed | Preserves uncertainty about cost or timing.
Separately | Prevents one completed step from being used as evidence for unrelated approvals.''',
    d='''Which presentation line is accurate? | Q314 acknowledged; technical reviews open; no operating permission issued | Connection secured because the acknowledgement arrived | Annual output guaranteed at 120 kW | Export rights confirmed by the proposed nameplate rating | The accurate line separates receipt, ongoing review, and the absence of permission.
Which unit measures energy rather than power? | kWh | kW | MW | W | Kilowatt-hours measure energy; watts, kilowatts, and megawatts measure power.
What follows from submitting the missing inverter data? | That input can be reviewed; other requirements remain separate. | Every review automatically closes. | The system can operate immediately. | Upgrade costs become zero. | Completing one information submission does not establish outcomes for all technical or commercial matters.
Which statement about costs is supported? | Upgrade costs and allocation remain unconfirmed. | All upgrades are free because the system is rooftop solar. | The application number is the upgrade price. | Acknowledgement makes the developer's budget binding on the utility. | The brief explicitly establishes no confirmed upgrade cost or cost-allocation decision.''',
    dialogue='''Elena | The presentation says connection secured. We have an acknowledgement for Q314, but is that heading too strong?
Amir | It is. The [[application acknowledgement::Application acknowledgement confirms receipt of Q314, not connection approval or permission to operate.]] confirms receipt, not approval. Inverter data remain incomplete, the metering review is open, and no permission to operate has been issued.
Elena | Can I describe our queue status as capacity reserved, or would that imply a commitment the record does not establish?
Amir | Describe the [[review queue::The review queue identifies an administrative stage, not reserved capacity or an approved connection.]] status accurately. We have no basis here to claim reserved capacity, an approved export allowance, or a completed connection decision from that administrative step.
Elena | I will replace secured with application submitted and acknowledged, technical review ongoing. What should I say about the 120 kW figure beside the project name?
Amir | Label it proposed [[nameplate capacity::Nameplate capacity is rated power on a stated basis, not annual energy or an approved export allowance.]]. It describes power on its stated rating basis. It is not annual energy output, which would use kilowatt-hours, and it does not establish actual generation.
Elena | I will change the label. The slide currently uses the same 120 figure under annual generation, which the rating does not support.
Amir | Correct. Nor does the figure establish an [[export limit::An export limit governs power sent to the network; the proposed nameplate rating does not establish it.]]. The permitted operating arrangement depends on the applicable review and terms, not simply the size written on the proposed equipment.
Elena | The technical team is preparing the missing inverter information. I can give them the action, but I should not promise that supplying it completes every review.
Amir | Exactly. The [[inverter::Inverter data are one outstanding input; submitting them does not automatically close metering review or other requirements.]] data are one open input. The metering review remains separate, and other applicable requirements still need their own verified status under the actual utility process.
Elena | The investor slide also shows our internal operating target. We have no confirmation that the required reviews will finish by then.
Amir | Mark it as an internal target, not [[permission to operate::Permission to operate is the relevant required authorization; an internal target date does not supply it.]] or a confirmed date. In this case, no operating date has been issued, and no one should interpret the slide as authorization to energize or operate.
Elena | We should remove the claim that upgrades will cost nothing as well. I do not see any verified study or cost decision supporting that assumption.
Amir | Yes. Potential [[network upgrades::Network upgrades are changes to network facilities; their scope and cost are unconfirmed here.]] and their costs remain unconfirmed here. An application acknowledgement does not determine whether upgrades are needed or which party would pay for them.
Elena | I will separate the engineering questions from the commercial ones. A technical answer might identify work, but the responsibility for its cost still needs its own basis.
Amir | That is the [[cost allocation::Cost allocation assigns costs to parties; identifying technical work does not itself settle who pays.]] distinction. Use the applicable rules and agreements rather than assume that a rooftop project, a queue position, or a proposed budget settles responsibility.
Elena | What can I put in the next-actions box? The investors need to see which submission our team is preparing and which review remains open.
Amir | Say the team is submitting the missing data for review while the [[metering arrangement::The metering arrangement remains under review, separate from the completed administrative receipt of the application.]] is being assessed. That is concrete progress, with the open items visible, and does not imply that either review has reached a favorable decision.
Elena | My revised slide will distinguish proposed power, acknowledged application, open technical items, unconfirmed costs and timing, and the absence of operating permission.
Amir | Good. The eventual [[interconnection agreement::The interconnection agreement sets connection terms, distinct from the application and any separate operating requirements.]] and required operating authorizations each need their actual status reported. Do not let a short heading collapse all those stages into one unsupported claim.''',
    rehearsal=['Read the corrected conversation, labeling 120 kW as proposed nameplate power.', 'Switch roles for turns 11-20; separate an internal target, upgrade cost allocation, and operating permission.', 'Read the checked Z206 transfer twice with 75 kW and the open metering review. Do not invent annual generation.'],
    transfer_title='Report another application stage',
    transfer_setup='A proposed 75 kW project has acknowledgement for application Z206. Metering review is open, and no permission to operate is issued.',
    transfer='''Developer: "The application reference is ___." | Z206 | Z206 is the identifier supplied for the separate acknowledged application.
Coordinator: "The proposed nameplate power is ___ kW." | 75 | Seventy-five is the proposed power rating, not annual energy output.
Developer: "Metering review remains ___." | open | The case explicitly identifies metering review as still open.
Coordinator: "Permission to operate is ___." | unissued | The brief says no permission to operate has been issued.'''))


BOOK['units'].append(unit(
    title='Asset Management and Maintenance',
    scene='The cheapest purchase is not the cheapest comparison',
    skill='Compare a stated cost basis, test an assumption, and keep the purchase decision separate from partial arithmetic.',
    brief='Two fictional asset options are compared over ten years. Option A costs $10,000 to purchase and $2,000 per year in maintenance. Option B costs $14,000 to purchase and $1,000 per year in maintenance. The exercise uses constant annual amounts and no discounting. Installation, energy, downtime, disposal, residual value, and technical equivalence have not been assessed. Analyst Sam finds a slide calling A the lowest-cost choice because its purchase price is lower. Asset manager Priya requests a purchase-and-maintenance comparison, with its limits stated. Neither option is approved for purchase.',
    cast='Sam | Asset analyst\nPriya | Asset manager',
    culture=('Challenge the comparison, not the budget owner', 'A low initial price can be attractive when a team faces a tight annual budget. Show which costs the slide includes before challenging its conclusion. A transparent comparison lets colleagues discuss affordability and long-term cost as related but different questions.'),
    a='''What is Option A's ten-year purchase-and-maintenance total? | $30,000 | $12,000 | $20,000 | $10,000 | Ten years of $2,000 maintenance plus the $10,000 purchase equals $30,000.
What is Option B's corresponding total? | $24,000 | $15,000 | $14,000 | $30,000 | Ten years of $1,000 maintenance plus the $14,000 purchase equals $24,000.
What does the supplied comparison establish? | B is $6,000 lower on this limited undiscounted basis. | B is approved for purchase. | A is technically inferior. | All possible ownership costs are included. | The arithmetic favors B on the stated basis but excludes several costs and technical questions.''',
    vocabulary='''asset management | Coordinating asset decisions across performance, risk, cost, and life. | develop an asset-management plan
purchase price | The amount paid to acquire an asset. | compare purchase prices
capital expenditure (CAPEX) | Spending on acquiring or improving long-lived assets under the applicable accounting treatment. | assess capital expenditure
operating expenditure (OPEX) | Costs of operating the business or assets under the relevant accounting treatment. | forecast operating expenditure
preventive maintenance | Planned maintenance intended to reduce failures or deterioration. | schedule preventive maintenance
corrective maintenance | Maintenance performed to address an identified fault or failure. | track corrective maintenance
condition-based maintenance | Maintenance guided by evidence of the actual asset condition. | evaluate condition-based maintenance
maintenance interval | The period or usage between planned maintenance actions. | review the maintenance interval
recurring cost | A cost expected to occur repeatedly over a period. | estimate recurring costs
assessment horizon | The period over which options are evaluated. | define the assessment horizon
life-cycle cost | Cost across the relevant stages of an asset's life on a defined basis. | assess life-cycle cost
total cost of ownership | The included acquisition, operation, maintenance, and other ownership costs over a stated period. | compare total cost of ownership
downtime | Time during which an asset is unavailable for its intended service. | account for downtime
failure mode | A particular way an asset or component can fail. | assess a failure mode
asset criticality | The importance of an asset based on the consequences of its failure or unavailability. | assess asset criticality
remaining useful life | The estimated period of useful service still available from an asset. | estimate remaining useful life
replacement cycle | The timing or pattern used to replace assets. | plan the replacement cycle
residual value | The value remaining at the end of the assessment period. | estimate residual value
disposal cost | The cost of removing or disposing of an asset at the relevant stage. | include disposal costs
discounted cash flow | Evaluation of future cash flows using an explicit discount-rate basis. | distinguish discounted cash flow
sensitivity analysis | Testing how a result changes when an assumption changes. | run a sensitivity analysis
technical equivalence | Comparable ability to meet the specified technical requirements. | establish technical equivalence
cost boundary | The set of costs included or excluded from an analysis. | state the cost boundary
decision criteria | The factors used to assess and choose among alternatives. | agree decision criteria''',
    precision='A totals $30,000 and B totals $24,000 on the supplied purchase-and-maintenance basis. B is $6,000 lower despite its $4,000 higher purchase price. Neither number is a complete life-cycle estimate.',
    precision_extra='If B maintenance were $1,600 per year instead, its ten-year total would be $30,000, equal to A on this limited basis. That sensitivity result changes no technical finding and does not approve either purchase.',
    phrases='''Identify the narrow comparison | The slide compares purchase prices only.
State the higher upfront amount | B costs four thousand dollars more to purchase.
Name the horizon | We are comparing ten years.
Explain the recurring cost | A has two thousand dollars of annual maintenance.
Calculate A | Ten thousand plus ten times two thousand gives thirty thousand dollars.
Calculate B | Fourteen thousand plus ten times one thousand gives twenty-four thousand dollars.
State the limited result | B is six thousand dollars lower on this purchase-and-maintenance basis.
Preserve the exclusions | Installation, energy, downtime, disposal, and residual value are excluded.
Avoid a broad label | This is not a complete life-cycle-cost comparison.
Name the financial assumption | The figures are undiscounted and use constant annual amounts.
Check technical suitability | Technical equivalence remains unassessed.
Test an assumption | At sixteen hundred dollars a year, B's maintenance changes the comparison.
State the sensitivity result | B would then total thirty thousand dollars over ten years.
Separate affordability | A lower upfront price and a lower long-term total are different considerations.
Avoid an approval claim | Neither option is approved for purchase.
Close with the decision basis | Present the arithmetic, exclusions, and unresolved decision criteria together.''',
    notes='''On this basis | Limits a result to the included costs and assumptions.
Upfront | Refers to the initial expenditure, not the total over time.
Per year | Must be multiplied by the stated number of years.
Undiscounted | Does not adjust future amounts to a present-value basis.
Would then | Marks an alternative assumption rather than the original estimate.
Unassessed | Keeps technical suitability separate from the cost calculation.''',
    d='''Why is lowest-cost choice unsupported for A? | It uses purchase price while ignoring the supplied recurring maintenance difference. | A has no purchase price. | Ten-year costs must always equal the initial payment. | B has already been selected by engineering. | A is cheaper upfront, but the supplied ten-year maintenance comparison favors B.
At $1,600 annual maintenance, what would B total over ten years? | $30,000 | $16,000 | $15,600 | $24,000 | Fourteen thousand plus ten times sixteen hundred equals thirty thousand dollars.
Which label fits the original calculation? | Ten-year undiscounted purchase-and-maintenance comparison | Complete discounted life-cycle cost | Confirmed procurement approval | Verified technical-equivalence assessment | The calculation includes only the stated purchase and maintenance amounts without discounting.
What remains necessary before a full decision? | Assess omitted costs, technical suitability, and the relevant decision criteria. | Choose B automatically because one subtotal is lower. | Choose A automatically because its first payment is lower. | Assume all omitted costs are zero. | The limited arithmetic leaves material financial and technical matters unresolved.''',
    dialogue='''Sam | A costs ten thousand upfront and B fourteen thousand. The slide calls A the lowest-cost choice. Is that too broad?
Priya | Yes. It compares [[purchase price::Purchase price is the acquisition amount only; the slide incorrectly uses it to describe the entire cost choice.]], not the full cost basis. Both options have recurring maintenance, and their annual amounts differ enough to change the longer comparison.
Sam | A needs two thousand dollars a year in maintenance; B needs one thousand. We are using ten years and constant annual figures, without discounting.
Priya | Keep that [[assessment horizon::The assessment horizon is the ten-year period used to multiply recurring annual costs and compare the options.]] visible. For A, ten thousand plus ten times two thousand gives thirty thousand dollars. We should not compare ten years of one option with one year of another.
Sam | B totals twenty-four thousand: fourteen thousand plus ten times one thousand. That is six thousand lower on this basis.
Priya | Correct. The [[recurring cost::The recurring maintenance cost accumulates over the ten-year period and reverses the ranking based on purchase price alone.]] reverses the purchase-price ranking. But describe that as a purchase-and-maintenance result, not proof that B is the best asset for every purpose.
Sam | The calculation leaves out installation, energy, downtime, disposal, and residual value. We also have not established that both options satisfy the technical requirements equally.
Priya | State the [[cost boundary::The cost boundary identifies included and excluded costs, preventing the partial comparison from appearing to cover all ownership effects.]] beside the totals. An omitted cost is not automatically zero. The audience should see what this comparison answers and what still requires assessment.
Sam | I will label this purchase and maintenance, not complete ownership cost.
Priya | Exactly. [[Total cost of ownership::Total cost of ownership requires an explicit scope of relevant ownership costs; this exercise supplies only purchase and maintenance.]] needs an explicit scope and period. Our figures cover only two categories, so we should not imply that all relevant ownership effects have been evaluated.
Sam | The maintenance forecast is uncertain. Could we test a different amount for B to show how sensitive the result is to that assumption?
Priya | Use a [[sensitivity analysis::Sensitivity analysis changes an assumption to test its effect; here it examines a higher annual maintenance amount for B.]]. At sixteen hundred dollars a year, B's ten-year maintenance is sixteen thousand, bringing its total with purchase to thirty thousand dollars.
Sam | That would match A on this limited basis. It would not prove the two options have identical performance, risks, or costs outside the comparison.
Priya | Correct. [[Technical equivalence::Technical equivalence concerns ability to meet the required performance, which financial equality on a limited basis does not establish.]] remains unassessed. A matching subtotal does not tell us whether either option meets the required duty, reliability, operating conditions, or other technical criteria.
Sam | We also have no residual-value estimate. One asset might retain more value at the end of ten years, but we cannot assume an amount.
Priya | Keep [[residual value::Residual value is the value remaining at the assessment horizon; it is excluded and has not been estimated here.]] among the exclusions. The same applies to disposal costs and downtime. We need their actual basis before including them in a wider analysis.
Sam | The heading says present value, but we have only added the amounts. I will need to correct that heading too, unless a separate discounted analysis is available.
Priya | No. This is not [[discounted cash flow::Discounted cash flow uses an explicit discount-rate basis for future amounts; the supplied arithmetic deliberately does not do that.]]. We have not applied a discount rate. Use undiscounted purchase-and-maintenance comparison so the heading does not promise an analysis we did not perform.
Sam | I will show A at thirty thousand and B at twenty-four thousand, with the alternative B-maintenance case, exclusions, and no purchase approval.
Priya | Good. Put the unresolved [[decision criteria::Decision criteria include the factors needed for the actual choice; limited cost arithmetic does not settle every financial or technical consideration.]] beside those figures. Affordability, technical suitability, risk, and the wider cost basis remain part of the actual decision, not assumptions hidden by a low price.''',
    rehearsal=['Read the corrected dialogue with $30,000 for A and $24,000 for B over ten years.', 'Switch roles; explain the $1,600 annual-maintenance sensitivity without implying technical equivalence.', 'Read the checked C/D exchange twice. Keep the five-year, undiscounted, purchase-and-maintenance basis explicit.'],
    transfer_title='Compare the same included costs',
    transfer_setup='Over five years, C costs $8,000 plus $1,000 annual maintenance. D costs $10,000 plus $400 annual maintenance. Use undiscounted purchase and maintenance only.',
    transfer='''Analyst: "C totals $___." | 13,000 | Eight thousand plus five years at one thousand equals thirteen thousand.
Manager: "D totals $___." | 12,000 | Ten thousand plus five years at four hundred equals twelve thousand.
Analyst: "D is $___ lower on this basis." | 1,000 | The difference between thirteen thousand and twelve thousand is one thousand.
Manager: "The comparison excludes ___ costs." | other | The setup includes purchase and maintenance only, leaving other cost categories outside the calculation.'''))

BOOK['units'].append(unit(
    title='Emergency Preparedness and Storm Response',
    scene='Requested resources are not all available',
    skill='Hand over storm-response resources with exact counts, distinct statuses, and a clear receiving owner.',
    brief='At the 19:30 local coordination handover, six external crews have been requested. Three are confirmed: one is at the staging location and two are en route. The other three remain unconfirmed. Twenty lodging spaces were requested; twelve are confirmed and eight are pending. Arrival times for the two traveling crews are not verified. Outgoing coordinator Daniel hands over to Sofia, who accepts tracking the open requests and providing the next status update at 20:00. Confirmed, arrived, briefed, and authorized for deployment are separate stages; this record establishes no new operational assignment or restoration promise.',
    cast='Daniel | Outgoing logistics coordinator\nSofia | Incoming logistics coordinator',
    culture=('Totals can hide different stages', 'A fast handover often compresses requested, confirmed, and arrived into available. Use the categories explicitly and check whether one count is a subset of another. A concise but structured read-back is more useful than a larger total that double-counts people or resources.'),
    a='''How many requested crews are confirmed? | Three | Six | Five | One | The brief confirms three of the six requested crews, with three still unconfirmed.
How many of the confirmed crews have arrived at staging? | One | Three | Two | Six | One confirmed crew is at staging; the other two confirmed crews are en route.
How many lodging spaces remain pending? | Eight | Twelve | Twenty | Three | Twenty were requested and twelve confirmed, leaving eight spaces pending.''',
    vocabulary='''emergency operations center (EOC) | A location or function coordinating information and resources during an emergency. | support the emergency operations center
incident command | The authority structure directing an incident response under the applicable system. | coordinate with incident command
mutual assistance | Support provided by other organizations under applicable arrangements. | request mutual assistance
resource request | A documented request for specified people, equipment, or support. | track a resource request
resource confirmation | Verification that the requested resource is committed on stated terms. | obtain resource confirmation
staging location | A designated place where resources assemble before further assignment. | report arrival at staging
mobilization | Preparing and moving resources for an assigned response. | track mobilization status
demobilization | Organized release and return of resources when no longer required. | plan demobilization
en route | Traveling toward the relevant destination, not yet arrived. | report crews en route
estimated time of arrival (ETA) | An estimate of when a person or resource will reach a destination. | verify the estimated time of arrival
deployment authorization | Permission to assign or send resources to specified work under the applicable process. | verify deployment authorization
crew roster | A list of personnel assigned to a crew or response. | reconcile the crew roster
credential verification | Checking the relevant qualifications or authorizations of personnel. | complete credential verification
shift handover | Transfer of current information and responsibilities between shifts. | conduct a shift handover
operational period | A defined interval used for response planning and coordination. | identify the operational period
situation report | A structured update of current conditions, actions, and resource status. | issue a situation report
logistics | Coordination of resources, movement, accommodation, and other support. | coordinate response logistics
lodging allocation | Assignment of accommodation capacity to the relevant personnel. | confirm lodging allocation
resource shortfall | The gap between required or requested resources and those available or confirmed. | identify a resource shortfall
fatigue management | Arrangements to address risks arising from tiredness and work-rest demands. | follow fatigue-management requirements
communications plan | The defined channels, contacts, and arrangements for response communication. | follow the communications plan
access restriction | A limitation on entry or movement in an affected area. | verify access restrictions
request owner | The named person responsible for following up a request. | identify the request owner
status reconciliation | Checking that different reports describe the same resources without conflict or duplication. | complete status reconciliation''',
    precision='The one arrived crew and two en-route crews are subsets of the three confirmed crews. They are not three additional crews. Six requested minus three confirmed leaves three requests unconfirmed.',
    precision_extra='Twelve confirmed lodging spaces are not twenty available spaces. Likewise, crew arrival does not automatically establish briefing, qualification checks, or deployment authorization. The next update time does not promise that the remaining resources will be confirmed.',
    phrases='''Timestamp the handover | This is the resource position at 19:30 local time.
State the request total | Six external crews were requested.
Separate confirmations | Three crews are confirmed and three remain unconfirmed.
Break down the confirmed group | One confirmed crew is at staging and two are en route.
Avoid double counting | Those three statuses describe the same confirmed group.
Qualify arrival timing | Arrival times for the traveling crews are not verified.
State lodging demand | Twenty lodging spaces were requested.
State lodging confirmation | Twelve spaces are confirmed and eight remain pending.
Name the receiving owner | Sofia has accepted tracking the open requests.
Separate acceptance from supply | Accepting the handover does not confirm the missing resources.
Set the communication time | The next status update is at 20:00 local time.
Avoid an availability claim | Requested does not mean available for deployment.
Preserve operational boundaries | Arrival at staging does not itself authorize a work assignment.
Keep categories consistent | Use requested, confirmed, en route, and arrived as separate status fields.
Report unchanged conditions | The next update will include unresolved requests even if their status is unchanged.
Close with read-back | Please repeat the crew counts, lodging counts, owner, and next update time.''',
    notes='''Of the three | Signals a subset rather than an additional count.
En route | Indicates travel, not confirmed arrival.
Pending | Keeps a request open rather than silently treating it as supplied.
Accepted tracking | Transfers follow-up responsibility without creating a supplier commitment.
As of 19:30 | Prevents the handover snapshot from appearing timeless.
At 20:00 | Commits to an update, not to resolving every resource shortfall.''',
    d='''Which crew summary avoids double counting? | Six requested; three confirmed, comprising one arrived and two en route | Six requested; six confirmed because three plus one plus two equals six | One confirmed because only one has arrived | Nine requested because three are confirmed | The arrived and en-route counts are subsets of the three confirmed crews.
Which lodging statement is supported? | Twelve confirmed; eight pending from a request for twenty | Twenty available because twenty were requested | Eight confirmed and twelve canceled | Twelve confirmed plus twenty more confirmed | The brief gives twenty requested and twelve confirmed, leaving eight pending.
What does the 20:00 commitment promise? | A new status update | All crews arriving | All lodging confirmed | Restoration of every affected service point | Sofia accepts a communication commitment, not a guarantee of resource delivery or service restoration.
What follows from a crew arriving at staging? | Arrival is established, while other required deployment stages remain separate. | Every operational assignment is automatically authorized. | All credentials are verified without review. | The crew counts twice in the confirmed total. | Arrival does not itself establish briefing, qualification verification, or authorization for work.''',
    dialogue='''Daniel | This is the resource position at nineteen thirty local time. Six external crews were requested, and three are confirmed. I need to hand over the remaining requests.
Sofia | I will accept the [[shift handover::The shift handover transfers information and responsibility without changing the actual confirmation or arrival status of resources.]]. First, break down those three confirmed crews. I want to distinguish who has arrived from who is still traveling before I update the situation report.
Daniel | One is at staging and two are en route. Three requested crews remain unconfirmed. Arrival times for the traveling crews are unverified.
Sofia | So the [[en route::En route means traveling; these two confirmed crews have not yet arrived at staging.]] group is part of the three confirmed, not an additional two. I will not add one arrived and two traveling to the confirmed total again.
Daniel | Please correct the earlier six-available line. It appears to count the same three crews twice, once as confirmed and again by travel status.
Sofia | I will correct the [[situation report::The situation report must preserve actual categories and counts, correcting the unsupported claim of six available crews.]]. It should show six requested, three confirmed, and three unconfirmed, with the arrival breakdown nested within the confirmed group.
Daniel | Lodging also needs a qualification: twenty spaces requested, twelve confirmed, eight pending. The request remains open.
Sofia | I will record that [[resource shortfall::The resource shortfall is requested minus confirmed capacity, here eight pending lodging spaces.]] explicitly. A request for twenty does not mean twenty spaces are available, and we should not assign accommodation on the basis of the request alone.
Daniel | Please take ownership of both the unconfirmed crews and the pending lodging spaces. I want the outgoing record to identify who is following them up.
Sofia | I accept that as the [[request owner::The request owner accepts follow-up responsibility, which does not itself confirm the missing crews or lodging.]]. My acceptance transfers coordination responsibility, not supplier confirmation. The open requests remain open until their status is verified and recorded.
Daniel | When is your next update? The coordination lead needs a consistent time to refresh the resource summary across the response team.
Sofia | Twenty hundred local time. I will provide a [[status reconciliation::Status reconciliation checks consistent resource reporting and prevents duplicate counting before the next update.]] then, including any requests still unresolved. That is an information commitment, not a promise that every crew or lodging space will be confirmed.
Daniel | The crew at staging has arrived, but this snapshot says nothing about its briefing, qualification checks, or an authorized work assignment. Please keep those stages separate.
Sofia | Agreed. Arrival at the [[staging location::The staging location is an assembly point; arrival does not establish readiness or deployment authorization.]] is not permission to deploy. I will leave the applicable operational checks and assignments with the authorized response process rather than infer them from presence.
Daniel | Someone may ask whether these crews will restore a neighborhood tonight. Our logistics counts cannot support that promise, and no such assignment is established.
Sofia | Correct. [[Deployment authorization::Deployment authorization permits specified work; the logistics snapshot supplies neither that authorization nor a restoration promise.]] and restoration planning are separate operational matters. I can report the resource status without claiming when any particular service point will be restored.
Daniel | The next shift also asked when the two traveling crews will arrive. I have no verified ETA to hand over.
Sofia | I will mark the [[estimated time of arrival::Estimated time of arrival concerns reaching the destination; confirmed participation does not establish that estimate.]] as unverified. Any update needs its source and time basis, particularly if access restrictions or other conditions change during the response.
Daniel | Please read the final numbers back so I can close the administrative handover without leaving a different version in my outgoing report.
Sofia | Six crews requested, three confirmed: one at staging, two en route. Three unconfirmed. [[Lodging allocation::Lodging allocation must use confirmed capacity: twelve spaces are confirmed, with eight still pending.]] is twelve confirmed, eight pending. I own follow-up and will update at twenty hundred local time.''',
    rehearsal=['Read the corrected dialogue with one arrived plus two en route within the three confirmed crews.', 'Switch roles; distinguish 12 confirmed lodging spaces from 20 requested and 20:00 from an arrival promise.', 'Read the checked transfer twice using five confirmed crews, three unconfirmed, 14 lodging spaces, and four still needed.'],
    transfer_title='Count subsets only once',
    transfer_setup='Eight crews are requested; five confirmed crews comprise two at staging and three en route. Three remain unconfirmed. Eighteen lodging spaces are requested and fourteen confirmed.',
    transfer='''Coordinator: "The confirmed crew total is ___." | five | Two at staging plus three en route make five confirmed crews.
Receiver: "The unconfirmed crew count is ___." | three | Eight requested minus five confirmed leaves three unconfirmed crews.
Coordinator: "Confirmed lodging spaces total ___." | fourteen | Fourteen is the supplied count of confirmed accommodation spaces.
Receiver: "The lodging shortfall is ___ spaces." | four | Eighteen requested minus fourteen confirmed leaves four spaces pending.'''))


BOOK['units'].append(unit(
    title='Customer Programs and Energy Efficiency',
    scene='Lower consumption does not isolate the program effect',
    skill='Report an observed energy reduction while separating measurement, explanation, and verified savings.',
    brief='A fictional office used 10,000 kWh in a baseline month and 8,500 kWh in a post-installation month after an efficiency retrofit. Both readings cover 30 days. The second month had milder weather and average daily occupancy fell from 40 to 30 people. No adjusted baseline or agreed savings-verification analysis has been completed. Program specialist Leila finds a draft claiming the retrofit proved 15% savings and a 15% bill reduction. Analyst Victor must help report the observed 1,500 kWh, or 15%, consumption decline without assigning the entire change to the retrofit. Rates and bill components are not supplied.',
    cast='Leila | Efficiency program specialist\nVictor | Energy analyst',
    culture=('A qualified result can still be useful', 'Teams may feel pressure to turn a promising result into a simple success claim. State the observed change clearly, then name the factors that prevent stronger attribution. This preserves useful evidence without treating either enthusiasm or skepticism as a substitute for analysis.'),
    a='''What measured energy change is supplied? | A 1,500 kWh reduction, equal to 15% of baseline use | A proved 15% retrofit effect | A guaranteed 15% bill reduction | A 1,500 kW fall in peak demand | Ten thousand minus 8,500 is 1,500 kWh, which is 15% of the baseline 10,000.
Which other conditions changed? | Weather and occupancy | Only the equipment, with all conditions fixed | The reading period from 30 to 60 days | The currency used on the bill | The brief states milder weather and a fall in average daily occupancy from forty to thirty.
What has not been completed? | An adjusted baseline and savings-verification analysis | The two monthly readings | Identification of the reading periods | The arithmetic difference between the readings | The observations exist, but the analysis needed to isolate a savings effect remains incomplete.''',
    vocabulary='''energy efficiency | Providing the relevant service with less energy under a defined comparison. | improve energy efficiency
energy conservation | Reducing energy use through changes in behavior, service, or activity. | encourage energy conservation
retrofit | A modification or addition to improve an existing system or building. | assess an efficiency retrofit
energy conservation measure (ECM) | A defined intervention intended to reduce energy or related resource use. | evaluate an energy conservation measure
baseline period | The reference period used to establish pre-intervention conditions or use. | define the baseline period
reporting period | The period for which performance or results are being assessed. | identify the reporting period
metered consumption | Energy use measured by the relevant meter over a stated interval. | compare metered consumption
measurement and verification (M&V) | A defined process for assessing and verifying savings against an appropriate basis. | develop a measurement and verification plan
adjusted baseline | Reference use adjusted to relevant comparison conditions under an explicit method. | calculate an adjusted baseline
weather normalization | Adjusting energy analysis to a defined weather basis. | apply weather normalization
heating degree days | A weather indicator based on temperature relative to a specified heating reference. | use heating degree days
cooling degree days | A weather indicator based on temperature relative to a specified cooling reference. | use cooling degree days
occupancy | The presence or number of people using a space over a defined basis. | track occupancy changes
operating hours | The time during which a facility or system is operated. | document operating hours
independent variable | An input used to explain variation in another measured quantity. | identify relevant independent variables
confounding factor | A factor that complicates attribution of an observed change to one cause. | account for confounding factors
attribution | Assigning an observed effect to a particular cause or intervention. | qualify savings attribution
avoided energy use | Energy estimated not to have been used compared with an appropriate counterfactual basis. | estimate avoided energy use
gross savings | Savings associated with an intervention before specified program-attribution adjustments. | distinguish gross savings
net savings | Program savings after the relevant adjustments for attribution and other specified effects. | assess net savings
rebound effect | Increased use of a service that may offset some expected efficiency savings. | assess the rebound effect
persistence | The extent to which an effect continues over time. | evaluate savings persistence
uncertainty | The limits on confidence or precision in an estimate or conclusion. | report savings uncertainty
bill savings | A reduction in monetary charges under the relevant rates and billing conditions. | distinguish bill savings''',
    precision='The observed reduction is 1,500 kWh divided by the baseline 10,000 kWh, or 15%. It is measured consumption change, not yet a verified retrofit effect. Milder weather and lower occupancy also changed the comparison.',
    precision_extra='Energy savings and bill savings are not interchangeable. Prices, fixed charges, demand charges, and other billing components can affect the money paid. This case supplies no rate information, so it supports no bill-savings percentage.',
    phrases='''State the readings | Consumption fell from ten thousand to eight thousand five hundred kilowatt-hours.
Name the period | Both readings cover thirty days.
Calculate the difference | The observed reduction is fifteen hundred kilowatt-hours.
State the denominator | That is fifteen percent of baseline consumption.
Qualify attribution | We cannot assign the whole decline to the retrofit from these readings alone.
Name the weather change | The reporting month had milder weather.
Name the occupancy change | Average daily occupancy fell from forty to thirty people.
Avoid a false constant | The comparison conditions were not unchanged.
Identify the missing analysis | An adjusted baseline and verification analysis have not been completed.
Distinguish the measures | Lower energy use does not automatically mean the same percentage reduction in the bill.
Preserve the unit | These figures are energy in kilowatt-hours, not peak power in kilowatts.
Correct the claim | Replace proved savings with observed consumption reduction.
Keep the result useful | The decline is real in the supplied readings, while its causes remain to be assessed.
State the method boundary | Use the applicable measurement and verification plan for a verified savings claim.
Avoid invented adjustments | Do not subtract an assumed weather effect without a supported method.
Close with the evidence | Report the readings, changed conditions, and unresolved attribution together.''',
    notes='''Fell from | Describes an observed change without assigning its cause.
Because of | Adds a causal claim that these readings alone do not establish.
Of baseline | Identifies the denominator for the 15% calculation.
Same period length | Removes one difference but does not make all conditions comparable.
Not yet verified | Does not mean that the intervention had no effect.
Energy versus money | Distinguishes consumption units from the monetary bill.''',
    d='''Which headline is supported? | Metered use fell 15%; retrofit attribution remains unverified. | Retrofit proved exactly 15% savings. | Every customer bill will fall 15%. | Peak demand fell 1,500 kW. | The readings support a consumption decline but not the causal, billing, or peak-demand claims.
Why do equal 30-day periods not settle attribution? | Weather and occupancy still differed. | Equal periods make all other factors identical. | Thirty days always proves program savings. | The meter must be wrong if conditions changed. | Equal duration controls one comparison feature but does not remove the stated weather and occupancy differences.
What is the occupancy decline? | 25%, from 40 to 30 people | 10%, because ten people fewer means ten percent | 15%, matching the energy decline | 33.3% of the original forty | Ten fewer divided by the original forty equals twenty-five percent.
Which bill statement is justified? | Bill savings cannot be calculated from the supplied information. | The bill necessarily fell by 15%. | The fixed charge necessarily disappeared. | A kilowatt-hour equals a dollar. | Rates and billing components are missing, so consumption figures alone do not determine monetary savings.''',
    dialogue='''Leila | The draft says our retrofit proved fifteen percent energy savings and the same reduction in bills. The meter readings fell, but can we support both claims?
Victor | We can support the [[metered consumption::Metered consumption fell by 1,500 kWh; those observations alone do not establish the cause.]] change: ten thousand to eight thousand five hundred kilowatt-hours. That is fifteen hundred less, or fifteen percent of the original reading.
Leila | Both readings cover thirty days. I initially thought matching the period length meant we could attribute the whole difference to the equipment installed between them.
Victor | It removes one difference, but the [[reporting period::The reporting period had different weather and occupancy; equal duration does not make all conditions comparable.]] had milder weather and fewer occupants. Those changes can affect energy use, so the conditions were not otherwise held constant.
Leila | Average daily occupancy fell from forty to thirty people. That is ten fewer, or twenty-five percent of the original forty, not a ten percent change.
Victor | Correct. [[Occupancy::Occupancy fell from forty to thirty people; its contribution to the energy decline requires analysis.]] is a separate measured condition. We cannot assume its effect on energy is proportional to the headcount change or simply subtract twenty-five percent.
Leila | So we should not try to correct the energy result with a guessed number for people, then assign whatever remains to the retrofit.
Victor | Exactly. An [[adjusted baseline::An adjusted baseline represents reference use under relevant comparison conditions using an explicit method, not arbitrary subtraction.]] needs an explicit, supported method. It is not an informal subtraction that makes the result fit the program story.
Leila | The weather changed too. The second month was milder, but we have not quantified the resulting heating or cooling effect in this analysis.
Victor | [[Weather normalization::Weather normalization adjusts analysis to a defined weather basis; it has not been completed here.]] may form part of the applicable method. The appropriate approach must be established from the project and data, not improvised from the word milder.
Leila | I do not want to discard the meter result. Can the headline state the fifteen-percent consumption decline and flag the attribution separately?
Victor | Say observed consumption fell fifteen percent, with [[attribution::Attribution concerns how much change is due to the retrofit; that causal question remains unresolved.]] to the retrofit unverified. That preserves both the measured result and the limit on what it demonstrates about the intervention.
Leila | The program manager heard unverified as no benefit. Please help me correct that impression without claiming an effect we have not measured.
Victor | No. [[Uncertainty::Uncertainty limits the supported conclusion; it is not proof that the retrofit had no benefit.]] is not a finding of zero benefit. We have not isolated the effect, and that means we should avoid both an exact success claim and an unsupported dismissal.
Leila | The monetary claim needs correcting as well. We have no rates, fixed charges, credits, demand charges, or other billing information in the supplied case.
Victor | Then we cannot calculate [[bill savings::Bill savings concerns money under actual billing conditions; missing rates and charges prevent a supported percentage.]]. A fifteen percent energy decline does not automatically produce a fifteen percent bill decline, even when the energy readings themselves are accurate.
Leila | I will keep the units visible. Kilowatt-hours measure the energy used over the period; these monthly readings do not establish what happened to peak demand.
Victor | Good. The [[measurement and verification::Measurement and verification supplies the defined basis for assessing savings and must address relevant comparison conditions.]] process needs the relevant comparison conditions and method. Our immediate communication should identify the missing analysis rather than invent its outcome.
Leila | The revised summary will give both readings, the equal thirty-day periods, the weather and occupancy changes, and the fact that no adjusted analysis is complete.
Victor | That makes the [[confounding factors::Confounding factors complicate attribution, here weather and occupancy changes occurring alongside the retrofit.]] visible. Keep the fifteen percent as an observed consumption reduction, not a certified savings result or a promise about future bills.''',
    rehearsal=['Read the corrected dialogue with 1,500 kWh and 15 percent as the observed consumption decline.', 'Switch roles; distinguish the 25 percent occupancy decline from an unmeasured energy effect.', 'Read the checked transfer twice with 1,200 kWh and 10 percent, preserving unverified attribution and unavailable bill savings.'],
    transfer_title='Report a decline without inventing its cause',
    transfer_setup='Two equal-length periods show 12,000 and 10,800 kWh. Weather and operating hours changed. No adjusted analysis or billing rates are supplied.',
    transfer='''Analyst: "The observed reduction is ___ kWh." | 1,200 | Twelve thousand minus ten thousand eight hundred equals twelve hundred kilowatt-hours.
Manager: "That equals ___ percent of baseline use." | 10 | Twelve hundred divided by twelve thousand equals ten percent.
Analyst: "Attribution to the intervention remains ___." | unverified | Changed conditions and missing adjusted analysis prevent verified causal attribution.
Manager: "Monetary bill savings are not ___." | calculable | The case supplies no billing rates or other information needed for monetary savings.'''))

BOOK['units'].append(unit(
    title='Executive Reliability and Investment Updates',
    scene='Fewer interruptions, more total outage minutes',
    skill='Translate reliability indices, check a comparison, and distinguish a metric trend from an investment promise.',
    brief='A fictional utility serves 1,000 customers in each of two years. Using the same sustained-interruption definitions and event coverage, Year 1 records 1,200 customer interruptions and 90,000 customer-minutes interrupted. Year 2 records 1,000 customer interruptions and 120,000 customer-minutes interrupted. The same major-event treatment applies in both years. Analyst Ravi presents the results to community liaison Celia. A draft headline says reliability improved on every measure. A proposed investment is also described as guaranteed to reduce next-year interruptions, although no validated impact estimate is supplied. Both claims need qualification.',
    cast='Ravi | Reliability analyst\nCelia | Community liaison',
    culture=('Translate an average without turning it into everybody', 'Community members may compare an average with their own outage experience and conclude that one must be wrong. Explain the population and units. An average can describe the system accurately while concealing substantial differences between individual customers or neighborhoods.'),
    a='''What is Year 1 SAIFI? | 1.2 interruptions per customer | 90 minutes per customer | 1,200 interruptions for every customer | 0.9 interruptions per customer | Divide 1,200 customer interruptions by 1,000 customers to obtain 1.2.
What is Year 2 SAIDI? | 120 minutes per customer | 1 interruption per customer | 120,000 minutes for every customer | 12 minutes per customer | Divide 120,000 customer-minutes by 1,000 customers to obtain 120 minutes.
Which overall description matches the two indices? | Average frequency fell while average total interruption duration rose. | Both frequency and duration improved. | Every customer had exactly one interruption. | The proposed investment already reduced the results. | SAIFI falls from 1.2 to 1.0, while SAIDI rises from 90 to 120 minutes.''',
    vocabulary='''System Average Interruption Duration Index (SAIDI) | Average total sustained-interruption time per customer over a stated period. | explain SAIDI in minutes
System Average Interruption Frequency Index (SAIFI) | Average sustained-interruption count per customer over a stated period. | explain SAIFI as frequency
sustained interruption | An interruption meeting the duration threshold in the applicable reporting definition. | define sustained interruptions
customer interruption | One counted interruption affecting one customer. | count customer interruptions
customer-minute interrupted | One interruption minute for one customer. | sum customer-minutes interrupted
customers served | The customer population used as the denominator. | state customers served
Customer Average Interruption Duration Index (CAIDI) | Average duration per sustained customer interruption on a stated basis. | distinguish CAIDI from SAIDI
momentary interruption | A short interruption classified under the applicable reporting definition. | distinguish momentary interruptions
major event day | A day classified as a major event under the stated reliability methodology. | state major-event-day treatment
event coverage | The set of events included in a reported measure. | align event coverage
reporting methodology | The definitions and procedures used to calculate the measures. | document the reporting methodology
denominator | The quantity by which another is divided to calculate a ratio or average. | check the denominator
frequency | How often counted events occur over the stated period or basis. | explain interruption frequency
duration | How long an interruption or accumulated interruption time lasts. | explain interruption duration
system average | A measure averaged over the defined system population. | qualify the system average
distribution of outcomes | How results vary across customers, locations, or events. | examine the distribution of outcomes
reliability trend | The direction of change in defined service-reliability measures over time. | interpret the reliability trend
resilience | The ability to withstand, adapt to, and recover from disruptive events. | distinguish resilience from a single reliability index
investment proposal | A plan requesting resources for a specified project or improvement. | assess an investment proposal
benefit estimate | An estimate of the favorable effects expected from an action. | validate the benefit estimate
business case | The stated rationale, costs, benefits, risks, and assumptions supporting a decision. | review the business case
counterfactual | An estimate or model of what would occur without the intervention. | establish the counterfactual basis
target outcome | The result an initiative aims to achieve, not a guaranteed result. | distinguish the target outcome
performance commitment | A defined undertaking about performance on a specified basis. | qualify the performance commitment''',
    precision='SAIFI is 1.2 in Year 1 and 1.0 in Year 2. SAIDI is 90 and 120 minutes respectively. Frequency fell, but total interruption duration per customer rose. The headline improved on every measure is therefore false.',
    precision_extra='On this same basis, CAIDI is 90/1.2 = 75 minutes in Year 1 and 120/1.0 = 120 minutes in Year 2. These averages do not mean every customer had identical experiences, and historical trends do not guarantee an investment effect.',
    phrases='''Define frequency | SAIFI describes average sustained interruptions per customer.
Define total duration | SAIDI describes average total sustained-interruption minutes per customer.
State the period | These figures cover each full reporting year.
Show the denominator | Both years use one thousand customers.
Calculate Year 1 frequency | Twelve hundred divided by one thousand gives 1.2.
Calculate Year 2 frequency | One thousand divided by one thousand gives 1.0.
Calculate Year 1 duration | Ninety thousand customer-minutes divided by one thousand gives ninety minutes.
Calculate Year 2 duration | One hundred twenty thousand divided by one thousand gives one hundred twenty minutes.
Summarize the mixed trend | Interruptions were less frequent on average, but total interruption time increased.
Correct the headline | The data do not show improvement on every measure.
Qualify the average | Individual customers may have experienced different outcomes.
Check the comparison | Use the same definitions, event coverage, and major-event treatment.
Distinguish CAIDI | CAIDI describes average duration per customer interruption, not per customer served.
Separate resilience | A single annual index does not describe every aspect of resilience.
Qualify the investment | The proposed benefit needs a supported estimate and assumptions.
Close with the decision | Present the measured trend separately from the investment proposal and its uncertainty.''',
    notes='''Per customer | Uses the served population, including those with no counted interruption.
Per interruption | Uses interruption counts rather than all customers served.
Total duration | Accumulates time across relevant interruptions.
On average | Does not claim that every customer experienced the same result.
Same coverage | Makes the comparison meaningful across reporting periods.
Guaranteed | Is unsupported by the unvalidated investment estimate in this case.''',
    d='''Which Year 1 calculation gives CAIDI? | 90,000 customer-minutes divided by 1,200 customer interruptions = 75 minutes | 90,000 divided by 1,000 = 90 minutes | 1,200 divided by 1,000 = 1.2 minutes | 1,000 divided by 90,000 = 90 minutes | CAIDI divides accumulated customer-interruption minutes by customer interruptions, giving seventy-five minutes.
Which interpretation of Year 2 SAIFI is accurate? | The system average is one counted interruption per customer. | Every customer had exactly one interruption. | Every interruption lasted one minute. | All customers were interrupted at the same time. | A system average does not require identical interruption counts or experiences for every customer.
What must be aligned for the comparison? | Definitions, reporting periods, population basis, and event coverage | Units alone, regardless of included events | Customer totals alone, regardless of period | Chart labels alone, regardless of calculation rules | Changing measurement scope can create a misleading trend even when each separate calculation is correct.
Which investment statement is supported? | The benefit remains a proposal requiring a validated basis. | Historical averages guarantee next year's result. | The draft heading proves the investment caused improvement. | The proposal automatically removes every outage. | No validated impact estimate is supplied, so the promised improvement is not established.''',
    dialogue='''Celia | The headline says reliability improved on every measure, but the chart shows SAIDI increasing. I need a clear explanation before presenting this to community representatives.
Ravi | Start with [[frequency::Frequency concerns how often interruptions occur; SAIFI falls from 1.2 to 1.0 on the supplied customer basis.]]. SAIFI is the average count of sustained interruptions per customer. It falls from one point two in Year 1 to one in Year 2.
Celia | We get those figures by dividing twelve hundred customer interruptions and then one thousand by the same thousand customers served in each year.
Ravi | Correct. Keep the [[denominator::The denominator is the served-customer population used in the division, one thousand in both years of this comparison.]] visible. It is the defined customer population, not only the customers who experienced interruptions, and it does not count network equipment failures.
Celia | Residents will challenge an average of one if they personally had three interruptions. I want to explain that without dismissing their experience.
Ravi | Exactly. A [[system average::A system average summarizes the population while allowing individual customers to have different counts, including none or several.]] can coexist with uneven outcomes. Some customers may have none and others several; the average alone does not describe that distribution.
Celia | Now the duration measure. We have ninety thousand customer-minutes in Year 1 and a hundred twenty thousand in Year 2, again across a thousand customers.
Ravi | That gives [[SAIDI::SAIDI is average total sustained-interruption duration per customer, calculated here as ninety and one hundred twenty minutes respectively.]] of ninety and one hundred twenty minutes. It measures total interruption time per customer over the year, not the length of one typical incident.
Celia | Then interruptions became less frequent on average, but customers experienced more total interruption time on the system-average basis. That is a mixed trend, not universal improvement.
Ravi | Yes. The [[duration::Duration here concerns accumulated interruption time; it rose even while the average interruption count fell.]] measure worsened while frequency improved. We must say both, rather than choose whichever number supports the preferred headline about overall progress.
Celia | Someone may ask how long an interruption lasted on average. That requires a different denominator from the number of customers served, does it not?
Ravi | Use [[CAIDI::CAIDI divides customer-minutes interrupted by customer interruptions, yielding seventy-five and one hundred twenty minutes on this consistent basis.]] on this same measurement basis: ninety thousand divided by twelve hundred is seventy-five minutes; one hundred twenty thousand divided by one thousand is one hundred twenty minutes.
Celia | So CAIDI is duration per customer interruption, while SAIDI is accumulated duration per customer served. Similar acronyms conceal an important distinction.
Ravi | Correct. Also preserve the [[event coverage::Event coverage identifies which interruptions are included; a trend comparison requires consistent scope rather than mixing different event sets.]]. The supplied years use the same sustained-interruption definitions and major-event treatment, which is necessary for interpreting the comparison we just made.
Celia | Please put the major-event treatment next to the chart. If that changes between years, we need to explain it before comparing the trend.
Ravi | Exactly. State the [[reporting methodology::Reporting methodology defines calculation and classification rules; changing those rules can undermine a comparison even when arithmetic is correct.]], period, and scope. Readers should not have to discover a changed definition after reacting to a large improvement or deterioration in the headline.
Celia | The investment slide promises fewer interruptions next year, but we have no validated estimate explaining the size or certainty of that effect.
Ravi | Then label it a [[target outcome::A target outcome is an intended result, not a guaranteed effect; the supplied proposal lacks a validated impact estimate.]], not a guarantee. The business case needs a supported benefit estimate, assumptions, costs, and risks; these historical indices cannot supply that causal forecast by themselves.
Celia | I will present the two measured trends, explain the averages, and place the investment proposal in a separate section with its remaining evidence needs.
Ravi | Good. Community questions about [[resilience::Resilience includes withstanding and recovering from disruption; a single annual average does not capture every aspect of that broader capability.]] may reach beyond these annual averages. Explain what the indices measure accurately, then identify the additional evidence needed rather than stretching one number to answer everything.''',
    rehearsal=['Read the corrected exchange with SAIFI 1.2 then 1.0 and SAIDI 90 then 120 minutes.', 'Switch roles; distinguish CAIDI per customer interruption from SAIDI per customer served.', 'Read the checked transfer twice using 1.5, 120, and 80. Keep the measures as averages, not identical individual experiences.'],
    transfer_title='Compute two distinct indices',
    transfer_setup='A fictional year has 500 customers served, 750 sustained customer interruptions, and 60,000 customer-minutes interrupted on one consistent reporting basis.',
    transfer='''Analyst: "SAIFI is ___ interruptions per customer." | 1.5 | Seven hundred fifty customer interruptions divided by five hundred customers equals 1.5.
Liaison: "SAIDI is ___ minutes per customer." | 120 | Sixty thousand customer-minutes divided by five hundred customers equals one hundred twenty.
Analyst: "CAIDI is ___ minutes per customer interruption." | 80 | Sixty thousand customer-minutes divided by seven hundred fifty customer interruptions equals eighty.
Liaison: "These are ___, not identical individual experiences." | averages | The measures summarize groups and do not require every customer's experience to match.'''))
