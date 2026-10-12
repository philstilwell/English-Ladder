"""Additional localization conversations on regional formats, input methods, and text boundaries."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Changing the interface language does not convert the currency',
    skill='Distinguish language, regional presentation, underlying values, and transaction currency.',
    setup='A fictional travel app switches its interface language from English to French. An order remains denominated in USD 120. No currency conversion is requested or performed, but a display change incorrectly replaces the dollar label with EUR while leaving 120 unchanged. A separate date label reads 03/04/2026 without specifying the intended date. Tester Claire and engineer Dev must preserve the actual currency and request an unambiguous date reference.',
    cast='Claire | Localization tester\nDev | Product engineer',
    reference=('Microsoft. Globalize date, time, and number formats.', 'https://learn.microsoft.com/en-us/windows/apps/design/globalizing/use-patterns-to-format-dates-and-times'),
    dialogue='''Dev | Switching to French changes the button text correctly. The price now says one hundred twenty euros, which seems appropriate for the language.
Claire | The order is still denominated in US dollars. Changing the interface language does not perform a [[currency conversion::Currency conversion changes an amount between currencies under an actual conversion process, which the case explicitly says has not occurred.]].
Dev | Then we changed the currency label without changing the actual transaction, creating a false statement about the price.
Claire | Exactly. Preserve the [[currency code::The currency code identifies USD as the transaction currency and must not be replaced merely because the interface language changed.]] from the order. French-language presentation can still describe a US-dollar amount.
Dev | We need to separate language selection from the transaction currency instead of deriving one automatically from the other.
Claire | Yes. The [[regional format::Regional format affects presentation conventions and should not silently alter the underlying currency or economic amount.]] may change how an amount is presented, but not what currency the customer is charged.
Dev | I will compare the underlying value and currency with the displayed result before and after the language switch.
Claire | Good. That separates a formatting defect from an actual change in the transaction data.
Dev | The date label also says zero-three slash zero-four slash twenty-twenty-six. Can you tell me which date the customer will read?
Claire | Not reliably without the [[date interpretation::Date interpretation is ambiguous when a short numeric date lacks a stated ordering convention or an unambiguous underlying reference.]] and expected locale behavior. We need the actual underlying date and product rule.
Dev | I should not assume March fourth or April third based only on my own usual date order.
Claire | Correct. Ask for an [[unambiguous reference::An unambiguous reference establishes the intended date independently of a short display whose month and day order can be read differently.]] before recording an expected result.
Dev | Once the intended date is confirmed, we can test the supported display and input behavior against it.
Claire | Include the input path as well. A screen can display one convention while parsing the customer's entry using another.
Dev | I will record language, regional settings, currency, and date behavior as separate configuration details.
Claire | That makes the [[test environment::The test environment identifies the actual configuration needed to reproduce the result instead of treating a language name as a complete locale or transaction specification.]] reproducible and avoids treating a language name as the whole configuration.
Dev | The currency correction should show the same USD order using the appropriate presentation, not invent an exchange rate.
Claire | Exactly. No conversion is requested in this case, so no converted amount or euro charge should be claimed.
Dev | I will correct the currency mapping and obtain the date reference before building the expected-result comparison.
Claire | Then we can verify both findings against actual data rather than a plausible-looking localized screen.''',
    transfer_title='A French screen still contains a US-dollar order', transfer_setup='The order is USD 120 before and after the language switch. No conversion occurs.',
    transfer='''Tester: "The transaction currency remains ___." | USD | The supplied order retains its US-dollar denomination after the language switch.
Engineer: "The numerical amount remains ___." | 120 | No conversion or other amount change occurs in the case.
Tester: "The interface ___ changes." | language | The supplied change concerns the interface wording rather than the transaction currency.
Engineer: "Do not invent a currency ___." | conversion | The scenario explicitly states that no conversion was requested or performed.'''),
scenario(title='Enter confirms an input candidate instead of sending the message',
    skill='Explain an input-method composition defect without treating every key press as completed text entry.',
    setup='In a fictional support chat, a tester uses a Japanese input method editor. Pressing Enter while selecting a conversion candidate should confirm the candidate in this tested configuration. Instead, the app sends the unfinished message. Engineer Kai and tester Yuna need to document the input method, platform, composition state, and actual event behavior. The case does not prescribe one universal event-order fix for every browser.',
    cast='Yuna | Localization QA tester\nKai | Chat engineer',
    reference=('W3C. UI Events: composition events and input method editors.', 'https://www.w3.org/TR/uievents/'),
    dialogue='''Kai | The ticket says Enter sends the message too early, but Enter is our normal send shortcut. What action did the user intend?
Yuna | In this configuration, the user was confirming a candidate in the [[input method editor::The input method editor mediates composition and candidate selection, so a key can serve an input function before the message is ready to send.]], not asking the chat app to send.
Kai | Then the key press has a different role while text is still being composed.
Yuna | Correct. The [[composition session::The composition session is the active process of building or choosing input text, which must be distinguished from completed message entry.]] had not been handled correctly when the app submitted the message.
Kai | We need the exact platform and input method, because I cannot reproduce this by typing ordinary Latin letters.
Yuna | I recorded those details, the [[candidate selection::Candidate selection is the user's choice among possible input conversions and is distinct from submitting the completed chat message.]], and the sequence that produces the early send.
Kai | A screenshot of the final message would show the damage but not explain the interaction that caused it.
Yuna | Exactly. The recording and [[event trace::The event trace records the observed input and composition events so the engineer can investigate the real sequence in the tested environment.]] show the observed sequence in this environment.
Kai | I should inspect our shortcut handling alongside the composition state rather than assume every Enter means send.
Yuna | Yes. Keep the [[committed text::Committed text is the accepted input result, which differs from an unfinished composition candidate still being selected.]] distinct from the unfinished candidate the user is still selecting.
Kai | We also need to test cancellation and another input path so the fix does not trap people in the composer.
Yuna | Agreed. Follow the actual supported environments; the event ordering and available signals can vary.
Kai | I will not promise that one key-code check solves every input method or browser combination.
Yuna | That is important. We need a tested implementation, not a universal rule inferred from one recording.
Kai | The expected result is that confirming the candidate does not accidentally submit the unfinished chat message.
Yuna | Correct. Then test the normal [[submit action::The submit action is the separate request to send the completed message, which must still work after the composition-related defect is corrected.]] after composition has completed under the product's intended interaction.
Kai | I will attach the updated build with the environment details and the shortcut behavior for retesting.
Yuna | I will repeat candidate confirmation, cancellation, and intentional sending on the supported configurations in the test plan.
Kai | The report can state which combinations passed instead of marking all international input complete.
Yuna | Exactly. The fix should respect the input process while preserving the deliberate send action.''',
    transfer_title='The key was used to confirm a candidate', transfer_setup='In the tested configuration, Enter confirms the selected input candidate. The user has not requested message submission.',
    transfer='''Tester: "The user is confirming a ___." | candidate | The supplied action selects the intended input conversion, not a send command.
Engineer: "The message should not be ___ yet." | submitted | The user has not requested submission in this composition interaction.
Tester: "Record the active input ___." | method | The actual input configuration is necessary to reproduce and investigate the behavior.
Engineer: "Retest intentional sending after composition is ___." | complete | The normal send action still needs verification after input composition finishes.'''),
scenario(title='Counting visible characters correctly',
    skill='Explain a Unicode text-boundary defect using visible content, stored sequences, and the product limit.',
    setup='A fictional profile field promises ten user-perceived characters. It rejects nine simple letters plus one accented letter represented by a base and combining mark, counting that last visible letter twice. Ravi and Morgan must align the counting policy with the promise without stripping accents from names.',
    cast='Ravi | Localization tester\nMorgan | Profile engineer',
    reference=('Unicode. Standard Annex 29: Unicode text segmentation.', 'https://www.unicode.org/reports/tr29/'),
    dialogue='''Morgan | The field rejects this profile value at ten visible characters. Our counter says eleven, so is the tester counting incorrectly?
Ravi | The last visible letter uses a base letter and a [[combining mark::The combining mark joins the base letter in this supplied representation, so two code points can contribute to one user-perceived character.]]. The two counts are measuring different things.
Morgan | Then the stored sequence contains more than one code point for the final letter that the user perceives as one.
Ravi | Exactly. A [[code point::A code point is a Unicode value in the stored sequence and does not necessarily correspond one-to-one with a user-perceived character.]] is not automatically the same as a user-perceived character.
Morgan | We should define the unit behind the product's promised limit before changing the counter.
Ravi | Yes. The current promise concerns [[grapheme clusters::Grapheme clusters provide a text-segmentation model for user-perceived characters, unlike simply counting every code point separately.]] or an explicitly defined equivalent policy, not an unexplained low-level length.
Morgan | We need to use the supported segmentation behavior and test the actual boundary cases instead of inventing a rule from this one name.
Ravi | Correct. The [[text segmentation::Text segmentation identifies appropriate text boundaries under a defined model, which is needed for a limit described in user-perceived characters.]] policy should match the product requirement and actual runtime.
Morgan | Could we just remove accents before counting so the current implementation accepts the value?
Ravi | No. That would alter the person's [[display name::The display name is user content whose meaningful accents must not be stripped merely to hide an implementation mismatch.]] rather than fix the mismatch between the promised limit and the implementation.
Morgan | We should also check deletion and cursor movement so an edit does not leave a detached mark.
Ravi | Yes. The same boundary assumptions can affect interaction even if the initial length check is corrected.
Morgan | Some visually similar text can have different stored representations. Our tests should identify the actual sequence being used.
Ravi | Record the representation and the [[normalization policy::The normalization policy concerns how equivalent text representations are handled and should be explicit rather than silently used to erase meaningful content.]] without assuming that normalization means removing meaningful accents.
Morgan | We can preserve the user's content while applying the actual validated rules for storage and display.
Ravi | Exactly. The expected result is not simply a green counter; the name must remain intact and editable.
Morgan | I will review the limit wording, segmentation implementation, and supported boundary behavior together.
Ravi | I will include the ten-character case and adjacent lengths so the retest checks the limit rather than one isolated example.
Morgan | We should report the exact tested representations and avoid claiming every Unicode sequence is covered.
Ravi | Good. Clear units and scoped evidence will make the fix understandable without turning the name itself into the problem.''',
    transfer_title='The accent must remain part of the name', transfer_setup='The field promises ten user-perceived characters. The supplied ten-character value contains a base-plus-combining-mark representation of its final letter.',
    transfer='''Tester: "The visible value contains ___ user-perceived characters." | ten | The case explicitly supplies a ten-character value under the stated user-facing count.
Engineer: "The last letter includes a combining ___." | mark | The final visible letter is represented by a base character plus a combining mark.
Tester: "Do not strip the ___ to hide the defect." | accent | Removing meaningful name content would not repair the implementation-policy mismatch.
Engineer: "Match the counter to the defined segmentation ___." | policy | The implementation must follow the stated counting unit and validated segmentation behavior.'''),
]
