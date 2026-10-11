"""Additional original marketing conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A global slogan that does not travel',
        skill='Explain a localization problem and negotiate a usable creative brief.',
        setup='A software campaign uses the slogan "Hit the ground running." The regional team says a literal translation sounds physical rather than helpful. The launch date is fixed, but the headline is not. No regional performance results exist yet.',
        cast='Nadia|Regional marketing lead\nJon|Global creative director',
        dialogue='''Jon|Your team rejected the headline. Is the problem the translation, or do you want a different campaign altogether?
Nadia|The promise works. The idiom does not. We need [[transcreation::Transcreation adapts the creative idea and intended effect rather than translating each word literally.]], not a word-for-word version of an English sporting image.
Jon|What would stay consistent? I need a recognizable campaign across the launch markets, not six unrelated propositions.
Nadia|Keep the first-day setup benefit and product name. Let us change the headline and the example beneath it.
Jon|The example currently mentions an American holiday weekend. I suppose that will need attention too.
Nadia|Yes. I will flag those [[cultural references::The holiday is a culturally specific reference that may not carry the same meaning elsewhere.]] in the brief, with an explanation of the intended effect.
Jon|Can you give the regional writer a direction without prescribing the final line?
Nadia|Something like "Start your first project with a clear plan." That is a direction, not our proposed final headline.
Jon|It sounds less playful than the original. Are we abandoning the brand's personality?
Nadia|No. The [[tone of voice::Tone of voice describes how the brand sounds; changing an idiom does not require abandoning that personality.]] can remain warm and confident without using an unfamiliar metaphor.
Jon|Send two options. Will I receive English versions so I can understand what changed?
Nadia|Yes, with a [[back-translation::A back-translation renders the adapted text back into the original language for review of meaning.]] and a note explaining the nuance each English rendering loses.
Jon|That should help. I do not want to approve a smooth English explanation that conceals an awkward regional line.
Nadia|A native-speaking reviewer will check the actual copy. Your review can focus on whether the benefit and boundaries are intact.
Jon|The design has room for forty characters in that slot. Please make that constraint visible before writing starts.
Nadia|I will include the [[character limit::The character limit is the specific layout constraint the writer must receive before producing options.]], along with screenshots of the narrow mobile version.
Jon|Do you expect this adaptation to improve conversion? The launch team will ask why we changed a tested global line.
Nadia|We expect clearer meaning. We have no regional results yet, so I will not attach a conversion claim to it.
Jon|All right. Send the options tomorrow morning. I will review the proposition while your team checks the naturalness.
Nadia|Then we will record the chosen [[localized asset::The localized asset is the market-specific deliverable, distinct from its explanatory back-translation.]] and its reviewer in the launch folder.''',
        transfer_title='A price example in the wrong currency',
        transfer_setup='A Canadian campaign uses a US-dollar price example. The approved benefit is unchanged, but local pricing has not been supplied.',
        transfer='''Regional lead: The benefit can stay, but the price needs ___.|localization|Localization adapts market-specific details such as the currency and applicable price.
Creative lead: Do not turn a currency conversion into an approved ___.|offer|An arithmetic conversion does not establish the commercial offer available locally.
Regional lead: I will request the actual local price from the pricing ___.|owner|The responsible pricing owner must supply the commercial detail still missing.
Creative lead: Keep the pricing line out of the final asset until that detail is ___.|confirmed|The price is currently missing, so confirmation must precede its publication.'''),
    scenario(
        title='The agency delivered impressions, but not the agreed placements',
        skill='Distinguish delivery volume from inventory quality and negotiate a remedy.',
        setup='An agency booked 500,000 impressions on an agreed publisher list. Its report shows 520,000, including 80,000 outside that list. The client has not accepted a remedy. The contract and placement report are available for review.',
        cast='Leah|Media manager\nMarco|Agency account director',
        dialogue='''Leah|Your summary says we overdelivered. The placement breakdown shows eighty thousand impressions on publishers outside the agreed list.
Marco|I see them. The total is higher than the booking, but that does not settle whether we met the [[insertion order::The insertion order records the media booking terms against which the placement delivery must be assessed.]].
Leah|Exactly. We bought particular placements. How many impressions can you reconcile to the approved publishers?
Marco|Four hundred forty thousand, assuming the current report is complete. I will check the raw delivery records before treating that as final.
Leah|That would leave sixty thousand against the five-hundred-thousand booking. Please do not offset them with the excluded inventory.
Marco|Understood. I will separate approved [[inventory::Inventory refers to the advertising placements available or supplied, not simply the total number of impressions.]] from the off-list placements in the revised report.
Leah|How did those publishers enter the campaign? The list was attached to the booking.
Marco|The buying team needs to trace that. I will not guess at a platform error before we inspect the settings and change history.
Leah|We also requested a viewability report. An impression appearing in a delivery count does not tell us whether it was viewable.
Marco|I will supply the [[viewability::Viewability is a separate measurement of whether an impression met specified opportunity-to-be-seen criteria.]] figures with their measurement basis, separately from the publisher-list reconciliation.
Leah|Thank you. I want those two questions kept separate in the client update.
Marco|For the shortfall, would you consider a [[makegood::A makegood is replacement media offered to remedy a delivery problem; it still needs agreement.]] on the approved publishers, subject to availability and your acceptance?
Leah|Possibly, but the promotion ends Friday. Extra impressions next month may have little value to us.
Marco|Then timing has to be part of the remedy. I can price the available replacement placements and discuss a credit internally.
Leah|Do not book anything yet. Send both options with dates and any change in format.
Marco|I will make the proposed [[flight dates::Flight dates specify when the advertising will run, which matters because this promotion ends Friday.]] explicit so the replacement cannot drift beyond the promotion unnoticed.
Leah|And show whether accepting an option would resolve the entire dispute or only the delivery shortfall.
Marco|Yes. Any [[credit note::A credit note records an agreed reduction to the amount billed; it is not automatically created by offering replacement media.]] will follow the agreed commercial resolution, not an assumption in this call.
Leah|Please send the corrected delivery table first. I need something reliable for this afternoon's review.
Marco|You will have it by two, with any unresolved reconciliation clearly marked and no new placements booked.''',
        transfer_title='An event campaign ends before the replacement run',
        transfer_setup='A campaign is 20,000 impressions short. The agency offers replacement delivery after the advertised event has finished. The client has not agreed.',
        transfer='''Client: Extra impressions after the event do not solve our timing ___.|problem|The advertised event has ended, so later delivery may not serve the original purpose.
Agency: I will label the replacement as a proposal, not an accepted ___.|remedy|The client has not agreed to the proposed replacement delivery.
Client: Check the booking terms before promising an automatic ___.|refund|The supplied facts do not establish an automatic contractual right to a refund.
Agency: We will document the resolution once both sides ___.|agree|A resolution must reflect agreement rather than the agency's unilateral proposal.'''),
    scenario(
        title='The landing page works with a mouse, but not a keyboard',
        skill='Give specific accessibility feedback and coordinate a practical release check.',
        setup='A landing-page review finds an image-only offer, an unlabeled icon link, and a signup form whose keyboard focus disappears. The campaign designer and web producer must assign fixes. This is a focused review, not certification of the entire website.',
        cast='Dev|Campaign designer\nRenee|Web producer',
        dialogue='''Dev|The desktop preview looks good. You left three accessibility comments. Which one blocks the signup journey?
Renee|The [[focus indicator::The focus indicator shows which interactive element currently receives keyboard input; its disappearance obstructs keyboard navigation.]] disappears at the form. I cannot tell which field I am entering without using the mouse.
Dev|I changed the field styling yesterday. I may have removed the outline with the default border.
Renee|Please restore a visible state and test it through the whole form. The problem is not just the first field.
Dev|What about the offer image? Its text is already visible in the artwork.
Renee|We need an appropriate [[text alternative::A text alternative makes the image's meaningful information available when the image itself cannot be used.]]. Better still, put the offer in real page text where people can resize and access it.
Dev|I can keep the illustration and move the offer outside it. Does the illustration still need a full description?
Renee|That depends on its purpose. If it adds no information beyond the nearby text, treat it as decorative rather than repeating everything.
Dev|The small arrow beside the offer links to the terms. I called it "blue arrow" in the image description.
Renee|For that [[functional image::A functional image acts as a control or link, so its alternative should identify the action or destination.]], describe the destination. "Offer terms" is useful; the arrow's color does not explain the link.
Dev|Understood. I will also put visible wording beside it so the destination is not a guessing game.
Renee|Good. The button and helper text need a [[contrast check::A contrast check examines whether foreground and background colors provide sufficient visual distinction for their intended use.]] after your new colors are applied.
Dev|Could we approve this from the automated report if all three warnings disappear?
Renee|No. Run the report, then test the journey manually. A clean scan does not establish that every interaction is accessible.
Dev|I will test keyboard navigation. Can you check the labels with the team's screen-reader setup?
Renee|Yes, including the [[error message::The error message must communicate a failed input clearly; a border color alone does not explain the problem.]] after an invalid email address. A red border alone is not enough.
Dev|I will give you a test link with the form connected to our test list, not the live campaign list.
Renee|Thanks. We can verify the [[accessible name::The accessible name identifies a control to assistive technology and should accurately express its purpose.]] of each control and the confirmation state after submission.
Dev|I will fix the layout and focus styles this morning. Please keep the review comments open until you recheck them.
Renee|Agreed. We will record exactly what passed, without labeling this limited check a full-site accessibility certification.''',
        transfer_title='A decorative photo beside complete text',
        transfer_setup='An article includes a decorative office photo. The offer and all instructions are already in readable page text. A separate icon is the only link to the booking page.',
        transfer='''Designer: The office photo adds no new information; its alternative can be ___.|empty|A decorative image can have an empty alternative rather than repeat nearby information.
Producer: The booking icon is different because it has a ___.|function|The icon operates as a link and is therefore not merely decorative.
Designer: Its accessible label should identify the booking ___.|destination|A useful label tells the user where the functional image's link leads.
Producer: Test that link using a keyboard before calling the change ___.|complete|Visual appearance alone does not verify that the link is usable by keyboard.'''),
]
