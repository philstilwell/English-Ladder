"""Original Restaurant Serving learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='restaurant-servers',
    title='Restaurant Serving English',
    cover_label='ENGLISH FOR RESTAURANT TEAMS',
    cover_title='Restaurant\nServing',
    cover_size=39,
    tagline='Clear orders. Confident service.',
    audience='For restaurant servers, food runners, section leads, and guest-facing food-service teams.',
    map_intro='Eight lessons on orders, menu choices, allergies, delays, corrections, payment, shared service, and section handovers. Three additional conversations cover availability, service charges, and accessible ordering.',
    notes_title='Warm service. Precise details.',
    notes_intro='Good service depends on listening closely while several things happen at once. Move between friendly guest-facing language and concise kitchen messages. Keep the table, seat, dish, request, timing, and responsible person clear.',
    field_notes=[
        ('Ask one useful question', 'A short clarification can prevent a long correction. Repeat the exact detail that is unclear and ask the guest to attach it to a person or dish. Do not turn an unidentified modifier into a table-wide instruction.', '"Which dish should have no onions?"'),
        ('Translate kitchen shorthand', 'Colleagues may say fire, covers, or on the fly. Guests need a clear explanation of their meal. Use internal shorthand only when the listener understands its local meaning.', '"The kitchen estimates another eight minutes for your mains."'),
        ('Show the complete comparison', 'A set price and an individual dish price are not interchangeable. Name what each includes before describing the difference. A supplement increases the stated base; it is not a replacement price.', '"The steak set is $29 with dessert; steak alone is $27 without dessert."'),
        ('Own the next step', 'An apology is more useful when followed by a specific action within your authority. Separate a replacement offer from an approved bill adjustment, and transfer live queries to a named colleague.', '"I can offer the remake; the shift lead needs to review any bill adjustment."'),
    ],
    scope_note='All restaurants, prices, guests, and service events are fictional. This book teaches workplace English, not food-safety certification, medical advice, or payment compliance. Follow current local law and actual allergy, food-handling, payment, and emergency procedures. Menu descriptions do not establish allergen safety. Do not delay urgent help for a routine service conversation.',
    sources=[
        dict(title='US Bureau of Labor Statistics. Waiters and Waitresses.',
             url='https://www.bls.gov/ooh/food-preparation-and-serving/waiters-and-waitresses.htm',
             note='Occupational context for order-taking, kitchen communication, guest service, clearing, and payment work. The original cases do not represent employment statistics.', checked='10 October 2026'),
        dict(title='US Food and Drug Administration. Food Allergies.',
             url='https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies?lv=true',
             note='Background for allergen and cross-contact terminology. The allergy dialogue never certifies a dish or substitutes for current ingredient and preparation checks.', checked='10 October 2026'),
        dict(title='US Food and Drug Administration. Food Code 2026.',
             url='https://www.fda.gov/food/fda-food-code/food-code-2026',
             note='A model food code offered for jurisdictional adoption, not an automatically universal restaurant rule. Consult applicable current local requirements.', checked='10 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Confirming seats and order details',
    scene='Who asked for no onions?',
    skill='Attach each dish and modifier to the correct guest, then read back the order before sending it.',
    brief='At fictional table 12, three guests are ordering. Seat one wants mushroom pasta; seat two wants salad with dressing separately; seat three has not chosen. Someone says "no onions," but server Lena cannot tell which dish the request belongs to. She has not sent the order. Guest Sam at seat two confirms that the onion request belongs to the salad. The dialogue follows Lena and section lead Cam checking that clarified request before transmission. Seat three still needs time. No allergy is reported in this case, and the onion request must not be treated as a confirmed allergy or a rule for every dish.',
    cast='Lena | Server\nCam | Section lead',
    culture=('Clarification is part of attention', 'A guest may speak while another person is ordering, or answer on behalf of someone else. A brief, neutral check avoids blame and keeps the exchange moving. Say which detail needs clarification rather than asking the whole table to repeat everything.'),
    a='''Which seat has not chosen? | Seat three | Seat one | Seat two | All three seats | The brief explicitly leaves seat three's dish undecided.
Which request already belongs to the salad? | Dressing separately | No mushrooms in the pasta | A completed third main | Dressing mixed through the salad | Seat two requested salad with the dressing served separately.
What did Lena need to clarify when she first heard the request? | Which dish should have no onions | Which dish should have dressing mixed in | Whether seat three had ordered pasta | Whether seat one wanted a different main | The onion request initially lacked a dish reference; Sam subsequently attached it to the salad.''',
    vocabulary='''cover | One diner counted for restaurant service or planning. | serve three covers
seat number | Identifier linking an order to a place at a table. | confirm the seat number
table number | Identifier used to locate a dining table. | check the table number
order pad | Written surface used to record guest orders. | update the order pad
point of sale | System for entering orders and recording sales, often abbreviated POS. | enter the order at the point of sale
order ticket | Record of dishes and instructions sent for preparation. | read the order ticket
modifier | Instruction changing an item from its standard preparation or presentation. | attach a modifier
omission | Requested removal of an ingredient or component. | confirm the omission
substitution | Replacement of one component with another when available and permitted. | check a substitution
on the side | Served separately rather than mixed into or placed on the dish. | serve dressing on the side
read-back | Spoken repetition of recorded details to check accuracy. | give a read-back
seat reference | Link showing which guest a detail concerns. | clarify the seat reference
course | Stage of a meal, such as a starter or main. | enter the main course
main | Principal dish in a meal. | choose a main
starter | Dish served before the main course in the relevant menu format. | order a starter
garnish | Item added to finish or accompany a dish. | identify the garnish
accompaniment | Food served alongside a principal item. | describe the accompaniment
preparation request | Guest instruction about how an item should be prepared. | confirm the preparation request
dietary requirement | Food-related need that must be described accurately and handled appropriately. | clarify a dietary requirement
preference | Stated choice that must not automatically be labeled a medical condition. | record a preference
pending choice | Selection that has not yet been made. | keep a choice pending
send the order | Transmit a confirmed order through the restaurant's system. | send the order
order sequence | Agreed order in which information or dishes are handled. | preserve the order sequence
confirmation | Explicit agreement that repeated details are correct. | obtain confirmation''',
    precision='No onions needs a clear dish reference. Do not attach it to every plate because the speaker was unclear. A modifier describes the requested change; a reported allergy requires its own accurate communication and the actual allergy process.',
    precision_extra='Seat three has not chosen is not the same as seat three is not eating. Confirmed items and pending choices can coexist. Follow the restaurant process for sending partial orders, but never invent a third dish to complete a ticket.',
    phrases='''Clarify the dish | Which dish should have no onions?
Check the guest | Is that request for your salad?
Read back seat one | Seat one is the mushroom pasta.
Read back seat two | Seat two is the salad with dressing on the side.
Preserve the pending choice | Seat three is still deciding.
Attach the modifier | I have noted no onions for your salad.
Avoid a table-wide change | I will not apply that request to the other dishes.
Ask briefly | May I check one detail before I send this?
Translate separately | You would like the dressing served separately, correct?
Separate request and guarantee | I will confirm any preparation question through our kitchen process.
Keep the record aligned | The seat reference and modifier need to stay together.
Avoid an invented allergy | No allergy has been reported in this exchange.
Confirm understanding | Have I matched the dishes and requests correctly?
Allow time | I will give seat three another moment to choose.
Keep transmission accurate | The order has not been sent yet.
Close with the corrected detail | Salad for seat two, no onions, dressing on the side.''',
    notes='''Which dish | Targets the missing reference instead of questioning the guest's reason.
Still deciding | Describes an unfinished choice without canceling the meal.
On the side | Common serving phrase meaning separately.
Put on the request | Refers to recording the instruction, not adding onions to the food.
Yet | Distinguishes an unsent order from one already in preparation.
Matched correctly | Invites correction before an avoidable error moves to the kitchen.''',
    d='''Which clarification is most useful? | Which dish should have no onions? | Shall I put no onions on the whole table? | Is the pasta the one with both changes? | Should I send three portions of pasta? | The question asks for the missing dish reference without blame or unsupported changes.
What should be sent as the salad modifier after Sam confirms? | No onions, dressing on the side | No mushrooms in every dish | Dressing mixed through all dishes | Cancel seat three's meal | Sam confirms the onion request for the salad, which already has separate dressing.
Which statement preserves the pending choice? | Seat three is still deciding. | Seat three ordered mushroom pasta. | Seat three is not eating. | All three mains are confirmed. | The brief leaves the third choice open rather than establishing a dish or cancellation.
What does the onion request establish medically? | No allergy diagnosis or report by itself | A confirmed onion allergy for all diners | That no allergy process is ever needed | That all foods are safe | A requested omission alone does not supply an allergy report or a safety conclusion.''',
    dialogue='''Lena | Cam, can you check table twelve with me before I send it? Three guests, two mains chosen. I clarified the onion request with Sam at seat two.
Cam | Yes. Which dish gets the [[modifier::The modifier changes the salad order; Lena has confirmed that the onion request belongs to Sam at seat two.]]? Your first note says no onions between the two mains, so I cannot tell which one it follows.
Lena | It belongs to the salad, not the pasta. Sam also wants the dressing separately. I have corrected the note against seat two.
Cam | Salad, no onions, dressing [[on the side::On the side means the dressing is served separately, as Sam requested for the salad.]]. That is clear. What is seat one having?
Lena | Mushroom pasta, unchanged. Seat three was still looking at the menu when I came over, so I have left that choice open.
Cam | Keep it as a [[pending choice::Seat three has not selected a dish; a pending choice is neither a cancellation nor an order.]], then. Do not copy the pasta into the third seat just to fill the space.
Lena | I will go back to that guest. Before I do, can you repeat what you have? I want to catch any mismatch now.
Cam | Here is the [[read-back::A read-back repeats the recorded details so the colleagues can catch an error before transmission.]]: table twelve, seat one mushroom pasta; seat two salad, no onions, dressing on the side; seat three still deciding.
Lena | Correct. The salad has both requests. I originally wrote them between the items because two people were speaking at once.
Cam | Now the [[seat reference::The seat reference attaches both salad requests to seat two and leaves seat one's pasta unchanged.]] makes the connection clear. Keep the requests attached to that item in the system too.
Lena | I have not sent anything yet. I wanted to settle the unclear detail first rather than ask the kitchen to interpret my note.
Cam | Good. The [[order ticket::The order ticket communicates preparation instructions; its modifiers must stay with the correct dish when sent.]] needs the same dish-and-seat links. A general no-onions note across the table would give the kitchen a different instruction.
Lena | The screen shows three diners, but only two main dishes so far. That is why the totals do not match yet.
Cam | Three [[covers::Covers counts diners; three diners does not establish three completed main-course orders.]], two confirmed mains. That is fine while the last person is choosing. The diner count does not supply a missing order.
Lena | Sam said no onions, but did not report an allergy. I repeated the request and confirmed the dish rather than guessing the reason.
Cam | Record the [[omission::The omission is removal of onions from the salad; no allergy has been reported in this case.]] accurately. If an allergy is reported, use our allergy procedure; do not treat an ordinary modifier as a substitute for that process.
Lena | I will return to seat three now and ask what they would like. Then I can repeat the complete order to the table.
Cam | Get that last [[confirmation::Confirmation checks the actual chosen dish and details; the unfinished third choice cannot be confirmed in advance.]] from the guest. Leave Sam's salad request as it is unless Sam changes it.
Lena | Understood: pasta unchanged, salad with its two requests, third main still open. I will come back if the guest needs a kitchen check.
Cam | All right. Follow our process when you [[send the order::Send the order means transmit the checked details, after resolving the remaining choice through the restaurant's process.]]. Keep the dish, seat, and instructions together so the kitchen receives what the guests actually asked for.''',
    rehearsal=["Check the cloze answers. Read Lena and Cam's exchange, stressing table twelve, seat one, seat two, and seat three.","Switch roles. Say the final read-back without changing the pasta or inventing the third main.","Complete the table 8 transfer and check its key. Repeat with a partner: fish, seat two, soup unchanged, two covers."],
    transfer_title='Attach a different request',
    transfer_setup='Table 8 has two covers. Seat one orders tomato soup; seat two orders grilled fish. A lemon-separately request is clarified as belonging to the fish. No third diner or allergy is reported.',
    transfer='''Server: "The lemon request belongs to the ___." | fish | The clarification specifically attaches the separate lemon to the grilled fish.
Guest: "That is seat ___." | two | The guest ordering grilled fish is in seat two.
Server: "The tomato soup remains ___." | unchanged | No modification to the soup is supplied in the facts.
Guest: "There are two ___." | covers | Covers counts diners, and this table has two diners.''',
))

BOOK['units'].append(unit(
    title='Explaining menu choices and prices',
    scene='The steak set or steak alone?',
    skill='Explain a supplement, calculate comparable menu prices, and leave the purchase choice with the guest.',
    brief='The fictional lunch set is $24 and includes a main and dessert. Choosing steak adds a $5 supplement to that set price. The a la carte steak is $27 without dessert. Both steak options include potatoes. Guest Jordan initially thinks the steak set must cost $24, then wonders whether potatoes cost extra. Server Priya must compare the $29 steak set with the $27 steak alone, explain the two-dollar difference, and avoid inventing a separate dessert price, drink inclusion, or tax policy. No choice has been made at the start.',
    cast='Jordan | Lunch guest\nPriya | Server',
    culture=('Help the guest compare', 'A recommendation should explain a relevant difference without pressuring the guest or implying a more expensive option is always better. State the total for each option and its inclusions. Let the guest decide whether the added item is worth the difference.'),
    a='''What is the steak set price? | $29 | $24 | $27 | $32 | The $24 base plus the $5 steak supplement equals $29.
Which item is included in both steak options? | Potatoes | Dessert | Coffee | A separate starter | Both the steak set and a la carte steak include potatoes.
What is not supplied? | A separate dessert price | The set base price | The steak supplement | The a la carte steak price | The case gives the set comparison, not a standalone dessert price.''',
    vocabulary='''set menu | Group of included courses offered for a stated price, subject to listed conditions. | explain the set menu
a la carte | Ordered as individual menu items rather than as a set. | order a la carte
supplement | Additional charge added to a stated base price. | apply the steak supplement
base price | Starting price before specified additions. | state the base price
inclusive price | Price covering the items or charges explicitly named as included. | explain the inclusive price
inclusion | Item or service covered by the quoted option. | compare the inclusions
exclusion | Item or charge not covered by an option. | clarify an exclusion
price difference | Amount separating two prices on a comparable basis. | calculate the price difference
standalone price | Price charged for an item bought separately. | verify the standalone price
upgrade | Change to a different or enhanced option, often at an added cost. | explain the upgrade
main-and-dessert set | Meal option combining a main course and dessert. | choose the main-and-dessert set
side dish | Food served alongside a principal dish. | include a side dish
portion | Amount served to one person or as specified. | describe the portion
menu description | Written account of a dish or offer. | read the menu description
daily special | Dish or offer identified as special for the relevant service period. | explain the daily special
availability | Whether an item can currently be ordered. | check availability
value comparison | Assessment of price alongside the contents or benefits of an option. | make a value comparison
additional charge | Amount payable beyond a specified quoted price. | identify an additional charge
price clarification | Explanation resolving uncertainty about what an amount means. | give a price clarification
itemized total | Sum showing the individual components that make up the charge. | present an itemized total
optional extra | Additional item that is not compulsory or automatically included. | describe an optional extra
menu pairing | Combination of items offered or suggested together. | explain the menu pairing
price basis | Items and conditions to which a quoted price applies. | state the price basis
guest choice | Selection made by the diner after receiving relevant information. | confirm the guest choice''',
    precision='The $5 supplement belongs to the $24 set base: $24 + $5 = $29. It is not added to the $27 a la carte price. The comparison is $29 with dessert versus $27 without dessert, with potatoes in both.',
    precision_extra='A two-dollar difference between these options does not establish that every dessert costs two dollars separately. Do not promise identical portions, included drinks, or an all-in bill total when those details are absent. Explain the menu prices actually supplied.',
    phrases='''Introduce the set | The lunch set includes a main and dessert.
State the base | The set starts at $24.
Explain the addition | Steak carries a $5 supplement on that set.
Give the combined price | That makes the steak set $29.
Introduce the alternative | The a la carte steak is $27.
Name the difference in contents | The a la carte option does not include dessert.
Keep shared inclusions clear | Both steak options include potatoes.
Calculate the difference | The set is two dollars more than steak alone.
Avoid an unsupported standalone price | That difference is not a quoted separate dessert price.
Respond to a price misunderstanding | The $24 is the base, before the steak supplement.
Do not invent a surcharge | No extra potato charge is listed in these options.
Keep the choice open | Would you prefer the set with dessert or the steak alone?
Avoid pressure | It depends on whether you want the included dessert.
Separate unknown details | I would need to check any detail not stated on this menu.
Confirm the chosen option | Let me confirm which option you would like.
Summarize evenly | $29 with dessert, or $27 without dessert; potatoes are included in both.''',
    notes='''Starts at | Signals a base price that may change with a specified selection.
Carries a supplement | Common menu language for an added charge.
That makes | Introduces the result of a transparent calculation.
Both | Prevents a shared inclusion from sounding exclusive to one option.
Two dollars more | Compares these options without assigning every component a standalone price.
Would you prefer | Gives the decision to the guest after the comparison.''',
    d='''Which calculation is correct? | $24 + $5 = $29 for the steak set | $27 + $5 = $32 for the steak set | $24 - $5 = $19 for the steak set | $27 - $24 = $3 for dessert | The supplement is added to the set base, not to the a la carte price.
Which comparison is complete? | $29 with dessert versus $27 without dessert; both include potatoes. | $24 versus $27 with identical inclusions | $29 without potatoes versus $27 with potatoes | $5 versus $27 for the entire meal | This comparison gives the actual prices and distinguishes shared and different inclusions.
What cannot be inferred from the two-dollar difference? | The restaurant's standalone dessert price is $2. | The steak set costs $2 more. | The set includes dessert. | Both steak options include potatoes. | A difference between bundled offers does not establish the separate selling price of a component.
Which recommendation avoids pressure? | If you want dessert, the set includes it for two dollars more than steak alone. | The set saves five dollars compared with steak alone. | You can add any dessert later for two dollars. | The set includes coffee as well as dessert. | The recommendation uses the supplied price and inclusion difference without inventing benefits or removing choice.''',
    dialogue='''Jordan | Could you help me with the lunch menu? I saw twenty-four dollars beside the set, but there is another amount beside the steak.
Priya | Certainly. Twenty-four dollars is the [[base price::The base price is the set's starting amount before the listed five-dollar steak supplement is added.]] for a main and dessert. Choosing steak adds five dollars, so that particular set comes to twenty-nine.
Jordan | So the steak is five dollars extra on the set? I first read that as a separate price, which did not seem right.
Priya | Exactly. It is a [[supplement::A supplement is an addition to the stated base, not a replacement price or the cost of the whole dish.]] to the set. Twenty-four plus five is twenty-nine for the steak set, including dessert.
Jordan | I also see steak listed separately at twenty-seven. Is that another way of ordering the same main without taking the lunch set?
Priya | Yes, that is the [[a la carte::A la carte identifies an individual menu item rather than the main-and-dessert set being compared.]] option. The steak is twenty-seven without dessert. Both options include potatoes, so you do not need to add them to this comparison.
Jordan | Good, I was about to ask about the potatoes. I do not want to discover I need to order a side as well.
Priya | Potatoes are a shared [[inclusion::An inclusion is covered by the quoted option; potatoes are included in both steak choices in this menu.]] here. The difference stated on this menu is the dessert, alongside the two different menu prices.
Jordan | Then the set is two dollars more than the steak alone. I am not especially hungry, so I am deciding whether I want dessert.
Priya | That is the correct [[price difference::The price difference is twenty-nine minus twenty-seven, or two dollars between these two specific options.]]. If you want the included dessert, the set is twenty-nine. If not, the steak alone is twenty-seven.
Jordan | Could I order the steak alone and add dessert for two dollars later, or does that price only work with the set?
Priya | I would need to check the [[standalone price::The standalone price applies to a dessert bought separately; the two-dollar bundle difference does not establish it.]] before quoting that. The two-dollar comparison does not mean every separately ordered dessert has a two-dollar price.
Jordan | That makes sense. I may not want dessert after the steak. Could you give me a moment to choose?
Priya | Of course. A useful [[value comparison::A value comparison considers both price and inclusions, allowing the guest to decide whether the dessert matters.]] depends on what you want to eat. The more expensive option is not automatically the better choice for you.
Jordan | Is coffee included with the dessert in that set? I sometimes see that elsewhere, but I cannot find it in this description.
Priya | Coffee is not part of the stated [[main-and-dessert set::The main-and-dessert set names the included courses; coffee is not supplied as an inclusion in this comparison.]] in the details we are comparing. I would check its price and status separately rather than tell you it is part of the set.
Jordan | Thanks. I will leave coffee for now. Could you repeat just the two steak prices for me?
Priya | Then the [[price basis::The price basis specifies what each quoted amount covers, avoiding unsupported claims about other items or charges.]] is twenty-nine for steak, potatoes, and the included dessert, or twenty-seven for steak and potatoes without dessert.
Jordan | Let me check with my friend about dessert before I decide. I have not chosen the set yet.
Priya | Certainly. I will wait for your [[guest choice::The guest choice must be confirmed explicitly; discussing an option at length does not authorize ordering it.]]. When you are ready, tell me set or a la carte, and I will confirm the option before entering it.''',
    rehearsal=["Check the answers, then read the menu exchange with a partner. Stress twenty-four plus five and twenty-nine versus twenty-seven.","Switch roles. Repeat the final comparison, keeping potatoes in both options and dessert in the set only.","Complete and check the fish-set transfer. Read both prices aloud; do not turn the bundle difference into a standalone dessert price."],
    transfer_title='Compare another set',
    transfer_setup='A fictional main-and-dessert set has a $20 base and a $4 fish supplement. Fish alone costs $22 without dessert. Both options include rice. No separate dessert price is supplied.',
    transfer='''Server: "The fish set costs ___ dollars." | twenty-four | Twenty dollars plus the four-dollar supplement equals twenty-four dollars.
Guest: "Fish alone is ___ dollars." | twenty-two | The stated a la carte price is twenty-two dollars without dessert.
Server: "Both options include ___." | rice | Rice is included in both options under the supplied menu.
Guest: "The separate dessert price is ___." | unspecified | The bundle comparison does not supply a standalone dessert price.''',
))

BOOK['units'].append(unit(
    title='Receiving an allergy question',
    scene='Checking the bun before ordering',
    skill='Receive a reported allergy, ask the kitchen a precise question, and communicate unresolved ingredient and preparation information.',
    brief='At table 6, guest Eli reports a sesame allergy and asks whether the burger bun is suitable. Server Noor has an old menu description, not current ingredient or cross-contact information. Kitchen lead Cam is available to discuss the question before any order is sent. The conversation does not supply a verified bun ingredient list, a confirmed preparation arrangement, or a safe alternative. Noor must preserve the reported allergen, check the current product and handling information through the real allergy procedure, and avoid replacing an unanswered question with reassurance.',
    cast='Eli | Guest reporting a sesame allergy\nNoor | Server',
    culture=('Take the disclosure seriously', 'Thank the guest for identifying the allergy and make the next step clear. Do not test whether the guest sounds serious enough or rely on how a product looks. The guest should hear what is known, what needs checking, and who is handling the question.'),
    a='''Which allergen does Eli report? | Sesame | An unspecified dislike | A confirmed milk allergy | A general dislike of bread | Eli explicitly reports a sesame allergy in the brief.
What information does Noor hold? | An old menu description | A verified current bun specification | A confirmed cross-contact assessment | A guaranteed safe alternative | The available description is old and does not establish current ingredients or handling.
Who is available before an order is sent? | Kitchen lead Cam | Only a future supplier next month | No responsible colleague | Another diner making a guess | Cam is identified as available to discuss the allergy question.''',
    vocabulary='''food allergy | Immune-system reaction to a food protein that can be serious. | report a food allergy
allergen | Substance capable of causing an allergic reaction in a susceptible person. | identify the allergen
sesame | Seed recognized among the major food allergens in the United States. | flag a sesame allergy
ingredient list | Record of substances intentionally used in a product. | check the current ingredient list
product specification | Detailed information describing a particular supplied food product. | verify the product specification
supplier label | Label information attached to or associated with a supplied product. | inspect the supplier label
recipe | Specified ingredients and method for making a dish. | check the current recipe
cross-contact | Unintended introduction of an allergen into another food. | assess allergen cross-contact
shared equipment | Equipment used for more than one food or preparation. | check shared equipment
preparation area | Place where food is handled or assembled. | verify the preparation area
allergen matrix | Structured record showing allergen information across relevant menu items. | consult the current allergen matrix
current product | Actual product presently used, which may differ from an older description. | identify the current product
recipe change | Alteration to a dish's ingredients or method. | verify a recipe change
product substitution | Use of a different supplied item in place of the usual one. | check for a product substitution
allergy flag | Clear system marker identifying a reported allergy for the relevant order. | enter an allergy flag
kitchen lead | Responsible kitchen colleague coordinating the relevant preparation question. | consult the kitchen lead
order hold | Pause before progressing an order while a necessary matter is resolved. | maintain the order hold
ingredient verification | Check of the ingredients in the actual relevant product. | complete ingredient verification
handling information | Details about how food is stored, prepared, and served. | obtain handling information
unsupported assurance | Reassuring claim without adequate information or authority. | avoid an unsupported assurance
reported allergen | Substance the guest identifies as the source of an allergy. | repeat the reported allergen
alternative dish | Different menu item that still requires appropriate checks for the guest. | check an alternative dish
allergic reaction | Response to an allergen that may require urgent medical attention. | follow allergic-reaction procedures
emergency response | Immediate action through the applicable emergency arrangements. | activate the emergency response''',
    precision='A plain-looking bun is not an ingredient list. Ingredient information and cross-contact information answer related but different questions. Removing visible seeds does not establish suitability. An old menu description cannot certify the actual product being prepared today.',
    precision_extra='No reaction or exposure occurs in this scenario. Do not invent treatment instructions or tell a guest to test the food. Actual symptoms or urgent concerns require the appropriate emergency response, not completion of a routine menu inquiry.',
    phrases='''Acknowledge the disclosure | Thank you for telling me about the sesame allergy.
Repeat the allergen | I have heard sesame; is that correct?
State the information limit | This old description does not verify today's bun.
Pause the order | I will check before sending an order.
Name the next person | I will speak with Cam, our kitchen lead.
Ask about the actual product | Which bun is being used for this service?
Ask about the record | Can you verify its current ingredient information?
Include handling | We also need the relevant cross-contact information.
Avoid appearance-based reassurance | A plain surface does not establish the ingredients.
Do not improvise a fix | Removing visible seeds would not answer the safety question.
Keep the guest informed | The question is still being checked.
Avoid a false alternative | A different dish would need its own appropriate checks.
Preserve the allergy flag | The reported sesame allergy must stay linked to your order.
Separate receipt and resolution | Cam has received the question; it is not resolved yet.
Avoid unsupported certainty | I cannot confirm suitability from the information available.
Return to the guest accurately | I will explain the verified information and any remaining limits before you choose.''',
    notes='''Thank you for telling me | Receives the information without questioning the guest's credibility.
Today's bun | Directs the check to the actual product, not an outdated menu.
Before sending | Places verification ahead of order transmission.
Also | Makes clear that handling is an additional issue, not answered by ingredients alone.
Still being checked | Gives an honest interim status.
Cannot confirm | Marks an information limit without inventing a safe or unsafe verdict.''',
    d='''Which first response is best? | Thank you for telling me; I will check the current bun and handling information with Cam. | The bun looks plain, so it is safe. | Pick off any visible seeds. | Try a small bite first. | The response acknowledges the allergy and directs the unresolved questions to current product and preparation checks.
Which distinction matters? | Ingredients and cross-contact are separate questions. | A plain appearance proves no sesame. | An old menu is always current. | Receiving a question automatically resolves it. | A product's intended ingredients do not alone answer how unintended allergen contact is managed.
What does Cam's availability establish? | A kitchen lead can discuss the query. | The bun has been certified suitable. | No allergy flag is needed. | A different dish is automatically safe. | Availability provides a responsible contact, not a completed product or preparation assessment.
Which guest update is accurate? | I cannot confirm suitability yet; the current information is being checked. | Every dish is safe for every allergy. | The old description is enough. | A reaction has occurred even though none is reported. | The update preserves the unresolved status without offering a false guarantee or inventing a clinical event.''',
    dialogue='''Eli | Before I order, I need to ask about the burger bun. I have a sesame allergy, and the picture does not tell me what is in the bread.
Noor | Thank you for telling me. I will repeat the [[reported allergen::The reported allergen is sesame, which must be communicated accurately rather than replaced by a vague dietary note.]] when I speak with the kitchen: sesame. Is that correct, and is the bun the item you want me to check?
Eli | Yes, sesame, and I am asking about the bun first. I know some bread can contain it even without seeds on the surface.
Noor | I have only an old description here, not verified information for the [[current product::The current product is the bun actually used today; an old description cannot establish its present ingredients.]]. I will check with Cam, our kitchen lead, before sending an order.
Eli | Please include how it is handled, not just the ingredients. I would rather wait for an accurate answer than have someone tell me it is probably fine.
Noor | Of course. I will ask about the ingredients and [[cross-contact::Cross-contact concerns unintended allergen introduction, which is not answered solely by the bun's intended ingredient list.]]. I cannot confirm suitability from this description, and I will not put the order through while that question is unresolved.
Eli | Have you been able to pass that question to Cam? I would like to know it has reached the person checking the kitchen information.
Noor | Yes, Cam has received it. We need the current [[ingredient list::The ingredient list must match the actual bun in use, rather than an older menu or another supplied product.]] for today's bun. That check has not been completed, so the old description is not our answer.
Eli | Good. Please ask about preparation as well. I have had to be careful with shared equipment at other restaurants.
Noor | Yes. The relevant [[handling information::Handling information covers preparation and service conditions, making it distinct from the list of intentional ingredients.]] still needs verification through our allergy procedure. I made clear that you are asking about both ingredients and preparation.
Eli | Thank you. I also do not want anyone to remove visible seeds and assume that has answered the question. The bread itself matters.
Noor | Agreed. We need the actual [[product specification::The product specification describes the supplied item; visual appearance alone is not equivalent to verified product information.]] and relevant supplier information. A plain surface or removal of visible seeds is not enough to establish suitability.
Eli | I will wait. Please do not bring me a different dish in the meantime; I need to choose after the check.
Noor | Understood. The [[order hold::The order hold prevents this unresolved allergy query from being treated as an ordinary confirmed order ready for preparation.]] remains in place. Any alternative would need its own appropriate checks and your agreement before we proceed.
Eli | Has the kitchen actually checked the bun yet, or are they still finding the information?
Noor | Certainly. The [[ingredient verification::Ingredient verification is the actual check of the relevant product; receiving the question does not mean that check is complete.]] and preparation checks are not complete yet. I will keep their actual status clear rather than describe Cam receiving the question as a final answer.
Eli | If the bun does not work for me, could we discuss another option afterward? I have not picked one yet.
Noor | I will not. Any [[alternative dish::An alternative dish is a separate option requiring appropriate checks, not an automatically safe replacement for the bun.]] would need its own checks and your choice. Your order has not been sent.
Eli | That is fine. I will wait for the verified information before deciding. Please keep the sesame allergy attached to the discussion if someone else takes over.
Noor | Yes. The [[allergy flag::The allergy flag preserves the reported sesame allergy with the relevant order and handoff; it does not itself certify suitability.]] and the unresolved question must stay together. I will return with the information we can actually confirm and explain any remaining limits.''',
    rehearsal=["Check the cloze answers. Read the conversation, keeping sesame clear in every handoff and update.","Switch roles. Stress the difference between Cam receiving the question and completing the ingredient and handling checks.","Complete the peanut-sauce transfer and check the key. Repeat all four lines without claiming the sauce is suitable."],
    transfer_title='Receive a different allergen question',
    transfer_setup='At table 9, guest Alex reports a peanut allergy and asks about a sauce. The server has an old description only. Kitchen lead Imani accepts the query. No ingredient or handling answer is yet verified.',
    transfer='''Server: "The reported allergen is ___." | peanut | Alex reports peanut, which must be repeated without changing the allergen.
Colleague: "The product being questioned is the ___." | sauce | The inquiry concerns the sauce, not an invented bread or dessert.
Server: "The receiving kitchen lead is ___." | Imani | Imani explicitly accepts the query as the named kitchen lead.
Colleague: "Suitability is not yet ___." | confirmed | Neither current ingredients nor handling has been verified in this exchange.''',
))

BOOK['units'].append(unit(
    title='Coordinating courses and delays',
    scene='Eight more minutes?',
    skill='Explain a kitchen estimate against a guest departure time without converting readiness into a guaranteed meal completion.',
    brief='Table 14 has finished its starters. The mains were fired at 7:20. At 7:30, the kitchen estimates another eight minutes because one dish is still being prepared. The guests need to leave at 7:50. Server Tomas must explain the current estimate and offer a discussion about timing, while avoiding a promise that the mains will arrive exactly at 7:38 or that the guests can finish comfortably before departure. No cancellation, faster substitute, priority slot, or price adjustment has been approved in this case.',
    cast='Tomas | Server\nRiley | Guest at table 14',
    culture=('Tell the guest what the clock actually means', 'Internal timing can sound like a promise when repeated without context. Translate preparation status into guest-facing language, acknowledge the departure constraint, and check realistic options. Do not hide uncertainty behind kitchen jargon or assume the guest has enough time to eat.'),
    a='''When were the mains fired? | 7:20 | 7:30 | 7:38 as a completed event | 7:50 | The kitchen began the relevant preparation stage at the stated 7:20 time.
What is the current estimate at 7:30? | Another eight minutes | Eight minutes total since 7:20 | Guaranteed service at 7:30 | Guaranteed departure at 7:38 | The estimate is eight additional minutes from the 7:30 update.
What is the guests' departure requirement? | Leave at 7:50 | Begin starters at 7:50 | Arrive at 7:50 | Have the mains ready by 7:50 | The guests explicitly need to leave at 7:50.''',
    vocabulary='''fire | Kitchen instruction to begin or advance preparation at the required service stage. | fire the mains
fired time | Recorded time when the relevant preparation instruction was given. | confirm the fired time
pickup | Kitchen-to-service handoff when dishes are ready for collection. | coordinate pickup
pass | Kitchen area where finished dishes are checked and handed to service staff. | collect from the pass
expeditor | Person coordinating dish completion and kitchen-to-floor delivery. | check with the expeditor
course pacing | Timing of successive stages of a meal. | adjust course pacing
ticket time | Elapsed time associated with an order ticket, measured from a specified event. | check the ticket time
readiness estimate | Approximate expectation for when food will be ready at the stated stage. | give a readiness estimate
remaining time | Additional duration expected from the current update. | state the remaining time
departure deadline | Latest time by which guests need to leave. | acknowledge the departure deadline
service window | Period available for serving or completing a specified service activity. | discuss the service window
preparation stage | Current step in making a dish. | confirm the preparation stage
table update | Information given to guests about their order or service. | deliver a table update
timing constraint | Limit that affects when something needs to occur. | clarify the timing constraint
bottleneck | Step limiting the progress of the overall process. | identify the bottleneck
coordinated service | Arrangement for related dishes to reach guests in a planned sequence. | arrange coordinated service
rush request | Request to accelerate work that still requires confirmation. | check a rush request
priority | Relative precedence given to a task under the actual service arrangement. | confirm priority
on the fly | Urgent preparation request in restaurant shorthand, not a guarantee of instant service. | request a dish on the fly
elapsed time | Duration already passed between specified points. | calculate elapsed time
update point | Agreed occasion for communicating the next status. | agree an update point
timing discussion | Conversation about feasible options under a time constraint. | offer a timing discussion
completion promise | Commitment that a stated outcome will occur by a defined time. | avoid an unsupported completion promise
contingency | Alternative arrangement available if the intended plan cannot work. | verify a contingency''',
    precision='Eight more minutes at 7:30 points to approximately 7:38 for the stated readiness estimate. It is not eight minutes from 7:20. Readiness, delivery to the table, eating, payment, and departure are separate events.',
    precision_extra='The twelve minutes between 7:38 and 7:50 is a clock difference, not proof of a comfortable meal. Confirm what the kitchen estimate covers and discuss actual options. Do not promise an accelerated dish or cancellation before the appropriate decision is made.',
    phrases='''Acknowledge the wait | I am sorry your mains are taking longer than you expected.
Give the current update | At 7:30, the kitchen estimates another eight minutes.
Name the remaining work | One dish is still being prepared.
Translate the estimate | That points to around 7:38, not a guaranteed service time.
Preserve the source | This is the kitchen's current estimate.
Repeat the constraint | You need to leave at 7:50.
Avoid a false comfort claim | I cannot promise that leaves enough time for your meal.
Separate stages | Kitchen readiness and arrival at the table are different stages.
Offer a discussion | Let me discuss the timing options with you and the kitchen.
Avoid invented priority | I cannot promise a faster slot before it is confirmed.
Clarify the clock | The eight minutes is from the 7:30 update.
Keep the earlier time clear | The mains were fired at 7:20.
Do not promise a substitute | Any alternative timing needs to be checked.
Agree the next communication | Let us agree when you will receive the next update.
Do not dismiss the deadline | Your departure time matters to the decision.
Close accurately | The estimate is still provisional, and the timing options need discussion.''',
    notes='''Another | Marks additional time from the current update.
Around | Signals approximation rather than a fixed appointment.
Current estimate | Allows for a changed status without pretending certainty.
Need to leave | Identifies a departure constraint, not a food-readiness target.
Before it is confirmed | Keeps a request distinct from an accepted commitment.
Enough time | Requires the guest's practical needs, not arithmetic alone.''',
    d='''Which timing explanation is accurate? | At 7:30 the kitchen estimates eight more minutes, pointing to around 7:38. | The mains were served at 7:20. | Eight minutes from 7:20 guarantees service at 7:28. | The guests can definitely finish by 7:50. | The explanation anchors the additional eight minutes to the current update and retains uncertainty.
What does 7:50 minus 7:38 establish? | A twelve-minute clock interval, not guaranteed dining time | A promise that payment is complete | A confirmed twelve-minute cooking time | That the guests can stay indefinitely | Arithmetic alone does not establish delivery, eating, payment, or a comfortable departure.
Which offer stays within the facts? | I can discuss the timing options with you and the kitchen. | I guarantee a replacement in two minutes. | The bill is already canceled. | Your table has automatically received top priority. | A timing discussion is available without inventing an approved operational or financial change.
Which phrase needs translation for a guest? | Your mains were fired at 7:20. | You need to leave at 7:50. | One dish is still being prepared. | The current estimate is eight more minutes. | Fired is internal kitchen shorthand and may need a plain-language explanation of the preparation stage.''',
    dialogue='''Riley | Could you check our mains, please? We have finished the starters, and we need to leave at seven fifty. I am beginning to worry about the time.
Tomas | I am sorry about the wait. I have a current [[readiness estimate::The readiness estimate is provisional information about food readiness, not a promise that the whole meal will finish on time.]] from the kitchen: at seven thirty, they expect another eight minutes. One dish is still being prepared.
Riley | Another eight minutes from now? I thought the mains had gone in earlier. I am trying to work out whether we can stay.
Tomas | The [[remaining time::Remaining time means additional time from the seven-thirty update, not total time since preparation began.]] is from the seven-thirty update. That points to around seven thirty-eight for the stated estimate, but I cannot guarantee arrival at that exact time.
Riley | When did they start preparing them? We are not upset with you, but we do need to know where we stand.
Tomas | The [[fired time::The fired time records the preparation instruction at seven twenty; it is distinct from the later readiness estimate.]] was seven twenty. In our kitchen language, that is when the mains were called for preparation. It does not mean they were ready or served then.
Riley | All right. If they are ready around seven thirty-eight, that leaves twelve minutes before we have to go. That sounds rather tight for us.
Tomas | I agree that your [[departure deadline::The departure deadline is seven fifty, which must be considered separately from preparation or service estimates.]] matters. The twelve minutes is only the difference between those times; it does not guarantee enough time to receive the food, eat, and settle the bill.
Riley | Can you move our order ahead of everyone else? I realize the kitchen is busy, but we cannot miss the event we are going to.
Tomas | I can discuss a [[rush request::A rush request asks for acceleration; it does not establish accepted priority or a faster confirmed completion time.]] with the kitchen. I cannot promise a different position or faster completion before they confirm what is actually possible.
Riley | Would it be quicker to change one of the dishes? I do not want to cancel the whole meal if a realistic option is available.
Tomas | We can have a [[timing discussion::A timing discussion explores feasible options without claiming that a substitute or cancellation has already been approved.]] about that. I would need the kitchen to check any alternative; I do not have a confirmed substitute time to offer you now.
Riley | Please check. We would rather hear what is possible now than sit here hoping the food will arrive.
Tomas | Understood. My next [[table update::A table update should communicate the actual order status and options, not repeat reassurance unsupported by the kitchen.]] should tell you what the kitchen can confirm and what remains uncertain. We should also agree when you will hear from me again.
Riley | Does that time mean ready in the kitchen or actually at our table? We will still need time to eat and pay.
Tomas | Correct. [[Pickup::Pickup is the kitchen-to-service handoff, which remains distinct from delivery to the table and completion of the meal.]] and delivery to the table are separate from the cooking estimate. I will clarify which stage the estimate covers when I speak with the kitchen.
Riley | Thank you. We still need to leave at seven fifty, even if the food is delayed. That is the constraint we need you to work with.
Tomas | I will carry that [[timing constraint::The timing constraint remains the guests' seven-fifty departure; an uncertain kitchen estimate does not remove it.]] into the conversation. I will not represent your departure as flexible or assume you can stay longer.
Riley | Thank you. Please check before changing anything. We still have the original order for now.
Tomas | Agreed. I will avoid a [[completion promise::A completion promise would commit to a finished outcome; the available estimate does not justify such a guarantee.]] I cannot support. Your order status, the current estimate, and any decision we make next will stay clear.''',
    rehearsal=["Check the answers and read the delay conversation. Stress seven thirty, another eight minutes, and seven fifty.","Switch roles. Repeat the readiness explanation without promising table arrival or enough time to eat.","Complete the new-estimate transfer. Check the arithmetic and key, then read both the approximate readiness and fixed departure times."],
    transfer_title='Anchor a new estimate',
    transfer_setup='At 8:10, the kitchen estimates six more minutes for a dish. The guests need to leave at 8:30. No faster alternative or guaranteed table-delivery time has been confirmed.',
    transfer='''Server: "The estimate starts from ___." | 8:10 | The additional six minutes is anchored to the 8:10 update.
Guest: "That points to around ___." | 8:16 | Adding six minutes to 8:10 produces the approximate 8:16 time.
Server: "Your departure requirement is ___." | 8:30 | The supplied deadline is departure at 8:30, not food readiness.
Guest: "A faster alternative remains ___." | unconfirmed | No quicker option has been confirmed in this scenario.''',
))

BOOK['units'].append(unit(
    title='Correcting a dish without blame',
    scene='Pasta ordered, risotto delivered',
    skill='Acknowledge an order mismatch, offer a specific remedy, and separate replacement timing from a bill-adjustment decision.',
    brief='At table 3, guest Alex ordered vegetable pasta but received mushroom risotto. The ticket confirms vegetable pasta. Server Dana checks the mismatch and learns that the kitchen can remake the pasta with an estimated ten-minute wait. Dana may offer that replacement, but any bill adjustment requires shift lead review. The cause of the wrong delivery is not established. No allergy is reported. Alex has not accepted the remake at the start, and neither compensation nor a guaranteed ten-minute arrival has been approved.',
    cast='Alex | Guest at table 3\nDana | Server',
    culture=('An apology can be direct', 'Name the mismatch without making the guest prove an error already confirmed by the ticket. Take responsibility for the next step without guessing which colleague caused the problem. A sincere apology does not require inventing a free meal or a guaranteed preparation time.'),
    a='''What does the ticket confirm? | Vegetable pasta | Mushroom risotto | Two identical risottos | A canceled order | The ticket supports the guest's vegetable-pasta order rather than the dish delivered.
What replacement can Dana offer? | A pasta remake with an estimated ten-minute wait | A guaranteed two-minute steak | An automatic free meal | A completed refund | The kitchen offers the pasta remake, with its timing stated as an estimate.
Who must review a bill adjustment? | The shift lead | Any guest at a nearby table | Dana automatically without review | An unnamed supplier | The case assigns bill-adjustment review to the shift lead.''',
    vocabulary='''order mismatch | Difference between what was ordered and what was delivered or recorded. | acknowledge the order mismatch
remake | Newly prepared replacement for a dish that needs correction. | request a remake
replacement offer | Proposed substitute or corrected item that the guest may accept. | explain the replacement offer
service recovery | Actions addressing a service failure and its effect on the guest. | manage service recovery
apology | Direct expression of regret for an error or inconvenience. | offer a clear apology
inconvenience | Practical difficulty or disruption caused to the guest. | acknowledge the inconvenience
ticket check | Review of the order record to establish what was entered. | perform a ticket check
delivered dish | Food actually brought to the guest. | identify the delivered dish
ordered dish | Food the guest requested. | confirm the ordered dish
confirmed mismatch | Discrepancy established by the available record and observation. | state the confirmed mismatch
cause | Reason an error occurred, which may require further investigation. | avoid guessing the cause
blame | Attribution of fault to a person or group. | avoid unsupported blame
remedy | Action intended to put a problem right. | offer an available remedy
estimated wait | Approximate expected delay before a specified next event. | explain the estimated wait
acceptance | Agreement to a proposed option. | confirm acceptance
bill adjustment | Authorized change to an amount on the guest's bill. | request a bill adjustment
comp | Informal restaurant term for an item provided without charge under authorization. | obtain approval for a comp
discount | Reduction from a stated price. | authorize a discount
refund | Return of money already paid. | process an approved refund
void | Cancellation of a transaction or entry through the relevant system procedure. | record an authorized void
shift lead | Person coordinating service decisions during a shift. | consult the shift lead
approval limit | Boundary on the decisions someone may authorize. | observe an approval limit
resolution status | Whether the proposed correction has actually been agreed and completed. | confirm the resolution status
follow-up check | Later confirmation that the corrective action occurred and met the stated need. | make a follow-up check''',
    precision='The ticket confirms pasta, so the server can acknowledge the mismatch without guessing its cause. The kitchen offers a remake; the guest still needs to accept it. An available remedy is not the same as a completed resolution.',
    precision_extra='A remake, comp, discount, void, and refund are different actions. A refund returns paid money; a bill adjustment may happen before payment. Follow actual approval and payment procedures, and do not describe shift-lead review as a completed financial decision.',
    phrases='''Acknowledge the mismatch | You ordered vegetable pasta, and we brought mushroom risotto.
Apologize directly | I am sorry; that is not the dish you ordered.
Refer to the record | I checked the ticket, and it confirms the pasta.
Avoid blaming the guest | You do not need to explain the order again.
Offer the actual remedy | The kitchen can remake the vegetable pasta.
State the estimated wait | The current estimate is ten minutes.
Ask for acceptance | Would you like that replacement?
Keep timing honest | I cannot guarantee an exact arrival time.
Avoid guessing fault | I have not established how the mismatch happened.
Address the practical effect | I understand that the extra wait affects your meal.
Separate the financial question | Any bill adjustment needs the shift lead's review.
Do not promise an unauthorized comp | I cannot confirm a free item before approval.
Name the next action | I will bring the bill question to the shift lead.
Keep consent clear | I will wait for your go-ahead before arranging the replacement.
Check completion later | I will confirm that the correct dish reaches you.
Confirm the next step | I will check the bill question first, then come back for your decision.''',
    notes='''We brought | Acknowledges the service error without assigning unsupported individual blame.
Confirms | Identifies evidence for what was ordered.
Can remake | Describes an available action, not one already completed.
Would you like | Requests the guest's decision.
Current estimate | Preserves uncertainty in preparation timing.
Needs review | Marks a pending decision rather than approval.''',
    d='''Which apology fits the facts? | I am sorry; the ticket confirms pasta, but we brought risotto. | I am sorry; your order was entered as risotto. | I am sorry; the kitchen has confirmed who took the wrong plate. | I am sorry; I have already removed the charge. | The apology acknowledges the confirmed mismatch without blaming the guest or inventing a cause.
Which offer is authorized? | A pasta remake with an estimated ten-minute wait | A guaranteed ten-minute arrival and free meal | A refund already completed | Any replacement at any price with no check | Dana may offer the remake, while timing remains estimated and billing requires review.
Which statement keeps the financial decision accurate? | I will ask the shift lead to review the bill question. | I have already approved a comp. | Every remake legally requires a refund. | The kitchen estimate authorizes a discount. | The supplied authority covers referral for review, not a completed adjustment or universal rule.
When can the issue be described as fully resolved? | After the relevant agreed actions are actually completed and checked | Immediately when an apology is spoken | Before the guest accepts an offer | As soon as someone guesses the cause | An apology and offer are steps toward resolution, not evidence that the correction and related decisions are complete.''',
    dialogue='''Alex | Excuse me, this is mushroom risotto. I ordered vegetable pasta. Could you check? Everyone else has their main, and I do not want to start the wrong dish.
Dana | I am sorry about the [[mistake::The ticket confirms pasta but risotto arrived, so mistake acknowledges an established service error without assigning blame.]]. The ticket says vegetable pasta. We brought you something different.
Alex | Can I still get the pasta? I had been looking forward to it, but I am worried the others will finish before mine arrives.
Dana | The kitchen can make a [[remake::A remake is a newly prepared corrected dish, here the vegetable pasta originally ordered.]]. Their current estimate is ten minutes. Would you like me to arrange that?
Alex | Is that ten minutes from now? We have already waited for the first round, so I need a realistic idea before I decide.
Dana | They have quoted an [[estimated wait::An estimated wait is approximate; Dana cannot turn the kitchen's estimate into a guaranteed arrival time.]] of ten minutes. I cannot promise the exact arrival time, and I understand another wait disrupts your meal.
Alex | Will there be anything off the bill? I do not feel comfortable paying as though everything arrived correctly.
Dana | I can ask for a [[bill adjustment::A bill adjustment changes the charge and requires the shift lead's review under this case's stated authority.]]. Our shift lead needs to review that; I can offer the replacement but cannot approve the charge change myself.
Alex | I thought the replacement might be free. Are you saying you cannot promise that yet?
Dana | That is right. I cannot promise it will be [[complimentary::Complimentary means provided without charge; the offered remake has not been approved as free.]] before the lead decides. I will explain both the wrong dish and the additional wait.
Alex | Was the order entered incorrectly? I heard you say the ticket has pasta on it.
Dana | The ticket is correct. I do not yet know the [[cause::Cause concerns how the delivery error happened; the correct ticket alone does not identify the responsible stage or person.]] of the delivery error. I can acknowledge it without guessing which colleague made it.
Alex | If I do take the pasta, will you make sure it is mine this time? I would rather not go through this again.
Dana | Yes. I will [[check back::Check back means return to verify the correction and update the guest if the timing changes.]] on the corrected dish and keep you updated if the kitchen's timing changes.
Alex | Before I decide, could you speak to the lead about the bill? Please do not start the replacement yet.
Dana | Understood. I will wait for your [[go-ahead::The go-ahead is the guest's permission to proceed; Alex has expressly asked Dana not to start the remake yet.]]. Hearing the offer is not the same as agreeing to it.
Alex | Thank you. Can the lead speak with me if there are questions? I would prefer to explain what the extra wait means for us.
Dana | I will pass that request to the [[shift lead::The shift lead reviews the charge question and can receive Alex's request for a direct conversation.]], along with the ticket, what arrived, and the ten-minute estimate.
Alex | All right. For now, please check the bill question. Then I will decide whether to wait for the pasta.
Dana | That is our [[next step::The next step is the bill review and update; neither the financial decision nor Alex's remake choice is complete.]]. I am sorry your meal has been interrupted. I will return with the decision rather than leave you wondering what is happening.''',
    rehearsal=["Check the cloze answers. Read the apology and offer with a partner, acknowledging the wrong dish without assigning blame.","Switch roles. Keep Alex's go-ahead pending and the bill decision with the shift lead throughout.","Complete the soup transfer and check its key. Repeat the dish names, estimated wait, and named lead accurately."],
    transfer_title='Offer a different correction',
    transfer_setup='Table 7 ordered lentil soup but received tomato soup. The ticket confirms lentil soup. A remake is available with an estimated seven-minute wait. Lead Noor must review any bill adjustment.',
    transfer='''Server: "The ticket confirms ___ soup." | lentil | Lentil is the ordered soup confirmed by the ticket.
Guest: "The delivered soup was ___." | tomato | Tomato is the soup actually delivered in this scenario.
Server: "The estimated remake wait is ___ minutes." | seven | Seven minutes is the stated estimate, not a guaranteed arrival time.
Guest: "The bill question goes to ___." | Noor | Noor is named as the lead responsible for reviewing an adjustment.''',
))

BOOK['units'].append(unit(
    title='Explaining and splitting a bill',
    scene='What does three ways mean?',
    skill='Clarify equal payments versus item-based checks, state the arithmetic, and confirm the method before processing payment.',
    brief='Three diners have a fictional $72 bill, with all listed charges included. Guest Morgan asks to split it "three ways." The restaurant can arrange equal payments or separate checks by item before payment is processed. Server Jules must ask which method the diners mean. Equal shares would be $24 each; item-based shares cannot be calculated without the item allocation. No additional charge, tip decision, completed payment, or refund is supplied. Morgan later confirms that the group wants three equal payments, and Jules reads back that choice before processing.',
    cast='Morgan | Guest speaking for the group\nJules | Server',
    culture=('Do not make the social decision for the table', 'Guests may use split loosely, while differing about who should pay for shared dishes. Clarify the method without judging fairness or announcing private assumptions about relationships. Keep the conversation practical and confirm amounts before a payment is submitted.'),
    a='''What is the stated bill total? | $72 with all listed charges included | $72 plus an invented charge | $24 for the entire table | An unknown total | The scenario supplies a seventy-two-dollar total with its listed charges already included.
What does three ways need to clarify? | Equal payments or separate checks by item | Whether there are three diners at all | Whether the meal happened yesterday | Whether every diner ordered identical food | The phrase can refer to different allocation methods even with three diners.
What is each equal share? | $24 | $36 | $18 | $27 | Seventy-two divided by three equals twenty-four dollars per equal share.''',
    vocabulary='''check | Restaurant bill listing the guest's charges. | bring the check
bill total | Amount due for the listed charges. | confirm the bill total
itemized bill | Bill showing individual items or charges. | review the itemized bill
split payment | Payment of one amount through multiple payments or payers. | arrange a split payment
equal share | Same portion of the total assigned to each person. | calculate an equal share
separate check | Individual bill assigned to a particular diner or group. | prepare separate checks
item allocation | Assignment of particular ordered items to particular payers. | confirm the item allocation
shared item | Dish or charge used by more than one diner. | allocate a shared item
allocation method | Agreed way of dividing the total or items. | clarify the allocation method
subtotal | Sum before the specified additional components included in a final total. | distinguish the subtotal
listed charge | Amount explicitly shown on the bill. | verify a listed charge
service charge | Charge imposed under the restaurant's stated terms, distinct from a discretionary tip. | explain a service charge
gratuity | Usually a tip; an automatic mandatory charge may instead be a service charge under applicable rules. | clarify a gratuity
payment method | Means used to pay, such as a card or cash. | confirm the payment method
card terminal | Device used to submit a card payment. | present the card terminal
authorization | Approval stage for a payment under the relevant payment system. | check payment authorization
payment receipt | Record acknowledging the payment transaction. | provide a payment receipt
outstanding balance | Amount that remains unpaid. | confirm the outstanding balance
partial payment | Payment of less than the full amount due. | record a partial payment
payment confirmation | Evidence or acknowledgment that a payment was completed at the relevant stage. | check payment confirmation
rounding | Adjustment to an available monetary precision under the relevant method. | explain rounding
duplicate charge | Repeated charge for the same item or transaction where duplication is at issue. | investigate a duplicate charge
reconciliation | Comparison of payments and amounts due to check that records agree. | complete payment reconciliation
settle the bill | Complete payment of the amount due. | settle the bill''',
    precision='Three equal shares of $72 are $24 each. That arithmetic does not show what each diner consumed. Separate checks by item need an agreed allocation, including shared items, before amounts can be determined.',
    precision_extra='The scenario supplies a total with all listed charges included; do not add a guessed fee or assume a tip decision. Confirm actual restaurant terms and the guest-selected payment amounts. Agreeing a split is not proof that money has been collected.',
    phrases='''Clarify the request | Do you mean three equal payments or separate checks by item?
State the total | The bill total is $72.
Explain equal shares | Three equal shares would be $24 each.
Explain the other method | For item-based checks, I need to know which items belong to each person.
Handle shared dishes | How should the shared items be allocated?
Avoid a fairness assumption | I will use the method your group agrees on.
Check the timing | We can arrange either method before processing payment.
Confirm the selected method | You would like three equal payments, correct?
Read back the amount | That is $24 for each of the three payments.
Do not invent an extra charge | The stated total already includes all listed charges.
Separate the tip decision | Would you like to decide on any optional tip separately?
Keep payment status factual | The split is agreed, but no payment has been processed yet.
Check the terminal amount | Please check the amount before confirming the payment.
Track what remains | We need to record each actual payment against the balance.
Offer a receipt | Would each person like their own payment receipt?
Close before processing | Three equal payments of $24, against the $72 total.''',
    notes='''Do you mean | Offers two concrete interpretations instead of making a guess.
Would be | Gives the amount conditional on choosing equal shares.
By item | Refers to consumption allocation rather than equal portions of the total.
Before processing | Locates the clarification before a transaction occurs.
Each | Makes clear that twenty-four dollars applies to every equal share.
Agreed, but not processed | Separates a payment plan from completed payment.''',
    d='''Which first question resolves the ambiguity? | Do you mean equal payments or separate checks by item? | You all ate exactly the same amount, correct? | Shall I split only the food and leave the shared charges on one card? | Three ways always means three unequal checks, right? | The question presents the two supported methods without guessing the group's intention.
Which arithmetic is correct for equal shares? | $72 divided by 3 is $24 each. | $72 divided by 3 is $36 each. | Three payments of $24 leave $24 unpaid. | Three payments of $72 equal the original bill. | Three times twenty-four equals the full seventy-two-dollar total.
What is needed to calculate item-based checks? | An agreed allocation of items and shared charges | Only the number of diners | A guessed tip amount | An assumption that all dishes cost the same | Item-based amounts depend on who is assigned each charge, not simply the diner count.
What does confirmation of three equal payments establish? | The intended allocation, not completed payment | That every card has been charged | That a refund was issued | That all fees may be added again | Agreeing the method precedes processing and does not prove that any payment has been completed.''',
    dialogue='''Morgan | Could we split this three ways, please? There are three of us, and we would like to sort it out before everyone starts reaching for a card.
Jules | Certainly. Do you mean three [[equal shares::Equal shares divide the total into the same amount for each diner, unlike separate checks based on individual items.]], or would you like separate checks according to what each person ordered? We can arrange either before payment.
Morgan | What would it come to if we divided it equally? We shared a couple of dishes, so that may be easiest.
Jules | The [[bill total::The bill total is the stated seventy-two dollars, including all listed charges in this fictional scenario.]] is seventy-two dollars. Divided equally among three people, that is twenty-four dollars each. Those three amounts add back to seventy-two.
Morgan | If someone wants to pay only for their own meal, can you do that too? We would need to sort out the shared starters.
Jules | Yes. That requires an [[item allocation::Item allocation assigns charges to the relevant diners; their amounts cannot be calculated from the diner count alone.]]. We would also need your agreement about shared items rather than assume an equal division of those.
Morgan | We did share some food, so equal payments may be simpler for us. Let me confirm with the others before you enter anything.
Jules | Of course. The [[allocation method::The allocation method is the group's agreed way of dividing the bill, which the server should not choose for them.]] should be your group's choice. I will wait rather than treat our discussion as permission to process a payment.
Morgan | They have agreed. We want three equal payments, not separate bills based on individual dishes. Twenty-four each sounds right to us.
Jules | Thank you. I will arrange the [[split payment::The split payment applies three agreed twenty-four-dollar payments to one seventy-two-dollar bill; it does not change the total.]] as three payments of twenty-four dollars against the seventy-two-dollar total. Please confirm that is the method you want.
Morgan | Yes, that is correct. I want to make sure the number on the terminal will match that amount, not the whole seventy-two dollars.
Jules | We will check each amount on the [[card terminal::The card terminal displays the payment being submitted; checking its amount helps prevent an incorrect full-bill charge.]] before it is confirmed. Agreeing twenty-four each does not mean a payment has already been taken.
Morgan | Does the seventy-two already include everything listed on this check? I just want to be sure we are dividing the final figure.
Jules | Correct. The [[listed charge::A listed charge is already part of the supplied total; splitting the payment does not justify charging it a second time.]] amounts are included in the stated total. I will not invent an additional fee or assume a tip choice from this request.
Morgan | Could we each have a receipt for our own payment? Two of us need one for our records.
Jules | We can provide the relevant [[payment receipt::A payment receipt records an actual transaction; it should not be represented as proof of payment before processing occurs.]] through our payment process. It needs to reflect the payment that is actually completed, not just the split we have agreed.
Morgan | We will pay one at a time, then. Could you show each person the amount before they tap?
Jules | Yes. The [[outstanding balance::The outstanding balance is what remains unpaid after actual recorded payments, not an amount inferred solely from the agreed split.]] must reflect the actual payments recorded. Three agreed amounts are not a substitute for checking which transactions have completed.
Morgan | Yes, twenty-four each. We are all agreed now. You can bring the terminal when you are ready.
Jules | Exactly. We will obtain [[payment confirmation::Payment confirmation establishes the relevant completed transaction status, which remains separate from agreeing a payment plan.]] through the actual process. Three equal payments of twenty-four dollars is the instruction I am working from.''',
    rehearsal=["Check the answers. Read the exchange, contrasting equal payments with separate checks by item.","Switch roles. Say three payments of twenty-four against seventy-two, then confirm that agreement is not completed payment.","Complete and check the ninety-six-dollar transfer. Read four equal shares of twenty-four without changing the total."],
    transfer_title='Clarify four ways',
    transfer_setup='Four diners have a $96 total with all listed charges included. The restaurant supports equal payments or item-based checks before payment. The diners confirm equal payments. No payment has been processed.',
    transfer='''Server: "You have chosen ___ payments." | equal | The diners explicitly choose equal payments rather than item-based checks.
Guest: "Each share is ___ dollars." | twenty-four | Ninety-six divided by four equals twenty-four dollars per diner.
Server: "The full total remains ___ dollars." | ninety-six | Changing the allocation does not change the stated ninety-six-dollar total.
Guest: "The payments are not yet ___." | processed | The scenario confirms the method but supplies no completed payment.''',
))

BOOK['units'].append(unit(
    title='Agreeing on clearing and shared service',
    scene='An empty plate still in use',
    skill='Check permission to clear specific items and coordinate shared service without inferring that an empty plate is finished.',
    brief='At table 2, one diner has an empty plate, but the shared vegetable dish still contains food. The diner is using that plate for another portion. Server Mina and food runner Leo need to coordinate clearing. Extra sharing plates can be offered, but active items should remain unless the guest agrees otherwise. No request to end the meal or prepare the table for new guests has been made. The colleagues discuss the words Leo can use, then agree that he will ask what can be cleared rather than silently remove the plate.',
    cast='Mina | Server responsible for table 2\nLeo | Food runner helping with clearing',
    culture=('Ask rather than apply a dining stereotype', 'Dining customs differ, but nationality is not a reliable instruction for a particular table. An empty plate, a pause, or a cutlery position can be ambiguous. Ask a short question about the actual item and respect the answer without making guests explain their culture.'),
    a='''Why is the empty plate still needed? | The diner is using it for another portion. | The meal has definitely ended. | The table is being reset for new guests. | The plate is abandoned as an established fact. | The brief states that the diner will use the plate for more shared food.
What remains in the shared dish? | Vegetables | Only an empty serving vessel | A confirmed discarded meal | Nothing at all | The shared vegetable dish still contains food in this case.
What may the team offer? | Extra sharing plates | Unrequested removal of all active dishes | A new reservation without asking | A bill adjustment already approved | Extra sharing plates are available to offer, while clearing still needs clarification.''',
    vocabulary='''clear | Remove dining items that are ready to be taken away. | ask before clearing
pre-bus | Remove agreed finished items during a meal before the table's final clearing. | pre-bus discreetly
busser | Team member who supports clearing, resetting, and related dining-room tasks. | coordinate with the busser
food runner | Colleague who carries prepared dishes to guests and may assist service. | brief the food runner
sharing plate | Plate provided for taking a portion from a shared dish. | offer a sharing plate
shared dish | Food presented for more than one person to serve from. | leave the shared dish
serving utensil | Tool used to transfer food from a serving dish to a plate. | provide a serving utensil
place setting | Arrangement of dining items for one person. | maintain the place setting
side plate | Small plate used for bread, sides, or another specified purpose. | offer a side plate
sideboard | Service furniture or station used to hold dining-room supplies. | restock the sideboard
service station | Area holding supplies and equipment for dining-room work. | organize the service station
cutlery | Knives, forks, and spoons used for eating. | replace the cutlery
flatware | Common US term for eating utensils such as knives, forks, and spoons. | provide clean flatware
crockery | Plates, bowls, and other ceramic dining vessels. | handle the crockery
glassware | Drinking vessels made of glass. | collect finished glassware
active item | Item still being used or needed by a guest. | leave active items
finished item | Item the guest has finished using and agrees can be removed. | identify finished items
clearing permission | Guest agreement to remove a particular item. | obtain clearing permission
service cue | Action or signal that may suggest a service need but can require clarification. | clarify a service cue
meal pace | Speed and rhythm at which guests are eating. | respect the meal pace
table reset | Preparation of a cleared table for its next guests. | begin an authorized table reset
table turnover | Transition from one party's use of a table to the next. | manage table turnover
unobtrusive service | Assistance that meets guest needs without unnecessary interruption. | provide unobtrusive service
guest preference | Individual request about how service should be provided. | confirm the guest preference''',
    precision='Empty describes the plate contents at one moment. Finished describes the guest no longer needing it. The two are not equivalent here. A shared dish with food and an empty individual plate can belong to the same continuing meal.',
    precision_extra='May I clear this plate? asks about a particular item. Are you finished with everything? is broader and can create pressure or misunderstanding. Identify the item, wait for the answer, and keep the agreed clearing action aligned across the team.',
    phrases='''Ask about an item | May I clear this plate, or are you still using it?
Accept continued use | Of course; I will leave it for your next portion.
Check the shared dish | Would you like the vegetables to stay on the table?
Offer practical help | Would extra sharing plates be useful?
Avoid an assumption | An empty plate does not necessarily mean the guest has finished.
Coordinate the team | Please leave that plate; it is still in use.
State the observed fact | The shared dish still has food in it.
Keep the question narrow | Ask about the specific item rather than the whole meal.
Wait for permission | Let the guest answer before reaching for the plate.
Respect a refusal | Certainly; I will leave it where it is.
Avoid cultural guesses | We should ask this table what they prefer.
Separate stages | Clearing one finished item is not a table reset.
Preserve the shared arrangement | Leave the serving dish and active plates in place.
Keep extra items optional | We can offer more plates without adding them automatically.
Pass on the preference | The diner is keeping the plate for another portion.
Close the service loop | Confirm what may be cleared and tell the colleague helping you.''',
    notes='''This plate | Makes the permission request specific.
Or are you still using it | Gives a comfortable way to decline clearing.
Of course | Accepts the preference without making it an inconvenience.
Still | Signals continued use despite the empty surface.
Would be useful | Offers help instead of imposing equipment.
Not necessarily | Challenges an assumption without saying the cue is never meaningful.''',
    d='''Which question is most appropriate? | May I clear this plate, or are you still using it? | Shall I clear everyone's plates now? | Would you like the bill now the plates are empty? | May I remove the shared vegetables with this plate? | The question checks the actual plate and allows the diner to keep using it.
What does the empty plate establish? | Its current contents, not that it is no longer needed | Permission to remove every dish | The diner's nationality | A request for the bill | The plate is empty but remains in use for another portion.
Which instruction should Mina give Leo? | Leave the active plate and ask what may be cleared. | Remove the vegetables because one plate is empty. | Treat the meal as complete. | Add an unrequested charge for extra plates. | The instruction preserves active items while allowing a specific clearing-permission check.
How should cultural differences be handled? | Ask the individual table about its preference. | Infer the answer from nationality. | Use one cutlery position as universal proof. | Require guests to explain their cultural background. | A direct, respectful question establishes the actual preference without relying on group stereotypes.''',
    dialogue='''Leo | Mina, one plate at table two is empty. I was about to take it away, but the vegetable dish in the middle still has food.
Mina | Please leave that [[active item::The active item is the empty plate still needed for another portion; its empty surface does not make it finished.]] for now. The diner is using the plate for another portion, so empty does not mean finished in this situation.
Leo | I see. They are sharing, so the empty plate is not finished with. I will leave it where it is.
Mina | A [[service cue::A service cue may suggest a need, but the empty plate is ambiguous and requires checking with the guest.]] can help us notice a need, but it is not always permission. We should check the actual item before reaching across the table.
Leo | What would you say without interrupting the conversation too much? I want the question to be clear but not sound as though I am trying to hurry them.
Mina | Ask for [[clearing permission::Clearing permission is the guest's agreement to remove the specific item, which should be obtained before taking it.]] briefly: May I clear this plate, or are you still using it? Then pause long enough for an answer.
Leo | If they say they are using it for more vegetables, I can simply say of course and leave it. I do not need them to justify it.
Mina | Exactly. Respect the [[guest preference::The guest preference is the actual table's request, not a rule inferred from nationality or an empty plate.]]. We should not turn a small service question into a discussion of their dining customs or why they want to keep the plate.
Leo | We can offer extra plates as well, correct? That might make sharing easier, but I should not bring a stack of them without asking.
Mina | Yes, offer a [[sharing plate::A sharing plate can help guests take portions from a shared dish, but the extra item remains an offer.]] or more if useful. Say, Would extra sharing plates help? We have that option available, but it should remain their choice.
Leo | I will keep the vegetables in place too. There is still food there, and no one has asked us to remove the dish.
Mina | Good. The [[shared dish::The shared dish still contains vegetables for continued service, so one empty individual plate does not establish permission to remove it.]] and the individual plate belong to the same ongoing meal. Do not treat them as unrelated clearing decisions.
Leo | If another guest has actually finished with a glass or plate, may I check that item separately? I do not want to leave everything unnecessarily.
Mina | Yes. A [[finished item::A finished item can be removed with appropriate agreement without treating the entire table as finished with the meal.]] can be handled separately. Ask specifically, and keep the action narrow enough that we do not accidentally clear something another diner is using.
Leo | Right. I will check the glass separately, not start taking the whole setting away while they still have food.
Mina | Correct. A [[table reset::A table reset prepares the setting for new guests; clearing one agreed item during a meal is a different stage.]] is another stage. Our immediate task is to support this table's meal, not turn an empty plate into a deadline.
Leo | I will ask the diner, leave the active items, and offer extra sharing plates. Then I will tell you what they want so we stay consistent.
Mina | Thank you. That supports their [[meal pace::Meal pace is the guests' eating rhythm, which the team can respect by checking needs instead of rushing active items away.]]. It also prevents a second colleague from returning a moment later and asking to take the same plate.
Leo | I will keep it brief at the table. May I clear this plate, or are you still using it? Then I wait for the answer.
Mina | Exactly. [[Unobtrusive service::Unobtrusive service meets the real need with minimal disruption, combining a specific question with respectful follow-through.]] means noticing, asking briefly, and following the answer. Clear what is agreed, leave what is active, and keep the team informed.''',
    rehearsal=["Check the answers. Read Mina and Leo's exchange, then repeat the exact plate-clearing question in turn.","Switch roles. Pause after the permission question; distinguish an empty plate from a plate no longer needed.","Complete and check the dessert transfer. Repeat the offer of extra plates without implying clearing permission."],
    transfer_title='Check a shared dessert plate',
    transfer_setup='At table 9, an empty plate is still needed for more shared dessert. The dessert dish contains food. Extra small plates can be offered. No permission to clear the active plate has been given.',
    transfer='''Server: "The empty plate is still ___." | needed | The diner needs the plate for another portion of shared dessert.
Colleague: "The shared dish contains ___." | dessert | The remaining food in the supplied shared dish is dessert.
Server: "Extra small plates can be ___." | offered | The plates are an available offer, not an automatic addition.
Colleague: "Clearing permission has not been ___." | given | The scenario supplies no guest permission to remove the active plate.''',
))

BOOK['units'].append(unit(
    title='Handing over a live section',
    scene='Two tables, two unfinished tasks',
    skill='Give a concise table-by-table handover that separates meal stage, payment status, and an unresolved charge query.',
    brief='At 8:00, outgoing server Ben hands tables 4 and 5 to Maya. Table 4 has received its mains, but dessert has not been ordered. Table 5 has an open check and a pending query about a possible duplicate coffee charge. The shift lead is reviewing that query; no duplicate has yet been confirmed and no adjustment is approved. Ben needs Maya to accept both follow-ups explicitly. The handover does not establish a dessert order, a settled bill, or a resolved coffee issue. Maya agrees to take responsibility for the next guest-facing steps.',
    cast='Ben | Outgoing server\nMaya | Incoming server',
    culture=('A handover is an accepted responsibility', 'A rushed list of table numbers can hide unfinished work. State the meal stage, the open request, and the person handling any decision. Ask the receiving colleague to repeat the important details so that moving between shifts does not make a live guest concern disappear.'),
    a='''What is table 4's meal stage? | Mains served; dessert not ordered | Dessert served and paid | Mains not yet ordered | Meal canceled | The brief states that the mains are served while dessert remains unchosen.
What is table 5's check status? | Open | Paid and closed | Refunded in full | Never created | Table 5 has an open check while the coffee query remains under review.
Who is reviewing the possible duplicate coffee charge? | The shift lead | Maya as an already completed decision | The guest as sole approver of every system change | No one | The shift lead is already reviewing the query, but no result is supplied.''',
    vocabulary='''section | Group of tables assigned to a server or service team. | take over a section
live table | Table still receiving service or awaiting completion of a task. | identify live tables
outgoing server | Colleague transferring responsibility at a shift or section change. | brief the outgoing server
incoming server | Colleague accepting responsibility for the next service period. | confirm the incoming server
handover | Transfer of relevant information and responsibility between colleagues. | complete the section handover
handover time | Time at which the responsibility transfer is recorded or agreed. | state the handover time
table status | Current service stage and relevant conditions for a table. | summarize the table status
mains served | Status indicating main dishes have reached the guests. | confirm mains served
dessert decision | Guest choice about whether and what dessert to order. | follow up the dessert decision
open check | Bill that has not been settled and closed in the relevant system. | monitor the open check
pending query | Question awaiting an answer or decision. | carry forward a pending query
suspected duplicate | Possible repeated charge that still requires verification. | review a suspected duplicate
charge review | Examination of whether a billed amount is correct. | request a charge review
decision owner | Person authorized or responsible for resolving a specified question. | identify the decision owner
service owner | Person responsible for the guest-facing follow-up. | name the service owner
accepted follow-up | Next action explicitly taken on by the receiving colleague. | record an accepted follow-up
read-back confirmation | Repetition demonstrating that the receiving colleague understood the important details. | obtain read-back confirmation
closed check | Bill marked settled and closed through the actual payment process. | verify a closed check
status change | Actual transition from one confirmed state to another. | communicate a status change
exception note | Record highlighting an issue outside routine service flow. | preserve an exception note
unresolved item | Task or question that has not been completed or answered. | track the unresolved item
continuity of service | Uninterrupted attention to guest needs across staff changes. | maintain continuity of service
handover gap | Missing information or ownership during a transfer of responsibility. | prevent a handover gap
follow-through | Completion of an accepted action and appropriate communication of its result. | ensure follow-through''',
    precision='Mains served does not imply dessert ordered. Open check does not imply the bill is correct or the disputed item is wrong. A possible duplicate charge must remain a query until the review establishes the result.',
    precision_extra='The shift lead owns the charge decision; Maya can own the guest-facing update and follow-up. Explicit acceptance keeps these roles connected. Do not close the issue merely because the outgoing server has finished a shift.',
    phrases='''Open the transfer | It is 8:00, and I am handing over tables 4 and 5.
State table 4's stage | Table 4 has its mains.
Keep dessert accurate | Dessert has not been ordered.
Name the first follow-up | Please check whether table 4 wants dessert.
State table 5's balance status | Table 5 has an open check.
Identify the query | They have asked about a possible duplicate coffee charge.
Preserve uncertainty | The duplication has not been confirmed.
Name the decision owner | The shift lead is reviewing the charge query.
Avoid false compensation | No adjustment has been approved yet.
Ask for acceptance | Can you take both follow-ups?
Read back table 4 | I will follow up dessert without treating it as already ordered.
Read back table 5 | I will track the coffee review and update the guests.
Keep payment separate | The check remains open until the actual payment process is completed.
Preserve the record | Keep the unresolved query visible in the handover notes.
Avoid a false closure | The issue is not resolved just because the section changes hands.
Close with ownership | Maya has accepted both guest-facing follow-ups; the shift lead retains the charge review.''',
    notes='''Has its mains | Describes delivery, not the next course choice.
Has not been ordered | Prevents a future possibility from becoming a recorded order.
Possible duplicate | Preserves the uncertainty under review.
Is reviewing | Marks an active process, not a completed decision.
Can you take | Requests explicit ownership rather than assuming it.
Remains open | Keeps the payment state tied to actual events.''',
    d='''Which handover for table 4 is correct? | Mains served; dessert not ordered; follow up the dessert choice. | Dessert already entered for everyone | Mains still need ordering | The table has left and paid | The message preserves the known meal stage and identifies the unfinished dessert follow-up.
Which coffee description is justified? | A possible duplicate charge under shift-lead review | A confirmed fraudulent charge | A completed refund | An error already removed from every record | The brief supplies a pending query, not a confirmed error, motive, or adjustment.
Which ownership arrangement is clear? | Maya accepts guest follow-up while the shift lead reviews the charge. | Everyone assumes someone else will handle it. | Ben's departure automatically closes the query. | Maya announces approval before receiving a decision. | The arrangement distinguishes guest communication from the decision authority and gives both work streams an owner.
What must precede calling table 5's check closed? | The actual relevant payment and closure process | Merely changing servers | Writing possible duplicate in a note | Assuming dessert is unnecessary | A staffing handover does not establish that the bill has been paid or closed.''',
    dialogue='''Ben | Maya, it is eight o'clock. I need to hand over tables four and five before I leave the section. Each has a different follow-up still open.
Maya | I am ready for the [[handover::The handover transfers relevant table information and accepted responsibility, not just a list of numbers.]]. Please give me the current stage and unfinished request for each table so I can take them on clearly.
Ben | Table four has received its mains. Dessert has not been ordered, so please check their choice when it is appropriate in the service.
Maya | Understood: [[mains served::Mains served means the main dishes have reached table four; it does not establish that dessert has been ordered.]], dessert not ordered. I will not enter desserts on the assumption that your mention of them means the guests have already chosen.
Ben | Exactly. Ask about dessert when they are ready. There is nothing on the dessert ticket to chase.
Maya | I will handle the [[dessert decision::The dessert decision is the guest's pending choice; the incoming server should ask rather than treat it as an existing order.]] with table four. That is the first task I am accepting. What is happening at table five?
Ben | Table five still has an open check. They asked about what may be a duplicate coffee charge, and the shift lead is reviewing that question.
Maya | So the [[open check::The open check remains unsettled in the relevant process; the handover does not supply payment or closure.]] has a live query attached. I should not treat the bill as settled or the coffee line as already corrected.
Ben | Exactly. I have not been given a review result, and no bill adjustment has been approved. The guest needs an accurate update once there is a decision.
Maya | I will preserve the wording [[suspected duplicate::A suspected duplicate is a possible repeated charge under review, not a confirmed error or approved adjustment.]]. I will not tell them the charge is definitely wrong simply because a query has been raised.
Ben | The lead has the bill question. Can you check for the answer and keep table five updated after I leave?
Maya | I can be the [[service owner::The service owner takes responsibility for guest-facing follow-up while the shift lead remains responsible for the charge decision.]] for that follow-up. The shift lead makes the relevant decision; I track it and explain the actual outcome to the guests.
Ben | That is the distinction. Please keep the unresolved question visible in the notes as well, so it does not disappear when the section assignment changes.
Maya | I will retain the [[exception note::The exception note preserves the unusual unresolved coffee query alongside the table's ordinary service and payment status.]] and the current status. A change of server should not make a pending charge question look like routine payment completed.
Ben | Can you read back both tasks once more? I want to be sure I have not mixed the table numbers while we are moving between them.
Maya | My [[read-back confirmation::Read-back confirmation checks that the receiving server has matched each table with the correct unfinished task.]] is table four: follow up the dessert choice. Table five: track the shift-lead coffee review and give the guests the actual update.
Ben | Correct. Five is still open, and we have no approved adjustment. Please keep that separate from the fact you have taken the table.
Maya | Agreed. Any [[status change::A status change must reflect an actual new event or decision, not an assumption caused by the handover.]] will reflect what actually occurs. Accepted follow-up is not the same as completed service, approved adjustment, or settled payment.
Ben | Good. You have both follow-ups, and the shift lead still has the charge decision. That gives each next step a clear person to contact.
Maya | Yes, I accept both. I will maintain [[continuity of service::Continuity of service keeps guest needs attended to across the staffing change without losing unresolved work.]] for the two tables, check the pending decision, and keep the records aligned with what the guests are actually told.''',
    rehearsal=["Check the answers and read the handover with a partner. Keep table four and table five's tasks separate.","Switch roles. Repeat Maya's two accepted follow-ups, preserving the shift lead's separate charge-review responsibility.","Complete the tea-charge transfer and check the key. Read Noor's handover without calling the query confirmed or the check paid."],
    transfer_title='Hand over two different tables',
    transfer_setup='At 9:00, Noor takes tables 8 and 9. Table 8 has mains served and no dessert order. Table 9 has an open check with a possible duplicate tea charge under lead review. Noor accepts both follow-ups.',
    transfer='''Outgoing server: "Table 8 needs a ___ follow-up." | dessert | Dessert is not ordered, so Noor needs to check that choice.
Incoming server: "Table 9's check remains ___." | open | No payment or closure is established for table nine.
Outgoing server: "The queried item is ___." | tea | The possible duplicate concerns tea rather than an invented coffee charge.
Incoming server: "The receiving server is ___." | Noor | Noor explicitly accepts both follow-ups in this handover.''',
))
