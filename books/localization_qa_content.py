"""Localization QA English: language evidence that developers can reproduce."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='localization-qa', title='Localization QA English',
    balanced_answer_columns=True,
    category='Technology & data', cover_label='ENGLISH FOR LOCALIZATION QUALITY ASSURANCE',
    cover_title='Localization QA', cover_size=34,
    tagline='Turn language findings into clear, reproducible product improvements.',
    audience='For localization quality assurance testers, linguistic reviewers, and software, game, and VR specialists collaborating with English-speaking development teams.',
    roles='Localization QA testers, linguistic testers, localization engineers, game localization reviewers',
    summary='Practical English for contextual bug reports, terminology, placeholders, plural rules, visual and bidirectional testing, cultural adaptation, VR subtitles, and release triage.',
    map_intro='Eight development-team situations connect linguistic reasoning with reproducible evidence. Explain what users see, why it changes meaning, and how the corrected behavior will be checked.',
    notes_title='A language bug needs product context.',
    notes_intro='A grammatically possible translation can still describe the wrong action. Effective localization QA explains the intended meaning, identifies the exact resource and build, and distinguishes a content correction from a rendering or implementation defect.',
    field_notes=[
        ('Show the trigger', 'Include the locale, build, screen or scene, relevant state, and exact steps. A screenshot documents the result but may not explain how to reach it.', '"This string appears after the player equips the shield, not on the purchase screen."'),
        ('Explain the linguistic distinction', 'Use a gloss or back-translation to explain the issue to colleagues who do not read the target language. Treat that explanation as evidence, not as a replacement for target-language review.', '"The current word means a fee; this action means rushing forward."'),
        ('Preserve the contract', 'Variable names, markup, and message syntax may have runtime requirements. Localize the surrounding language without casually changing functional tokens.', '"The word order changes, but the placeholder identifier must remain intact."'),
        ('Define verified scope', 'A corrected resource, a merged change, and a tested release package are different states. Name the actual build and affected locales when reporting verification.', '"The fix passed in this package; the other platform is still untested."')],
    scope_note=FICTION + 'Professional English practice, not a universal localization specification or a substitute for qualified target-language, accessibility, cultural, legal, or engineering review. Product rules, timings, test data, and release policies in the cases are fictional. Actual behavior depends on the supported locales, platform, framework, version, and approved style guide. Do not infer cultural preferences from nationality or reverse stored text to imitate a writing direction.',
    sources=[
        source('Microsoft. How to perform localization testing.', 'https://learn.microsoft.com/en-us/globalization/testing/how-to-perform-localization-testing', 'Context for linguistic, visual, and functional validation; all cases and dialogue are original.'),
        source('Unicode CLDR. Plural rules.', 'https://cldr.unicode.org/index/cldr-spec/plural-rules', 'Plural categories are locale-dependent grammatical selections, not universal numeric ranges. Check the actual runtime data.'),
        source('ICU. Formatting messages.', 'https://unicode-org.github.io/icu/userguide/format_parse/messages/', 'Context for complete messages, arguments, and locale-aware selection; no framework-specific implementation is prescribed.'),
        source('W3C. Inline markup and bidirectional text.', 'https://www.w3.org/International/articles/inline-bidi-markup/', 'Distinguishes surrounding direction, embedded runs, and isolation from manually reversing stored content.')], units=[])

BOOK['units'].append(unit(
    title='Reporting a contextual mistranslation', scene='Charge means an attack here, not a fee',
    skill='Explain a semantic error through reproducible scene context and an English gloss.',
    brief='In fictional game build 420, Japanese locale ja-JP, the shield tutorial uses resource action.charge. The target text means a monetary fee, but the button makes the character rush forward with a shield. The same English source word appears in the store. Tester Emi has reproduced the issue three times after equipping the shield. Developer Sam needs the intended meaning and resource context, not a guess about which translator caused it.',
    cast='Emi | Localization QA tester\nSam | Gameplay developer',
    culture=('Translate the reasoning for the engineering team', 'A colleague who does not read the target language can still act on an exact resource, a concise meaning explanation, and a reproducible behavior. Avoid turning the report into criticism of the translator.'),
    a='''What does the tutorial action actually do? | Rush forward with a shield | Collect a monetary fee | Purchase a shield | Open a billing form | The brief identifies a movement action rather than a store payment.
What does the current target text mean? | A monetary fee | A confirmed attack command | A shield durability value | A network recharge | The supplied gloss identifies the financial meaning as the contextual error.
Which evidence makes the report reproducible? | Build, locale, resource, and shield-equipping steps | A complaint that the language feels bad | The translator's presumed nationality | A store screenshot alone | These details identify the environment and trigger for the tutorial defect.''',
    vocabulary='''localization QA | Quality assurance focused on localized language and product behavior. | conduct localization QA
linguistic defect | Language error affecting meaning, grammar, or approved usage. | report a linguistic defect
source string | Text provided as the basis for localization. | inspect the source string
target string | Localized text in the destination language or locale. | review the target string
string ID | Identifier linking a text resource to its use. | include the string ID
in-context review | Inspection of language where it actually appears in the product. | perform an in-context review
reproduction steps | Ordered actions that produce the observed behavior. | supply reproduction steps
build number | Identifier for the tested software package or version. | record the build number
locale tag | Identifier for a language and optional regional or other locale distinctions. | specify the locale tag
expected behavior | Product result required by the agreed specification or context. | describe expected behavior
actual behavior | Result observed in the tested environment. | capture actual behavior
English gloss | Brief English explanation of a target expression's meaning. | provide an English gloss
back-translation | Rendering of translated content back into the source language for explanation. | attach a back-translation
semantic mismatch | Difference between intended meaning and the meaning conveyed. | isolate the semantic mismatch
context screenshot | Image showing the relevant text and surrounding product state. | attach a context screenshot
resource reuse | Use of one text resource in multiple product contexts. | investigate resource reuse
developer comment | Context note attached to a resource for implementation or translation. | add a developer comment
reproducibility | Ability to produce the finding again under stated conditions. | confirm reproducibility''',
    precision='The fee meaning is wrong in the shield tutorial. The English word charge alone does not reveal whether one resource is suitable for both the store and combat.',
    precision_extra='A back-translation explains a meaning to the team; it is not proof that the revised target text is natural or correct. Verify the actual localized product.',
    phrases='''Locate the defect | This appears in the shield tutorial after equipping the shield.
State the contrast | The target text means a fee, but the action is a forward attack.
Supply context | The affected string ID is action.charge in build 420.
Explain the gloss | This is an English explanation of the target meaning, not the proposed final translation.
Avoid blame | We need to check what context accompanied the resource.
Request separation | Can these distinct meanings use separate resources?
Scope the evidence | I reproduced this three times in ja-JP.
Define verification | Retest the tutorial and the store after the resources change.''',
    notes='''Means versus sounds like | Means identifies the semantic problem; sounds like can leave the developer unsure whether the issue is style or meaning.
Here versus everywhere | Here ties the finding to a context without claiming the word is wrong in every use.
Reproduced versus caused by | Reproduced reports a repeatable result without proving who or what introduced it.''',
    d='''Which bug title is most useful? | ja-JP shield tutorial uses fee meaning for attack in build 420 | Japanese is wrong everywhere | Translator does not understand games | Store button looks fine | The precise title identifies the locale, context, meaning error, and tested build.
What should be checked before editing a shared resource? | Every context that uses it | Only the longest word | The developer's first language | Whether the screenshot has a border | A shared resource can affect both tutorial and store contexts.
Which explanation helps an English-speaking engineer? | The target means fee; the button triggers a forward attack | The target is obviously strange | Trust my opinion without context | Delete all Japanese resources | The semantic contrast connects language evidence with observed product behavior.
What establishes correction? | Target-language review and in-product retest | Editing a spreadsheet alone | Renaming the ticket | Assuming three reproductions mean three separate bugs | A resource edit still needs linguistic and product verification.''',
    dialogue='''Sam | I see the screenshot, but I cannot read the Japanese text. What is wrong with the tutorial button?
Emi | The [[English gloss::The English gloss explains that the target expression conveys a monetary fee, allowing the engineer to understand the semantic contrast.]] is a monetary fee. Here, pressing the button makes the character rush forward with a shield.
Sam | So this is not just a preference between two natural ways of describing the same move?
Emi | Right. It is a [[semantic mismatch::The semantic mismatch changes the action's meaning from a combat move to a financial charge, rather than merely changing style.]] between the label and the action the player performs.
Sam | Which environment should I use? I tried the store on yesterday's package and did not see an obvious problem.
Emi | Use [[build number::The build number identifies the tested package, here 420, rather than assuming another package has the same resources.]] 420 and ja-JP. Start the shield tutorial, equip the shield, and open its action prompt.
Sam | I can follow that. The store result would not tell me whether the combat use is correct.
Emi | Exactly. Those [[reproduction steps::The reproduction steps identify the tutorial state that triggers the finding, unlike testing an unrelated store context.]] produced the same label on all three runs.
Sam | Do you have the resource identifier, or are we searching for every occurrence of the English word charge?
Emi | The [[string ID::The string ID identifies action.charge as the affected resource, making the report traceable without searching by an ambiguous English word alone.]] is action.charge. The screenshot includes the surrounding prompt and the equipped shield.
Sam | That resource is also used in the store. We reused the source word because the English label was identical.
Emi | That [[resource reuse::Resource reuse can conceal distinct meanings when identical English wording is shared across contexts that require different target expressions.]] may explain the context problem, but the actual resource history still needs checking.
Sam | We could separate the combat and payment resources and give each one a note about what the player is doing.
Emi | A [[developer comment::A developer comment supplies context for the resource so the target-language reviewer can distinguish the intended combat action from payment.]] would help, especially if it states whether the label names an action or a cost.
Sam | Once the localized combat text is updated, can we close this from the translation sheet?
Emi | We still need [[in-context review::In-context review verifies the localized wording where the player actually encounters it, rather than treating a spreadsheet change as completed product verification.]] in the built tutorial and a check that the store remains correct.
Sam | I will split the resources and attach the updated package when it is ready for testing.
Emi | I will compare [[expected behavior::Expected behavior is the agreed attack meaning in this tutorial, which the revised label must convey in the actual product.]] with the displayed target text and record the tested package.
Sam | Good. The ticket can describe the exact meaning problem without guessing which person introduced it.
Emi | Yes. The [[context screenshot::The context screenshot preserves the visible tutorial state and surrounding language as evidence, without substituting for the reproducible steps.]] and steps give us a clear shared reference for the fix.''',
    rehearsal=['Read the corrected exchange and stress the contrast between fee and forward attack.', 'Switch roles and repeat the build, locale, resource, and reproduction steps exactly as printed.'],
    transfer_title='A different context uses the same source word', transfer_setup='The store uses charge for a payment. The tutorial uses charge for a forward attack. A single resource currently serves both.',
    transfer='''Tester: "The store meaning concerns a ___." | payment | The supplied store context uses charge in its financial sense.
Developer: "The tutorial meaning concerns an ___." | attack | The supplied tutorial context uses charge for forward combat movement.
Tester: "The contexts need separate ___." | resources | Separate resources can express different meanings that share one English word.
Developer: "Retest both product ___." | contexts | The change must preserve correct language in both the store and tutorial.'''))

BOOK['units'].append(unit(
    title='Protecting placeholders while changing word order', scene='A fluent sentence can still break the runtime contract',
    skill='Distinguish translatable wording from functional arguments and explain reordering needs.',
    brief='A fictional gift notification has named placeholders {sender} and {item}. The approved target-language sentence places the item before the sender. A reviewer changed {sender} to a translated variable name, which the runtime does not recognize. The English source was previously assembled from separate fragments. Tester Noura and engineer Alex need a complete localizable message, intact named arguments, and checks using long names and item labels.',
    cast='Noura | Localization tester\nAlex | UI engineer',
    culture=('Describe grammar as a product requirement', 'Different word order is not a request to make the target language imitate English. Explain the relationship the sentence must express and the functional tokens the system expects.'),
    a='''Which change broke the supplied runtime contract? | Translating the placeholder name | Placing the item earlier in the sentence | Reviewing the complete message | Testing a long sender name | The runtime expects the exact named argument and does not recognize its translated replacement.
What does the target sentence require? | Item before sender | English word order in every locale | Removing the item entirely | Replacing every name with English text | The brief explicitly states the approved target-language order.
What should replace assembled fragments? | A complete localizable message | A longer hard-coded English fragment | A screenshot-only label | An untranslated error message | A complete message allows the target language to express its required structure.''',
    vocabulary='''placeholder | Token replaced by a runtime value. | preserve the placeholder
named argument | Runtime value referenced by a stable name. | pass the named argument
interpolation | Insertion of values into a message pattern. | test interpolation
message pattern | Structured template used to format a complete message. | review the message pattern
string concatenation | Joining fragments to form text. | avoid brittle string concatenation
word order | Arrangement of words and phrases in a sentence. | support target-language word order
grammatical agreement | Required matching of grammatical features between related words. | check grammatical agreement
inflection | Change in word form expressing grammatical information. | account for inflection
token integrity | Preservation of required functional tokens through processing. | validate token integrity
escape sequence | Syntax representing characters that need special handling. | preserve the escape sequence
markup tag | Structured marker controlling text or presentation. | validate the markup tag
runtime value | Data inserted while the product executes. | test realistic runtime values
argument type | Expected kind of value supplied to a message. | verify the argument type
parser error | Failure to interpret structured syntax. | investigate the parser error
literal text | Content displayed as written rather than interpreted as a token. | distinguish literal text
translator instruction | Note defining context and handling requirements. | add translator instructions
round-trip test | Check that content survives export and reimport correctly. | run a round-trip test
resource schema | Defined structure and constraints for localization data. | validate the resource schema''',
    precision='Reordering intact named placeholders can support target grammar. Renaming a required argument changes the runtime contract in this case.',
    precision_extra='Different message systems have different syntax. Validate the actual formatter and resource schema instead of treating every brace or tag as ordinary punctuation.',
    phrases='''Separate wording and syntax | Translate the surrounding words, but preserve the argument names.
Explain ordering | The item needs to precede the sender in this sentence.
Identify the failure | The runtime no longer recognizes the renamed placeholder.
Request a full message | Can we localize this as one complete message?
Check the value | Is this argument a display name or an internal identifier?
Preserve formatting | This tag is functional markup, not text for the user.
Test realistic data | Include long names and multiword item labels.
Verify the pipeline | Check the exported and reimported resource, not only the editor preview.''',
    notes='''Reorder versus rename | Reorder changes position; rename changes the identifier the system may require.
Sentence versus fragments | A sentence has a complete grammatical relationship that separately translated fragments may not preserve.
Rendered versus stored | Rendered describes the displayed result; stored describes the underlying resource or value.''',
    d='''Which instruction preserves the supplied contract? | Keep {sender} intact while moving it to the required position | Translate {sender} into a different variable name | Remove the sender value | Hard-code the test user's name | The exact argument name must survive even when its position changes.
What can fragment assembly prevent? | Natural target-language structure | Any possible English display | Every runtime value | All screenshot capture | Separately assembled fragments can constrain word order and grammatical relationships.
What should a test name represent? | A realistic runtime value | A permanent replacement for the argument | A new locale code | A translation approval | Realistic values reveal issues hidden by short editor placeholders.
Which check catches export damage? | A round-trip test | A ticket title change | Testing only the source screenshot | Counting the reviewers | Exporting and reimporting can reveal altered tokens or syntax in the resource pipeline.''',
    dialogue='''Alex | The revised sentence reads naturally according to the reviewer, but the notification now shows an unresolved token.
Noura | The [[placeholder::The placeholder is the functional token replaced by runtime data; changing its expected name can leave it unresolved.]] for the sender was renamed during translation. The runtime still supplies the original identifier.
Alex | Does preserving that identifier mean we also have to keep the sender at the start of the sentence?
Noura | No. The [[named argument::A named argument identifies the value independently of its position in the message, allowing the supported formatter to place it where the target sentence needs it.]] must remain intact, but its position can follow the target sentence structure.
Alex | In this approved wording, the item appears before the sender. Our old implementation joins several English fragments.
Noura | That [[string concatenation::String concatenation joins fragments whose English sequence can prevent the target language from forming the required complete sentence.]] is the structural problem. Give the translator the full message and its intended meaning.
Alex | I can expose one message with the two arguments instead of expecting every language to use the same fragment sequence.
Noura | Good. The [[word order::Word order concerns the placement of the item and sender in the target sentence, not permission to change their functional identifiers.]] can then change without changing which value each argument represents.
Alex | Are the argument values already display text, or should the translation alter their grammatical form?
Noura | We need that contract documented. [[Inflection::Inflection changes word forms for grammatical purposes and cannot be assumed safe for arbitrary names or supplied labels without a defined message design.]] is not something we can safely invent for arbitrary names and item labels.
Alex | I will describe the value types and provide examples so the reviewer knows what can appear in each slot.
Noura | Add a [[translator instruction::A translator instruction explains the resource context and token requirements so reviewers can distinguish localizable language from functional syntax.]] identifying the protected arguments and the relationship the message must express.
Alex | The resource also includes presentation tags. A reviewer thought one tag was an English word that needed translation.
Noura | Then validate [[token integrity::Token integrity means required arguments and markup survive localization and processing without being renamed, deleted, or malformed.]] for both arguments and markup, using the actual resource schema.
Alex | The editor preview looks correct after my change. Is that enough to send it for final review?
Noura | Run a [[round-trip test::A round-trip test checks the exported and reimported resource, where processing can alter tokens even if the editor preview was correct.]] through export and import, then inspect the built notification with realistic values.
Alex | I will include a long sender name and a multiword item label instead of testing only A and B.
Noura | That tests [[interpolation::Interpolation inserts actual values into the message, so realistic names and labels reveal behavior that placeholder-only previews can miss.]] and gives the language reviewer a meaningful sentence to inspect.
Alex | If the formatter rejects the pattern, I will report the syntax error separately from the wording question.
Noura | Exactly. A [[parser error::A parser error means the message syntax could not be interpreted and should be distinguished from a fluent but semantically incorrect sentence.]] needs engineering evidence; a language concern needs its own contextual explanation. Test both in the target build.''',
    rehearsal=['Read the corrected exchange and stress reorder, rename, and preserve.', 'Switch roles and repeat the printed distinction between complete-message grammar and protected runtime tokens.'],
    transfer_title='The variable moved but kept its name', transfer_setup='The target message moves {sender} after {item}. Both identifiers remain intact and the supported formatter resolves both values.',
    transfer='''Engineer: "The argument names remain ___." | intact | The brief preserves both exact identifiers required by the runtime.
Tester: "Their ___ has changed." | position | The target message changes where the arguments appear, not their names.
Engineer: "Both values are ___ by the formatter." | resolved | The supplied formatter successfully replaces both identifiers with their values.
Tester: "Now verify the complete target ___." | sentence | Functional resolution does not replace a review of the full localized sentence.'''))

BOOK['units'].append(unit(
    title='Explaining plural categories to engineers', scene='Two and five cannot share every grammatical form',
    skill='Use a small test matrix to explain locale-dependent plural selection without equating categories with numbers.',
    brief='A fictional Russian item counter is wired to English-style one-versus-other logic. For the integer test values in this lesson, the expected Russian cardinal categories are 1 and 21: one; 2 and 22: few; 5 and 11: many. The current build sends all values except 1 to other. Tester Pavel and engineer Zoe must test category selection separately from the target wording. Decimal cases and other locales are outside this small matrix, not implicitly passed.',
    cast='Pavel | Localization QA tester\nZoe | Application engineer',
    culture=('Make a grammar rule testable', 'Show the developer a minimal contrast and expected category rather than asking for a vague more natural plural. A category name is a technical label, not an English translation of the number.'),
    a='''Which category is expected for 22 in this matrix? | few | one | many | The English singular category | The supplied Russian integer matrix places twenty-two in few.
Which tested value uses one besides 1? | 21 | 11 | 5 | 2 | The case explicitly lists twenty-one with one, unlike English-style singular selection.
What has not been covered by this matrix? | Decimal cases and other locales | The six listed integers | The current one-versus-other defect | The expected category for eleven | The brief limits coverage to the stated integer cases in this locale.''',
    vocabulary='''cardinal number | Number expressing quantity rather than position. | test cardinal numbers
ordinal number | Number expressing position in a sequence. | distinguish ordinal numbers
plural category | Locale-dependent label selecting an appropriate grammatical message form. | select the plural category
CLDR | Unicode Common Locale Data Repository supplying locale conventions and data. | check the CLDR data
minimal pair | Contrast where a controlled change reveals a required linguistic distinction. | provide a minimal pair
message branch | Alternative selected within a structured message. | exercise each message branch
fallback branch | Alternative used when the specified selection rules direct to it. | verify the fallback branch
exact-value selector | Message condition matching a specified numeric value. | distinguish an exact-value selector
integer test case | Test using a whole-number value. | add integer test cases
decimal operand | Numeric information used by a plural rule for decimal values. | inspect decimal operands
visible fraction digits | Written fractional digits that may affect locale rule selection. | preserve visible fraction digits
boundary value | Input near a rule transition or limit. | test boundary values
selection logic | Rules choosing which message alternative is used. | inspect selection logic
locale data version | Version of the locale rules bundled with the runtime. | record the locale data version
test matrix | Organized set of inputs and expected results. | build a plural test matrix
category coverage | Extent to which required grammatical categories are exercised. | report category coverage
grammatical number | Linguistic distinction related to quantity in word forms or agreement. | explain grammatical number
hard-coded plural | Fixed plural behavior that ignores required locale variation. | replace hard-coded plurals''',
    precision='For the supplied integer matrix, 21 selects one and 11 selects many. The label one therefore does not universally mean the exact numeric value 1.',
    precision_extra='Cardinal and ordinal rules are different. Decimal representation and runtime locale-data versions can matter; passing six integer cases is not complete plural coverage.',
    phrases='''Show the contrast | Two and five require different branches in this locale.
Separate label and value | The category one is not an exact-value test for one.
State the matrix | Twenty-one selects one; eleven selects many in this integer case.
Locate the logic | The build is applying the English-style split.
Test both layers | Check branch selection and the wording inside each branch.
Limit coverage | This matrix does not cover decimals or every supported locale.
Check the runtime | Which locale-data version is bundled in this package?
Explain the fallback | The fallback branch is required, but it does not replace the other needed forms.''',
    notes='''One versus equals one | One can name a grammatical category; equals one specifies an exact number.
Cardinal versus ordinal | Two items expresses quantity; second item expresses position.
Covered versus supported | A tested case is covered; a product's broader support claim requires its full stated scope.''',
    d='''Which explanation corrects the engineer's assumption? | One is a locale category, not always the exact value 1 | Every language has only singular and plural | Few always means the numbers two through four | Other is never needed | Category labels follow locale rules rather than universal English numeric ranges.
Which pair exposes the supplied English-style defect? | 1 and 21 | 1 and 1 | Two identical screenshots at 1 | Two English source labels | Both values require one here, but the current build sends twenty-one to other.
What needs checking after category routing is fixed? | The target wording in each branch | Only the source language | Whether the ticket number is even | The translator's keyboard layout | Correct selection does not prove that the chosen target message is linguistically correct.
Which verification claim is supported after these six tests pass? | The listed integer matrix passed | All languages and decimals passed | Ordinal formatting passed everywhere | Every runtime version is equivalent | Passing the stated cases supports only their defined test scope.''',
    dialogue='''Zoe | The counter works for one item and more than one item in English. Why do we need extra alternatives?
Pavel | The target locale uses different [[plural category::A plural category selects a grammatical form under locale-specific rules, so an English one-versus-other split is insufficient for this Russian integer matrix.]] selections. Our six integer examples make the difference visible.
Zoe | Walk me through the expected result without assuming that I can judge the Russian endings myself.
Pavel | The [[test matrix::The test matrix pairs each supplied integer with its expected category, allowing the engineer to verify routing independently of reading the target wording.]] assigns one and twenty-one to one, two and twenty-two to few, and five and eleven to many.
Zoe | I thought the category called one meant only the exact numeric value one. Twenty-one currently goes to other.
Pavel | That confuses a category with an [[exact-value selector::An exact-value selector matches a particular number, while a plural category can include other values under the locale's grammatical rules.]]. The category name is not a universal numeric definition.
Zoe | Then the defect is in how we choose the alternative, not necessarily in the words stored inside it.
Pavel | Correct. Test the [[selection logic::Selection logic determines which branch receives each input, a separate question from whether the text inside that branch is correct.]] first, then have the target-language reviewer check each resulting message.
Zoe | I will log the selected category for each value so we can see whether the counter is routing correctly.
Pavel | That gives us [[category coverage::Category coverage identifies which required categories have actually been exercised, rather than treating one passing count as proof of all forms.]] for this matrix. Keep the expected and actual categories next to each other.
Zoe | Should we delete other because none of these six expected results uses it?
Pavel | No. This is a limited [[integer test case::An integer test case uses a whole-number input; this limited set does not justify removing branches needed by the message system or other numeric forms.]] set, not a reason to remove required fallback structure.
Zoe | We also display fractional quantities elsewhere, but those screens are not part of this counter test.
Pavel | Track them separately. [[Visible fraction digits::Visible fraction digits can affect locale rule selection, so fractional representations need deliberate tests rather than an assumption from integer results.]] can matter, so a decimal check is not simply another integer screenshot.
Zoe | I will record the formatting library and the locale rules packaged with this build before comparing environments.
Pavel | Include the [[locale data version::The locale data version identifies the actual rules used by the tested runtime and helps explain differences between environments.]] so we are testing the actual product rather than an assumed rule set.
Zoe | What should I tell the team when these six cases pass? I do not want the report to overstate the result.
Pavel | Say the listed [[cardinal number::Cardinal numbers express quantity, so passing these counter cases does not establish ordinal formatting or untested locale coverage.]] cases passed in this build. Do not include ordinal or decimal coverage that we have not run.
Zoe | Understood. The counter needs locale-aware selection and a separate linguistic check of the selected text.
Pavel | Exactly. A clear [[minimal pair::A minimal pair or controlled contrast demonstrates the required linguistic distinction, helping the engineer understand why apparently similar counts need different behavior.]] explains the requirement, and the matrix turns that explanation into repeatable evidence.''',
    rehearsal=['Read the corrected exchange, then read the six supplied number-category pairs aloud in order.', 'Switch roles and distinguish exact numeric value, plural category, and tested coverage.'],
    transfer_title='The category label was read as an equality test', transfer_setup='Use the supplied Russian integer matrix: 21 selects one, 22 selects few, and 11 selects many. No decimal test result is supplied.',
    transfer='''Tester: "Twenty-one selects ___." | one | The supplied locale matrix places twenty-one in the one category.
Engineer: "Twenty-two selects ___." | few | The supplied locale matrix places twenty-two in the few category.
Tester: "Eleven selects ___." | many | The supplied locale matrix places eleven in the many category.
Engineer: "Decimal coverage remains ___." | untested | No decimal result is supplied, so integer success cannot establish decimal coverage.'''))

BOOK['units'].append(unit(
    title='Diagnosing layout without weakening the translation', scene='The short preview passed but the real button clips',
    skill='Distinguish text expansion, clipping, font support, and layout constraints using a visual test report.',
    brief='A fictional settings button fits its English label and a pseudolocalized sample. The approved German translation clips its final word at the supported narrow viewport. Its complete meaning is required, and the current design allows two lines. A separate label displays missing-glyph boxes. Tester Lena and UI engineer Chris must distinguish the width problem from font coverage and retest the actual target build.',
    cast='Lena | Localization QA tester\nChris | UI engineer',
    culture=('Discuss constraints without blaming the language', 'A longer translation is not automatically bad writing. Identify what the user must understand and which layout limits are actually required before requesting a shorter phrase.'),
    a='''What does the approved design allow? | Two lines in the button | Only one line in every locale | Removing the final word | An unsupported font size | The brief explicitly allows two lines, so the existing clipping is not an unavoidable design requirement.
What does a pseudolocalized pass establish here? | Only that the tested sample fit | Every real translation fits | German wording is too long by definition | The font contains every glyph | The actual target translation still clips despite the sample passing.
Which separate issue do boxes indicate in this case? | Missing glyphs | A required two-line layout | A successful translation review | A confirmed spelling error | The brief distinguishes missing-glyph boxes from the button's width problem.''',
    vocabulary='''pseudolocalization | Artificial transformation of source text to expose internationalization issues. | run pseudolocalization
text expansion | Increase in space needed by a localized expression. | allow for text expansion
truncation | Loss of displayed text because it exceeds a limit. | report truncation
clipping | Hiding text or graphics outside a rendering boundary. | inspect text clipping
overflow | Content extending beyond its allocated space. | test overflow behavior
line wrapping | Movement of text onto additional lines. | permit line wrapping
viewport | Visible area available for rendering content. | record the viewport
glyph | Visual form used to display a character or character sequence. | inspect the missing glyph
font fallback | Use of another font when the selected font lacks required support. | verify font fallback
font coverage | Set of characters or scripts supported by a font. | check font coverage
shaping | Conversion of characters into appropriate contextual glyph forms and positions. | test text shaping
line height | Vertical space allocated to each line of text. | adjust line height
ellipsis | Omission marker used when displayed content is shortened. | inspect the ellipsis
safe area | Region reserved to keep content clear of constrained or obstructed display zones. | respect the safe area
responsive layout | Arrangement that adapts to available display dimensions. | validate the responsive layout
text scaling | User or system adjustment of displayed text size. | test text scaling
visual regression | Unintended visual change relative to an established result. | capture a visual regression
layout constraint | Rule limiting content size or placement. | review the layout constraint''',
    precision='A pseudo sample is a useful stress test, not a guarantee for every real string. The approved German text must be checked in the supported viewport.',
    precision_extra='Width, glyph coverage, shaping, and line height are different concerns. Shortening the sentence does not repair a font that cannot display a required character.',
    phrases='''Describe the loss | The final word is clipped at the supported narrow viewport.
Preserve meaning | That word distinguishes saving locally from syncing online.
Check the constraint | Does the approved design allow this label to wrap?
Separate defects | The boxes are a font-coverage issue, not the same width defect.
Limit the pseudo claim | The pseudo sample passed; the real target string did not.
Test scaling | Please include the supported text-size settings.
Define the result | The full label must remain legible without overlapping the adjacent control.
Compare builds | Capture the same viewport and state before and after the change.''',
    notes='''Fits versus reads correctly | Fits concerns available space; reads correctly also concerns complete meaning and legibility.
Shorter versus clearer | A shorter label can remove a necessary distinction rather than improve the wording.
Font versus language | A rendering failure does not establish that the target-language text is linguistically wrong.''',
    d='''Which first request follows the design facts? | Allow the approved two-line wrap and retest | Delete the final word immediately | Shrink every locale to unreadable text | Declare German unsupported | The design permits two lines and the complete approved meaning is required.
Which test distinguishes the two findings? | Check width behavior and font coverage separately | Count only English characters | Compare ticket priorities | Rename the font file without rendering | The case contains a layout issue and a separate missing-glyph issue.
Which result is sufficient for this button's visual check? | Complete legible text without overlap in the supported states | A passing source-language screenshot only | An ellipsis hiding the required distinction | A reviewer saying longer languages are difficult | The expected result preserves the full meaning in the supported layout.
What should a before-and-after comparison keep consistent? | Viewport, state, and text-size settings | Only the file name | The number of people in the meeting | An arbitrary different screen | Comparable conditions are needed to attribute the visual difference to the fix.''',
    dialogue='''Chris | The pseudolocalized build passed last week. Why is the German settings button still reported as a layout defect?
Lena | [[Pseudolocalization::Pseudolocalization tests artificial text and can expose structural issues, but a passing sample does not guarantee that every real translation fits.]] gave us a useful sample, but the approved real translation needs more space in this control.
Chris | Could the reviewer just shorten the phrase? The English version fits comfortably on one line.
Lena | The last word carries a required distinction. [[Text expansion::Text expansion changes the space needed for a localized expression and is not by itself evidence that the translation is unnecessarily wordy.]] is not evidence that the translation is wrong.
Chris | Which supported screen size shows the problem? I need the exact dimensions for the comparison.
Lena | I recorded the [[viewport::The viewport identifies the available rendering area so the engineer can reproduce the narrow-layout result under the same conditions.]] in the ticket and attached the same settings state from both builds.
Chris | I can see the final word disappearing at the right edge. It is not intentionally replaced with three dots.
Lena | Correct. That is [[clipping::Clipping hides part of the rendered label at its boundary, distinct from a deliberate and acceptable shortening rule.]], and the hidden word changes what the user can understand.
Chris | The design file allows two lines. The component seems to have inherited a no-wrap rule from a different button.
Lena | Then test [[line wrapping::Line wrapping can use the two lines permitted by this design while preserving the complete label, rather than deleting required meaning.]] within that approved design before asking the language team to remove meaning.
Chris | I will also check that the second line does not collide with the neighboring control at larger supported text settings.
Lena | Yes. Include [[text scaling::Text scaling changes the space required by the displayed text, so a fix at one default size does not establish all supported visual states.]] in the retest and keep the full label legible.
Chris | The screenshot below shows boxes in another label. Will the wider button solve that too?
Lena | No. That is a separate [[font coverage::Font coverage concerns whether the font can display the required characters, so widening a button does not repair missing glyph support.]] finding. The selected font does not provide the required glyphs there.
Chris | We need to inspect the fallback font and verify its actual rendering on the target platform.
Lena | Exactly. [[Font fallback::Font fallback can provide missing character support, but its actual appearance and metrics still need verification in the target environment.]] can affect appearance and spacing, so check the result rather than only the configuration.
Chris | I will keep the width and missing-glyph issues in separate linked tickets because their fixes and checks differ.
Lena | That makes the [[visual regression::A visual regression comparison should use consistent conditions and distinguish separate layout or rendering changes rather than conflating their causes.]] comparison easier to interpret when the next package arrives.
Chris | We will compare the full German label at the same viewport and supported text sizes, then inspect the other label's glyphs.
Lena | Good. The [[layout constraint::The layout constraint is the actual approved space and wrapping behavior, not an assumed English-only one-line limit.]] should reflect the approved design and complete meaning, not an accidental English-only limit.''',
    rehearsal=['Read the corrected exchange and distinguish clipping, expansion, and missing glyphs.', 'Switch roles and repeat the printed retest conditions without deleting any required label meaning.'],
    transfer_title='The width fix did not repair the font', transfer_setup='The button now wraps completely on two lines. Another label still contains missing-glyph boxes.',
    transfer='''Engineer: "The button now uses two ___." | lines | The supplied fix displays the complete button label across two lines.
Tester: "Its width-related finding is ready for ___." | verification | The changed behavior should be checked against the defined supported conditions.
Engineer: "The other label still has missing ___." | glyphs | The remaining boxes indicate the separate supplied character-rendering issue.
Tester: "Keep the font ticket ___." | open | The width change does not resolve the still-present font problem.'''))

BOOK['units'].append(unit(
    title='Explaining mixed-direction text defects', scene='The Arabic sentence must not reverse the order ID',
    skill='Separate paragraph direction, embedded text direction, and stored data when reporting a bidirectional defect.',
    brief='In a fictional Arabic order-confirmation screen, the stored identifier is AB-123. The surrounding sentence reads right to left, while this identifier must retain its left-to-right order. Punctuation appears in the wrong visual position when the identifier is inserted. Developer Owen proposes reversing the stored identifier. Tester Salma must explain why directional handling and isolation need investigation instead. The order data itself is correct.',
    cast='Salma | Localization tester\nOwen | Frontend engineer',
    culture=('Use the right level of explanation', 'Explain the mixed directions with the exact identifier and surrounding context. Do not require every engineer to become a linguist, but do distinguish data order from visual presentation.'),
    a='''What is the correct stored identifier? | AB-123 | 321-BA | A translated order number | An unspecified replacement | The brief explicitly identifies AB-123 as the correct underlying data.
What should not be done to imitate the screen direction? | Reverse the stored identifier | Inspect surrounding directional handling | Preserve the actual order data | Test punctuation with embedded text | Reversing correct data would create a new error rather than address the display problem.
Which part reads right to left? | The surrounding Arabic sentence | Every identifier in every context | The stored Latin identifier by definition | The file's bytes in reverse | The brief distinguishes the surrounding sentence from the embedded left-to-right identifier.''',
    vocabulary='''right-to-left | Writing direction progressing primarily from right to left. | test a right-to-left interface
left-to-right | Writing direction progressing primarily from left to right. | preserve a left-to-right identifier
bidirectional text | Text combining runs with different writing directions. | inspect bidirectional text
base direction | Direction established for the containing text context. | set the base direction
directional run | Consecutive text with a shared directional behavior. | isolate the directional run
logical order | Sequence in which text is stored and interpreted as content. | preserve logical order
visual order | Sequence or placement in which text appears on screen. | inspect visual order
directional isolation | Separation of an embedded text run's directional effects from its surroundings. | apply directional isolation
neutral punctuation | Punctuation whose display behavior depends on surrounding directional context. | test neutral punctuation
mirroring | Direction-sensitive change in presentation or layout. | review interface mirroring
Unicode bidi algorithm | Unicode rules for displaying mixed-direction text. | use the Unicode bidi algorithm
direction attribute | Markup setting that supplies text-direction information. | inspect the direction attribute
embedded identifier | Code or label inserted within surrounding prose. | preserve the embedded identifier
directional control | Character affecting directional interpretation of text. | inspect directional controls
caret movement | Behavior of the insertion point while navigating text. | test caret movement
selection range | Portion of text selected by a user or program. | verify the selection range
copy-paste fidelity | Preservation of intended content when copying and pasting. | check copy-paste fidelity
layout mirroring | Reversal of appropriate interface arrangement for directional conventions. | validate layout mirroring''',
    precision='Right-to-left surrounding prose does not mean every embedded identifier should be reversed. Preserve AB-123 and investigate how the renderer handles the mixed-direction boundary.',
    precision_extra='Text direction, language, and alignment are different properties. Check the actual platform and supported bidirectional behavior, including copy and selection.',
    phrases='''Name the data | The stored identifier is correct: AB-123.
Locate the boundary | The punctuation moves when this left-to-right value enters the Arabic sentence.
Reject data reversal | Reversing the stored characters would change the identifier.
Separate properties | Right alignment alone does not define text direction.
Request isolation | Can we isolate the embedded run from the surrounding prose?
Check interaction | Copy the identifier and verify that its logical order is unchanged.
Scope mirroring | Mirror appropriate layout elements, not every asset or data value.
Retest variants | Include identifiers, numbers, and punctuation in the same surrounding context.''',
    notes='''Direction versus alignment | Direction affects text ordering; alignment positions a block within available space.
Logical versus visual | Logical order concerns stored content; visual order concerns presentation.
Reverse versus mirror | Reversing characters changes their sequence; directional mirroring is a presentation behavior with context-specific rules.''',
    d='''Which proposed fix would corrupt the supplied identifier? | Store 321-BA instead of AB-123 | Investigate directional isolation | Preserve the existing data | Test the same sentence on the target platform | The proposed reversal changes the correct identifier instead of fixing its presentation.
Which evidence should accompany the report? | Stored identifier, surrounding text context, and screenshot | Only a claim that Arabic is difficult | A reversed database export | A different English-only screen | These items distinguish correct source data from the faulty mixed-direction display.
Which check goes beyond a screenshot? | Copy and paste the identifier to verify content | Rename the screenshot file | Remove every number | Translate the internal identifier | Copy-paste testing can reveal content-order problems not established by a visual check alone.
Which statement is accurate? | A right-aligned block can still have incorrect directional handling | Right alignment automatically solves every bidi issue | Every arrow must always be mirrored | All punctuation has a fixed direction independent of context | Alignment and text-direction behavior are distinct and require separate inspection.''',
    dialogue='''Owen | The Arabic confirmation puts punctuation in the wrong place. Would reversing the order ID before display fix it?
Salma | The [[logical order::Logical order is the stored content sequence, which is already correct as AB-123 and must not be reversed to imitate the surrounding writing direction.]] is already correct. Reversing AB-123 would create a different identifier.
Owen | I was treating the whole sentence as though every character should run in the same direction.
Salma | It is [[bidirectional text::Bidirectional text combines differently directed runs, here Arabic prose and a left-to-right Latin identifier within one sentence.]]. The Arabic prose and the embedded identifier do not share one uniform direction.
Owen | The container is right-aligned. I assumed that also told the browser how to handle the characters.
Salma | Alignment is not the [[base direction::Base direction supplies the directional context for text, which is distinct from positioning a block against the right margin.]]. We need to inspect the actual directional information and rendering context.
Owen | The identifier itself should still read A, B, hyphen, one, two, three when copied out.
Salma | Yes. Preserve that [[embedded identifier::The embedded identifier is the intact left-to-right code inserted into surrounding prose, not text whose characters should be translated or reversed.]] and investigate the boundary around it.
Owen | The punctuation seems to move when the identifier is followed by another number in the sentence.
Salma | That is useful evidence about [[neutral punctuation::Neutral punctuation can be affected by surrounding directional runs, so its position must be tested in the full mixed-direction context.]]. Include the full context rather than cropping out the adjacent number.
Owen | We should check whether the inserted run is isolated so its directional behavior does not affect neighboring content.
Salma | Exactly. [[Directional isolation::Directional isolation separates the embedded run's directional effects from the surrounding prose, addressing presentation without changing the underlying identifier.]] is a rendering concern; it does not require rewriting the order data.
Owen | I will use the platform's supported directional handling and test the result instead of adding arbitrary reversed strings.
Salma | Record the [[visual order::Visual order is the displayed arrangement, which should be inspected separately from the correct stored character sequence.]] in screenshots, then check the interactive behavior as well.
Owen | Which interactions are most useful for this confirmation screen besides reading the label?
Salma | Check [[copy-paste fidelity::Copy-paste fidelity confirms that the copied identifier retains its intended content and order rather than merely looking acceptable on screen.]], selection, and any editable field that reuses the same component.
Owen | The selection highlight can cover the right characters while keyboard navigation still feels wrong, so those need distinct observations.
Salma | Yes. [[Caret movement::Caret movement concerns the insertion point's navigation behavior, which requires an interaction test rather than a screenshot-only judgment.]] belongs in the interaction report, not an assumption from the static image.
Owen | I will keep the identifier unchanged and attach the mixed-direction examples to the component ticket.
Salma | Good. Also keep [[layout mirroring::Layout mirroring concerns appropriate interface arrangement and is distinct from reversing identifiers or every visual asset indiscriminately.]] separate. A right-to-left interface does not mean every asset or data value should be reversed.''',
    rehearsal=['Read the corrected exchange and distinguish logical order, visual order, and alignment.', 'Switch roles and read back AB-123 exactly, then repeat the printed verification steps.'],
    transfer_title='The screenshot looked right but copying changed the ID', transfer_setup='The expected identifier is AB-123. A proposed workaround displays it plausibly but copies 321-BA.',
    transfer='''Tester: "The expected identifier is ___." | AB-123 | The brief supplies AB-123 as the correct identifier.
Engineer: "Copying produces ___." | 321-BA | The copied result is the reversed sequence described in the case.
Tester: "That changes the underlying ___." | content | A different copied sequence is a data-content problem, not merely alignment.
Engineer: "Reject the reversal ___." | workaround | The workaround fails to preserve the required identifier during interaction.'''))

BOOK['units'].append(unit(
    title='Discussing cultural adaptation without stereotypes', scene='The victory gesture reads as a taunt to some testers',
    skill='Present cultural feedback as scoped evidence and compare adaptations against the intended player experience.',
    brief='In a fictional cooperative game tutorial, a character celebrates teamwork with a hand gesture. Four of six target-locale reviewers interpret it as taunting another player; two do not. The narrative brief requires encouragement, not humiliation. The team has an approved neutral celebration animation available, but replacing the asset still needs product review. Tester Inez must describe the observed interpretation without claiming every person in the locale reacts identically.',
    cast='Inez | Culturalization tester\nMason | Narrative designer',
    culture=('Report audience evidence, not national character', 'A review panel can identify a risk without representing every member of a culture. Explain the intended effect, the observed interpretation, and the scope of the evidence.'),
    a='''What is the intended narrative effect? | Encourage teamwork | Humiliate another player | Teach a payment rule | Signal a game crash | The brief explicitly defines encouragement as the intended effect.
What does the review establish? | Four of six reviewers read the gesture as taunting | Everyone in the locale is offended | No reviewer noticed a problem | The product change is already approved | The supplied evidence is the stated panel result, not a universal cultural claim.
What alternative is available for review? | An approved neutral celebration asset | Deleting the whole tutorial without review | A new untested insult | An automatic global ban on gestures | The case supplies a neutral asset while retaining the product-review requirement.''',
    vocabulary='''culturalization | Adaptation of content with attention to cultural context and interpretation. | review culturalization findings
cultural nuance | Context-dependent meaning or association relevant to an audience. | explain the cultural nuance
audience segment | Defined group within the intended audience. | identify the audience segment
target market | Market for which a product version is intended. | specify the target market
pragmatic meaning | Meaning conveyed through use and context beyond literal words. | explain pragmatic meaning
register | Level or style of language appropriate to a situation. | match the register
tone of voice | Consistent manner in which a product or character communicates. | preserve the tone of voice
transcreation | Creative adaptation preserving intended effect rather than literal wording. | evaluate transcreation
narrative intent | Purpose or effect intended by a story element. | preserve narrative intent
character voice | Distinctive manner of speech associated with a fictional character. | maintain character voice
sensitivity review | Review of potentially harmful or inappropriate audience implications. | request sensitivity review
cultural reference | Element relying on shared contextual knowledge. | explain the cultural reference
idiomatic expression | Phrase whose natural meaning may not follow word-for-word translation. | review the idiomatic expression
literal rendering | Translation closely following surface wording rather than contextual effect. | avoid misleading literal rendering
reviewer sample | Group of reviewers whose observations provide the stated evidence. | describe the reviewer sample
interpretation risk | Possibility that content conveys an unintended meaning to users. | document interpretation risk
asset substitution | Replacement of a visual or audio resource with another. | propose asset substitution
content approval | Authorization for specified product content. | record content approval''',
    precision='Four of six reviewers interpreting the gesture as a taunt is a scoped finding. It supports review of an encouragement mismatch, not a claim about every person in the locale.',
    precision_extra='A proposed adaptation should preserve the actual narrative purpose and go through the relevant review. Tester preference alone is not product approval.',
    phrases='''State the evidence | Four of the six reviewers read this as a taunt.
Avoid universals | I am describing this panel, not every player in the market.
Connect the intent | The scene is meant to encourage cooperation.
Explain the effect | The gesture can make the character seem to mock a teammate.
Compare alternatives | The neutral celebration preserves the intended positive response.
Separate preference | This is an interpretation risk, not merely my preferred animation.
Request review | Can narrative and product review the scoped substitution?
Preserve the record | Keep the original finding and the approved replacement decision linked.''',
    notes='''Can imply versus always means | Can imply identifies a possible contextual reading; always means makes a much stronger universal claim.
Adapt versus censor | Adapt describes a content change for an intended effect without presuming its ethical or editorial judgment.
Sample versus population | A reviewer sample provides limited evidence and should not be described as every possible user.''',
    d='''Which report preserves the evidence accurately? | Four of six reviewers interpreted the gesture as taunting | This nationality dislikes every gesture | Every player will abandon the game | The animation is objectively illegal everywhere | The accurate report states the actual sample result without unsupported universal or legal claims.
What makes the finding relevant to the scene? | Taunting conflicts with the encouragement brief | The tester prefers a different color | The file name is long | The English dialogue has ten words | The observed interpretation conflicts with the supplied narrative purpose.
Which comparison should guide the alternative review? | Whether the neutral asset preserves encouragement | Whether all reviewers share a nationality | Whether the new asset is larger | Whether the ticket can close without testing | The substitution needs to preserve the intended effect in the actual product context.
What remains necessary before reporting implementation complete? | Product review, implementation, and verification | A tester suggestion alone | Deleting the panel result | Assuming available means deployed | An available alternative is not evidence that the change has been authorized and verified.''',
    dialogue='''Mason | The report says the celebration may read as a taunt. Are you saying players in this market always interpret it that way?
Inez | No. The [[reviewer sample::The reviewer sample is the six people who supplied the stated observations, not every member of the target audience.]] was six people, and four gave that interpretation. Two did not.
Mason | That is more specific than the headline I heard. What does the interpretation change in the tutorial?
Inez | It conflicts with the [[narrative intent::Narrative intent is the scene's stated purpose of encouraging cooperation, which differs from humiliating or mocking a teammate.]]. The character is meant to encourage teamwork, not mock another player.
Mason | The animation contains no spoken insult, so I initially treated it as outside the language review.
Inez | Its [[pragmatic meaning::Pragmatic meaning includes the effect conveyed in context, so a gesture can communicate a taunt even without an explicitly insulting line.]] comes from the scene and gesture together, not only the subtitle.
Mason | Can you describe the risk without turning the observation into a fixed rule about the whole culture?
Inez | Yes. I will state the [[interpretation risk::Interpretation risk identifies a possible unintended audience reading supported by the panel, without claiming that every user must respond identically.]] and the exact panel result, with the tutorial context attached.
Mason | We have a neutral celebration animation that was already approved as an asset. It might preserve the positive response.
Inez | That is a concrete [[asset substitution::Asset substitution replaces the relevant resource with an available alternative, but its use in this scene still requires the specified product review.]] to review. Availability does not by itself approve replacing it in this scene.
Mason | Narrative should compare the alternatives and check whether the character still sounds and behaves like the same person.
Inez | Exactly. Preserve the [[character voice::Character voice is the distinctive communication style of the fictional character, which should remain coherent when content is adapted.]] rather than flattening every localized moment into the same generic response.
Mason | We may also need a different line if the new animation changes the timing or emotional emphasis.
Inez | Then review the [[tone of voice::Tone of voice concerns how the character or product communicates, including emotional emphasis rather than only literal word equivalence.]] with the target-language text and the actual animation together.
Mason | Would you call this transcreation, or is it simply correcting a mistranslated word?
Inez | It is closer to [[transcreation::Transcreation adapts an expression or creative element to preserve its intended effect, rather than limiting the task to word-for-word substitution.]] because we are preserving an intended effect across contexts, not replacing one misspelled word.
Mason | I will bring the panel evidence and the alternative to product and narrative review without claiming we already have a final decision.
Inez | Keep the [[content approval::Content approval is the actual authorization for the specified change, which is separate from the tester's finding or the existence of an alternative asset.]] linked to the finding so later reviewers know exactly what was authorized.
Mason | After implementation, we can review the complete scene again rather than judge the asset in isolation.
Inez | Good. That [[sensitivity review::Sensitivity review checks the relevant audience implications in context and should retain the limits of the evidence rather than asserting universal cultural reactions.]] should retain the sample limits and check whether the adaptation achieves the intended encouragement.''',
    rehearsal=['Read the corrected exchange and stress four of six, may, and intended effect.', 'Switch roles and compare the two supplied animations using only the narrative brief and panel result.'],
    transfer_title='A panel result became a universal claim', transfer_setup='Four of six reviewers interpret a gesture as a taunt. The scene is intended to encourage teamwork.',
    transfer='''Tester: "Four of six reviewers perceived a ___." | taunt | The supplied panel result identifies taunting as the reported interpretation.
Designer: "The intended effect is ___." | encouragement | The narrative brief explicitly requires a positive teamwork response.
Tester: "Our evidence comes from a reviewer ___." | sample | Six reviewers are a limited observed group, not the entire audience.
Designer: "Avoid a ___ claim about every player." | universal | The supplied evidence does not establish that every player shares the interpretation.'''))

BOOK['units'].append(unit(
    title='Reporting VR subtitle and audio mismatches', scene='The caption ends before the localized line does',
    skill='Explain timing and speaker attribution in an interactive scene without treating a recording as a static text resource.',
    brief='In a fictional VR training scene, the localized spoken line lasts 4.2 seconds. Its subtitle uses the old 2.4-second end cue and disappears 1.8 seconds before the speech ends. The voice belongs to instructor Mara, who is behind the learner, but the subtitle labels another character. Tester Jae and audio implementer Priya must separate timing, speaker attribution, and in-headset readability. No universal reading-speed limit or comfort threshold is supplied.',
    cast='Jae | Localization QA tester\nPriya | Audio implementer',
    culture=('Report what the learner experiences', 'An asset can be correct in a file viewer but wrong during head movement or branching playback. Include the actual scene trigger and distinguish observed usability from unmeasured assumptions.'),
    a='''How early does the subtitle disappear? | 1.8 seconds before the speech ends | 4.2 seconds after speech ends | 2.4 seconds after speech begins and ends together | Exactly zero seconds early | The difference between the 4.2-second line and 2.4-second end cue is 1.8 seconds.
Who is the actual speaker? | Mara | The incorrectly labeled other character | The tester | An unidentified narrator by default | The brief identifies instructor Mara as the voice heard behind the learner.
What remains a separate check? | In-headset readability | Only whether the audio file exists | Whether the English filename is short | A universal threshold invented from the numbers | The case requires a real headset check and supplies no universal usability threshold.''',
    vocabulary='''voice-over | Recorded speech used within a media or interactive experience. | review the localized voice-over
subtitle cue | Timed instruction controlling a subtitle's display. | inspect the subtitle cue
cue-in | Time at which a subtitle or media event begins. | verify the cue-in
cue-out | Time at which a subtitle or media event ends. | correct the cue-out
timecode | Time reference identifying a point in media. | record the timecode
speaker attribution | Identification of who is speaking. | verify speaker attribution
off-screen speaker | Speaker outside the current visible scene or view. | identify the off-screen speaker
spatial audio | Sound presented with directional or positional information. | test spatial audio
head-locked display | Display element that remains positioned relative to the viewer's head. | review the head-locked display
world-locked display | Display element anchored to the virtual environment. | test the world-locked display
field of view | Portion of the environment visible to the viewer. | check the field of view
occlusion | Blocking of content by another object or layer. | report subtitle occlusion
reading speed | Rate needed to read displayed text within its available duration. | evaluate reading speed
speaker label | Text identifying the source of a spoken line. | correct the speaker label
audio-text mismatch | Inconsistency between recorded speech and displayed text. | report an audio-text mismatch
branching dialogue | Conversation with different paths triggered by choices or state. | test branching dialogue
subtitle segmentation | Division of a line into displayed subtitle units. | review subtitle segmentation
closed caption | Optional text conveying speech and relevant non-speech audio information. | verify closed captions''',
    precision='The early disappearance is 4.2 minus 2.4, or 1.8 seconds. Correcting that timing does not automatically correct the wrong speaker label or establish headset readability.',
    precision_extra='Subtitles and captions can overlap in product terminology, but accessibility requirements may include speaker and non-speech information. Use the actual specification; do not invent a universal words-per-second or comfort rule.',
    phrases='''Locate the timing | The cue-out still uses the old 2.4-second endpoint.
State the difference | The subtitle disappears 1.8 seconds before the localized line ends.
Identify the speaker | This voice belongs to Mara, behind the learner.
Separate the defects | Timing and speaker attribution need separate verification.
Use the real environment | The desktop preview does not establish in-headset readability.
Check the trigger | This happens on the retry branch after the learner selects help.
Preserve full meaning | Segment the line without dropping the instruction.
Scope the result | The tested headset and branch passed; other paths remain in the test plan.''',
    notes='''Lasts versus ends at | Lasts gives duration; ends at gives a point on a specified timeline.
Behind versus invisible | Behind describes a spatial relation; invisible may have a different rendering cause.
Synchronized versus readable | Synchronized concerns timing; readable also depends on text, placement, size, and viewing conditions.''',
    d='''Which calculation describes the supplied timing defect? | 4.2 minus 2.4 equals 1.8 seconds early | 4.2 plus 2.4 equals 1.8 seconds | The subtitle is always 4.2 seconds late | No comparison is possible | The supplied line duration and old cue endpoint share the described start, leaving a 1.8-second gap.
Which fix addresses attribution? | Label the line with Mara's identity | Extend the duration only | Lower the audio volume | Reverse the subtitle text | The wrong character label requires a speaker-identity correction, separate from duration.
Why test in the headset? | Viewing direction and placement affect the experienced result | A desktop screenshot proves every VR state | Headsets cannot display text | Localized lines have universal fixed timing | The actual viewing environment adds conditions not established by a flat preview.
What should not be claimed from this brief? | A universal reading-speed limit | A 1.8-second early disappearance | The need to correct the speaker label | The presence of an off-screen speaker | The scenario explicitly supplies no universal readability or comfort threshold.''',
    dialogue='''Priya | The localized recording plays correctly in the audio editor. What is the problem in the headset scene?
Jae | The [[cue-out::The cue-out still ends the subtitle at the old 2.4-second point even though the localized line lasts 4.2 seconds from the same start.]] still uses the old two-point-four-second endpoint. The new line lasts four-point-two seconds.
Priya | So the subtitle disappears one-point-eight seconds before the speaker finishes, rather than staying with the complete instruction.
Jae | Correct. I captured the [[timecode::The timecode identifies the observed media position and lets the implementer compare the subtitle endpoint with the actual localized recording.]] and scene trigger so you can compare the same playback event.
Priya | I can update the timing from the localized asset. Did you notice anything else that should be tracked separately?
Jae | The [[speaker label::The speaker label names the wrong character, which requires an identity correction rather than only a longer subtitle duration.]] names another character. The voice is Mara, the instructor behind the learner.
Priya | The label may have been copied from the previous branch. Extending the cue would leave that wrong identity visible for longer.
Jae | Exactly. [[Speaker attribution::Speaker attribution tells the learner who is speaking and must be checked independently from whether the subtitle appears for the right duration.]] is a separate finding, especially when the learner cannot see the person speaking.
Priya | I will verify the branch mapping and the recorded asset identifier before changing the label.
Jae | Good. The [[off-screen speaker::The off-screen speaker is outside the learner's current view, making clear attribution useful rather than assuming visual recognition of the character.]] is behind the learner at this moment, not a new narrator.
Priya | The desktop preview shows the subtitle clearly after I adjust the endpoint. Do we still need another headset pass?
Jae | Yes. The [[field of view::The field of view and actual viewing direction affect what the learner can see, so a desktop preview does not establish the in-headset result.]] and viewing direction change the experienced placement.
Priya | We should inspect whether the panel stays visible and whether objects obscure it when the learner turns.
Jae | Record any [[occlusion::Occlusion occurs when another object or layer blocks the subtitle, which is a separate presentation issue from correct text and timing.]] separately from the timing fix. A complete line is not useful if it is hidden.
Priya | The localized sentence is also longer. We may need a better division into subtitle units rather than forcing it into one block.
Jae | Review the [[subtitle segmentation::Subtitle segmentation divides the line into readable units while preserving the full instruction, rather than deleting content to fit an old timing pattern.]] with the language reviewer and preserve the whole instruction.
Priya | We will use the product's actual readability requirements instead of declaring a universal rate from this one recording.
Jae | Exactly. [[Reading speed::Reading speed depends on the displayed text and available duration within the actual usability requirements, which this case does not replace with a universal threshold.]] needs the actual text, duration, and viewing conditions.
Priya | I will attach the revised package with both the cue and speaker mapping changes for the retry path.
Jae | Then I will retest that [[branching dialogue::Branching dialogue can use different assets and mappings on different paths, so verification must identify the path actually exercised.]] path in the headset and report the tested scope without marking every other path passed.''',
    rehearsal=['Read the corrected exchange and state the 4.2 minus 2.4 calculation aloud.', 'Switch roles and distinguish timing, speaker attribution, and in-headset readability using the printed facts.'],
    transfer_title='The timing passed but the label is still wrong', transfer_setup='The subtitle now lasts the full 4.2 seconds. The label still names someone other than Mara.',
    transfer='''Implementer: "The timing now covers the full ___." | line | The supplied update keeps the subtitle visible through the full spoken line.
Tester: "The actual speaker is ___." | Mara | The case explicitly identifies Mara as the recorded speaker.
Implementer: "The speaker label remains ___." | incorrect | The displayed label still names another character after the timing change.
Tester: "Keep attribution open for ___." | correction | A successful timing change does not resolve the remaining identity error.'''))

BOOK['units'].append(unit(
    title='Negotiating localization release decisions', scene='Merged is not verified in the release package',
    skill='Separate impact, scheduling priority, fix status, and locale-specific verification during release triage.',
    brief='A fictional release candidate contains a mistranslated destructive-action button: it reads Keep files but actually deletes them. The corrected resource has been merged, but the packaged release candidate has not been rebuilt or retested. A second ticket concerns optional punctuation in a help paragraph. Tester Ana and producer Ben need impact-based triage, an explicit affected-locale scope, and verification of the actual release package. No tester has authority to waive the release criteria.',
    cast='Ana | Localization QA lead\nBen | Release producer',
    culture=('Make pushback specific and proportionate', 'Describe the user consequence and the missing evidence rather than saying everything is a blocker. Separate a serious meaning reversal from a stylistic preference and name who can decide release exceptions.'),
    a='''What is the serious user consequence? | A button says Keep files but deletes them | A help paragraph contains optional punctuation | A build number has four digits | A translation sheet has a comment | The button reverses the meaning of a destructive action and can mislead users.
What has actually happened to the correction? | It has been merged into the resource source | The release package has passed retesting | Every locale has been approved | The release criteria were waived | The brief states only the merge, not a rebuilt or verified release candidate.
Who can waive the criteria in this case? | No authority is supplied for the tester | Any person who closes a ticket | The translator automatically | The person who takes a screenshot | The scenario expressly says the tester has no waiver authority.''',
    vocabulary='''release candidate | Package proposed for final release validation. | test the release candidate
string freeze | Controlled point after which text changes follow an agreed process. | manage the string freeze
late string change | Text modification introduced after the usual content cutoff. | assess a late string change
severity | Degree of impact caused by a defect. | assign defect severity
priority | Relative urgency or scheduling order for action. | agree fixing priority
release blocker | Issue preventing release under the actual release criteria. | identify a release blocker
waiver | Authorized exception to a stated requirement. | request a documented waiver
risk acceptance | Explicit authorized decision to proceed with a stated residual risk. | record risk acceptance
fix verification | Check that the implemented correction resolves the reported issue. | complete fix verification
regression scope | Set of related behavior checked for unintended effects. | define regression scope
merge status | State of a change entering the relevant source branch. | report merge status
package manifest | Record identifying the resources included in a built package. | inspect the package manifest
locale coverage | Supported or tested locale scope, as explicitly defined. | report tested locale coverage
test evidence | Recorded results supporting a verification claim. | attach test evidence
linguistic sign-off | Documented language approval for a defined scope. | obtain linguistic sign-off
known issue | Documented unresolved problem with stated status and impact. | maintain the known-issue record
rollback plan | Defined approach for restoring an earlier acceptable state if needed. | review the rollback plan
release notes | Communication describing the delivered changes and known limitations. | prepare accurate release notes''',
    precision='The merged resource is not proof that the release candidate contains the fix. Verify the packaged button behavior and wording before claiming the affected locale passed.',
    precision_extra='Severity describes impact; priority describes scheduling. Release blocking and exceptions depend on the actual agreed criteria and decision authority.',
    phrases='''State the consequence | The label promises to keep files, but the action deletes them.
Separate the issues | That meaning reversal is not equivalent to optional punctuation.
Report the actual state | The resource is merged; package verification is still pending.
Request evidence | Which release candidate contains the corrected resource?
Limit sign-off | My sign-off covers only the tested build and locale.
Name authority | Any exception needs the designated release decision owner.
Define regression | Retest the destructive action and related confirmation flow.
Close precisely | Mark verified only after the actual package passes the stated checks.''',
    notes='''Severe versus urgent | Severe describes impact; urgent describes timing pressure, and neither alone states the release authority.
Merged versus shipped | Merged concerns source integration; shipped concerns the actual delivered package.
Accepted risk versus fixed | Accepted risk remains a known risk under an authorized decision; fixed claims the defect was corrected.''',
    d='''Which triage comparison is justified? | Meaning reversal and optional punctuation have different user impacts | Both are identical because both involve text | Punctuation is automatically more dangerous | Every linguistic issue is harmless | The destructive-action label can mislead users in a materially different way from optional punctuation.
Which claim overstates the fix status? | The release candidate is verified because the resource was merged | The source change has been merged | The package still needs rebuilding | The affected locale needs retesting | Merge status does not establish what the package contains or how it behaves.
What should linguistic sign-off identify? | Build, locale, and verified scope | Only the reviewer's first name | Every future release automatically | A guarantee that no bug can exist | A scoped approval must identify the actual material and conditions reviewed.
What distinguishes a waiver from a correction? | A waiver accepts an exception without making the defect disappear | A waiver rewrites the resource automatically | A waiver proves every test passed | A waiver is the same as a screenshot | An authorized exception changes the release decision, not the underlying observed defect.''',
    dialogue='''Ben | The release meeting is in an hour. The translation change is merged, so can we mark the deletion-label ticket verified?
Ana | Not yet. The [[release candidate::The release candidate is the actual package being evaluated, which has not yet been rebuilt or retested with the corrected resource.]] has not been rebuilt or retested. We need evidence from the package we intend to release.
Ben | The source change is small. It replaces the phrase Keep files with the correct destructive-action wording.
Ana | The [[severity::Severity concerns the user impact, here a label promising preservation while the action deletes files, rather than the size of the text edit.]] comes from the consequence, not the number of words changed.
Ben | We also have a punctuation preference in help. I do not want every language ticket presented as equally critical.
Ana | Agreed. [[Priority::Priority concerns the relative order and urgency of work and can distinguish the meaning reversal from an optional punctuation change.]] should reflect impact and the actual schedule. These two findings are not equivalent.
Ben | What do you need from engineering to establish whether the next candidate includes the corrected resource?
Ana | A build identifier and the [[package manifest::The package manifest identifies what resources the built package contains, helping verify inclusion instead of inferring it from source merge status.]], followed by a direct check of the affected flow.
Ben | The merge record can tell us when the source changed, but not prove the package was created from that version.
Ana | Exactly. [[Merge status::Merge status describes source integration and must remain separate from the actual built package and its verification result.]] is one step in the chain, not the final test result.
Ben | Once the package is ready, can you retest just the label and leave the rest of the flow alone?
Ana | The [[regression scope::Regression scope identifies related behavior that should be checked, here the destructive action and its confirmation flow rather than the label in isolation.]] should include the destructive action and confirmation flow, because wording and behavior must agree.
Ben | We can prioritize that check and keep the optional punctuation decision separate from the release-critical discussion.
Ana | Good. I will attach [[test evidence::Test evidence records the actual conditions and results supporting verification, rather than substituting a verbal assurance that the change is small.]] with the locale, package, steps, and observed result.
Ben | If the package cannot be retested before the meeting, can you accept the remaining risk on behalf of QA?
Ana | I do not have that [[waiver::A waiver is an authorized exception to a requirement, and the case gives the tester no authority to grant one.]] authority. The designated decision owner needs the actual impact and missing evidence.
Ben | Understood. We should not describe an accepted exception as though the defect itself had been fixed.
Ana | Correct. [[Risk acceptance::Risk acceptance is an explicit authorized decision about remaining risk, not a technical correction or proof that a failed condition has disappeared.]] must remain distinct from verified correction.
Ben | Your report can say the resource is merged, the candidate needs verification, and the punctuation issue has its own status.
Ana | Yes. My [[linguistic sign-off::Linguistic sign-off applies to a defined reviewed scope, not every locale or package merely because one source resource was edited.]] will name the tested build and locale rather than imply approval of untested packages.''',
    rehearsal=['Read the corrected exchange and stress merged, packaged, verified, and accepted.', 'Switch roles and deliver the printed release status without claiming a waiver or untested locale approval.'],
    transfer_title='The source fix is not yet in a tested package', transfer_setup='The correction is merged. A new release candidate has not been tested. The tester cannot waive the release criteria.',
    transfer='''Producer: "The resource correction is ___." | merged | The source change has entered the relevant branch in the supplied case.
Tester: "Package verification remains ___." | pending | No new release-candidate test result is supplied in this case.
Producer: "An exception requires the designated decision ___." | owner | The tester lacks waiver authority, so the actual authorized role must decide.
Tester: "Do not describe accepted risk as ___." | fixed | An exception decision does not itself correct the underlying defect.'''))
