"""Original Cooks and Kitchen Staff learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='cooks-kitchen-staff',
    title='Cooks and Kitchen Staff English',
    cover_label='ENGLISH FOR KITCHEN TEAMS',
    cover_title='Cooks and\nKitchen Staff',
    cover_size=36,
    tagline='Clear calls. Coordinated kitchens.',
    audience='For line cooks, prep cooks, kitchen assistants, station leads, and food-service production teams.',
    map_intro='Eight kitchen conversations: clarify a prep quantity, count a delivery, replace a revised ticket, coordinate the pass, explain a shortage, check an allergy modification, report a faulty scale, and hand over unfinished work.',
    notes_title='Say the quantity. Name the stage.',
    notes_intro='Kitchen communication needs to be brief enough for service and complete enough to prevent mistakes. Numbers need units, revised tickets need a clear total, and ready must identify which items have actually reached which stage.',
    field_notes=[
        ('A number needs a unit', 'Twenty-four portions, containers, and liters describe different amounts. Confirm the intended unit before starting a batch, then keep it visible on the prep list and in the read-back.', '"Twenty-four portions from the current recipe, not twenty-four containers."'),
        ('A revision can replace', 'A second slip is not always an additional order. Confirm whether it replaces the earlier ticket, identify the current total, and keep a substitution attached to the correct item.', '"Revised ticket 41 replaces the old quantity: three tarts total."'),
        ('Partial progress is useful', 'State what is complete and what remains. Two plates at the pass do not make a four-main ticket ready. An estimate for the remaining work is not a finished-table call.', '"Two plated, two still at the station; current estimate four more minutes."'),
        ('Keep the next owner visible', 'A shortage, allergy question, equipment fault, or unfinished closing check needs a responsible person. Name the actual next step without pretending an unresolved review is complete.', '"The server will obtain the diners\' choice before the proposed substitution is used."'),
    ],
    scope_note='All kitchens, tickets, quantities, and incidents are fictional. This book teaches workplace English, not culinary certification, food-safety procedures, medical advice, or equipment repair. Follow current local requirements, approved recipes, allergen controls, equipment instructions, and emergency procedures. No example authorizes serving unverified food, bypassing a control, or repairing faulty equipment.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Cooks.',
             url='https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm',
             note='Occupational context for recipe-based preparation, station work, portioning, and kitchen coordination. The original cases do not reproduce workplace transcripts.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Food Allergies.',
             url='https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies?lv=true',
             note='Background for allergy and cross-contact terminology. Removing a named topping does not verify a complete dish or its preparation.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Food Code 2026.',
             url='https://www.fda.gov/food/fda-food-code/food-code-2026',
             note='Model code offered for jurisdictional adoption. The language exercises do not replace applicable local rules or the actual kitchen food-safety system.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Have Food Allergies? Read the Label.',
             url='https://www.fda.gov/consumers/consumer-updates/have-food-allergies-read-label',
             note='Ingredient-source context, including casein and whey as milk proteins. Label information must match the actual product; it does not alone settle kitchen handling.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Clarifying a prep list',
    scene='Twenty-four of what?',
    skill='Clarify an ambiguous prep quantity, confirm the recipe basis, and read back the instruction before production starts.',
    brief='The prep list says "soup: 24" without a unit. Yesterday\'s sheet used portions, while a storeroom label uses containers. Prep cook Asha has not started a batch. Lead Mateo intended twenty-four portions from the current recipe, not twenty-four containers. Asha needs to ask about the unit, confirm the current recipe, and make the corrected instruction visible. The conversation supplies no container capacity, portion volume, ingredient weights, or recipe conversion factor. Those details must come from the actual approved recipe and production arrangements, not from guessing what the number means.',
    cast='Asha | Prep cook\nMateo | Kitchen lead',
    culture=('A short question prevents a large error', 'In a busy kitchen, a clarification can feel like slowing down. Make it specific: state the item, the ambiguous number, and the missing unit. A confident read-back shows attention and protects production without turning the exchange into a challenge to rank.'),
    a='''What is missing from soup: 24? | The unit | The word soup | The number itself | A confirmed completed batch | The number is present, but it does not say portions, containers, or another unit.
What did Mateo intend? | Twenty-four portions from the current recipe | Twenty-four containers regardless of size | Twenty-four liters established by the brief | Yesterday's recipe without checking | The lead clarifies portions and the current recipe as the intended production basis.
What has Asha started? | No batch yet | Twenty-four containers | A completed soup service | An invented conversion calculation | The brief explicitly says no batch has started before the clarification.''',
    vocabulary='''prep list | Record of food-preparation tasks and required quantities. | clarify the prep list
mise en place | Ingredients, equipment, and organization prepared for the work ahead. | organize mise en place
portion | Specified amount intended for one serving or defined use. | prepare twenty-four portions
batch | Quantity produced together in one preparation cycle. | plan the batch
batch size | Amount to be produced in a particular batch. | confirm the batch size
recipe yield | Quantity or number of portions an approved recipe produces. | check the recipe yield
portion size | Specified amount allocated to each serving. | follow the portion size
unit of measure | Stated basis such as grams, liters, containers, or portions. | name the unit of measure
container capacity | Amount a particular container can hold. | verify container capacity
production quantity | Amount planned for preparation. | confirm the production quantity
standardized recipe | Defined recipe specifying ingredients, method, and yield for consistent production. | follow the standardized recipe
current recipe | Recipe version established for the present task. | use the current recipe
recipe version | Identified edition or revision of a recipe. | confirm the recipe version
scaling factor | Ratio used to adjust a recipe from its original yield to a target yield. | calculate the scaling factor
ingredient weight | Mass of a recipe component. | verify the ingredient weight
volume | Space occupied by a substance, measured in a stated unit. | measure the volume
tare | Container weight excluded to determine the contents' net weight. | account for the tare
net weight | Contents' weight excluding packaging or container weight. | record the net weight
gross weight | Combined weight of contents and relevant container or packaging. | distinguish gross weight
production sheet | Record of planned and actual kitchen output. | update the production sheet
prep target | Required output for a preparation task. | confirm the prep target
read-back | Repetition of an instruction to confirm the details understood. | give a read-back
clarification | Question or explanation that resolves an ambiguity. | request clarification
task start | Point at which the assigned preparation begins. | confirm the task start''',
    precision='A portion is not a container unless the actual arrangement explicitly makes them equivalent. The number twenty-four cannot be converted into liters, containers, or ingredient weights without the relevant recipe and capacity information.',
    precision_extra='Yesterday used portions is context, not a substitute for confirming today. The lead establishes twenty-four portions from the current recipe. Check the approved yield and portion size before any scaling; the exercise supplies no numeric conversion factor.',
    phrases='''Identify the ambiguity | The prep list says soup, twenty-four, but the unit is missing.
Ask the exact question | Do you mean twenty-four portions or twenty-four containers?
State the intended quantity | I mean twenty-four portions.
Name the recipe basis | Use the current recipe.
Keep the rejected interpretation clear | Not twenty-four containers.
State the work status | I have not started the batch yet.
Avoid a volume guess | We have not specified a total volume in this exchange.
Check the recipe yield | I will use the yield stated in the approved recipe.
Separate container and serving | Container size does not define the portion count by itself.
Make the correction visible | Let us add portions to the prep list.
Read back completely | Soup: twenty-four portions, using the current recipe.
Clarify the version | Which approved recipe version applies to this task?
Avoid copying by habit | Yesterday's sheet does not settle today's missing unit.
Keep weights grounded | Ingredient quantities must come from the actual recipe calculation.
Confirm before starting | I will check the corrected instruction before production starts.
Close the clarification | We now agree on the item, quantity, unit, and recipe basis.''',
    notes='''Do you mean | Offers the relevant interpretations without accusing anyone of incompetence.
I mean | Corrects the intended meaning directly.
Not | Makes the rejected interpretation explicit in a noisy environment.
Yet | Indicates that clarification is occurring before a batch has begun.
Using | Links the quantity to the specified recipe basis.
By itself | Prevents one available fact from being treated as enough for a conversion.''',
    d='''Which read-back is complete? | Soup: twenty-four portions using the current recipe, not twenty-four containers. | Soup: twenty-four of something. | Twenty-four containers because the storeroom label says containers. | Twenty-four liters because soup is liquid. | The read-back preserves the clarified unit and recipe basis while rejecting the mistaken interpretation.
What information is still needed to calculate ingredient amounts? | The actual recipe yield, portion size, and approved scaling details | Only the word soup | An arbitrary container count | Yesterday's number without its recipe | The brief supplies the target portions but no ingredient quantities or numeric conversion basis.
Which statement correctly describes production status? | No batch has started. | The soup has already been served. | All ingredients have been weighed as a supplied fact. | Twenty-four containers are complete. | Asha has paused before production, so no completed preparation should be invented.
Why add portions to the list? | To make the clarified unit visible to the next reader | To change the target to containers | To certify all food-safety controls | To imply the batch is already complete | Updating the wording prevents the original ambiguity from being passed to another colleague.''',
    dialogue='''Asha | Mateo, can I check the soup line before I start? It says twenty-four, but there is no unit beside the number.
Mateo | Thank you for checking the [[prep list::The prep list contains the ambiguous soup quantity; clarifying it prevents the wrong production amount from being started.]]. I mean twenty-four portions from the current recipe, not twenty-four containers.
Asha | That helps. Yesterday's sheet counted portions, but the storeroom label counts containers. I did not want to assume those two records meant the same thing.
Mateo | They do not establish the same [[unit of measure::The unit of measure identifies what the number counts; portions and containers are different units unless explicitly related.]]. Today's instruction is portions. The storage label does not change the production target I have given you.
Asha | I have not started a batch, so nothing needs undoing. I wanted to settle the quantity before collecting ingredients and beginning the preparation.
Mateo | Good. Keep the [[task start::The task start has not occurred; the clarification precedes production rather than correcting an already completed batch.]] clear in the handoff. We are clarifying an instruction, not reporting that twenty-four of anything has already been made.
Asha | Should I use the recipe we currently keep for this soup, rather than copy a quantity from yesterday's working sheet?
Mateo | Use the [[current recipe::The current recipe is the specified production basis; yesterday's working sheet is not automatically the correct recipe authority.]]. Confirm the approved version for the task, including its yield and portion size, before working out the required ingredients.
Asha | We have not named a volume here. I cannot turn twenty-four portions into a number of liters unless the recipe gives me the necessary basis.
Mateo | Exactly. The [[portion size::The portion size defines the amount per serving; it is needed to relate a portion count to an actual quantity.]] comes from the actual recipe arrangement. Do not invent it from the size of a container you happen to see.
Asha | I will check how many portions the approved recipe produces. That will tell me whether I need a whole batch or an appropriately scaled quantity.
Mateo | The [[recipe yield::The recipe yield states the output of the approved recipe, providing the basis for comparing it with the target portions.]] is the relevant starting point. The twenty-four target alone does not tell you the ingredient weights or the number of preparation cycles.
Asha | And the size of a storage container is a separate detail. One container could hold more than one serving, depending on the actual container and portion.
Mateo | Correct. [[Container capacity::Container capacity measures what a vessel can hold; it does not by itself define a serving or the required portion count.]] is not a synonym for portion count. We need to keep storage descriptions and production quantities distinct.
Asha | If the recipe needs scaling, I will use its actual yield and the target rather than multiply everything by twenty-four automatically.
Mateo | Yes. A [[scaling factor::A scaling factor relates target yield to recipe yield; twenty-four portions is not automatically a factor of twenty-four.]] depends on the recipe basis. Follow the approved method, and ask about any unresolved detail before changing ingredient amounts.
Asha | Let us add the word portions to the list now. Otherwise another cook could read the same short line and have the same question.
Mateo | Agreed. Make the [[production quantity::The production quantity is twenty-four portions, which should remain visible with its unit on the corrected instruction.]] explicit. The corrected entry should preserve soup, twenty-four portions, and the current recipe basis without implying the task is complete.
Asha | My repeat is soup, twenty-four portions, current recipe. No batch started. I will check the recipe details before beginning the actual preparation.
Mateo | That [[read-back::The read-back repeats item, quantity, unit, recipe basis, and current work status, confirming the instruction understood.]] is correct. We have resolved the missing unit, and the next step is to prepare against the approved recipe and actual kitchen process.''',
    transfer_title='Clarify a sauce quantity',
    transfer_setup='A prep line says sauce: 18. Lead Noor clarifies eighteen portions from the current recipe, not eighteen tubs. No batch has started, and no portion volume is supplied.',
    transfer='''Cook: "The target is eighteen ___." | portions | Noor explicitly names portions as the intended production unit.
Lead: "Use the ___ recipe." | current | The applicable basis is the current recipe, not a guessed older sheet.
Cook: "No batch has ___." | started | The scenario states that preparation has not begun.
Lead: "The target is not eighteen ___." | tubs | Tubs is the rejected interpretation of the ambiguous quantity.''',
))

BOOK['units'].append(unit(
    title='Reporting deliveries and stock discrepancies',
    scene='Six listed, four counted',
    skill='Report a delivery discrepancy using observed quantities, attributed statements, and a clear receiving decision owner.',
    brief='A delivery note lists six cases of tomatoes, but cook Ben can physically count four cases in the receiving area. The driver says two more may be on another trolley and has not checked. Receiving lead Lina is responsible for resolving the record through the actual receiving process. Ben must distinguish the delivery note from the observed count and the driver\'s unverified explanation. No full delivery, supplier fault, product-quality acceptance, or credit has been established. The count should not be recorded as six received merely to make the paperwork match.',
    cast='Ben | Cook helping receive the delivery\nLina | Receiving lead',
    culture=('A discrepancy is not an accusation', 'A firm count can be stated neutrally. Say what the note lists, what is physically present, and what someone has suggested but not checked. That gives the receiving lead useful information without labeling the driver dishonest or accepting a quantity that has not arrived.'),
    a='''What quantity is physically present? | Four cases | Six verified cases | Two cases only | An uncounted full pallet | Ben can physically count four cases in the receiving area.
What did the driver say? | Two more may be on another trolley. | Six have been independently verified. | A credit has been approved. | The supplier intentionally removed two cases. | The driver offers an unverified possibility, not a completed check.
Who must resolve the receiving record? | Lina, the receiving lead | Ben by inventing six received | An unrelated guest | No one because paperwork cannot differ | Lina is responsible for the record through the actual receiving process.''',
    vocabulary='''delivery note | Document listing goods associated with a delivery. | compare the delivery note
purchase order | Record of items and quantities ordered from a supplier. | check the purchase order
invoice | Supplier document requesting payment for stated goods or services. | reconcile the invoice
case | Shipping unit containing a specified group or quantity of product. | count the cases
case pack | Number or arrangement of items contained in a case. | verify the case pack
pallet | Platform used to handle and transport grouped goods. | identify the pallet
trolley | Wheeled equipment used to move goods. | check the trolley
receiving area | Location where incoming supplies are checked and processed. | inspect the receiving area
physical count | Quantity established by counting the items actually present. | record the physical count
listed quantity | Amount stated on a document. | compare the listed quantity
quantity discrepancy | Difference between two relevant quantity records or observations. | report a quantity discrepancy
short delivery | Delivery with less than the agreed quantity, once the relevant check establishes it. | verify a short delivery
unchecked location | Place suggested as holding goods but not yet verified. | identify the unchecked location
driver statement | Information attributed to the person delivering the goods. | record the driver statement
receiving lead | Person responsible for coordinating acceptance and receiving records. | contact the receiving lead
receipt record | Documentation of goods actually received under the relevant process. | correct the receipt record
acceptance check | Required examination before goods are accepted for the intended use. | complete acceptance checks
condition check | Review of the physical state of incoming goods. | perform a condition check
product identifier | Code or description distinguishing the delivered item. | verify the product identifier
lot code | Identifier linking goods to a production or supply lot. | retain the lot code
traceability | Ability to follow a product's identity and movement through records. | preserve traceability
supplier query | Question sent to a supplier about a discrepancy or detail. | raise a supplier query
credit note | Supplier document reducing an amount owed under an approved adjustment. | request a credit note
verified receipt | Receiving status supported by actual checks rather than expected paperwork. | record verified receipt''',
    precision='Six listed minus four present leaves two cases unaccounted for at this observation point. It does not establish where the other cases are or who caused the difference. May be on another trolley is not the same as checked and found.',
    precision_extra='Quantity verification and product acceptance are different checks. Four cases being present does not certify their condition, temperature, specification, or suitability. Follow the actual receiving process and keep any unresolved record or product question visible to the responsible lead.',
    phrases='''State the document | The delivery note lists six cases of tomatoes.
State the observation | I can count four cases here.
Calculate the difference | Two listed cases are not accounted for in this area.
Attribute the explanation | The driver says they may be on another trolley.
Preserve the check status | That trolley has not been checked yet.
Avoid recording an assumption | I cannot record six as received from this count.
Name the owner | Lina needs to resolve the receiving record.
Keep the report neutral | I am reporting the difference, not assigning fault.
Separate quantity and condition | This count does not complete the product acceptance checks.
Use a clear comparison | Six listed; four physically present.
Ask for the next step | What should happen through our receiving process now?
Keep the units consistent | The quantities are cases, not individual tomatoes.
Do not invent a credit | No supplier credit has been confirmed.
Retain the product identity | Keep the tomato product details with the discrepancy.
Update only after verification | Change the received quantity when the actual check supports it.
Close the report | The difference is reported, and the additional two cases remain unverified.''',
    notes='''Lists | Attributes a quantity to a document.
Can count | Identifies the directly observed amount.
May be | Preserves the uncertainty in the driver's statement.
Not accounted for here | States the local observation without claiming universal absence.
Through our process | Refers to the actual receiving arrangement rather than an improvised shortcut.
When supported | Makes a record change conditional on verification.''',
    d='''Which report is accurate? | Six cases listed, four present; the driver suggests two may be on an unchecked trolley. | Six verified because the note says six | The driver definitely stole two cases | Two damaged cases have been credited | The report distinguishes the document, physical observation, and unverified explanation.
What should not be recorded as established? | Six cases received | Four cases physically counted | The note lists six | The driver has not checked the other trolley | The current observation does not verify receipt of all six listed cases.
Which conclusion exceeds the evidence? | The supplier deliberately shorted the kitchen. | There is a quantity discrepancy to resolve. | Another location needs checking through the process. | The receiving lead owns the record question. | The cause and intent behind the discrepancy are not established by the count.
What remains separate from the quantity count? | Required product acceptance checks | The arithmetic difference between six and four | The fact that the unit is cases | The driver's attributed statement | Counting cases does not establish their condition or satisfy every required receiving control.''',
    dialogue='''Ben | Lina, can you review this tomato delivery with me? The note lists six cases, but I can physically count only four in the receiving area.
Lina | Thank you. Keep the [[listed quantity::The listed quantity belongs to the delivery document and must remain distinct from the goods physically verified.]] separate from your observed count. Six on the note does not let us record six received without the relevant check.
Ben | The driver says two more may be on another trolley. He has not looked yet, so I have not treated that explanation as a confirmed location.
Lina | That is an attributed [[driver statement::The driver statement is an unverified suggestion about another trolley, not evidence that the missing cases have been found.]]. Record it as a possibility he gave us, not as two additional cases already verified.
Ben | For the immediate count, I have four cases here. The unit is cases, not individual tomatoes or a number of pallets.
Lina | Good. The [[physical count::The physical count is four cases actually present in the receiving area, preserving both number and unit.]] should name the product and unit clearly. We need everyone comparing the same thing when they read the record.
Ben | So the difference between the note and what I see is two cases. I should not jump from that difference to a statement about why it happened.
Lina | Correct. It is a [[quantity discrepancy::A quantity discrepancy identifies a difference between listed and observed amounts; it does not establish cause or deliberate misconduct.]] to resolve through receiving. It could have an explanation, but we do not have that explanation verified yet.
Ben | I have not signed off six as received. I did not want the paperwork to appear complete while the extra two cases were still only a suggestion.
Lina | That protects the [[receipt record::The receipt record should reflect actual supported receipt, not an expected quantity entered merely to match the delivery note.]]. It needs to reflect what the actual process verifies, not what would make the numbers look tidy.
Ben | Should the other trolley be checked before anyone says this is a short delivery? At the moment, we do not know whether the cases are there.
Lina | Yes, the [[unchecked location::The unchecked location is the suggested other trolley; its possible contents remain unknown until the actual check occurs.]] needs to be resolved through our process. Do not convert not seen here into a final account of the whole delivery.
Ben | I also have not made any claim about the tomatoes' condition. Counting the cases is not the same as finishing every required receiving check.
Lina | Exactly. The [[acceptance check::The acceptance check concerns the required product and receiving criteria, which a simple quantity count does not complete.]] is a separate matter. Product identity, condition, and any required controls still need the appropriate actual checks.
Ben | I will keep the tomato details with the discrepancy. Otherwise a later note saying two cases missing could be confused with another delivery.
Lina | Preserve the [[product identifier::The product identifier links the count discrepancy to the correct tomatoes rather than leaving an ambiguous two-case note.]] and relevant delivery reference. Accurate context matters as much as the subtraction when another colleague follows it up.
Ben | If a supplier question or credit request becomes necessary, I will not mark one approved just because I have raised the discrepancy with you.
Lina | Correct. A [[credit note::A credit note is a supplier adjustment document; the current count discrepancy does not establish that any credit has been approved.]] is not established here. First keep the receiving facts accurate and follow the proper route for any later commercial action.
Ben | My handoff is six cases listed, four physically present, and a possible two on an unchecked trolley. You own the record question from here.
Lina | I accept that as [[receiving lead::The receiving lead is the responsible owner for resolving the record through the actual process, without inventing a completed outcome.]]. I will coordinate the next checks. The extra two cases remain unverified until the actual result supports an update.''',
    transfer_title='Report another count difference',
    transfer_setup='A delivery note lists eight flour sacks. Six are physically present. The driver suggests two may still be in the vehicle, which has not been checked. Receiving lead Noor accepts the query.',
    transfer='''Cook: "The note lists ___ sacks." | eight | Eight is the documented quantity, not the physically verified count.
Lead: "The observed count is ___." | six | Six sacks are physically present under the supplied facts.
Cook: "The suggested location is the ___." | vehicle | The driver suggests the vehicle, but that location remains unchecked.
Lead: "The receiving owner is ___." | Noor | Noor accepts responsibility for the receiving query in this scenario.''',
))

BOOK['units'].append(unit(
    title='Reading tickets and modifications',
    scene='Three total, not five',
    skill='Distinguish a replacement ticket from an added order and keep a one-item substitution linked to the current quantity.',
    brief='Ticket 41 originally requests two tarts. A new slip says "three tarts, revised 41." Cook Imani asks expediter Cole whether the new slip replaces or adds to the old quantity. Cole confirms that it replaces it: the total is three tarts, not five. One of the three has salad instead of potatoes. The conversation does not establish a seat number, cooking completion, or allergy. Imani must retain the one-item substitution, clarify the actual item identification through the ticket process, and prevent both versions from being treated as separate orders.',
    cast='Imani | Cook on the tart station\nCole | Expediter',
    culture=('Repeat the whole corrected meaning', 'A quick yes can confirm the wrong interpretation if two people are looking at different slips. Repeat replaces, the ticket number, the current total, and the affected item. Keep the superseded record traceable through the actual system without treating it as another active order.'),
    a='''What is the current total for ticket 41? | Three tarts | Five tarts | Two tarts plus three extra | One tart | Cole confirms that the revised quantity replaces the earlier quantity, giving three total.
How many tarts have the side substitution? | One of the three | All three | None | Five | The specified substitution applies to one tart, not the entire ticket.
What does salad replace? | Potatoes | The tart itself | All other guests' mains | The ticket number | Salad is supplied instead of potatoes for the one modified tart.''',
    vocabulary='''ticket number | Identifier linking an order and its updates. | confirm the ticket number
revised ticket | Updated order record changing a previous instruction. | read the revised ticket
replacement instruction | Direction that supersedes an earlier direction rather than adding to it. | confirm a replacement instruction
additional order | New quantity added beyond the existing confirmed order. | distinguish an additional order
current total | Complete quantity now required after applying the confirmed change. | state the current total
superseded ticket | Earlier record no longer governing the current instruction. | identify the superseded ticket
amendment | Change to an existing order or document. | acknowledge the amendment
modifier | Instruction changing a particular item's standard preparation or accompaniment. | attach the modifier
substitution | Replacement of one component with another. | confirm the substitution
instead of | Phrase indicating replacement rather than addition. | serve salad instead of potatoes
extra | Additional quantity beyond what is already included. | distinguish extra from replacement
all day | Kitchen shorthand for the total quantity outstanding across the stated order scope. | clarify the all-day count
expediter | Person coordinating order information and dish completion at the pass. | confirm with the expediter
ticket rail | Place where order slips are held and organized for service. | organize the ticket rail
duplicate production | Making an order twice because its records or instructions were misread. | prevent duplicate production
active instruction | Direction currently governing the work. | identify the active instruction
change acknowledgment | Explicit confirmation that a revision has been received and understood. | give change acknowledgment
item identification | Details distinguishing the particular dish affected by a request. | confirm item identification
seat mapping | Link between an ordered item and the guest's place at a table. | verify seat mapping
side order | Accompanying item ordered alongside a main or other dish. | clarify the side order
standard accompaniment | Side normally supplied with an item unless modified. | identify the standard accompaniment
one-item change | Modification affecting one item rather than every item in the order. | preserve the one-item change
order scope | Set of tickets or items to which a quantity or instruction applies. | state the order scope
revision trail | Record showing how an instruction changed over time. | preserve the revision trail''',
    precision='Revised 41 refers to the same ticket, but the meaning of the new quantity still needs confirmation. Here, Cole explicitly says replaces. Three total is not two plus three, and one salad substitution does not apply to all three tarts.',
    precision_extra='Salad instead of potatoes changes the side, not the tart count. Do not invent a seat number or report dishes ready from a quantity correction. Keep the current instruction identifiable and preserve any required revision history through the actual system.',
    phrases='''Identify both records | I have the original two-tart ticket and the revised slip for three.
Ask the key distinction | Does the revised quantity replace the old one or add to it?
Confirm replacement | It replaces the old quantity.
Give the total | Ticket 41 is three tarts total.
Reject the wrong addition | Not two plus three.
Specify the modification | One of the three has salad instead of potatoes.
Keep the other sides unchanged | The other two retain the standard potato accompaniment.
Avoid changing every plate | The salad substitution applies to one item only.
Check the affected item | We still need the correct item identification through the ticket process.
Keep the number stable | Both slips refer to ticket 41.
Prevent two active orders | Do not treat the earlier slip as another order to produce.
Preserve the record | Keep the revision trail according to our system.
Acknowledge the change | I have received and understood the replacement quantity.
Keep production status separate | This correction does not mean the tarts are already ready.
Clarify the scope | I am confirming this ticket, not every tart outstanding across the kitchen.
Close with a read-back | Ticket 41: three total, one salad instead of potatoes, earlier quantity replaced.''',
    notes='''Replace or add | Names the two interpretations that could cause duplicate production.
Three total | States the final quantity explicitly.
One of the three | Limits the modification to a single item.
Instead of | Means substitution, not both sides automatically.
This ticket | Limits the count to its stated order scope.
Received and understood | Confirms the meaning of the change, not just receipt of paper.''',
    d='''Which read-back is correct? | Revised ticket 41 replaces two with three total; one has salad instead of potatoes. | Five tarts because both slips count | Three extra tarts beyond the original two | Three tarts all with salad and potatoes | The read-back captures replacement, final quantity, and the one-item side substitution.
Which interpretation of instead of is correct? | Salad replaces potatoes for the specified tart. | Salad is automatically an extra side for everyone. | The tart itself is canceled. | Every ticket in the kitchen changes. | Instead of marks replacement of the named component within the specified item's scope.
What is not established by the revised ticket? | That the three tarts are prepared and ready | That the current total is three | That the old quantity is replaced | That one tart has the side substitution | A quantity instruction does not establish completed preparation or readiness.
What should the team avoid doing with the earlier slip? | Treating it as a second active order | Preserving its required history | Marking its superseded status through the actual process | Checking that both slips concern ticket 41 | Treating both versions as active would create duplicate production beyond the confirmed total.''',
    dialogue='''Imani | Cole, I have two slips for ticket forty-one. The original says two tarts, and the new one says three tarts, revised forty-one. Can I check the meaning before proceeding?
Cole | Yes. The [[revised ticket::The revised ticket updates the existing order; Cole confirms that its three-tart quantity replaces the earlier two.]] replaces the earlier quantity. We need three tarts total for ticket forty-one, not two from one slip and three from another.
Imani | Thank you. I was not sure whether three meant a new total or three additional items. Those would give us very different production counts.
Cole | The [[current total::The current total is three after replacement; adding the two slips would incorrectly produce five tarts.]] is three. Please read it as a replacement instruction so the earlier two do not remain a separate quantity to make.
Imani | I also see one tart has salad instead of potatoes. That changes one accompaniment, not the number of tarts, correct?
Cole | Correct. It is a [[one-item change::The one-item change applies the salad substitution to one of the three tarts, not to every item.]]. One tart has salad; the other two keep the standard potato accompaniment.
Imani | I will keep the side request attached to the affected tart. I do not have a seat number in this exchange, so I will not guess one.
Cole | Good. The [[item identification::Item identification must connect the substitution to the correct tart through the actual process, without inventing a seat reference.]] still needs to be clear through our ticket process. A correct quantity does not help if the side reaches the wrong diner.
Imani | The phrase instead of matters here. It does not mean I should put both salad and potatoes on the modified plate.
Cole | Exactly. The [[substitution::The substitution replaces potatoes with salad for the identified tart; it does not add both sides or change all plates.]] replaces potatoes on that item. Do not expand it into an extra side for every guest or cancel the tart itself.
Imani | What about the original slip? I want the record to remain traceable, but I do not want another cook to pick it up as fresh work.
Cole | Handle it as the [[superseded ticket::The superseded ticket is the earlier version no longer governing production; retaining history must not keep it active.]] through our actual system. Preserve the required history while making the current instruction unmistakable.
Imani | I will not add the two and three together. We should also keep the ticket number visible so this change is not applied to a different table.
Cole | Yes. The [[order scope::The order scope is ticket forty-one; its three-tart total is not a count of every outstanding tart in the kitchen.]] is ticket forty-one. We are not giving an all-day count for every tart outstanding across the kitchen.
Imani | That distinction is useful. A colleague asking three all day could mean a wider total than the three we are confirming on this one ticket.
Cole | Right. State the scope whenever it could be unclear. Our aim here is to prevent [[duplicate production::Duplicate production would result from treating the original and revised quantities as separate active orders instead of one replacement.]] from the two versions, not to change any other confirmed order.
Imani | My repeat is forty-one, three tarts total, one with salad instead of potatoes, and the earlier quantity replaced. I will confirm the affected item's identification through the system.
Cole | That is the [[change acknowledgment::Change acknowledgment confirms the replacement quantity and modification have been understood, not merely that a new slip arrived.]] I need. You have the new total and the limited substitution, without adding an invented seat number.
Imani | I will update the working instruction accordingly. I am not calling the ticket ready; this conversation has clarified what we need to prepare.
Cole | Correct. Keep the [[revision trail::The revision trail records how the instruction changed while leaving the current production status distinct from completed preparation.]] clear, and report production progress separately. Three required does not mean three cooked, plated, or released from the pass.''',
    transfer_title='Replace a different quantity',
    transfer_setup='Ticket 52 originally lists four pies. A revised slip lists six, and the expediter confirms replacement, not addition. One pie has peas instead of carrots. No seat number or readiness is supplied.',
    transfer='''Cook: "The current total is ___ pies." | six | The confirmed replacement sets the total at six, not four plus six.
Expediter: "The old quantity is ___." | replaced | The revised slip supersedes the earlier quantity rather than adding to it.
Cook: "One pie has ___ instead of carrots." | peas | Peas is the stated substitute for the one modified pie.
Expediter: "Readiness is not ___." | established | The quantity correction does not establish that any pie is ready.''',
))

BOOK['units'].append(unit(
    title='Coordinating the pass',
    scene='Two plated, two still cooking',
    skill='Answer a whole-ticket readiness question with a precise split of completed work, remaining work, and estimated timing.',
    brief='Ticket 28 contains four mains. Two are plated, and two are still at cook Rosa\'s station. Rosa estimates four more minutes for the remaining pair. Expediter Jules asks whether the whole table is ready. Rosa must report partial progress and the current estimate without calling all four ready, guaranteeing pickup in exactly four minutes, or inventing a dispatch decision. Plating alone does not establish that all relevant food checks have been completed. Actual holding, quality, and release arrangements remain governed by the kitchen process, not by this language exercise.',
    cast='Jules | Expediter coordinating the pass\nRosa | Cook completing ticket 28',
    culture=('Answer the scope of the question', 'An expediter may need a table-level answer while a cook is focused on one station. Start with not the whole ticket yet, then give the exact split. Clear partial progress is more useful than either a vague yes or a vague not ready.'),
    a='''How many mains are on ticket 28? | Four | Two total | Six | An unspecified number | The brief supplies four mains as the complete ticket quantity.
How many are plated? | Two | All four | None | Four plus another pair | Two mains are plated, while the other two remain at the station.
What is Rosa's estimate for the remaining pair? | Four more minutes | Guaranteed pickup now | Four minutes already elapsed as the estimate | A completed dispatch | Rosa estimates four additional minutes for the pair still at the station.''',
    vocabulary='''pass | Area where dishes are checked and handed from kitchen to service staff. | coordinate the pass
ticket readiness | Status of the complete order against the required ready-to-serve conditions. | confirm ticket readiness
plated | Arranged on a plate, without alone certifying every readiness check. | report two plated
cook station | Assigned kitchen work area responsible for particular preparation tasks. | check the cook station
remaining pair | Two items still outstanding within the stated group. | finish the remaining pair
partial progress | Work completed for some but not all of the required scope. | report partial progress
whole-table call | Status message referring to every relevant dish for a table. | make a whole-table call
pickup | Collection of dishes from the kitchen for service under the actual arrangement. | confirm pickup
dispatch | Release or movement of prepared dishes toward service. | coordinate dispatch
runner | Colleague taking dishes from the pass to the dining area. | brief the runner
plating sequence | Order in which dishes are assembled on plates. | coordinate the plating sequence
finishing step | Final preparation action before the next required stage. | complete the finishing step
garnish | Food element used to finish or accompany a dish. | check the garnish
quality check | Review against the relevant dish and service requirements. | complete the quality check
holding arrangement | Approved method and conditions for keeping food before the next stage. | follow the holding arrangement
readiness estimate | Approximate expectation for reaching a specified ready stage. | communicate the readiness estimate
remaining work | Tasks still needed before the defined completion point. | identify the remaining work
coordination point | Event or location where different stations align their work. | agree the coordination point
synchronized service | Planned delivery of related dishes together or in an agreed sequence. | coordinate synchronized service
release decision | Authorization or instruction to send dishes from the relevant stage. | confirm the release decision
status call | Brief spoken report of progress or readiness. | give a status call
update trigger | Change or condition prompting a fresh status message. | identify an update trigger
ready-to-run | Local service status indicating dishes can be collected under the actual process. | confirm ready-to-run status
full ticket | Entire order rather than one completed component. | check the full ticket''',
    precision='Two plated describes partial progress. Four more minutes describes an estimate for the remaining pair. Neither statement alone makes the full ticket ready to run. Keep quantity, location, stage, and timing together.',
    precision_extra='Do not infer food safety or quality from the word plated. Actual holding limits, checks, and release decisions must follow the real kitchen process. If the estimate changes, update the expediter rather than allow an earlier approximate time to become a false promise.',
    phrases='''Answer the whole-ticket question | Not the whole ticket yet.
Give the total | Ticket 28 has four mains.
State completed progress | Two are plated.
Locate the remainder | The other two are still at my station.
Give the estimate | I estimate four more minutes for the remaining pair.
Keep the scope clear | That estimate is for the two outstanding mains.
Avoid a premature call | I am not calling all four ready.
Separate plating and release | Plated does not mean the full release check is complete.
Coordinate holding properly | We need to follow our actual holding and quality arrangements.
Avoid an invented dispatch | No pickup decision has been confirmed in this exchange.
Make a useful repeat | Four total, two plated, two pending, around four more minutes.
Update a change | I will call you if that estimate changes.
Keep the runner informed | The runner needs the actual ready-to-run status.
Do not blur the count | Two at the pass is not four ready for the table.
Confirm the next stage | Let us verify the full ticket before the release call.
Close accurately | The table is partially prepared, not yet confirmed ready as a whole.''',
    notes='''Not the whole ticket | Corrects the scope immediately.
Two are, two are | Makes the split easy to hear during a busy service.
Still at my station | Gives a concrete location and incomplete stage.
I estimate | Identifies the speaker's forecast rather than a guaranteed time.
For the remaining pair | Limits the timing claim to the unfinished items.
If that changes | Creates an expectation of updated information.''',
    d='''Which status call answers Jules accurately? | Ticket 28: four total, two plated, two at the station, estimated four more minutes for the pair. | All four ready now | Nothing has been done | Two mains total, all complete | The call preserves the full quantity, partial completion, location, and estimated remaining time.
What does plated establish by itself? | A preparation stage, not completion of every food and release check | Guaranteed food safety in all conditions | Confirmed table delivery | Payment completed | Plating describes assembly and does not independently certify all required checks or later stages.
Which time statement overclaims? | The entire table will definitely be delivered in exactly four minutes. | Rosa estimates four more minutes for the pair. | The estimate may need updating. | Pickup still needs the actual process. | The estimate concerns the remaining pair and cannot guarantee the timing of every later service stage.
What should happen if the estimate changes? | Tell the expediter the revised status. | Keep repeating the old time as certain. | Pretend the dishes were already dispatched. | Change the ticket total without instruction. | Updated communication prevents a provisional earlier estimate from misleading the rest of the service team.''',
    dialogue='''Jules | Rosa, can I call ticket twenty-eight ready for the table? I need to know whether the runner can collect the whole order, not just one part of it.
Rosa | Not the whole ticket yet. I have [[partial progress::Partial progress means some required dishes have advanced, while the whole four-main ticket is not yet ready.]]: four mains total, two plated, and two still at my station.
Jules | Thank you. I could see two plates, but that did not tell me whether the other two were finished somewhere else or still being prepared.
Rosa | The [[remaining pair::The remaining pair is the two mains still at Rosa's station, distinct from the two already plated.]] is still here. My current estimate is four more minutes for those two, not a statement that the table is ready now.
Jules | Is that four minutes from this update? I need to pass on the current expectation without confusing it with how long the ticket has already been open.
Rosa | Yes. That [[readiness estimate::The readiness estimate is four additional minutes from the current update for the two unfinished mains, not elapsed ticket time.]] is additional time from now for the pair. It is approximate, and I will update you if it changes.
Jules | I will not tell the runner that all four are ready. Two visible plates are useful progress, but the table-level answer is still incomplete.
Rosa | Correct. The [[full ticket::The full ticket comprises all four mains; readiness of only two does not establish completion of the whole order.]] is four mains. We need to preserve that total when we discuss what is finished and what remains.
Jules | We also need to handle the plated dishes under our actual kitchen process while the others are being completed. I do not want a timing discussion to bypass that.
Rosa | Agreed. The [[holding arrangement::The holding arrangement must follow the actual kitchen requirements; the language estimate does not authorize arbitrary food holding.]] and relevant quality checks still apply. This count and estimate are not permission to ignore them.
Jules | Have you made a release decision for any part of the order? I am checking because preparation progress and permission to send are different things.
Rosa | No [[release decision::A release decision authorizes the relevant dispatch stage, which is not established merely by reporting two plated dishes.]] has been confirmed in this exchange. I am reporting where the four dishes stand, not announcing a pickup or dispatch instruction.
Jules | That is clear. I need to coordinate the service rather than let one station's progress turn into a premature ready call for the whole table.
Rosa | Exactly. [[Synchronized service::Synchronized service coordinates related dishes under the actual plan; a partial station update is not itself that final arrangement.]] needs the actual plan and checks. My estimate helps you coordinate, but it does not settle every part of the service sequence.
Jules | When you give the next call, please make clear whether you mean the remaining two are plated or whether all four have reached the required ready stage.
Rosa | I will name the [[status call::The status call should specify the actual stage and scope, distinguishing the pair's progress from whole-ticket readiness.]] precisely. Plated, checked, and ready to run are not interchangeable labels unless the actual process has reached those stages.
Jules | And if the four-minute expectation becomes unrealistic, tell me then rather than wait for me to discover the runner is still waiting.
Rosa | That is our [[update trigger::The update trigger is a material change to the estimate or status, prompting a fresh report before others rely on stale information.]]. A changed estimate or relevant readiness issue needs a fresh message so you can give the service team an accurate picture.
Jules | My repeat is four mains on twenty-eight, two plated, two at your station, estimated four more minutes for the pair. The whole table is not confirmed ready.
Rosa | Correct. We have not yet confirmed [[ready-to-run::Ready-to-run is the actual collection-ready status under the kitchen process; it is not established for all four by this update.]] status for all four. Keep that distinction in the handoff, and I will report the next actual change.''',
    transfer_title='Report a six-main ticket',
    transfer_setup='Ticket 63 has six mains. Four are plated, and two remain at the station. The cook estimates three more minutes for that pair. No whole-ticket release is confirmed.',
    transfer='''Cook: "The ticket total is ___ mains." | six | Six is the complete number required for ticket sixty-three.
Expediter: "The plated count is ___." | four | Four mains have reached plating, leaving two at the station.
Cook: "The remaining pair needs an estimated ___ more minutes." | three | Three additional minutes is the supplied estimate for the unfinished pair.
Expediter: "Whole-ticket release is not ___." | confirmed | Partial plating and an estimate do not establish the full release decision.''',
))

BOOK['units'].append(unit(
    title='Communicating a shortage and an alternative',
    scene='Five sides, three portions left',
    skill='Quantify a shortfall, present a proposed alternative, and assign responsibility for obtaining the diners\' decision.',
    brief='Three portions of potatoes remain unallocated when a new ticket requests five potato sides. Rice is available as a proposed alternative for two diners, but they have not agreed to it. Cook Dario explains the shortage to server Mei, who can ask the diners and return with their decision. Dario cannot silently substitute rice or describe the whole ticket as ready. The case supplies no additional potato stock, replenishment time, price difference, or dietary suitability assessment for rice. The team must keep the two-portion gap and pending choice visible.',
    cast='Dario | Cook managing the side station\nMei | Server handling the affected ticket',
    culture=('An alternative is an offer until accepted', 'Kitchen availability and guest preference are different parts of the decision. State the shortage early and give the server a clear option to discuss. A convenient alternative should not become a silent substitution, especially when price or dietary questions still require checking.'),
    a='''How many potato portions remain unallocated? | Three | Five | Two | None | The brief gives three potato portions available for allocation to the new ticket.
What is the shortfall against five requested portions? | Two portions | Three portions | Five portions | Eight portions | Five requested minus three available leaves two portions short.
Who can obtain the diners' decision about rice? | Mei, the server | Dario by silently changing plates | A diner who has not been asked | No one because availability equals acceptance | Mei is the named server who can ask the diners and return with their choice.''',
    vocabulary='''available stock | Quantity presently available under the actual stock and use conditions. | confirm available stock
unallocated portion | Prepared or available portion not yet assigned to a specific order. | count unallocated portions
allocation | Assignment of stock to a particular order or purpose. | confirm the allocation
committed stock | Quantity already assigned to existing requirements. | protect committed stock
shortfall | Amount by which supply is less than the stated requirement. | quantify the shortfall
remaining balance | Quantity left after specified allocations or use. | state the remaining balance
portion count | Number of defined servings available or required. | update the portion count
par level | Target stock quantity used for planning under the establishment's system. | review the par level
replenishment | Addition of stock to restore availability. | confirm replenishment
stockout | Situation in which an item is unavailable for the relevant demand. | report a stockout
eighty-six | Restaurant shorthand indicating an item is unavailable or should no longer be sold in the stated scope. | communicate an eighty-six call
availability board | Shared record of current menu or ingredient availability. | update the availability board
alternative side | Different accompaniment offered in place of the requested side. | propose an alternative side
starch | Menu category including foods such as potatoes, rice, or pasta, without implying equivalence. | compare the starch options
proposed substitution | Suggested replacement that has not yet been agreed. | label the proposed substitution
accepted substitution | Replacement explicitly agreed through the appropriate process. | record the accepted substitution
guest decision | Diner's choice after the relevant option and conditions are explained. | obtain the guest decision
order hold | Pause while an unresolved order detail is clarified. | maintain the order hold
side station | Kitchen area responsible for relevant accompaniments. | brief the side station
reallocation | Change in which order receives a quantity of stock. | authorize reallocation
yield variance | Difference between expected and actual usable output. | investigate a yield variance
forecast demand | Expected requirement used for preparation planning. | compare forecast demand
portion control | Consistent serving amounts under the applicable recipe and service specification. | maintain portion control
return message | Information brought back after a query or request is answered. | request a return message''',
    precision='The shortfall is two portions, not a complete absence of potatoes. Rice being available does not prove that two diners want it. Do not reduce portion sizes, borrow committed stock, or change prices without the actual authorized process.',
    precision_extra='One starch is not automatically equivalent to another for preference, ingredients, or dietary requirements. The server should communicate the option accurately and verify any relevant unanswered question. No replenishment time or price consequence is established by this case.',
    phrases='''State the available count | Three potato portions remain unallocated.
State the demand | The new ticket requests five.
Quantify the gap | We are two portions short.
Offer the actual alternative | Rice is available as a proposed alternative side.
Preserve the decision | The two diners have not accepted it yet.
Assign the question | Mei, can you ask the diners and bring back their choice?
Accept ownership | I will ask them and return with the decision.
Avoid a silent change | Do not substitute rice before the choice is confirmed.
Keep the remaining potatoes clear | The three available portions do not cover all five requests.
Avoid invented replenishment | We have no confirmed time for more potatoes.
Do not imply price equality | Any price question needs its actual answer.
Keep dietary questions separate | Rice availability is not a dietary-suitability confirmation.
Retain the unresolved item | The two-side decision remains open.
Do not distort portions | A shortage does not authorize smaller portions without approval.
Ask for a precise return | Tell me which diners accept which side.
Close the handoff | Three potato portions available, two choices pending, Mei obtaining the decision.''',
    notes='''Unallocated | Distinguishes free stock from portions already promised elsewhere.
Short | States a numerical gap rather than blaming the preparation team.
Proposed | Keeps the alternative from sounding agreed.
Bring back | Makes the communication loop explicit.
Which diners | Prevents a correct replacement from reaching the wrong person.
No confirmed time | Avoids a replenishment promise unsupported by the case.''',
    d='''Which shortage report is accurate? | Five requested, three unallocated potato portions, two short. | No potatoes exist anywhere. | Five portions are available. | Eight more portions are needed. | The comparison uses the stated demand and available count without exaggerating the shortage.
When may rice be described as accepted? | After the relevant diners' choice is actually confirmed | As soon as the kitchen says rice exists | Before Mei speaks to anyone | Whenever potatoes are short | Availability establishes an option, not a guest decision or agreed substitution.
Which handoff closes the communication loop? | Mei will ask the diners and return with their choices. | Someone should probably mention it. | Dario will assume both diners agree. | The ticket is automatically complete. | Naming the person and required return message gives the pending decision a clear owner.
What is not supported by the case? | Rice has the same price and is suitable for every dietary need. | Rice is available as an option. | Two potato portions are missing against demand. | The server needs the diners' decision. | Neither a price comparison nor a dietary-suitability assessment is supplied merely by rice availability.''',
    dialogue='''Dario | Mei, I need to flag the side count before this new ticket moves on. It requests five potato portions, and we have only three left unallocated.
Mei | So the [[shortfall::The shortfall is five requested minus three available, leaving two potato portions not covered by the current supply.]] is two portions. I should not tell the table that potatoes are completely gone, but we cannot cover all five requests.
Dario | Correct. Rice is available as an option for the other two sides, but nobody has asked the diners whether they want that change.
Mei | I will present it as a [[proposed substitution::The proposed substitution is an available rice option that remains unaccepted until the diners' relevant choice is confirmed.]], not as something the kitchen has already decided for them. I need to return with their actual choices.
Dario | Thank you. The three potato portions I counted are not assigned to another order. I do not want to confuse them with stock already promised elsewhere.
Mei | That makes the [[unallocated portion::An unallocated portion has not been assigned to another order; three such portions are available in the stated count.]] count clear. We have three available for allocation, not five available and not three already committed to another table.
Dario | Exactly. I also have no confirmed time for more potatoes. Please do not tell the guests another batch will be ready shortly unless that is actually checked.
Mei | I will not promise [[replenishment::Replenishment would add more stock, but the case supplies no confirmed additional quantity or timing.]] that has not been confirmed. My message will be the current count and the rice option, with the choice still open.
Dario | Can you take responsibility for asking the two diners and telling the station what they decide? I need a specific person to bring the answer back.
Mei | Yes. I will obtain the [[guest decision::The guest decision belongs to the diners; Mei explicitly accepts the task of asking and reporting it back.]] and return to you. I will identify the affected diners so a confirmed alternative is not attached to the wrong plate.
Dario | Good. Until then, I will not put rice on two plates and hope that saves time. The availability of an ingredient is not agreement to change the order.
Mei | Agreed. The [[order hold::The order hold preserves the unresolved side choice; it prevents a proposed alternative from becoming a silent change.]] on that unresolved detail stays clear. We have an option to discuss, not a completed replacement instruction.
Dario | If they ask whether the price changes, I do not have that answer from the information we have. That needs the actual authorized pricing response.
Mei | I will separate that from the [[alternative side::The alternative side is rice, but its availability does not establish a price consequence or settle dietary suitability.]] itself. I also will not claim it meets a dietary requirement without the appropriate ingredient and preparation checks.
Dario | Right. We should not stretch the three portions into five smaller servings just to make the count look complete. Our portion specification still matters.
Mei | The shortage does not change [[portion control::Portion control preserves the specified serving amount; a shortage does not authorize silently shrinking portions to cover demand.]]. I will explain the real option rather than hide the difference in the amount served.
Dario | If they accept rice, please bring back which two diners agreed. If they do not, tell me that too so we can use the proper next step.
Mei | I will make the [[return message::The return message reports the actual choices and affected diners, completing the communication loop without assuming acceptance.]] specific. Silence or the fact that I walked to the table will not count as acceptance.
Dario | Then we are aligned: five requested, three potato portions available, two pending choices, and you are asking about rice. The ticket is not complete yet.
Mei | Correct. An [[accepted substitution::An accepted substitution requires an actual confirmed choice; the present handoff establishes only the option and the person asking.]] will be recorded only after the relevant decision. I am taking the question now and will return with the answer.''',
    transfer_title='Offer a different available side',
    transfer_setup='A ticket requests seven portions of couscous, but five remain unallocated. Roasted carrots are available as a proposed alternative. Server Noor will ask the two affected diners. No acceptance or price decision is supplied.',
    transfer='''Cook: "The shortfall is ___ portions." | two | Seven requested minus five unallocated leaves two portions short.
Server: "The proposed alternative is roasted ___." | carrots | Roasted carrots are the available option named in the scenario.
Cook: "The server obtaining the choice is ___." | Noor | Noor explicitly owns asking the diners for their decision.
Server: "The substitution is not yet ___." | accepted | No diner has confirmed acceptance in the supplied facts.''',
))

BOOK['units'].append(unit(
    title='Checking dietary modifications',
    scene='No cheese is not the full question',
    skill='Upgrade a simple omission request to an accurately communicated allergy review without inventing ingredient or handling assurances.',
    brief='Ticket 17 says "no cheese." Server Arun then reports that the diner has a milk allergy. Cook Tessa has not checked the sauce specification and cannot confirm the dish\'s suitability. Lead Noor is available to review the question with the server. Tessa must preserve both the requested cheese omission and the newly reported milk allergy, keep the sauce and preparation questions open, and route them through the actual allergy process. No ingredient finding, accepted alternative, food exposure, or reaction is supplied. The exchange is a pre-service clarification, not a clinical assessment.',
    cast='Arun | Server carrying the allergy report\nTessa | Cook receiving the updated ticket information',
    culture=('New information can change the question', 'No cheese may begin as an omission instruction, but a later allergy report requires clear communication of the allergen and the relevant review. Do not criticize the timing of the disclosure or reduce the new information back to a preference. Keep the guest informed without promising suitability.'),
    a='''What additional information does Arun report? | The diner has a milk allergy. | The sauce has already been verified. | A safe replacement has been accepted. | The diner has had a reaction in this case. | Arun reports a milk allergy beyond the original no-cheese wording.
Which specification remains unchecked? | The sauce specification | A supplied verified medicine dose | A completed payment record | The ticket number itself | Tessa has not checked the sauce specification, so its relevant contents remain unverified.
Who is available to review the question? | Lead Noor with the server | Only an unidentified person next month | Another guest making a guess | No responsible person | Noor is available to review the question with Arun through the actual process.''',
    vocabulary='''omission request | Instruction to leave out a named component. | record the omission request
reported allergy | Allergy information attributed to the diner or relaying colleague. | communicate the reported allergy
milk protein | Protein originating from milk that matters in milk-allergy assessment. | identify milk protein
casein | Group of proteins found in milk and used in some food ingredients. | recognize casein as milk-derived
whey protein | Milk-derived protein associated with the liquid separated during cheesemaking. | identify whey protein
compound ingredient | Ingredient made from multiple components that may need separate checking. | examine a compound ingredient
sauce specification | Documented information describing the actual sauce product or recipe. | verify the sauce specification
ingredient declaration | Statement identifying ingredients in a food product. | review the ingredient declaration
allergen source | Food source associated with a relevant allergenic protein. | identify the allergen source
contains statement | Label statement identifying major food allergens intentionally present under the relevant labeling rules. | read the contains statement
advisory statement | Warning such as may contain that requires appropriate interpretation, not a guarantee from its absence. | interpret an advisory statement
recipe verification | Check that the relevant current recipe and ingredients are correctly identified. | complete recipe verification
cross-contact | Unintended transfer or introduction of an allergen into another food. | address cross-contact
shared utensil | Tool used across foods that may create a relevant handling question. | check shared-utensil use
preparation control | Required measure governing how food is prepared under the actual safety system. | follow preparation controls
allergen flag | Clear marker carrying the reported allergen with the relevant order. | preserve the allergen flag
ticket update | Change adding or correcting information on the order record. | communicate the ticket update
dish suitability | Whether the complete dish and preparation can meet the relevant verified requirement. | assess dish suitability
unverified component | Part of a dish whose relevant information has not been checked. | identify an unverified component
ingredient finding | Result actually established by checking a relevant ingredient source. | report an ingredient finding
safety assurance | Statement that a specified safety condition is met, requiring adequate evidence and authority. | avoid an unsupported safety assurance
pre-service review | Check performed before the relevant food is served. | request a pre-service review
review owner | Person responsible for coordinating the unresolved question. | identify the review owner
guest update | Accurate message to the diner about the query and its actual status. | provide a guest update''',
    precision='Leaving off cheese answers a topping instruction, not the whole milk-allergy question. The sauce, other components, and preparation conditions require appropriate verification. Casein and whey are examples of milk-derived proteins; do not rely only on the everyday word milk appearing in a dish name.',
    precision_extra='No sauce result is supplied. Do not change unchecked into contains milk or milk-free. An absent advisory statement is not a universal absence guarantee. Use the actual current product information and allergy process, and communicate what remains unresolved.',
    phrases='''Receive the update | Thank you; I have heard that the diner reports a milk allergy.
Keep the omission | The no-cheese request still belongs to ticket 17.
Expand the question accurately | Leaving off cheese does not confirm the whole dish.
Name the unchecked component | The sauce specification has not been checked.
Avoid a guessed ingredient | I cannot say whether this sauce contains milk from the information available.
Name the review owner | Noor can review the question with you.
Preserve the allergy marker | Keep milk allergy clearly linked to the ticket.
Ask about the actual recipe | We need the current sauce recipe or product information.
Include preparation | The relevant cross-contact and handling questions also need review.
Avoid a false safety claim | I cannot confirm suitability yet.
Keep the guest informed | Tell the diner the question is being checked, not already resolved.
Do not invent an alternative | Any replacement needs its own appropriate checks and the guest's choice.
Separate receipt and result | Receiving the allergy report is not completing the review.
Avoid blaming the disclosure | Let us handle the updated information clearly now.
Preserve the source | Arun reports the diner's milk allergy.
Close the handoff | Ticket 17, no cheese, milk allergy reported, sauce unchecked, Noor available to review.''',
    notes='''Still belongs | Preserves the original omission alongside new information.
Does not confirm | Rejects an unjustified leap from one modification to whole-dish suitability.
Has not been checked | Marks an information gap, not a positive or negative finding.
Current | Keeps the review tied to the actual recipe or product.
Also | Includes preparation questions beyond ingredients alone.
Not already resolved | Prevents a progress update from becoming reassurance.''',
    d='''Which statement correctly handles the new report? | Keep no cheese and add the reported milk allergy for the appropriate review. | No cheese proves the dish is suitable. | Ignore the allergy because the first ticket was shorter. | Replace milk with an unspecified preference. | The update preserves the omission and communicates the new allergen information accurately.
What does unchecked sauce mean? | No relevant ingredient conclusion is established yet. | The sauce definitely contains milk. | The sauce is certified milk-free. | The sauce can be served without further process. | An unchecked specification supports neither a positive ingredient finding nor an absence assurance.
Which statement about casein and whey is correct? | They are examples of milk-derived proteins relevant to ingredient checking. | They always mean the dish contains no milk protein. | They are synonyms for cheese omission. | They prove the entire kitchen is suitable for every diner. | These terms identify milk-derived proteins but do not by themselves complete a whole-dish or preparation assessment.
Which guest update is accurate? | The milk-allergy question is under review; suitability is not confirmed yet. | All checks are complete because the cook heard the report. | A substitute has been accepted without asking. | The diner had a reaction despite no such report. | The message communicates the actual unresolved stage without a false guarantee or invented event.''',
    dialogue='''Arun | Tessa, I need to update ticket seventeen. It says no cheese, but the diner has now told me they have a milk allergy. I want to make that explicit.
Tessa | Thank you. I will keep the [[omission request::The omission request is no cheese; it remains relevant but does not replace the broader reported milk-allergy information.]] and the allergy information together. Leaving off the cheese does not confirm that the complete dish is suitable.
Arun | I have not told the diner it is suitable. I said I would bring the information to the kitchen and return with an accurate answer.
Tessa | Good. The [[sauce specification::The sauce specification has not been checked, so its relevant ingredients cannot yet be stated as present or absent.]] has not been checked. We cannot answer the sauce question from the topping instruction alone.
Arun | Noor is available to review it with me. I can make sure the lead has the ticket number, the cheese omission, and the milk allergy exactly as reported.
Tessa | Please do. Keep the [[allergen flag::The allergen flag keeps the reported milk allergy attached to ticket seventeen as it moves between the server, cook, and lead.]] clear on ticket seventeen through our actual process. The new information should not disappear into a vague special-request note.
Arun | Should I say the sauce contains milk, or only that we have not checked it? I do not want to give the guest the wrong conclusion in either direction.
Tessa | Say it is an [[unverified component::An unverified component has not been checked; that status does not establish either milk content or absence.]]. We have no verified ingredient finding here. Do not turn unknown into definitely contains milk or definitely suitable.
Arun | We will need the actual current sauce information, not a memory of a recipe that may have been used on another service.
Tessa | Exactly. [[Recipe verification::Recipe verification checks the relevant current recipe and ingredients, rather than relying on recollection or a different sauce version.]] must match what is being prepared. If it is a supplied product, the current product information matters as well.
Arun | And the ingredient check needs to include the components of the sauce, not just whether its name happens to mention cream or milk.
Tessa | Yes. A [[compound ingredient::A compound ingredient contains multiple components, so its relevant subingredients may need checking rather than relying on its short name.]] can have components that need review. Casein and whey are milk-derived proteins; the familiar dish name is not a complete ingredient answer.
Arun | I will also ask Noor about the preparation arrangements. A suitable ingredient list would not by itself answer every question about handling.
Tessa | Correct. [[Cross-contact::Cross-contact concerns unintended allergen introduction during handling or preparation, which remains distinct from intentional ingredients.]] needs the appropriate process too. We should not present one completed ingredient check as proof that every relevant preparation question is settled.
Arun | I will tell the diner that Noor is reviewing the question with us. I will not say the review is complete simply because you have received the update.
Tessa | That is an accurate [[guest update::The guest update should describe the actual review stage without converting receipt of the allergy report into a completed suitability decision.]]. Keep the uncertainty visible, and do not propose an unverified replacement as automatically safe.
Arun | If the diner asks about a different dish, I will bring that specific option back for its own checks and obtain their decision before any change.
Tessa | Good. Any [[dish suitability::Dish suitability concerns the complete relevant dish and preparation, so another menu item needs its own appropriate assessment.]] conclusion must concern the actual dish and preparation. We do not have an accepted alternative or a verified outcome in this conversation.
Arun | My handoff to Noor is ticket seventeen, no cheese, milk allergy reported, sauce unchecked. I will ask for the actual review and report back.
Tessa | Yes. Noor is the [[review owner::The review owner coordinates the unresolved question; Noor's availability does not itself complete the checks or authorize service.]] available for that next step. Keep the food and message within our real allergy procedure until the relevant questions are properly resolved.''',
    transfer_title='Expand a different omission request',
    transfer_setup='Ticket 35 says no peanuts on top. The server then reports a peanut allergy. The dressing specification is unchecked. Lead Maya is available to review the question. No suitability result is supplied.',
    transfer='''Server: "The reported allergen is ___." | peanut | The reported allergy concerns peanut and must be preserved accurately.
Cook: "The unchecked component is the ___." | dressing | The dressing specification is explicitly the unresolved ingredient source.
Server: "The available review lead is ___." | Maya | Maya is named as available to review the updated question.
Cook: "Suitability is not yet ___." | confirmed | Removing a topping does not supply a completed whole-dish assessment.''',
))

BOOK['units'].append(unit(
    title='Reporting equipment and dish-station needs',
    scene='Scale B keeps going blank',
    skill='Report an observable equipment problem, identify the affected work, and request review and a verified alternative.',
    brief='At the pastry prep bench, scale B repeatedly shows a blank display. Cook Nia has stopped using it. No cause, repair, or measurement error has been established. Lead Omar needs to arrange the appropriate review and confirm whether scale A is available and suitable for the task. Nia should name the equipment and location, describe the observed display behavior, and keep both review and alternative status clear. The case supplies no permission to repair scale B, no proof that previous batches are defective, and no confirmed time for returning it to use.',
    cast='Nia | Cook at the pastry prep bench\nOmar | Kitchen lead receiving the equipment report',
    culture=('Describe the symptom before the cause', 'A useful fault report identifies the equipment, location, observed behavior, and work already stopped. Avoid presenting a guess as a diagnosis. Ask for the specific support needed so the lead can route the problem and assess an alternative through the actual procedure.'),
    a='''Which equipment is affected? | Scale B at the pastry prep bench | Scale A confirmed faulty | Every oven | An unidentified dishwasher | The report concerns scale B at the named pastry preparation location.
What has Nia observed? | The display repeatedly goes blank. | A confirmed internal electrical cause | A completed repair | A measured error in every previous batch | The supplied symptom is a repeatedly blank display, not a diagnosis or proven batch defect.
What is still needed about scale A? | Confirmation that it is available and suitable for the task | An assumption that it is already allocated to Nia | Permission to dismantle scale B | A guarantee of identical performance | Omar must verify the alternative rather than treat its mere existence as availability or suitability.''',
    vocabulary='''equipment identifier | Name or code distinguishing a particular piece of equipment. | state the equipment identifier
asset tag | Label used to identify equipment within an organization's records. | check the asset tag
fault report | Account of an equipment problem and its relevant context. | submit a fault report
display | Screen or indicator presenting a device's readings or status. | describe the blank display
intermittent fault | Problem that appears repeatedly but not necessarily continuously. | report an intermittent fault
observed symptom | Behavior directly noticed before its cause is established. | state the observed symptom
diagnosis | Established explanation of a fault after appropriate assessment. | avoid an unsupported diagnosis
out-of-use status | State indicating equipment has been removed from use under the relevant process. | communicate out-of-use status
pastry bench | Work surface or station used for pastry preparation. | identify the pastry bench
weighing task | Work requiring measurement of ingredient mass. | pause the weighing task
measurement result | Value produced by a measurement process. | verify the measurement result
measurement uncertainty | Characterization of doubt associated with a measurement result. | understand measurement uncertainty
resolution | Smallest displayed or distinguishable increment of a measuring device. | check the scale resolution
capacity | Maximum load or operating range specified for the equipment. | verify scale capacity
calibration | Comparison against a reference to establish measurement relationships, not necessarily adjustment. | review calibration information
verification | Check that specified requirements are met. | complete equipment verification
adjustment | Intervention changing equipment response to meet a required condition. | distinguish adjustment from calibration
service request | Request for authorized equipment assessment or maintenance. | raise a service request
authorized technician | Person permitted and qualified under the relevant arrangement to assess or service equipment. | contact an authorized technician
alternative equipment | Different device proposed for the required task. | verify alternative equipment
equipment availability | Whether a device can actually be assigned for use when needed. | confirm equipment availability
fit for task | Suitable for the specific intended work under applicable requirements. | confirm fit-for-task status
return to use | Resumption of operation after the required assessment and authorization. | authorize return to use
review status | Current stage of the assessment, distinct from a completed repair. | report review status''',
    precision='The display keeps going blank is an observation. The power supply has failed is a cause claim not supplied by this case. Describe the symptom without opening, adjusting, or repairing equipment outside the actual authorized process.',
    precision_extra='Scale A exists does not mean it is available, appropriate, or checked for this weighing task. Availability and suitability both need confirmation. A display fault also does not establish that every earlier ingredient weight or finished batch was wrong.',
    phrases='''Identify the device | Scale B at the pastry prep bench is affected.
Describe the symptom | Its display keeps going blank.
State the action already taken | I have stopped using it.
Avoid a guessed cause | I do not know the cause.
Name the affected work | The weighing task cannot continue on this scale as normal.
Request review | Please arrange the appropriate equipment review.
Ask about the alternative | Can you confirm whether scale A is available and suitable?
Do not claim a repair | No repair has been completed.
Keep the status clear | Scale B has not been cleared for return to use.
Separate previous-work questions | We have not established an error in earlier batches.
Preserve the location | The report concerns the pastry bench, not an unspecified station.
Stay within authority | I will not attempt an unauthorized repair.
Keep alternative status honest | Scale A is a proposed alternative until checked.
Ask for the actual next owner | Who will receive the service request?
Avoid a guessed timeline | No return-to-use time has been confirmed.
Close the report | Scale B, pastry bench, repeated blank display, use stopped, review needed.''',
    notes='''Keeps going | Describes repetition without inventing an exact frequency.
I have stopped | States an action already taken, not merely proposed.
Do not know | Separates observation from diagnosis.
Whether | Leaves the alternative genuinely open pending confirmation.
Available and suitable | Names two different checks.
Has not been cleared | Preserves the current operating status until the actual process changes it.''',
    d='''Which report is strongest? | Scale B at the pastry bench repeatedly goes blank; I stopped using it; the cause is unknown. | All kitchen equipment is broken. | The internal circuit has definitely failed. | Earlier batches are all defective. | The report names equipment, location, symptom, action, and uncertainty without an unsupported diagnosis.
Which request about scale A is appropriate? | Please verify that it is available and suitable for this task. | Its existence guarantees we can use it immediately. | Ignore its capacity and measurement requirements. | It proves scale B is repaired. | The alternative needs both practical availability and task suitability, not merely a known name.
What does the fault establish about previous batches? | No specific previous-batch error by itself | That every batch is unsafe | That every earlier weight was exact | That no review could ever be needed | A display symptom alone does not determine previous measurement results or eliminate appropriate follow-up questions.
Which statement falsely reports completion? | Scale B is repaired and cleared for use. | Review is needed. | Nia stopped using scale B. | No return time is confirmed. | The case supplies no completed repair, verification, or authorization to return scale B to use.''',
    dialogue='''Nia | Omar, I need help with scale B at the pastry prep bench. Its display keeps going blank, so I have stopped using it for the weighing task.
Omar | Thank you for making the [[fault report::The fault report identifies the specific equipment, observed problem, and action taken without claiming a diagnosed cause.]] specific. Scale B, pastry prep bench, repeated blank display, and use stopped. Do you know the cause, or only the symptom?
Nia | Only the symptom. I have not identified an internal fault, and I have not tried to open the scale or make a repair.
Omar | Keep that as an [[observed symptom::The observed symptom is the blank display; a cause or repair diagnosis requires appropriate assessment not supplied here.]]. We should not write that a particular component failed when we have not established it through the appropriate assessment.
Nia | Can you arrange the equipment review and check whether scale A is available? I need a confirmed way forward for the work at this bench.
Omar | I will arrange the appropriate [[service request::The service request routes the equipment problem for authorized review; submitting it is not the same as completing a repair.]]. I also need to check scale A rather than assume it can be assigned to you immediately.
Nia | I know it exists, but I do not know whether another station is using it. I also cannot confirm that it meets this task's requirements.
Omar | Exactly. [[Equipment availability::Equipment availability means the device can actually be assigned when needed; knowing scale A exists does not establish that.]] is one question, and suitability is another. We need both answered before presenting it as your confirmed alternative.
Nia | Please keep the location in the report. A message saying the scale is blank could send someone to a different bench or device.
Omar | I will include the [[equipment identifier::The equipment identifier distinguishes scale B from scale A or other devices, keeping the report tied to the correct asset.]] and the pastry location. That gives the person reviewing it a clear starting point without a guessed cause.
Nia | Does this automatically mean that everything I weighed earlier was wrong? I do not have evidence about those earlier readings from this symptom alone.
Omar | It does not establish a specific [[measurement result::A measurement result concerns an actual recorded value; the display symptom alone does not determine every earlier reading's accuracy.]] as wrong. Any question about earlier work needs its own appropriate review, not a blanket conclusion or a blanket reassurance.
Nia | I will not resume using scale B just because the display briefly comes back. The repeated blanking is the problem I am reporting.
Omar | Keep the [[out-of-use status::Out-of-use status preserves the stopped-use condition until the actual review and authorization process determines the next action.]] clear through our actual process. A momentary display change is not evidence that a repair or required check has been completed.
Nia | For scale A, we need more than a place to put ingredients. Its capacity and the required measurement performance have to fit the job.
Omar | Yes, it must be [[fit for task::Fit for task means meeting the actual weighing requirements, not merely being a different device that can display a number.]]. I will not call it suitable just because it is another scale or appears to be free.
Nia | Should I tell the pastry team that scale B will be back in service in a few minutes? No one has given me a review time.
Omar | Do not promise a [[return to use::Return to use requires the relevant actual assessment and authorization; no timing or completed decision is supplied here.]] time. We have a report to route and an alternative to verify, not a completed equipment decision.
Nia | My update to the team will be scale B unavailable for our task, use stopped, cause unknown, and scale A still awaiting your confirmation.
Omar | That accurately states the [[review status::Review status distinguishes the current unresolved equipment question from a repaired scale or confirmed replacement.]]. I will handle the review route and alternative check, and communicate the actual outcome before anyone treats the issue as resolved.''',
    transfer_title='Report another display problem',
    transfer_setup='Scale C at the cold-prep bench repeatedly goes blank. Cook Noor has stopped using it. The cause is unknown. Lead Maya will arrange review and verify whether scale D is available and suitable.',
    transfer='''Cook: "The affected scale is ___." | C | Scale C is the device with the reported display problem.
Lead: "Its location is the ___ bench." | cold-prep | The brief identifies the cold-preparation bench as the affected location.
Cook: "The cause remains ___." | unknown | No cause has been established by the observed display behavior.
Lead: "The proposed alternative is scale ___." | D | Scale D still needs availability and suitability confirmation.''',
))

BOOK['units'].append(unit(
    title='Closing and handing over unfinished work',
    scene='Counted is not checked',
    skill='Transfer unfinished closing work with explicit acceptance while preserving separate counts, reviews, and completion states.',
    brief='At shift change, cook Elena has completed the garnish count: twelve portions. A waste-log entry concerning three damaged tarts is awaiting the lead\'s review. The closing shelf check has not been performed. Incoming cook Owen is asked to accept that shelf check. The handover does not establish disposal of the tarts, approval of the waste entry, completion of shelf checks, or release of any food for service. Elena must give each item its actual status, and Owen must repeat the specific task he is accepting without implying that the whole kitchen is closed.',
    cast='Elena | Outgoing cook\nOwen | Incoming cook',
    culture=('Finished tasks do not erase unfinished ones', 'A confident handover can include incomplete work. Name it plainly, assign the next action, and keep a pending review with its decision owner. Avoid an all done summary that hides one unchecked area behind another completed count.'),
    a='''What task is complete? | The garnish count at twelve portions | The closing shelf check | The lead's waste review | Every kitchen closing task | The brief establishes only the garnish count as complete among these three items.
What awaits lead review? | The waste-log entry for three damaged tarts | An approved disposal certificate | A completed shelf inspection | A new garnish order | The waste entry is pending review, and no approval or disposal result is supplied.
What task is Owen asked to accept? | The unperformed closing shelf check | Retroactive approval of every waste entry | An invented repair | A completed task needing no action | The incoming cook is specifically asked to take responsibility for the shelf check.''',
    vocabulary='''closing checklist | Record of required end-of-service or shift tasks and their actual status. | follow the closing checklist
garnish count | Number of prepared garnish portions established by counting. | complete the garnish count
waste log | Record of food waste or relevant waste events under the actual process. | update the waste log
damaged product | Item affected by physical or other damage requiring appropriate handling. | identify damaged product
review pending | Status indicating a required assessment has not yet been completed. | mark review pending
shelf check | Examination of a storage shelf against the relevant requirements. | perform the shelf check
completed count | Quantity check actually finished, distinct from other controls. | report the completed count
carryover task | Work transferred unfinished to a later person or shift. | assign a carryover task
incoming cook | Colleague accepting work at the next shift or stage. | brief the incoming cook
outgoing cook | Colleague transferring responsibility or finishing a shift. | receive the outgoing cook's handover
task acceptance | Explicit agreement to take responsibility for a specified action. | confirm task acceptance
completion record | Evidence that a defined task was actually performed. | update the completion record
sign-off | Authorized acknowledgment of completion or approval in the relevant process. | obtain the required sign-off
disposal authorization | Permission for a disposal action under the applicable procedure. | verify disposal authorization
date marking | Labeling food with relevant dates under the actual food-safety system. | verify date marking
stock rotation | Organized use of stock in the required order. | check stock rotation
FIFO | First in, first out: rotation approach using earlier received stock first where appropriate. | follow the FIFO arrangement
FEFO | First expired, first out: rotation approach prioritizing the earliest applicable expiry. | distinguish FEFO from FIFO
storage location | Identified place where an item is held. | record the storage location
cleaning | Removal of food residue, dirt, and other unwanted material. | complete the required cleaning
sanitizing | Treatment reducing microorganisms to the required level under the applicable process. | verify the sanitizing step
warewashing | Cleaning and sanitizing utensils and food-contact equipment through the appropriate system. | follow warewashing procedures
unperformed check | Required examination that has not yet taken place. | disclose an unperformed check
closing handover | Transfer of actual end-of-shift status and unfinished work. | give a closing handover''',
    precision='Twelve garnish portions counted does not establish that shelves have been checked or that every food-safety control is complete. Keep quantity, task completion, and permission to use or dispose of food as separate matters.',
    precision_extra='A waste-log entry can await review even while another closing task is complete. Do not record disposal or approval unless it actually occurs. Follow the real handling requirements for damaged food; an administrative review is not permission to ignore immediate safety controls.',
    phrases='''Open the handover | I have one completed count and two unfinished matters to hand over.
Report the finished count | The garnish count is complete at twelve portions.
Name the pending review | The waste entry for three damaged tarts awaits the lead's review.
State the unchecked task | The closing shelf check has not been performed.
Ask for acceptance | Can you take the shelf check?
Accept precisely | I accept the shelf check; I have not completed it yet.
Preserve the decision owner | The lead still owns the waste review.
Avoid a false disposal record | No disposal action is established in this handover.
Keep the units | Twelve portions of garnish and three damaged tarts are different counts.
Do not call everything done | The whole closing checklist is not complete.
Record completion afterward | Mark the shelf check complete only after it has been performed.
Keep controls active | Follow the actual handling requirements for the damaged items.
Separate counting and suitability | A completed count does not by itself authorize service.
Identify the next update | Report the shelf-check result through the closing process.
Preserve the open entry | Keep the waste-review status visible until the decision is made.
Close with clear ownership | Owen accepts the shelf check; the lead retains the waste review.''',
    notes='''Complete at | Gives both completion status and the measured count.
Awaits | Marks a pending review without implying approval.
Has not been performed | States absence of the check clearly.
I accept | Establishes responsibility, not completion.
Only after | Links the record to the actual event.
Retains | Keeps an existing decision owner from disappearing during the shift change.''',
    d='''Which handover is accurate? | Garnish count complete at twelve; three-tart waste entry pending; shelf check not performed. | All closing tasks done | Waste approved and shelves checked because garnish is counted | Three portions of garnish and twelve damaged tarts | The message preserves the distinct quantities and statuses of all three matters.
What does Owen accepting the shelf check establish? | Ownership of the next task, not completion | That the shelves are already checked | Approval of the waste entry | Disposal of every damaged item | Task acceptance transfers responsibility while the check itself remains to be performed.
Which claim is unsupported? | The three damaged tarts have been disposed of with approval. | The waste entry awaits review. | Twelve garnish portions were counted. | The shelf check remains open. | The scenario supplies a pending log review but no approved disposal event.
How should completion be recorded? | After the actual required check, using its real result | Before checking because someone accepted the task | By copying a previous shift's sign-off | By replacing every pending label with done | Records must reflect actual performed work, not intentions, assumptions, or copied completion states.''',
    dialogue='''Elena | Owen, before I finish, I need to hand over three separate items. The garnish count is done, but the waste review and shelf check are not complete.
Owen | I am ready for the [[closing handover::The closing handover transfers actual completed and unfinished states, rather than compressing different tasks into an all-done summary.]]. Please give me each count and status separately so I do not confuse a finished task with one I need to take on.
Elena | The garnish count is complete at twelve portions. That is the quantity I counted, not a statement that every storage or closing check is done.
Owen | Understood. The [[completed count::The completed count establishes twelve garnish portions counted; it does not establish completion of other checks or authorize service.]] is twelve portions of garnish. I will keep that separate from shelf condition, storage checks, and any permission to use the food.
Elena | The waste-log entry concerns three damaged tarts. It still awaits the lead's review, and I have no approved outcome to pass to you.
Owen | I will keep that as [[review pending::Review pending means the lead has not completed the relevant waste-entry decision; the handover must not imply approval.]]. The three damaged tarts and the twelve garnish portions are different items with different statuses.
Elena | Correct. I am not reporting that the tarts have been disposed of, or that the entry has been approved. Those events are not established by this note.
Owen | Then I will not record [[disposal authorization::Disposal authorization is a separate actual permission; a pending waste-log entry does not establish it or a completed disposal.]] or a disposal event from the handover alone. The actual handling requirements still apply while the record is being reviewed.
Elena | The third item is the closing shelf check. It has not been performed. Can you accept responsibility for carrying it out through our closing process?
Owen | Yes, I accept that [[carryover task::The carryover task is the unperformed shelf check transferred to Owen, not the already completed garnish count.]]. I will perform the shelf check and report the actual result. Accepting it now does not mean it is already done.
Elena | Thank you. Please do not copy a previous sign-off or mark it complete because we have talked about it. The record needs to follow the real check.
Owen | The [[completion record::The completion record must follow the performed check and its actual result, rather than a promise or copied previous entry.]] will reflect what I actually do. I will not let an accepted task turn into a completed task before the work occurs.
Elena | We also should not use the garnish count as a shortcut for checking labels, storage arrangements, or whatever the actual shelf procedure requires.
Owen | Agreed. The [[shelf check::The shelf check concerns the relevant storage requirements and remains separate from the numerical garnish count.]] has its own requirements. I will follow the actual checklist rather than assume a known quantity proves the shelf has been checked.
Elena | The lead still owns the waste review. I am asking you to take the shelf task, not to approve the waste entry outside your authority.
Owen | That boundary stays clear in the [[waste log::The waste log entry remains with the lead for review; Owen's shelf-task acceptance does not approve that separate record.]]. I can preserve its pending status while taking responsibility for the shelf check.
Elena | Could you repeat the three items back? I want to make sure I have not blurred the quantities or left the unfinished task without an owner.
Owen | My [[task acceptance::Task acceptance explicitly assigns the shelf check to Owen while preserving the completed count and separately pending waste review.]] is the shelf check. Garnish is counted at twelve portions, the entry for three damaged tarts awaits the lead, and the shelf check is still unperformed.
Elena | That is correct. When the shelf check is finished, report its real result through the process. Until then, the kitchen closing work is not all complete.
Owen | I will keep the [[closing checklist::The closing checklist should show each task's true state, distinguishing counted, pending review, accepted, and completed work.]] accurate. My next action is the shelf check, while the lead retains the waste review and all actual food-handling controls remain in force.''',
    transfer_title='Transfer another unfinished closing check',
    transfer_setup='The sauce count is complete at nine portions. A waste entry for two damaged rolls awaits lead review. The refrigerator shelf check is unperformed. Incoming cook Noor accepts that check.',
    transfer='''Outgoing cook: "The completed sauce count is ___ portions." | nine | Nine portions is the completed sauce count supplied in this case.
Incoming cook: "The waste entry concerns two damaged ___." | rolls | Rolls, not sauce portions, are the damaged items awaiting review.
Outgoing cook: "The shelf check remains ___." | unperformed | The check has not occurred even though a receiving cook accepts it.
Incoming cook: "The receiving cook is ___." | Noor | Noor explicitly accepts responsibility for the next shelf check.''',
))
