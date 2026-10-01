"""Original Baristas and Cafe Staff learner-book content."""

from books.authoring import unit

BOOK = dict(
    slug='baristas-cafe-staff',
    title='Baristas and Cafe Staff English',
    cover_label='ENGLISH FOR THE CAFE COUNTER',
    cover_title='Baristas and\nCafe Staff',
    cover_size=38,
    tagline='Precise orders. Better conversations.',
    audience='For baristas, cafe counter staff, shift leads, and customer-facing coffee teams.',
    map_intro='Eight cafe conversations: clarify a drink order, compare textures, handle an allergy question, match a pickup, correct a label, discuss gift coffee, explain a combo price, and hand over the bar.',
    notes_title='Translate the menu into a clear choice.',
    notes_intro='Cafe shorthand is useful among colleagues but can confuse customers. Ask one precise question at a time, explain a comparison using the actual recipe, and keep the order details connected to the right cup.',
    field_notes=[
        ('Ask what the word means', 'Regular can describe a size, a coffee choice, or a familiar order. Check the intended meaning before using your own cafe convention.', '"By regular, do you mean our middle size or non-decaf coffee?"'),
        ('Compare one feature at a time', 'Foam, milk, espresso serving, flavor intensity, and caffeine are different features. Use the supplied recipe and avoid turning a texture comparison into an unsupported health or caffeine claim.', '"These two small drinks use the same espresso serving; the latte has less foam."'),
        ('Match the order, not just the name', 'A name can belong to more than one customer. Read back the ticket number and drink details, and separate a completed item from an order that is still in progress.', '"Ticket 67: large iced decaf latte. That one is still being made."'),
        ('Say what remains unchecked', 'An allergy query, remake time, grind request, or till reconciliation may still need a check. Explain the next step and keep a proposed action distinct from a finished result.', '"I will check the current product and preparation arrangements with our lead."'),
    ],
    scope_note='All cafes, recipes, tickets, prices, and incidents are fictional. This book teaches workplace English, not food-safety certification, medical advice, equipment operation, or cash-control procedures. Follow actual product information, local requirements, workplace allergen controls, equipment instructions, and payment rules. No example authorizes serving an unverified drink or bypassing a required check.',
    sources=[
        dict(title='National Coffee Association. Espresso.',
             url='https://www.aboutcoffee.org/brewing/espresso/',
             note='Background for espresso equipment, brewing-method vocabulary, and the distinction between flavor concentration and caffeine per serving. No universal cafe recipe is imposed.', checked='1 October 2026'),
        dict(title='National Coffee Association. Pour-over Coffee.',
             url='https://www.aboutcoffee.org/brewing/pour-over-coffee/',
             note='Context for whole beans, grinding, brewing methods, and matching grind to the intended brewer. Workplace instructions remain controlling.', checked='1 October 2026'),
        dict(title='World Coffee Research. Sensory Lexicon.',
             url='https://worldcoffeeresearch.org/resources/sensory-lexicon',
             note='Context for sensory descriptions of coffee flavor, aroma, and texture. No flavor wheel or lexicon text is reproduced.', checked='1 October 2026'),
        dict(title='US Food and Drug Administration. Food Allergies.',
             url='https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies?lv=true',
             note='Background for allergen and cross-contact terminology. A drink name or omitted syrup does not establish suitability for an allergy.', checked='1 October 2026'),
    ],
    units=[],
)

BOOK['units'].append(unit(
    title='Taking a precise drink order',
    scene='What does regular mean?',
    skill='Separate size, temperature, and coffee choice, then give a concise read-back before the drink is made.',
    brief='At this fictional cafe, regular is the middle cup size. Customer Alex asks for a regular latte, meaning non-decaf coffee rather than a particular size. Barista Nia has not started the drink. When asked separately, Alex chooses a small hot latte, non-decaf, with the standard dairy milk and no syrup, to take away. The task is to resolve the ambiguous word without correcting the customer as if there were one universal cafe vocabulary. No price, exact temperature, or caffeine quantity is supplied.',
    cast='Nia | Barista\nAlex | Customer',
    culture=('A clarification can sound welcoming', 'A short either-or question is often easier to answer than a list of technical terms. Explain your local size name without suggesting the customer used English incorrectly. Confirm choices in the same order each time so the read-back is easy to follow.'),
    a='''What does regular mean on this cafe menu? | The middle size | A universal caffeine amount | Small everywhere | The only available milk | The brief defines the local size convention, not a universal coffee meaning.
What did Alex initially mean? | Non-decaf coffee | A middle-size cup | An iced drink | An extra espresso serving | Alex uses regular for coffee choice rather than cup size.
Which order is confirmed? | Small hot non-decaf latte, standard dairy milk, no syrup, takeaway | Middle iced decaf latte | Large hot latte with vanilla | Small iced latte with oat drink | The separate answers establish every listed detail in the confirmed order.''',
    vocabulary='''barista | Worker who prepares and serves coffee drinks. | ask the barista
drink order | Specified beverage and selected variations. | confirm the drink order
cup size | Named or measured capacity option for a drink. | clarify the cup size
regular | Context-dependent label that may describe size or coffee choice. | clarify regular
small | Cafe-defined size below its larger options. | order a small latte
hot | Prepared as a hot drink rather than an iced version. | confirm hot or iced
iced | Served with ice according to the drink recipe. | make an iced latte
non-decaf | Coffee not sold as decaffeinated. | specify non-decaf coffee
decaf | Coffee processed to remove most caffeine, not necessarily all. | request decaf
latte | Espresso-based drink with milk; proportions depend on the recipe. | order a latte
espresso | Concentrated coffee brewed by forcing hot water through ground coffee under pressure. | prepare espresso
shot | Cafe serving of espresso, with size defined by its recipe. | confirm the shot count
standard milk | Milk used by default in a particular recipe. | identify the standard milk
dairy milk | Milk from an animal source rather than a plant-based drink. | specify dairy milk
plant-based drink | Beverage made from plant ingredients and used as a milk alternative. | check a plant-based drink
syrup | Liquid flavoring or sweetener added to a drink. | omit the syrup
modifier | Order detail that changes the standard item. | enter the modifier
takeaway | Order intended to be taken away from the premises. | mark as takeaway
for here | Order intended for consumption on the premises. | ask for here or to go
read-back | Spoken repetition used to confirm the received order. | give a read-back
clarifying question | Question that resolves a specific uncertainty. | ask a clarifying question
size convention | Local system for naming cup sizes. | explain the size convention
order entry | Recording of the selected item and its details. | check the order entry
preparation start | Point at which making the drink begins. | confirm before preparation start''',
    precision='Regular is not a reliable substitute for a complete order. In this cafe it names a size, but Alex means non-decaf. Ask which meaning is intended, then confirm the remaining choices separately.',
    precision_extra='A shot is a recipe-defined serving, not a universal caffeine quantity. Keep small, hot, non-decaf, milk choice, and syrup choice separate. None of those words alone supplies the price or an exact caffeine amount.',
    phrases='''Resolve the first word | When you say regular, do you mean size or non-decaf?
Explain the local label | Here, regular is our middle size.
Ask for size | Would you like small, regular, or large?
Separate temperature | Would you like that hot or iced?
Confirm coffee choice | Non-decaf coffee, correct?
Ask about milk | Would you like our standard dairy milk?
Check syrup | Any syrup, or none?
Check destination | Is that for here or to take away?
Repeat the core order | One small hot latte with non-decaf coffee.
Keep the omission explicit | No syrup in that one.
Confirm the milk | Standard dairy milk for this order.
Invite a correction | Have I got all of that right?
Pause preparation | I will confirm the details before we make it.
Correct the size | Small, not our regular size.
Acknowledge the clarification | Thanks; I understand which meaning you intended.
Close the read-back | Small, hot, non-decaf, standard milk, no syrup, takeaway.''',
    notes='''Regular versus standard | Both depend on local context; name the feature each describes.
Separate questions | Ask size and temperature separately when the original order is ambiguous.
Non-decaf | This describes the coffee choice without inventing a caffeine quantity.
No syrup | An explicit omission is easier to preserve than an assumed default.
For here or to go | To go is a common US alternative to takeaway.
Read-back rhythm | Group the item first, then size, temperature, and modifications.''',
    d='''Which question directly resolves the ambiguity? | Do you mean our middle size or non-decaf coffee? | You mean medium, obviously? | Shall I make the usual? | Is regular always hot? | The correct question names two plausible meanings without imposing either.
Which statement overclaims? | Non-decaf tells me the exact caffeine quantity. | Regular is our middle size here. | Alex wants a small drink. | The drink has not been started. | Coffee choice alone does not establish an exact caffeine quantity.
Which correction preserves Alex's request? | Small, not regular size; still non-decaf. | Regular size, now decaf. | Large because regular was ambiguous. | Iced because the order changed. | The correction changes the size interpretation without changing the confirmed coffee choice.
Why read the order back? | To verify the combined choices before preparation | To guarantee a serving time | To establish a price not listed | To replace the need for any product checks | A read-back confirms the details together and lets the customer correct a misunderstanding.''',
    dialogue='''Alex | Could I have a regular latte to take away, please? I am not sure what you call the sizes on this menu.
Nia | Certainly. When you say [[regular::Regular is the ambiguous word; the barista checks its intended meaning before selecting a size.]], do you mean our middle size, or do you mean non-decaf coffee? We use that word for size here.
Alex | I meant normal coffee rather than decaf. I do not need a big cup; the smallest latte would be enough for me.
Nia | Thanks, that helps. I will enter a [[small::Small is the size Alex chooses; regular referred to coffee choice, not the intended cup size.]] latte. The coffee choice is separate, so I will keep that as you requested.
Alex | Good. I sometimes end up with more coffee than I wanted because I use the same word for two different things.
Nia | It is easily mixed up. Would you like that [[hot or iced::Hot or iced asks about temperature style separately rather than inferring it from size or coffee choice.]]? I have not started making it, so we can confirm everything first.
Alex | Hot, please. I am taking it outside, and I would like something warm rather than a drink with ice in it.
Nia | A hot latte, understood. For the coffee, I have [[non-decaf::Non-decaf preserves Alex's clarified coffee choice without claiming a particular caffeine amount.]]. I am repeating that separately so it does not get confused with our size names.
Alex | Yes, that is right. What milk comes in it normally? I do not want to accidentally order a different version.
Nia | Our standard recipe uses [[dairy milk::Dairy milk is the stated default product category, which Alex asks the barista to identify.]]. Would you like that, or would you like to discuss one of the other options?
Alex | The standard milk is fine for this order. I would also like it without any syrup; I prefer it without added flavoring.
Nia | I have entered [[no syrup::No syrup records the explicit omission rather than leaving the bar to infer a default.]]. That is separate from the milk selection, and I will include both in the final read-back.
Alex | Thank you. I am not ordering a vanilla latte or anything like that, just the small hot latte we have been discussing.
Nia | Yes. And you said [[takeaway::Takeaway confirms the destination Alex supplied at the start, not an invented service arrangement.]], rather than drinking it here. I will make sure that is attached to the same order.
Alex | Correct. Can you repeat the whole thing once? I think we have settled it, but I would rather catch a mistake now.
Nia | Here is the [[read-back::A read-back repeats the complete received order so the customer can verify its combined details.]]: one small hot latte, non-decaf coffee, standard dairy milk, no syrup, to take away. Have I got that right?
Alex | Yes, exactly. So small is the size, and what I called regular meant the coffee choice. That makes sense now.
Nia | Exactly. Our [[size convention::Size convention names the cafe's local labeling system, which is different from Alex's use of regular.]] is small, regular, and large. You have chosen small; I have not changed your coffee choice.
Alex | Perfect. Thanks for checking rather than assuming I wanted the middle cup. That is all I would like to order today.
Nia | You are welcome. The [[order entry::Order entry is the recorded selection now checked with Alex, not proof the drink has already been made.]] now matches that read-back, so the bar can work from the confirmed details when preparing your drink.''',
    transfer_title='Confirm a different ambiguous order',
    transfer_setup='Customer Jo means decaf when saying regular coffee. After separate questions, Jo chooses a large iced latte with oat drink. Use these four confirmed details.',
    transfer='''Barista: "The coffee choice is ___." | decaf | Jo explicitly clarifies decaf as the intended coffee choice.
Customer: "The size should be ___." | large | Large is the selected cup size in this new order.
Barista: "The drink should be ___." | iced | Iced is the stated temperature style, not inferred from size.
Customer: "Please use ___." | oat drink | Oat drink is the specified milk alternative for this order.'''
))

BOOK['units'].append(unit(
    title='Comparing drinks without overclaiming',
    scene='Less foam, not more caffeine',
    skill='Compare drinks on the requested feature while distinguishing texture, espresso serving, and unsupported caffeine claims.',
    brief='Customer Morgan is choosing between the small latte and small cappuccino at this fictional cafe. Both recipes use the same espresso serving. The cappuccino has more foam; the latte has more liquid milk. Morgan wants less foam, not an extra espresso serving or a claim about caffeine. Barista Sora must explain the practical difference and recommend the option matching that preference. The recipes describe this cafe only. No laboratory caffeine measurement, universal cup proportion, or health recommendation is supplied.',
    cast='Morgan | Customer\nSora | Barista',
    culture=('Explain the contrast the customer needs', 'Specialist vocabulary can help when it answers a specific question. Start with the visible difference, such as more foam or more liquid milk. Add terms like texture only after connecting them to the customer preference. Avoid making taste sound objectively better or worse.'),
    a='''Which feature does Morgan want less of? | Foam | Caffeine established by measurement | Espresso servings | Liquid milk | The brief identifies less foam as the preference to satisfy.
What is the same in both recipes? | The espresso serving | The amount of foam | The amount of liquid milk | Every cafe recipe worldwide | Both small drinks use the same espresso serving in this fictional cafe.
Which option matches the stated preference? | The small latte | The small cappuccino because it has more foam | An extra-shot order not requested | No option can be compared | The latte has less foam than the cappuccino in the supplied recipes.''',
    vocabulary='''cappuccino | Espresso drink with milk and foam, made to a particular cafe recipe. | compare the cappuccino
foam | Aerated layer or texture containing bubbles in milk or another liquid. | reduce the foam
liquid milk | Milk considered separately from its aerated foam. | compare liquid milk
microfoam | Milk foam with very small bubbles and a smooth texture. | describe microfoam
texture | How a drink feels in the mouth. | compare the texture
mouthfeel | Sensation of a drink in the mouth beyond its flavor. | describe the mouthfeel
body | Perceived weight or fullness of a drink. | describe the body
flavor intensity | Perceived strength of taste or aroma. | compare flavor intensity
caffeine content | Amount of caffeine in a specified quantity or serving. | avoid guessing caffeine content
espresso serving | Recipe-defined amount of prepared espresso used in a drink. | use the same espresso serving
shot count | Number of recipe-defined espresso servings requested. | confirm the shot count
milk proportion | Share of a drink made up by milk. | compare the milk proportion
recipe basis | Specified formulation used for a comparison. | state the recipe basis
like-for-like | Comparing items on the same relevant basis. | make a like-for-like comparison
small size | Cafe-defined smaller serving used in this comparison. | compare the small size
aeration | Incorporation of air into a liquid. | describe milk aeration
steam wand | Machine part used to introduce steam into milk. | identify the steam wand
milk pitcher | Vessel used to hold milk during preparation. | identify the milk pitcher
crema | Foam-like surface layer produced on espresso during extraction. | distinguish crema from milk foam
extraction | Transfer of soluble coffee compounds into brewing water. | discuss extraction
concentration | Amount of a substance relative to the quantity of liquid. | distinguish concentration from serving amount
extra shot | Additional espresso serving beyond the recipe. | request an extra shot
preference | Customer's stated choice or desired feature. | match the preference
recipe variation | Difference in formulation between drinks or cafes. | allow for recipe variation''',
    precision='More foam does not mean more espresso. Here, the two small recipes contain the same espresso serving. Match the requested texture without promising an exact caffeine amount or making claims about every cafe.',
    precision_extra='Strong can mean intense flavor, concentrated coffee, or high caffeine. Ask which feature matters. A customer asking for less foam is not necessarily asking for a weaker flavor or less caffeine.',
    phrases='''Name the comparison | Are you comparing our small latte and small cappuccino?
Ask about preference | Is it the foam you would like less of?
State the shared feature | Both use the same espresso serving here.
Explain the cappuccino | Our small cappuccino has more foam.
Explain the latte | Our small latte has more liquid milk.
Recommend on evidence | The latte better matches your preference for less foam.
Limit the claim | I am describing our recipes, not every cafe.
Separate features | Foam and caffeine are different questions.
Clarify strong | By stronger, do you mean flavor or caffeine?
Avoid a false measurement | I do not have a measured caffeine figure for these drinks.
Keep the size consistent | I am comparing the two small sizes.
Confirm no extra shot | You are not asking for an additional espresso serving.
Use accessible language | Texture means how it feels in your mouth.
Separate crema | The espresso surface layer is not the same as milk foam.
Check understanding | Does the less-foamy option sound closer to what you want?
Close the choice | A small latte, based on your preference for less foam.''',
    notes='''Comparatives | More foam and less foam require a clear comparison item.
Same versus identical | The same espresso serving does not make every drink feature identical.
Here | This word limits a recipe statement to the actual cafe.
Would suit | A recommendation can match a stated preference without claiming universal superiority.
Strong | Clarify whether the speaker means taste, concentration, or caffeine.
Not necessarily | Use it to reject a false implication without inventing an alternative fact.''',
    d='''Which recommendation is best supported? | Choose the latte if less foam is your priority. | Choose the cappuccino because foam removes caffeine. | Add espresso because less foam means more caffeine. | Every latte everywhere is identical. | The supplied recipe comparison directly supports the latte for less foam.
Which statement preserves scope? | In our small recipes, the espresso serving is the same. | All cappuccinos use the same recipe worldwide. | Small always means one fixed volume. | More milk proves zero caffeine. | The phrase limits the comparison to the two actual cafe recipes.
What should Sora clarify if asked for stronger? | Whether Morgan means flavor or caffeine | Only the cup color | Whether foam is a medicine | A guaranteed caffeine figure from appearance | Strong has several possible meanings that require a specific follow-up question.
Which feature is not established? | Exact caffeine content in milligrams | More foam in the cappuccino | More liquid milk in the latte | The same espresso serving | No measured caffeine quantity is supplied in the brief or recipe comparison.''',
    dialogue='''Morgan | I usually order a cappuccino, but sometimes there is more foam than I enjoy. Would the small latte be a better choice here?
Sora | If you want [[less foam::Less foam is the customer's stated preference and the relevant basis for recommending the latte.]], our small latte is the closer match. The cappuccino has more foam, while the latte has more liquid milk.
Morgan | That sounds promising. I am not trying to order extra coffee, though. Does the latte automatically come with another shot because it has more milk?
Sora | No. In these two small recipes, we use the [[same espresso serving::The same espresso serving is the supplied shared feature; the texture difference does not add espresso.]]. The milk and foam differ, but that does not add another shot.
Morgan | So the difference you are describing is mainly what the milk feels like and how much foam there is on the drink?
Sora | Yes, that is the [[texture::Texture names how the drink feels, which is the comparison Morgan is asking about.]] difference relevant to your choice. Our latte has more liquid milk and less foam than our small cappuccino.
Morgan | I have heard people call cappuccino stronger. Does that mean I would get more caffeine if I chose it instead of the latte?
Sora | People use [[stronger::Stronger is ambiguous between perceived flavor and caffeine; it needs clarification rather than a single assumed meaning.]] in different ways. They may mean a more noticeable coffee flavor, rather than a larger amount of caffeine in the cup.
Morgan | I see. I do not need a caffeine number; I simply do not want an extra shot added without realizing it.
Sora | Then I will keep the [[shot count::Shot count identifies the espresso-serving quantity, which Morgan does not want increased.]] at the standard recipe. Neither choice here involves an extra shot unless you separately request one.
Morgan | That is useful. And when you say more liquid milk, you mean compared with your small cappuccino, not some bigger latte on another menu?
Sora | Exactly. It is a [[like-for-like::Like-for-like keeps the comparison on the two specified small drinks rather than mixing different sizes or cafes.]] comparison between our two small drinks. I am not comparing different cup sizes or promising the same recipe at another cafe.
Morgan | Thanks. I sometimes find menu descriptions assume I know all the coffee terms already. A straightforward comparison makes the choice easier.
Sora | Of course. The [[milk proportion::Milk proportion describes the milk share of the recipe and helps explain the difference without changing the espresso serving.]] affects the balance of this drink, but you can simply choose based on how much foam you enjoy.
Morgan | Then I would like the latte. Just to be clear, that is a recommendation about less foam, not a claim that one drink is healthier?
Sora | Correct. I am matching your [[preference::Preference is the customer's expressed desire for less foam, not a medical need or universal quality ranking.]] for less foam. I am not making a health recommendation or giving a measured caffeine comparison.
Morgan | Good. I also understand that another cafe might prepare these names a little differently, so I may need to ask there too.
Sora | Yes, [[recipe variation::Recipe variation allows for different formulations across cafes; these examples do not define universal drink proportions.]] is possible. Asking about the actual recipe is more reliable than assuming a name fixes every proportion everywhere.
Morgan | All right, a small latte, please. I am happy with the standard espresso serving and the less-foamy option you have described.
Sora | A small latte, understood, with no [[extra shot::Extra shot names the additional espresso serving Morgan explicitly does not request.]]. I will keep your order to the standard recipe we compared, rather than adding anything you did not ask for.''',
    transfer_title='Match a different texture preference',
    transfer_setup='At another fictional cafe, both small drinks use one espresso serving. The cappuccino has more foam; the latte has less. Customer Rei wants more foam, with no added espresso.',
    transfer='''Barista: "The closer match is the ___." | cappuccino | The cappuccino has more foam, matching Rei's stated preference.
Customer: "I want more ___, not more coffee." | foam | Foam is the feature Rei wants increased in the comparison.
Barista: "Both small recipes use ___ espresso serving." | one | One espresso serving is the shared recipe quantity supplied.
Customer: "Please do not add an ___." | extra shot | Rei explicitly declines an additional espresso serving beyond the recipe.'''
))

BOOK['units'].append(unit(
    title='Clarifying milk, syrup, and allergy questions',
    scene='Oat does not settle the question',
    skill='Acknowledge an allergy, preserve the separate modification, and route the actual product and preparation questions for checking.',
    brief='Customer Priya reports a milk allergy and asks for an oat latte without vanilla syrup. Barista Leo knows oat drink is available but has not checked the current carton ingredients or the shared-equipment arrangements. Shift lead Amina is available to review the request through the cafe allergy procedure. No drink has been prepared or consumed, and no reaction is reported. Leo must communicate what needs checking without claiming that oat, plant-based, or no vanilla automatically establishes suitability.',
    cast='Priya | Customer\nLeo | Barista',
    culture=('A clear limitation is respectful', 'A customer may hear yes, we have oat as yes, this is suitable for you. State availability and suitability separately. Acknowledge the allergy directly and explain who will check the actual ingredients and preparation arrangements, without asking the customer to approve an unknown risk.'),
    a='''Which allergy is reported? | Milk | Oats established as an allergy | Vanilla established as an allergy | No allergy, only preference | Priya explicitly reports a milk allergy, separate from the syrup omission.
What has Leo verified so far? | Oat drink is available | The complete drink is suitable | Shared-equipment controls are checked | The current carton has no relevant allergens | Availability is known, while ingredient and preparation checks remain incomplete.
Who can review the request? | Amina, the shift lead | An unnamed customer in the queue | A completed external laboratory report | Nobody identified in the brief | Amina is the named available lead for the cafe allergy procedure.''',
    vocabulary='''food allergy | Immune-system reaction to a food that can cause serious harm. | report a food allergy
milk allergy | Allergy to milk proteins, not simply a preference against milk. | communicate a milk allergy
allergen | Substance capable of triggering an allergic reaction. | identify the reported allergen
cross-contact | Unintended introduction of an allergen into food or drink. | assess cross-contact
ingredient list | Product information identifying its ingredients. | check the ingredient list
current carton | Actual carton being used now, not an earlier product version. | check the current carton
product formulation | Ingredients and composition of a particular product. | verify the product formulation
supplier change | Change in the source or supplied product. | check after a supplier change
shared equipment | Equipment used for more than one product or ingredient type. | check shared equipment
preparation arrangement | Actual method and controls used to prepare an order. | verify preparation arrangements
allergy procedure | Workplace process for receiving and handling allergy requests. | follow the allergy procedure
shift lead | Person leading the team during the current shift. | consult the shift lead
suitability | Whether a product and its preparation meet the stated need. | avoid assuming suitability
availability | Whether an item can currently be supplied. | confirm availability
oat drink | Beverage made using oats, with other ingredients varying by product. | check the oat drink
vanilla syrup | Vanilla-flavored liquid ingredient whose formulation must be checked. | omit vanilla syrup
omission | Instruction to leave out a specified component. | record the omission
contains statement | Label statement identifying specified allergens in a product. | review the contains statement
advisory statement | Precautionary label information about possible allergen presence. | read the advisory statement
milk protein | Protein from milk that may be relevant to milk allergy. | identify milk proteins
ingredient verification | Checking the relevant information for the actual product. | complete ingredient verification
allergy flag | Record or signal identifying an allergy-related order. | preserve the allergy flag
unverified | Not yet established by the required check. | mark suitability unverified
customer update | Message explaining the current status and next step. | give a customer update''',
    precision='No vanilla is an omission instruction. Milk allergy is a safety-related disclosure. Keep both in the message; neither replaces the need to check the actual oat product and preparation arrangements.',
    precision_extra='Plant-based and oat name a product category, not a completed assessment of the drink. A familiar brand, an old carton, or the absence of a remembered warning cannot substitute for current relevant information and actual controls.',
    phrases='''Acknowledge the allergy | Thank you for telling me about your milk allergy.
Keep the modification | You also want no vanilla syrup.
State availability | We have oat drink available.
Separate suitability | Availability does not confirm suitability for your allergy.
Name the first check | I need to check the current product information.
Name the second check | We also need to check our preparation arrangements.
Identify shared equipment | I have not yet verified the shared-equipment arrangements.
Involve the lead | I will ask Amina to review this through our allergy procedure.
Avoid an assurance | I cannot confirm this drink is suitable yet.
Keep the request together | Oat latte, no vanilla, reported milk allergy.
Explain the pause | We need the relevant checks before making a suitability statement.
Avoid an old label | We need information for the product in use now.
Reject a shortcut | Leaving out syrup does not settle the milk-allergy question.
Give a status update | The request is being checked; there is no confirmed outcome yet.
Promise communication | I will return with the result of the check.
Preserve the boundary | I will not describe an unchecked drink as allergy-safe.''',
    notes='''Available versus suitable | Availability concerns supply; suitability needs the relevant assessment.
Also | Use also to preserve the syrup instruction without replacing the allergy disclosure.
Yet | Not confirmed yet states an unresolved status rather than a final refusal or approval.
Current | This word identifies the actual product information needed now.
Reported allergy | Report the customer's words accurately without diagnosing or minimizing them.
Check with | Name the person and question, rather than offering an unexplained delay.''',
    d='''Which response is best? | We have oat drink, but I need to check the product and preparation for your milk allergy. | Oat always means allergy-safe. | No vanilla removes every milk risk. | A familiar carton is enough without checking. | The answer separates stock availability from ingredient and preparation suitability.
What does no vanilla establish? | A request to omit that syrup | A verified milk-free preparation system | A confirmed reaction | A complete ingredient assessment | The omission concerns one ingredient and does not settle the full allergy question.
Which summary should reach Amina? | Oat latte, no vanilla, reported milk allergy; relevant checks pending | Regular latte, customer dislikes sweet drinks | Oat latte already approved | Customer has consumed the wrong drink | The summary preserves all known details and the unresolved checking status.
Which claim is unsupported? | The complete drink is suitable for Priya's allergy. | Oat drink is available. | Amina can review the request. | No drink has been consumed. | Neither current product information nor preparation arrangements have yet been verified.''',
    dialogue='''Priya | Could I have an oat latte without vanilla syrup? I also need to tell you that I have a milk allergy.
Leo | Thank you for telling me. I will keep the [[milk allergy::Milk allergy is the reported safety-related information, separate from the customer's syrup preference.]] clearly attached to the request, as well as the instruction not to add vanilla.
Priya | Do you have oat drink today? I can see it mentioned on the menu, but I know products sometimes change.
Leo | We do have it. That confirms [[availability::Availability means the product is present; it does not establish suitability for the reported allergy.]], but I have not checked the current carton or our preparation arrangements for your allergy.
Priya | All right. I do not want a quick yes based only on the name. What do you need to check first?
Leo | We need the [[ingredient list::The ingredient list supplies product composition information for the actual carton rather than assumptions from its name.]] and other relevant information for the carton in use now. I will not rely on what an earlier product contained.
Priya | And the equipment matters too, does it not? I am asking because I can see several different milk products being used behind the counter.
Leo | Yes. We need to check the [[shared equipment::Shared equipment is relevant because preparation can introduce allergens even when a product name sounds suitable.]] and the actual arrangements for this order. I have not verified those details yet.
Priya | Thank you for being clear. Please keep the no-vanilla part on the order as well; that is still what I would like.
Leo | Certainly. The [[omission::Omission refers to leaving out vanilla syrup, a separate instruction that does not resolve the milk-allergy question.]] stays on the request. Removing that syrup alone would not answer the milk-allergy question for the rest of the drink.
Priya | Who can help check it? I would rather wait for a clear answer than have different people making different assumptions.
Leo | Amina is our [[shift lead::The shift lead is the named available person who can review the request through the cafe process.]]. I will ask her to review both the product information and preparation arrangements through our allergy procedure.
Priya | Could you tell her exactly what I asked for? I do not want the allergy to become just a note saying I prefer oat.
Leo | I will say: oat latte, no vanilla syrup, reported milk allergy. The [[allergy flag::The allergy flag preserves the disclosure as allergy-related information rather than reducing it to a preference.]] must remain distinct from the choice of oat drink.
Priya | That sounds right. You are not saying it has been approved already, just that you are going to check the actual situation?
Leo | Correct. The drink's [[suitability::Suitability is the unresolved question about the complete product and preparation, not merely whether oat drink is stocked.]] is not confirmed yet. I do not want my explanation of the next step to sound like a guarantee.
Priya | Understood. Nothing has been made for me yet, so please come back with the result before we go any further.
Leo | I will give you a [[customer update::A customer update communicates the review result or continuing uncertainty without implying that a pending check is complete.]] after the review. If something remains unknown, I will say that clearly instead of filling in the gap.
Priya | Thank you. I appreciate knowing what is happening, especially when the menu name by itself does not answer the question.
Leo | You are welcome. I will now take the full request to Amina under our [[allergy procedure::The allergy procedure is the actual workplace route for the request; this conversation does not substitute for its required checks.]], keeping the allergy and the separate no-vanilla instruction together.''',
    transfer_title='Keep a new allergy request intact',
    transfer_setup='Customer Noor requests a soy latte without caramel and reports a sesame allergy. Lead Rosa is available. Product and preparation checks are incomplete.',
    transfer='''Barista: "The reported allergy is ___." | sesame | Sesame is explicitly reported and must not be replaced by soy.
Customer: "Please leave out ___." | caramel | Caramel is the separate omission requested for this drink.
Barista: "The lead available to review this is ___." | Rosa | Rosa is the named available reviewer in the new scenario.
Barista: "Suitability remains ___." | unconfirmed | Both relevant checks are incomplete, so suitability cannot be asserted.'''
))

BOOK['units'].append(unit(
    title='Managing the queue and pickup',
    scene='Two customers named Sam',
    skill='Interrupt a mistaken pickup politely, match the ticket and drink, and explain readiness without inventing a wait.',
    brief='Two customers at the cafe are named Sam. Ticket 64 is a small hot latte and is complete. Ticket 67 is a large iced decaf latte and is still in progress. The Sam holding ticket 67 hears the name called and reaches toward the completed cup. Barista Hana notices before the cup is collected. No one has consumed the drink. Hana needs to clarify the ticket number and drink details, preserve the completed drink for the correct customer, and explain that ticket 67 is not ready. No reliable wait estimate is supplied.',
    cast='Sam | Customer holding ticket 67\nHana | Pickup barista',
    culture=('Correct the match without blaming the person', 'A shared name makes a mix-up understandable. Use a brief interruption, then give the identifying detail that resolves it. Do not call the customer careless. A number plus drink description is clearer than repeating the same name more loudly.'),
    a='''Which ticket belongs to this Sam? | 67 | 64 | Both tickets automatically | No ticket is known | The brief explicitly identifies this customer as holding ticket 67.
Which drink is complete? | Ticket 64, small hot latte | Ticket 67, large iced decaf latte | Both drinks | Neither drink | Ticket 64 is complete while the other drink remains in progress.
What wait can Hana promise? | No precise wait is established | Exactly one minute | Immediate collection of 67 | The time printed on another receipt | The brief provides no reliable estimate for completion of ticket 67.''',
    vocabulary='''pickup counter | Area where prepared orders are collected. | wait at the pickup counter
ticket number | Number used to identify an order. | confirm the ticket number
order name | Customer name attached to an order. | call the order name
duplicate name | Name shared by more than one current customer. | resolve a duplicate name
completed drink | Drink whose preparation is finished. | identify the completed drink
in progress | Started or underway but not yet finished. | mark the order in progress
ready call | Announcement that a specified item can be collected. | make a clear ready call
drink description | Identifying details such as size, temperature, and coffee choice. | repeat the drink description
cup label | Information attached to a cup to identify its order. | read the cup label
collection | Taking possession of the prepared order. | confirm before collection
order match | Agreement between the customer order and prepared item. | verify the order match
queue | Line or sequence of customers or pending orders. | manage the queue
queue position | Place in a waiting or production sequence. | explain queue position
preparation status | Current stage of making an item. | check preparation status
partial order | Order with some but not all items complete. | identify a partial order
estimated wait | Approximate expected remaining delay. | check the estimated wait
time promise | Commitment about when an item will be ready. | avoid an unsupported time promise
pickup mix-up | Confusion about which customer should collect an item. | prevent a pickup mix-up
identifier | Detail used to distinguish one order from another. | use a second identifier
readiness | State of being ready for the relevant next step. | confirm readiness
handover point | Place or stage where an item passes to the customer. | check at the handover point
collection check | Verification that the correct order is being collected. | complete the collection check
pending item | Item that has not yet reached the required finished state. | identify the pending item
polite interruption | Brief respectful intervention to prevent a misunderstanding. | use a polite interruption''',
    precision='A ready call applies to the identified drink, not everyone with the same name. Add the ticket number and key drink details. Keep ready for ticket 64 separate from in progress for ticket 67.',
    precision_extra='Order sequence does not always give a reliable completion time. Different drinks can take different paths through the bar. Explain the verified status and check an estimate instead of converting a queue position into a promise.',
    phrases='''Interrupt briefly | One moment, please; let me check the ticket.
Ask for the identifier | What number is on your receipt?
Identify the completed cup | This is ticket 64, the small hot latte.
Name the shared-name issue | We have two orders under Sam.
Confirm the other order | Yours is ticket 67, the large iced decaf latte.
State the status | That drink is still in progress.
Avoid a false wait | I do not have a checked wait estimate yet.
Use both identifiers | I will call the number and drink as well as the name.
Prevent collection | Please wait while I match this cup to the order.
Acknowledge the confusion | I understand why you thought that call was yours.
Keep the correct cup | This completed drink belongs to the other ticket.
Check before announcing | I will confirm readiness before calling it.
Explain the next update | I can check with the bar for an estimate.
Separate the orders | One is complete; the other is still being made.
Repeat key modifiers | Large, iced, and decaf are all on ticket 67.
Close the correction | Thank you; we have matched the right order now.''',
    notes='''One moment | A concise interruption can prevent a wrong handover without sounding accusatory.
This versus yours | Name the ticket after each pronoun when two orders are close together.
Still | Still in progress preserves the current unfinished state.
Ready for whom | A readiness statement needs the correct order identifier.
Yet | No estimate yet does not mean immediate service or an unlimited delay.
Number clarity | Repeat sixty-seven distinctly from sixty-four rather than saying the last digit alone.''',
    d='''Which call is least ambiguous? | Sam, ticket 64, small hot latte | Sam! | Your regular is here | The first one is ready for everyone | The number and description distinguish two orders with the same customer name.
Which status report is correct? | Ticket 64 is complete; ticket 67 is in progress. | Both are complete because Sam was called. | Ticket 67 is complete because the cup is visible. | Neither ticket exists until collection. | The report preserves the separately established preparation states.
Which response invents a fact? | Yours will definitely be ready in thirty seconds. | Your number is 67. | This cup is ticket 64. | We have two customers named Sam. | No reliable completion estimate is supplied, so thirty seconds is unsupported.
Why check before collection? | The name alone does not distinguish the orders. | Large and small mean the same thing. | Decaf means every drink is interchangeable. | A receipt number changes the recipe automatically. | Both customers share a name, requiring additional order details to match correctly.''',
    dialogue='''Sam | I heard Sam called. Is this my latte? I have been waiting near the counter, and I thought that must be mine.
Hana | One moment, please. Could I check your [[ticket number::The ticket number distinguishes the two customers sharing the name Sam before the drink is collected.]] before you take it? We have two customers named Sam waiting for different drinks.
Sam | Of course. My receipt says sixty-seven. I ordered the large iced decaf latte, so perhaps this is the other person's cup.
Hana | Thank you. This completed cup is [[sixty-four::Sixty-four identifies the finished small hot latte, not Sam's large iced decaf order.]], a small hot latte. Yours is sixty-seven, so I want to keep the two orders separate.
Sam | I can see the cup is smaller now. I just reacted to the name without looking closely at the label.
Hana | That is understandable. Your [[drink description::The drink description adds size, temperature, and coffee choice to the ticket identifier, making the match clearer.]] is large iced decaf latte. Those details do not match the small hot drink that was called.
Sam | Is mine finished somewhere else on the counter, then? I do not want to stand in the wrong place or miss another call.
Hana | Your drink is still [[in progress::In progress is the verified unfinished preparation state of ticket 67; it is not a ready-for-collection announcement.]]. I have checked the current status, and it has not reached the pickup stage yet.
Sam | All right. Do you know how long it will be? I am not asking you to rush it, just checking before I step aside.
Hana | I do not have an [[estimated wait::An estimated wait requires a current check; Hana has no reliable time to give at this point.]] to give you yet. I can check with the bar, but I do not want to invent a time.
Sam | That is fair. When you call it, could you say the number too? Otherwise we might both come forward again.
Hana | Certainly. I will include the number and drink in the [[ready call::The ready call will identify the specific completed order, reducing the ambiguity caused by a shared name.]], not just Sam. That will make the collection clearer for both of you.
Sam | Thanks. I have not picked this one up, so I will leave it here for the person with sixty-four.
Hana | Thank you. The [[completed drink::The completed drink is ticket 64's small hot latte; it remains separate from the pending ticket 67.]] belongs to that ticket. I will keep it matched to its order rather than treating the shared name as enough.
Sam | And mine is definitely still marked decaf? That is one of the details I particularly wanted to make sure had not been lost.
Hana | Yes. The [[cup label::The cup label carries the order details; the check confirms the requested decaf modifier remains attached to ticket 67.]] for your order retains large, iced, and decaf. We are clarifying collection, not changing those choices.
Sam | Good. I will stay nearby and listen for sixty-seven with the full drink description. That should be much easier to recognize.
Hana | Exactly. At the [[handover point::The handover point is where the final match matters before the prepared drink passes to the customer.]], we can match the number and drink before collection. That avoids relying on a name that two people share.
Sam | Thank you for catching it. I would have been surprised to walk away with a small hot drink after ordering something quite different.
Hana | You are welcome. We have resolved the [[pickup mix-up::The pickup mix-up concerns identity at collection; resolving it does not mean the pending drink has become ready.]], and yours remains in progress. I will make the next call clear once that drink is actually ready.''',
    transfer_title='Separate two orders under Lee',
    transfer_setup='Ticket 81 is a completed small tea. Ticket 84 is a large iced coffee still in progress. Both orders use Lee. The customer in front of you holds ticket 84.',
    transfer='''Barista: "Your ticket number is ___." | 84 | The customer in this exchange holds ticket 84, not 81.
Customer: "I ordered the large iced ___." | coffee | Coffee is the drink attached to ticket 84 in the brief.
Barista: "The completed small tea belongs to ticket ___." | 81 | Ticket 81 identifies the completed tea, a separate order.
Barista: "Your order remains ___." | in progress | Ticket 84 has not reached completion in the supplied facts.'''
))

BOOK['units'].append(unit(
    title='Handling remakes and mistaken labels',
    scene='The label is not the ticket',
    skill='Identify an order-label mismatch, request a checked remake, and keep timing and payment decisions separate.',
    brief='Ticket 22 requests a small iced latte with no syrup. Its cup label says hot vanilla latte. The customer has not collected the drink. Counter worker Ben catches the mismatch and asks barista Imani to arrange a replacement matching the ticket. A remake is available, but the current wait has not been checked. No refund, complimentary extra, or queue priority has been authorized. The conversation concerns correcting and verifying the order, not guessing how the mismatch happened or merely relabeling an unchecked drink.',
    cast='Ben | Counter worker\nImani | Barista',
    culture=('Own the correction without assigning a culprit', 'Point to the two records and name their difference. A neutral description makes it easier to correct the order quickly. Keep an apology or acknowledgement separate from an unsupported accusation, a promised refund, or a made-up completion time.'),
    a='''What does ticket 22 request? | Small iced latte with no syrup | Hot vanilla latte | Large cappuccino with syrup | A refund already approved | The ticket gives the intended size, temperature, and syrup omission.
What is wrong with the cup label? | It says hot vanilla latte | It confirms the ticket exactly | It says the customer has collected it | It authorizes a free extra | Hot and vanilla conflict with iced and no syrup on the ticket.
Which outcome is not established? | A checked remake wait | The customer's order details | The existence of a mismatch | That collection has not occurred | A remake is available, but nobody has checked its current wait.''',
    vocabulary='''remake | New preparation intended to replace an incorrect or unsatisfactory item. | request a remake
replacement | Item supplied instead of another item. | arrange a replacement
mismatch | Difference between records or items that should agree. | identify a mismatch
source ticket | Original order record used to verify the intended drink. | check the source ticket
incorrect label | Cup information that does not match the intended order. | correct an incorrect label
order specification | Complete stated details of the requested item. | preserve the order specification
temperature modifier | Order detail identifying hot or iced preparation. | check the temperature modifier
syrup omission | Instruction not to include a named or any syrup. | preserve the syrup omission
verification | Check that an item or record meets the relevant requirement. | complete verification
relabeling | Changing the information attached to an item. | distinguish relabeling from remaking
production error | Mistake during preparation or production. | investigate a production error
entry error | Mistake when recording information. | investigate an entry error
cause | Reason an event occurred, requiring evidence. | avoid guessing the cause
correction request | Message identifying what must be changed. | send a correction request
service recovery | Response intended to address a service failure. | coordinate service recovery
acknowledgement | Clear recognition of a reported issue. | give an acknowledgement
apology | Expression of regret for an error or inconvenience. | offer an apology
refund | Return of money under an applicable decision or policy. | request a refund review
complimentary item | Item supplied without charge under an authorized arrangement. | authorize a complimentary item
queue priority | Order's position or precedence in preparation. | confirm queue priority
remake status | Current stage of preparing the replacement. | update remake status
checked estimate | Time estimate obtained from the relevant current source. | give a checked estimate
customer-facing message | Explanation intended for the customer rather than internal shorthand. | prepare a customer-facing message
final match | Verification that the finished replacement agrees with the intended order. | confirm the final match''',
    precision='A label can be wrong even when the intended order is clear. Compare it with the source ticket. Changing the label alone does not verify what is in the cup or complete the requested remake.',
    precision_extra='A remake, a refund, and a complimentary item are different actions. Confirm only the action actually available or authorized. Keep an unchecked wait distinct from a checked estimate and from a guaranteed completion time.',
    phrases='''Identify the order | I need a correction for ticket 22.
State the ticket | The ticket says small iced latte, no syrup.
State the mismatch | The cup label says hot vanilla latte.
Protect the modifiers | Iced and no syrup both need to stay on the replacement.
Confirm collection status | The customer has not collected it.
Request the remake | Can you arrange a remake matching the ticket?
Avoid a label-only fix | Please verify the drink, not just the printed wording.
Acknowledge the issue | I see the mismatch.
Keep the cause open | We have not established how it happened.
Check timing | What is the current remake estimate?
Avoid a false promise | I have not checked the wait yet.
Separate payment | No refund decision has been made.
Avoid an extra offer | I have not been authorized to add a complimentary item.
Update the customer | We are correcting the order and checking the wait.
Verify before pickup | Match the replacement to the ticket before collection.
Close the loop | Please tell me when the checked replacement is ready.''',
    notes='''Says versus contains | A label says something; it does not by itself prove the drink contents.
Matching | A replacement must match all specified modifiers, not only the drink name.
Has not collected | This describes the actual stage without inventing consumption or harm.
Available versus complete | An available remake is not an already prepared replacement.
Yet | The wait is unchecked yet; that is not a promise of immediate service.
Separate decisions | Correction, compensation, and timing need their own factual basis.''',
    d='''Which request preserves the order? | Remake ticket 22 as a small iced latte with no syrup. | Change only the label to iced. | Keep vanilla because the cup says so. | Upgrade it without asking. | The request preserves every supplied order detail and asks for a real remake.
Which statement should Ben avoid? | Your replacement will definitely be ready in one minute. | We are correcting the mismatch. | The wait has not been checked yet. | The ticket requests no syrup. | No checked wait or guaranteed completion time has been supplied.
What does a corrected label alone establish? | Corrected wording, not verified drink contents | A completed remake automatically | A refund approval | That no production error is possible | Relabeling changes information and does not verify preparation or contents.
Which report avoids blame? | The ticket and cup label do not match. | Imani deliberately ignored the customer. | The customer must have ordered wrongly. | The machine is definitely defective. | The evidence establishes a mismatch but does not identify intent or cause.''',
    dialogue='''Ben | I need a correction for ticket twenty-two before it reaches the customer. The cup label does not match the order on the ticket.
Imani | Let us compare the [[source ticket::The source ticket is the order record used to establish the intended drink rather than trusting the conflicting label.]] with the label. Please give me the full drink details, including the size and any modifications.
Ben | The ticket says small iced latte with no syrup. The cup is labeled hot vanilla latte, so there are two clear differences.
Imani | I see the [[mismatch::Mismatch describes the disagreement between iced and no syrup on the ticket and hot vanilla on the label.]]. Both the temperature description and the syrup instruction conflict with the order we need to fulfill.
Ben | The customer has not collected it. I caught it while checking the cup against the ticket, before calling the order at pickup.
Imani | Thank you. We can arrange a [[remake::A remake means preparing a replacement to match the order, not merely changing the label on an unchecked drink.]] matching the ticket. I will not treat changing the words on the label as proof the drink is correct.
Ben | Good. Please keep it small and iced, with no syrup. I do not want one detail corrected while the other gets lost.
Imani | I will preserve the complete [[order specification::The order specification includes all confirmed details: small, iced, latte, and no syrup.]]. Small iced latte, no syrup, ticket twenty-two. That is the instruction for the replacement.
Ben | Do you know the current wait? I need to tell the customer what is happening, but I have not given them a time.
Imani | I have not obtained a [[checked estimate::A checked estimate comes from current production information; no reliable remake wait has yet been obtained.]] yet. A replacement is available, but I cannot turn that into an immediate completion promise.
Ben | Then I will explain that we caught a label mismatch and are correcting the order. I can say the wait is being checked.
Imani | That is an accurate [[customer-facing message::The customer-facing message explains the correction and unresolved timing in ordinary language without inventing a promise.]]. It tells them the next step without claiming the drink is ready or the delay will be a particular length.
Ben | Should I offer a refund or an extra drink? I would rather check before making an offer that someone else has to reverse.
Imani | No [[refund::Refund is a separate payment decision; the availability of a remake does not establish authorization to return money.]] has been authorized in this exchange. Keep any payment or complimentary-item request within the actual service-recovery process.
Ben | Understood. I will not turn a correction into a compensation promise. I will also avoid saying who caused it, since we do not know.
Imani | Exactly. We have identified the difference, not the [[cause::Cause requires evidence beyond the observed disagreement; the exchange does not establish who or what produced the error.]]. We can investigate separately without making the customer wait through an argument about blame.
Ben | When the replacement is prepared, please check it against the ticket and let me know. I will use the ticket number at pickup.
Imani | Yes, the [[final match::The final match verifies the replacement against the intended order before handover, rather than assuming a new cup is automatically correct.]] matters before collection. We need the right drink and the right identifying information, not simply a newly printed label.
Ben | Thank you. For now I will say the correction is underway and the wait is still being checked, without claiming more than that.
Imani | I will update you on [[remake status::Remake status reports the actual stage of the replacement; it must not convert an intended correction into completed work.]] as it changes. Until the replacement is prepared and checked, we should not describe ticket twenty-two as ready.''',
    transfer_title='Correct another label mismatch',
    transfer_setup='Ticket 35 requests a large hot latte with oat drink and no syrup. The label says iced with dairy milk. A remake is available; the wait remains unchecked.',
    transfer='''Counter: "The intended temperature is ___." | hot | Hot is the ticket instruction, while iced is the conflicting label.
Barista: "The specified milk alternative is ___." | oat drink | Oat drink is the confirmed product choice on ticket 35.
Counter: "The ticket also requests ___." | no syrup | The syrup omission must remain intact while correcting the other details.
Barista: "The current wait is still ___." | unchecked | No verified remake estimate is supplied in the new scenario.'''
))

BOOK['units'].append(unit(
    title='Discussing coffee beans for home',
    scene='Before the beans are ground',
    skill='Clarify the intended brewer, explain sensory wording, and avoid an irreversible choice based on an ambiguous request.',
    brief='Customer Jamie is buying a gift bag and asks for normal ground coffee. Jamie does not know the recipient brewer or whether the recipient owns a grinder. This cafe sells the same coffee whole or ground, but grinding cannot be undone. The bag describes a hazelnut flavor note; that wording describes a sensory impression, not an ingredient declaration. Barista Rafael needs to explain the distinction, ask for useful brewing information, and avoid guessing a grind setting or declaring allergen suitability from the tasting note. No purchase choice has yet been finalized.',
    cast='Jamie | Gift customer\nRafael | Barista',
    culture=('Make expertise usable', 'Customers buying gifts may not know equipment names. Explain why the brewer matters before listing specialist terms. Offer a clear next step, such as obtaining the brewer name, while leaving the purchase choice with the customer rather than pretending one grind fits every method.'),
    a='''What information is missing? | The recipient's brewer and grinder availability | Whether coffee is sold at all | Whether grinding can be undone | The existence of a flavor note | The customer does not know the brewing equipment or whether a grinder is available.
What does hazelnut mean on this bag? | A flavor note, not an ingredient declaration | Proof of added hazelnuts | Proof the coffee is suitable for every nut allergy | A specified grind setting | The brief explicitly defines the wording as a sensory description.
What should happen before choosing a grind? | Clarify the intended brewing method | Select normal as a universal setting | Grind first and restore whole beans later | Infer the brewer from the gift recipient's name | The brewing method is needed to choose a relevant grind rather than guessing.''',
    vocabulary='''whole bean | Coffee sold as intact roasted beans rather than ground particles. | choose whole bean
ground coffee | Roasted coffee reduced to particles for brewing. | buy ground coffee
grind size | Size of the coffee particles after grinding. | match the grind size
grind setting | Grinder adjustment used to produce a target particle size. | confirm the grind setting
brewer | Device or equipment used to make coffee. | identify the brewer
brewing method | Process used to extract coffee into water. | clarify the brewing method
drip brewer | Device that passes water through coffee held in a filter. | use a drip brewer
pour-over | Brewing method in which water is poured over coffee in a filter. | prepare a pour-over
French press | Immersion brewer with a plunger and filter. | identify a French press
espresso machine | Device that brews espresso using pressurized water. | identify an espresso machine
cold brew | Coffee extracted using cool or cold water over an extended period. | distinguish cold brew
burr grinder | Grinder that reduces beans between two abrasive grinding surfaces. | use a burr grinder
blade grinder | Grinder that chops beans using rotating blades. | identify a blade grinder
coarse grind | Relatively large coffee particles. | request a coarse grind
fine grind | Relatively small coffee particles. | request a fine grind
particle size | Dimension of individual ground-coffee pieces. | compare particle size
roast level | Degree to which coffee has been roasted. | describe the roast level
origin | Geographic source identified for a coffee. | check the coffee origin
blend | Coffee combining more than one component lot or source. | describe a blend
single origin | Coffee presented as from one defined source, whose scope should be checked. | clarify single origin
tasting note | Word describing a sensory impression of flavor or aroma. | explain a tasting note
aroma | Smell perceived from coffee. | describe the aroma
ingredient declaration | Information stating what ingredients a product contains. | check the ingredient declaration
gift recipient | Person who will receive the purchased gift. | ask about the gift recipient''',
    precision='A hazelnut tasting note does not establish added hazelnut, and it does not certify absence of allergens. Ingredient and handling questions require relevant product information, not an interpretation of flavor language.',
    precision_extra='Normal ground is not a universal technical setting. Ask about the brewer before grinding. Whole beans avoid an immediate grind choice, but they are not automatically convenient if the recipient has no suitable grinder.',
    phrases='''Ask about use | How will the recipient brew the coffee?
Clarify normal | Which brewing method do you mean by normal ground?
Explain the reason | The useful grind depends on the brewer.
Ask for equipment | Do you know the brewer name or type?
Offer recognizable examples | Is it a drip brewer, French press, or espresso machine?
Avoid guessing | I do not want to choose a grind from that word alone.
Explain the irreversible step | Once we grind these beans, we cannot turn them back into whole beans.
Keep the options clear | We sell this coffee whole or ground.
Ask about a grinder | Does the recipient have a grinder?
Clarify the label | Hazelnut here is a tasting note.
Separate ingredients | That is not an ingredient declaration.
Avoid an allergy claim | The flavor note does not establish allergen suitability.
Describe sensory language | It names a flavor impression someone may perceive.
Leave the choice open | We have not finalized the grind choice yet.
Offer a next step | You could check the brewer details before we grind the bag.
Confirm before action | I will wait for a clear choice before grinding.''',
    notes='''Ground versus grind | Ground is the product form; grind can name the particle size or the action.
For | Ground for a French press identifies intended use, not coffee origin.
Note | A tasting note describes perception rather than a list of added ingredients.
Could | A suggested next step leaves the decision with the customer.
Cannot undo | State the practical consequence before the irreversible preparation step.
Not established | Unknown equipment should remain unknown rather than becoming an assumed default.''',
    d='''Which response to normal ground is strongest? | What brewer will the recipient use? | Every brewer takes exactly the same grind. | Normal must mean espresso. | I will grind it before we ask. | The brewer supplies the missing context needed for a useful grind choice.
What can Rafael infer from hazelnut alone? | A stated sensory description, not ingredient or allergy status | Guaranteed added hazelnuts | Guaranteed absence of all allergens | The recipient owns a grinder | Tasting language does not establish product composition, handling, or recipient equipment.
Why not automatically recommend whole beans? | The recipient may not have a suitable grinder. | Whole beans cannot be sold. | Whole beans always contain syrup. | Grinding is fully reversible. | Grinder availability is unknown, so convenience cannot be assumed.
Which statement preserves the decision stage? | The grind choice has not been finalized. | A French-press grind has been approved. | The customer selected fine grind. | The bag is already ground correctly. | Neither the intended brewer nor a final grind choice is established.''',
    dialogue='''Jamie | I am buying a bag for a friend. Could you make it normal ground, please? I do not usually buy coffee for someone else.
Rafael | Certainly, but first, do you know their [[brewing method::Brewing method supplies the intended use needed to clarify the ambiguous request for normal ground coffee.]]? The useful grind depends on how they make coffee, rather than one setting that works for every brewer.
Jamie | I am not sure. I have seen a coffee machine in their kitchen, but I could not tell you what type it is.
Rafael | That is fine. The [[brewer::Brewer is the equipment Rafael needs identified; simply knowing a machine exists does not establish its type.]] might be a drip machine or an espresso machine, for example, and those are not the same grinding request.
Jamie | I had not realized that. Can you just grind it now and make it coarser later if my friend tells me it is wrong?
Rafael | We cannot restore larger particles once they have been reduced. I would confirm the [[grind size::Grind size is the particle-size choice that should be established before the irreversible grinding step.]] before doing that, rather than promise that a wrong setting can be undone.
Jamie | All right. You sell the same coffee as whole beans too, do you not? Maybe that would avoid deciding immediately.
Rafael | We do offer [[whole bean::Whole bean describes the unground product option, which preserves a later grinding choice but requires suitable equipment to use.]]. That leaves grinding until later, but it helps to know whether your friend has a suitable grinder.
Jamie | I do not know that either. I can ask someone who lives with them without spoiling the gift, so perhaps I should check.
Rafael | That sounds useful. We have not finalized the [[grind setting::Grind setting remains undecided because the recipient's equipment is unknown; Rafael must not invent a default.]], and I have not ground the bag. There is time to get the relevant information first.
Jamie | One other question: the bag says hazelnut. Does that mean someone added hazelnuts to the coffee, like a flavored syrup?
Rafael | On this bag, hazelnut is a [[tasting note::Tasting note names the sensory wording on this bag; it is not presented as an added ingredient.]]. It describes a flavor impression associated with the coffee, not a statement that hazelnuts were added.
Jamie | So it is describing how the coffee may taste. It is not the same kind of information as the ingredients on food packaging?
Rafael | Correct. A tasting note is not an [[ingredient declaration::An ingredient declaration concerns product contents, while a tasting note concerns sensory perception.]]. If someone has an ingredient or allergy question, we need the relevant product information instead.
Jamie | Could somebody read that note as proof that there are no nut ingredients, since it is only describing flavor? I would not want to misunderstand.
Rafael | No. It does not establish [[allergen suitability::Allergen suitability cannot be inferred either positively or negatively from the sensory word hazelnut alone.]] either way. We should not turn the distinction into an assurance about an ingredient or preparation question we have not checked.
Jamie | That makes sense. For this gift, I will first find out the brewing equipment and whether my friend already owns a grinder.
Rafael | Once you know the [[brewer type::Brewer type gives concrete equipment context for discussing a suitable grind rather than treating normal as a universal setting.]], we can discuss the grind request much more clearly. You can bring the name or a clear description of the equipment.
Jamie | Thank you. Please leave the bag unground while I check. I have not decided to buy it as whole beans permanently; I am just pausing.
Rafael | Understood. The [[purchase choice::Purchase choice remains open; pausing grinding is not the same as completing a whole-bean sale.]] is still open, and no grinding will happen from this conversation alone. We will confirm your actual choice before proceeding.''',
    transfer_title='Clarify a different gift-coffee request',
    transfer_setup='Customer Mina confirms the recipient uses a French press and wants the bag ground for it. The bag lists cocoa as a flavor note. No allergy assessment has been made.',
    transfer='''Customer: "The recipient uses a ___." | French press | French press is the confirmed brewer in this new scenario.
Barista: "We should match the grind to that ___." | brewer | The equipment provides the relevant basis for the grind discussion.
Customer: "Cocoa here is a ___." | flavor note | The brief identifies cocoa as sensory wording on the bag.
Barista: "That wording is not an allergy ___." | assessment | A flavor description does not supply a completed allergy assessment.'''
))

BOOK['units'].append(unit(
    title='Explaining counter prices and sold-out items',
    scene='The combo and the upcharge',
    skill='Explain the complete comparison, retain an applicable upcharge, and offer a confirmed available item without pressure.',
    brief='This fictional cafe lists a latte at $4, an oat-drink upcharge at $0.50, and a pastry at $3. Its $6 combo includes a standard latte and one eligible pastry; the oat upcharge still applies. For this transaction these figures include all compulsory charges. Customer Casey wants an oat latte and pastry. The requested almond pastry is sold out, but an eligible plain pastry is available at the same listed pastry price. Casey has not accepted that substitution or paid. Barista Dana must explain $6.50 as the oat combo, compared with $7.50 separately, without charging before the choice is confirmed.',
    cast='Casey | Customer\nDana | Counter barista',
    culture=('An offer needs a genuine choice', 'A confident price explanation names what is included and what costs extra. When an item is sold out, state that directly and offer a real available alternative. Avoid making a substitution sound compulsory just because it fits a promotion.'),
    a='''What is the oat combo price? | $6.50 | $6.00 | $7.50 | $4.50 | The $6 combo still carries the specified $0.50 oat upcharge.
What would the same selected items cost separately? | $7.50 | $6.50 | $7.00 with no upcharge | $3.50 | Four dollars plus fifty cents plus three dollars equals seven dollars fifty.
Which pastry is available? | The eligible plain pastry | The requested almond pastry | Every pastry on the menu | No pastry at all | The brief distinguishes the sold-out almond pastry from the available plain option.''',
    vocabulary='''combo | Group of items sold together under a specified offer. | explain the combo
upcharge | Extra amount added for a selected variation. | apply the oat upcharge
base price | Price before specified optional additions. | state the base price
standalone price | Price for an item purchased separately. | compare the standalone price
eligible item | Item that qualifies for a particular offer. | confirm an eligible item
included item | Item covered by the stated offer price. | name the included items
optional addition | Extra item or variation selected by the customer. | confirm an optional addition
price breakdown | Explanation of the components making up a price. | give a price breakdown
combined price | Price for the selected items together. | state the combined price
separate purchase | Purchase of items at their individual prices. | compare a separate purchase
price difference | Amount by which two prices differ. | calculate the price difference
saving | Reduction compared with a stated comparison price. | explain the saving
sold out | No stock currently available for sale. | mark the pastry sold out
available alternative | Different item that can currently be supplied. | offer an available alternative
substitution | Replacement of a requested item with another. | confirm a substitution
customer acceptance | Customer's explicit agreement to an offered choice. | obtain customer acceptance
promotion terms | Conditions governing a special offer. | check the promotion terms
compulsory charge | Amount required rather than optionally selected. | include compulsory charges
displayed price | Price shown to customers. | verify the displayed price
checkout total | Amount due for the confirmed transaction. | confirm the checkout total
point of sale | System or place where the sale is recorded and paid. | check the point of sale
payment authorization | Approval for a payment transaction. | obtain payment authorization
itemized receipt | Receipt showing individual items or charges. | provide an itemized receipt
stock status | Whether and how an item is available. | update the stock status''',
    precision='The oat upcharge applies in both comparisons. Combo: $6 + $0.50 = $6.50. Separate: $4 + $0.50 + $3 = $7.50. The saving is $1 for the same selected items.',
    precision_extra='An available pastry is not an accepted substitution. Confirm the actual item and price before payment. These figures include compulsory charges only because this fictional transaction explicitly says so; real menus and tax arrangements vary.',
    phrases='''Explain the shortage | The almond pastry is sold out.
Offer the available item | We have the plain pastry available.
Keep acceptance open | Would you like that instead?
State the base offer | The standard latte-and-pastry combo is six dollars.
Retain the upcharge | Oat drink adds fifty cents, including with the combo.
Give the combined price | That makes the oat combo six dollars fifty.
Give the separate price | Bought separately, those items are seven dollars fifty.
Explain the saving | The combo is one dollar less for those same items.
Name the eligible pastry | The plain pastry qualifies for this offer.
Avoid a forced substitute | You do not have to choose the alternative.
Clarify included charges | These stated prices include the compulsory charges here.
Check the choice | Shall I enter the oat combo with the plain pastry?
Pause payment | I will confirm the choice before taking payment.
Read the breakdown | Six dollars for the combo, plus fifty cents for oat.
Correct a misunderstanding | The combo does not remove the oat upcharge.
Keep the record clear | The receipt should match the items you actually select.''',
    notes='''Including with | This phrase makes clear that the surcharge survives the promotion.
Instead | Use instead only for an offered or accepted replacement, not a silent change.
Same items | A fair saving comparison keeps the selected items unchanged.
Six fifty | Common spoken form for $6.50; repeat dollars and cents if unclear.
Sold out | This describes current stock, not permanent removal from the menu.
Before payment | Confirm item choice and applicable charges before processing the transaction.''',
    d='''Which calculation is correct? | $6 + $0.50 = $6.50 | $6 - $0.50 = $5.50 | $4 + $3 = $6.50 | $6 + $3 = $9.00 for the combo | The oat charge is added to the combo's six-dollar base.
How much less is the combo than separate purchase? | $1.00 | $0.50 | $1.50 | $3.00 | Seven dollars fifty minus six dollars fifty equals one dollar.
Which statement wrongly treats an offer as acceptance? | I have charged you for the plain pastry because almond is sold out. | The plain pastry is available. | Would you like the plain pastry instead? | The plain pastry qualifies for the combo. | Availability does not establish the customer's agreement to the alternative.
Why mention charge inclusion? | To keep this transaction's stated comparison complete | To claim every jurisdiction uses identical taxes | To guarantee all future prices | To make an unselected extra compulsory | The brief explicitly includes compulsory charges, so the comparison can use the supplied totals.''',
    dialogue='''Casey | Could I have an oat latte and an almond pastry? I saw a combo on the board, but I am not sure how the oat charge works.
Dana | I can explain it. First, the almond pastry is [[sold out::Sold out describes the requested pastry's current unavailability, which must be disclosed before offering another item.]]. We have a plain pastry available that qualifies for the combo, if you would like that instead.
Casey | Possibly. Please tell me the price before I decide, because I would like to compare the offer with buying the items separately.
Dana | The standard latte-and-pastry [[combo::Combo names the six-dollar package containing the standard latte and one eligible pastry.]] is six dollars. Oat drink adds fifty cents, and that addition still applies when you choose the combo.
Casey | So the offer does not mean the oat drink is automatically included at no extra charge? I want to make sure I heard that correctly.
Dana | Correct. The oat [[upcharge::Upcharge is the additional fifty cents that applies both to the combo and to the separately purchased latte.]] is fifty cents in either comparison. With it, the combo price is six dollars fifty.
Casey | And if I bought the latte with oat and the plain pastry as separate items, what would those same choices come to?
Dana | The [[separate price::The separate price adds the four-dollar latte, fifty-cent oat variation, and three-dollar pastry, totaling seven dollars fifty.]] is seven dollars fifty: four dollars for the latte, fifty cents for oat drink, and three dollars for the pastry.
Casey | That makes the combo a dollar less, then. I was getting confused because I kept comparing a standard latte with the oat version.
Dana | Yes, the [[saving::Saving is the one-dollar difference between the same selected items bought as a combo or separately.]] is one dollar for those same choices. Comparing the same milk option in both totals keeps the difference clear.
Casey | Does the plain pastry definitely qualify, or does the offer only apply to the almond one that is no longer available?
Dana | The plain pastry is an [[eligible item::Eligible item means the available plain pastry qualifies for the stated combo rather than being excluded from the promotion.]]. It has the same three-dollar separate price and can be the pastry in this combo.
Casey | Thank you. Are those the complete prices for this transaction, or will another required charge appear when you ring it up?
Dana | These figures include the [[compulsory charges::Compulsory charges are explicitly included in this fictional transaction, making the stated comparison complete for these choices.]] here. The oat combo is six dollars fifty; the same items separately are seven dollars fifty.
Casey | All right. I am still deciding whether I want the plain pastry. Please do not replace the almond one automatically just because it is available.
Dana | Of course. An available [[alternative::Alternative names a possible replacement; it is not an accepted selection until the customer chooses it.]] is your choice, not an instruction for me to charge you. I will wait for you to confirm the actual items.
Casey | I appreciate that. Could you repeat the combo breakdown once more, without the separate prices, so I can hear the two parts clearly?
Dana | The [[price breakdown::Price breakdown separates the six-dollar combo base from the fifty-cent oat addition, producing the stated six-fifty total.]] is six dollars for the combo plus fifty cents for oat drink. That is six dollars fifty with the plain pastry.
Casey | I understand now. Please give me a moment to decide about the pastry. I have not chosen a different item yet.
Dana | Certainly. We will confirm your [[selection::Selection is the customer's actual choice, still needed before treating the proposed plain-pastry combo as the agreed transaction.]] before payment. I have explained the options, but I will not enter a substitution as though you had already agreed.''',
    transfer_title='Calculate another cafe offer',
    transfer_setup='A different cafe lists a $7 standard combo and a $0.75 oat upcharge that still applies. The same items separately total $9.25. All compulsory charges are included. The muffin is available but not yet accepted.',
    transfer='''Counter: "The oat combo total is ___ dollars." | 7.75 | Seven dollars plus seventy-five cents gives seven dollars seventy-five.
Customer: "The separate total is ___ dollars." | 9.25 | Nine dollars twenty-five is the separate total supplied in the brief.
Counter: "The combo saves ___ dollars." | 1.50 | Nine dollars twenty-five minus seven dollars seventy-five equals one dollar fifty.
Counter: "The muffin substitution is not yet ___." | accepted | Availability does not show agreement, and acceptance remains pending here.'''
))

BOOK['units'].append(unit(
    title='Handing over the bar and till',
    scene='One order, three unfinished items',
    skill='Transfer drink, stock, and cash-check responsibilities while preserving the difference between counted, pending, and signed off.',
    brief='At 2:00, outgoing barista Ellis briefs incoming worker Noor. Ticket 108 contains coffee and tea: the coffee is complete, but the tea is pending. Large takeaway lids are unavailable; small lids remain. Ellis has counted the till, but lead Mara has not completed reconciliation. Noor accepts the tea follow-up and will check replenishment of the correct large lids. Mara retains the till review. No tea completion, large-lid delivery, approved substitute lid, or cash sign-off is established. The handover must keep these separate tasks and stages visible.',
    cast='Ellis | Outgoing barista\nNoor | Incoming cafe worker',
    culture=('Receiving a task is not completing it', 'A handover benefits from a short read-back with the order number, outstanding item, and next owner. A colleague can confidently accept responsibility while saying a check remains pending. Do not make the end of a shift sound like every task has ended.'),
    a='''What remains on ticket 108? | The tea | The already completed coffee only | A new pastry order | No item; the whole order is complete | The coffee is complete but the tea is explicitly still pending.
Which lids are unavailable? | Large takeaway lids | Small lids | All lids of every kind | No lids; stock is full | The shortage is specific to large takeaway lids, while small lids remain.
What is the till status? | Counted, with Mara's reconciliation pending | Fully signed off | Confirmed short by a stated amount | Already reconciled by Noor | A count is complete, but the separate reconciliation has not been completed.''',
    vocabulary='''shift handover | Transfer of current work information between outgoing and incoming staff. | conduct a shift handover
outgoing worker | Person transferring work at the end of a shift or assignment. | brief the outgoing worker
incoming worker | Person receiving responsibility for continuing work. | brief the incoming worker
open ticket | Order record with unfinished items or unresolved work. | identify an open ticket
item-level status | State of each individual item within an order. | report item-level status
remaining item | Item still needing completion within a known order. | name the remaining item
tea follow-up | Responsibility for checking and completing the pending tea through the actual process. | accept the tea follow-up
takeaway lid | Cover designed for the specified takeaway cup. | check the takeaway lid
lid size | Size specification relevant to the matching cup. | confirm the lid size
stockout | Situation in which a required stock item is unavailable. | report a stockout
replenishment | Restoration of stock through the relevant supply process. | check replenishment
compatible item | Item verified to fit and function for the intended use. | verify a compatible item
stock follow-up | Task of checking availability or replenishment. | assign stock follow-up
delivery estimate | Approximate expected arrival time for a supply item. | verify a delivery estimate
till | Cash drawer or register arrangement used for transactions. | count the till
cash count | Physical tally of cash held at a stated point. | record the cash count
reconciliation | Comparison of records and amounts to identify and resolve differences. | complete reconciliation
expected balance | Amount records indicate should be present. | compare the expected balance
actual balance | Amount found by the relevant count or measurement. | record the actual balance
variance | Difference between compared figures. | investigate a variance
review owner | Person responsible for the pending review. | name the review owner
sign-off | Required confirmation that a review or process is complete. | obtain sign-off
pending review | Review not yet completed. | retain pending-review status
handover read-back | Repetition of transferred tasks and states for confirmation. | give a handover read-back''',
    precision='Coffee complete does not mean ticket complete. Till counted does not mean till reconciled. A handover should preserve each item and stage so the incoming worker does not inherit a misleading all-done summary.',
    precision_extra='Small lids remaining do not prove they fit large cups. Report the exact shortage and request the correct replenishment or an approved compatible option through the actual process. Do not promise an arrival time without a checked estimate.',
    phrases='''Open the handover | I have three items to hand over at two o'clock.
Identify the open order | Ticket 108 still needs its tea.
Separate completion | The coffee is complete; the tea is pending.
Assign the follow-up | Can you take responsibility for the tea follow-up?
Accept responsibility | Yes, I will take that follow-up.
Name the shortage | Large takeaway lids are unavailable.
Keep remaining stock distinct | Small lids remain, but that does not establish compatibility.
Request replenishment | Please check the correct large-lid stock.
Avoid an arrival promise | There is no checked delivery estimate.
State the cash stage | The till has been counted.
Preserve the pending stage | Mara's reconciliation is still pending.
Name the owner | Mara retains the till review.
Avoid false sign-off | I am not reporting the till as signed off.
Read back the tasks | Tea follow-up and large-lid check are with me.
Separate acceptance | I have accepted the work; I have not completed it yet.
Close the handover | Update the records with the actual results as the tasks finish.''',
    notes='''Item versus order | One finished item does not establish completion of the full ticket.
Count versus reconciliation | A count produces an amount; reconciliation compares it with relevant records.
Still pending | This preserves unfinished work through a change of staff.
With me | Common shorthand for responsibility, not proof of completed action.
Correct size | State the needed specification rather than assuming another size works.
Signed off | Use only when the required completion or approval has actually occurred.''',
    d='''Which handover is accurate? | Ticket 108: coffee complete, tea pending; large lids unavailable; till counted, review pending. | Everything is done except some stock. | The till is signed off because Ellis counted it. | Ticket 108 is ready because its coffee is complete. | The complete report preserves each task and its distinct current stage.
What does Noor's acceptance establish? | Responsibility for the tea and stock follow-ups | Completed tea service | Delivered large lids | Mara's completed cash reconciliation | Accepting a task transfers responsibility but does not perform the task.
Which stock claim is unsupported? | Small lids are approved substitutes for the large cups. | Large lids are unavailable. | Small lids remain. | Replenishment needs checking. | Remaining stock alone does not establish fit, suitability, or substitution approval.
Who owns the pending till review? | Mara | Noor by automatic assumption | The customer with ticket 108 | No named person | The brief explicitly leaves the reconciliation review with lead Mara.''',
    dialogue='''Ellis | It is two o'clock, and I need to hand over an open order, a lid shortage, and the till status before I finish.
Noor | I am ready for the [[shift handover::Shift handover transfers current tasks and information; it does not imply that every outgoing task is finished.]]. Please take them one at a time so I can keep the customer order separate from stock and cash checks.
Ellis | Ticket one hundred eight has two drinks. The coffee is complete, but the tea is pending. It is not a fully completed order.
Noor | I will record the [[item-level status::Item-level status distinguishes the completed coffee from the pending tea within the same ticket.]] as coffee complete, tea pending. I will not mark the entire ticket complete just because one drink is finished.
Ellis | Can you take the tea follow-up from here? Please use the actual order details and update its status when the work has really been completed.
Noor | Yes, I accept the [[tea follow-up::Tea follow-up is the specific outstanding responsibility Noor accepts; accepting it does not establish the tea is ready.]]. That is my next responsibility on ticket one hundred eight, not a claim that I have already made the drink.
Ellis | Next, large takeaway lids are unavailable. We still have small lids, but I have not established an approved alternative for the large cups.
Noor | Understood. The [[stockout::Stockout concerns the specified large lids, not every lid or a confirmed suitable substitute.]] is for large lids. I will not assume the remaining small ones are compatible with a different cup size.
Ellis | Please check replenishment of the correct large lids. I have no confirmed delivery time to pass on, so do not promise one from this handover.
Noor | I will take the [[stock follow-up::Stock follow-up assigns checking of the correct replenishment; no delivery or arrival estimate is yet confirmed.]] and report what I actually find. The need is clear, but the arrival time and supply outcome remain unconfirmed.
Ellis | Finally, I have counted the till. Mara has not completed reconciliation, so the count is available but the review is still pending.
Noor | The [[cash count::Cash count is the completed tally, which must remain distinct from the uncompleted reconciliation against relevant records.]] is complete, while reconciliation is not. I will not turn counted into signed off when I update the next person.
Ellis | Exactly. We have not established a shortage or an overage in this conversation. Mara still needs to carry out the relevant comparison and review.
Noor | I will leave the [[reconciliation::Reconciliation is the comparison and review that Mara has not completed; the handover supplies no resulting variance.]] with Mara. There is no reason to invent a difference between actual and expected cash from a pending check.
Ellis | Thank you. Could you repeat who owns each unfinished part? I want to make sure none of the three items disappears when I leave.
Noor | My [[handover read-back::The handover read-back confirms both responsibility and unfinished status, reducing the chance that an open task is lost.]] is: I take the tea follow-up and correct large-lid stock check. Mara retains the till review, which remains pending.
Ellis | That is right. Please keep the results separate when they come in. A lid update does not close the tea order or the cash review.
Noor | Agreed. The [[review owner::Review owner identifies Mara as responsible for the cash review; Noor's other accepted tasks do not transfer that review automatically.]] for the till remains Mara. I will record each actual outcome against its own task rather than give one blanket completion message.
Ellis | Good. I can finish my shift knowing the outstanding work has a named owner, without pretending the work itself has already been finished.
Noor | Yes. The handover is clear, but the till has no [[sign-off::Sign-off is the required completed confirmation, which cannot be inferred from a cash count or a successful handover.]] yet. I have accepted the tea and stock tasks and will update their real status as I carry them out.''',
    transfer_title='Transfer a different afternoon handover',
    transfer_setup='Ticket 205 has tea complete and cocoa pending. Medium lids are unavailable. Incoming worker Jules accepts the cocoa and stock follow-ups. Lead Ben retains the till reconciliation, which is still pending.',
    transfer='''Incoming: "The remaining drink is ___." | cocoa | Cocoa is pending, while the tea is already complete.
Outgoing: "The missing lid size is ___." | medium | Medium is the specific shortage supplied in this new handover.
Incoming: "The till review remains with ___." | Ben | Ben is explicitly identified as the owner of reconciliation.
Outgoing: "The till review is still ___." | pending | No completed reconciliation or sign-off is established in this handover.'''
))
