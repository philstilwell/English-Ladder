"""Original curl, guard-length, and color-assessment conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Length in the way you wear it",
        skill="Distinguish visible curl length, strand thickness, and density when agreeing on a shape.",
        setup="Client Nia wears her hair in its natural curls. Stretched, it reaches below her shoulders; dry and unstretched, it sits at shoulder level. She wants to keep that dry shoulder-length outline and more crown volume. The consultation records fine individual strands and high density. No amount to remove or cutting method is agreed.",
        cast="Nia|Client\nAmir|Stylist",
        dialogue="""Nia|When I say shoulder-length, I mean how it sits when I leave it curly. Last time, the wet length looked right but the dry result felt too short.
Amir|Then let's use your [[dry outline::The dry outline is the visible shoulder-level shape Nia wants to retain, not the longer stretched endpoint.]] as the reference. You want the bottom to stay at shoulder level when worn naturally.
Nia|Exactly. If I pull a section straight, it goes below my shoulders. That's not how I wear it during the day.
Amir|That difference is [[shrinkage::Shrinkage describes the shorter visible length when curls recoil, not missing hair or a measured amount to cut.]]. We need to account for how your curls sit, without assuming every section springs back equally.
Nia|I'd like more height at the top, though. Does that mean losing the length around the bottom?
Amir|Your requested [[crown volume::Crown volume concerns fullness at the upper back of the head, separate from the retained outer length.]] is a separate goal. Let's discuss possible shape changes before deciding how much, if anything, comes off each area.
Nia|People call my hair thick, but the individual hairs feel quite fine. Is that a contradiction?
Amir|No. [[Strand thickness::Strand thickness describes individual hairs; fine strands can occur in a head with many hairs.]] describes each hair. Density describes how much hair grows in an area. Your consultation records fine strands with high density.
Nia|That explains it. I have a lot of hair, but I don't want a heavy product recommendation based just on the word thick.
Amir|Agreed. We'll keep [[density::Density concerns the amount of hair in an area, not the diameter of each strand or a product instruction.]] separate from strand thickness and your styling preferences. Neither description alone chooses a product for you.
Nia|The curls at the front sit differently from the back. Please don't assume the whole head behaves like one section.
Amir|I won't. We can compare the areas in their [[natural fall::Natural fall is how the hair sits without being held stretched, which is the relevant appearance for this request.]] and discuss the shape you actually wear.
Nia|Would it help if I showed you where I want the bottom edge in the mirror?
Amir|Yes. That gives us a shared visual reference. It still doesn't turn shoulder-length into a fixed number of centimeters to remove everywhere.
Nia|Right. I'm asking to keep that edge, not to cut every wet section to the same shoulder line.
Amir|Understood. We haven't agreed on a cutting method or an amount yet. First we'll confirm the shape and the length you want protected.
Nia|And the crown goal is more volume, not straightening. I want to keep wearing the curls.
Amir|That's clear. I'll record natural curls, retained dry shoulder-length outline, and a discussion of crown volume. No straightening service has been requested.
Nia|Please read that back before we start, including the dry-length point. That's the part I don't want lost.
Amir|Certainly. Shoulder-level when dry and unstretched; more crown volume to discuss; fine strands, high density; cutting details still to be agreed.""",
        transfer_title="Protect the unstretched endpoint",
        transfer_setup="A client wants chin-level hair when dry and unstretched, not the collarbone endpoint seen when stretched. Individual hairs are coarse, but density is low. No cutting amount is agreed.",
        transfer="""Client: Keep the dry outline at my ___ .|chin|The selected endpoint is the chin in the dry unstretched state, not the stretched collarbone position.
Stylist: The longer comparison shows the hair ___ .|stretched|The collarbone endpoint belongs to the stretched comparison, not the requested natural outline.
Client: The individual strands are ___ .|coarse|Coarse describes individual strand thickness, not how many hairs grow in an area.
Stylist: The recorded density is ___ .|low|Low density concerns the amount of hair in an area and can coexist with coarse strands.""",
        reference=("Wella Professionals: curl patterns and visible shrinkage", "https://www.wella.com/professional/en-US/blog/hair-care/whats-your-curly-hair-type"),
    ),
    scenario(
        title="A number needs a length",
        skill="Read a tool-specific guard chart and distinguish length left from length removed.",
        setup="For this consultation, the shop's identified hair-clipper chart lists nominal lengths: #1 = 3 mm, #2 = 6 mm, #3 = 10 mm, #4 = 13 mm. Client Pavel first says number two, thinking it means removing 2 mm. He clarifies a preference around 13 mm at the sides. Top, neckline, and beard remain unagreed; no cutting begins.",
        cast="Pavel|Client\nLeah|Barber",
        dialogue="""Pavel|Could you do a number two on the sides? I only want a little off, not a really close cut.
Leah|Let's check what you mean. On this hair-clipper chart, [[number two::Number two corresponds to a nominal 6 mm length on this specified chart, not removal of 2 mm.]] is listed as six millimeters remaining. Were you expecting that length?
Pavel|Oh, no. I thought two meant taking off two millimeters. I'd like the sides much longer than six.
Leah|The chart describes the length [[left::Left means retained after cutting, whereas Pavel initially understood the number as an amount removed.]], not the amount removed. It's worth checking before we choose a guard.
Pavel|About thirteen millimeters sounds nearer what I meant. Which number is that on your chart?
Leah|That's [[number four::The supplied chart assigns 13 mm to number four; the number is not a centimeter measurement.]]. We'll discuss the appearance at that length before treating the number as the whole haircut plan.
Pavel|And number three is ten millimeters? I can see the printed lengths now. They're not counting up one millimeter at a time.
Leah|Correct. Read the stated [[millimeters::The millimeter labels provide the actual nominal lengths; guard numbers are identifiers rather than a one-millimeter scale.]], not just the sequence of numbers. These are the listed nominal lengths for this identified tool system.
Pavel|My beard trimmer has numbers too. Could I use the same number and expect exactly the same result?
Leah|Not automatically. Check that tool's [[guide comb::The guide comb and its own documentation identify the length; another trimmer need not use the same numbering.]] and instructions. A remembered number from another device isn't enough to identify a matching length.
Pavel|So if I come back, I should mention the length as well as the number. That would avoid this mix-up.
Leah|Yes, along with the areas and appearance you liked. Tool settings and the final look still need checking on the actual hair.
Pavel|Does asking for thirteen millimeters at the sides mean you'll cut the top to thirteen as well?
Leah|No. We need a [[separate agreement::A side-length preference does not settle the top, neckline, or beard, which are expressly unagreed.]] about the top. The neckline and your beard haven't been discussed either.
Pavel|Please leave the beard out of today's haircut conversation for now. I haven't decided what I want done with it.
Leah|Understood. No beard work is agreed. We'll finish the haircut consultation without adding that service by assumption.
Pavel|And is thirteen a promise that every single hair will measure exactly thirteen afterward?
Leah|No. It's the chart's nominal length, not a guarantee about every hair. We still need to agree the shape and appropriate professional approach.
Pavel|Then my original number-two request was wrong. Please record the longer side preference and check the remaining details with me.
Leah|I will: around thirteen millimeters at the sides, number four on this chart as our reference, with the rest of the plan still to confirm.""",
        transfer_title="Read another chart entry",
        transfer_setup="Use the same chart: #1 = 3 mm, #2 = 6 mm, #3 = 10 mm, #4 = 13 mm. A client wants approximately 10 mm remaining at the sides. The beard has not been discussed. Interpret the request only; no technique is supplied.",
        transfer="""Client: I want approximately ___ millimeters remaining at the sides.|ten|Ten millimeters is the requested retained length, not the amount removed.
Barber: On this chart, that is guard number ___ .|three|Number three corresponds to 10 mm on the supplied tool-specific chart.
Client: The chart describes length left, not length ___ .|removed|Remaining length and the amount taken off are different measurements.
Barber: Work on the beard is still ___ .|unagreed|A side-length request does not authorize a separate, undiscussed beard service.""",
        reference=("Wahl: guide-comb lengths and adjustable clipper terminology", "https://wahlusa.com/media/wahl-home-haircutting.pdf"),
    ),
    scenario(
        title="Read the color record precisely",
        skill="Separate starting areas, a strand-test observation, the desired tone, and outstanding safety checks.",
        setup="Fictional record review, not service instructions: client Mara has natural regrowth recorded at level 5 and previously colored lengths at level 7, warm. An earlier professionally assessed strand sample is recorded as level 7, still warm. Her goal is level 7, cool. The applicable allergy-alert assessment is incomplete. No formula, whole-head service, price, or timing is approved.",
        cast="Mara|Client\nTariq|Colorist",
        dialogue="""Mara|The note says level seven on the test strand. Isn't that the level I wanted? I'm wondering why the color plan isn't ready.
Tariq|It matches the requested [[level::Level seven describes lightness or darkness here; it does not establish the desired cool tonal character.]], but the note also says still warm. Your goal is level seven with a cool tone.
Mara|So reaching seven doesn't mean the test looks like my goal. We need to read the words after the number too.
Tariq|Exactly. The recorded [[tone::Tone distinguishes the warm observed sample from the cool target even though both are described at level seven.]] is different. We shouldn't summarize that as a perfect match.
Mara|I can also see level five beside regrowth. Is that a second description of the same test strand?
Tariq|No. [[Regrowth::Regrowth identifies the naturally grown root area, which is recorded separately from the previously colored lengths.]] refers to the naturally grown area near your scalp. That starting area is recorded at level five.
Mara|And the level-seven warm entry beside lengths describes the hair that was colored before, not all my hair from root to tip.
Tariq|Right. The [[previously colored lengths::The longer previously colored area has its own starting record; it cannot be merged with the natural regrowth entry.]] have a different starting record. Keeping the areas separate prevents a misleading whole-head summary.
Mara|Does the strand result tell you exactly what every part of my hair will do if you use the same approach?
Tariq|No. The [[strand test::A strand test supplies information about the tested hair sample; it is not a whole-head guarantee or a skin allergy assessment.]] gives information about that sample. It doesn't guarantee an identical response across different areas.
Mara|I thought a test meant the safety checks were finished too. Is that a different part of the record?
Tariq|Yes. The applicable [[allergy-alert assessment::The allergy-alert assessment is a separate incomplete requirement; an acceptable-looking hair sample does not replace it.]] is incomplete. The hair sample's color result doesn't complete that requirement.
Mara|Then I shouldn't read test done as meaning everything is cleared for application. I can see why the labels matter.
Tariq|Exactly. We follow the actual product warnings, required checks, and salon procedures. This conversation doesn't provide a test method or permission to apply color.
Mara|Could you just increase the processing time to make the result cooler? I'm trying to understand what changes next.
Tariq|We can't invent that instruction from these notes. Any proposed service needs professional assessment and the product's actual directions; more time isn't an automatic solution.
Mara|All right. Before I book, I want to understand the proposed result, the cost, and how long the appointment would be.
Tariq|Those are still to be agreed. No formula, price, service duration, or whole-head application has been approved in this record.
Mara|Please keep the goal as level seven cool, and the sample as level seven warm. Don't overwrite one with the other.
Tariq|I won't. I'll retain the separate starting areas, the observed sample result, the requested goal, and the incomplete assessment so the next discussion starts from the facts.""",
        transfer_title="Do not convert a sample into clearance",
        transfer_setup="A fictional record lists a desired level 6 neutral and a tested hair sample at level 6 warm. The applicable allergy-alert assessment remains incomplete. No whole-head color service is authorized.",
        transfer="""Client: The sample and goal share level ___ .|six|Both entries state level six, so their difference is tonal rather than the supplied level.
Colorist: The requested tone is ___ .|neutral|Neutral is the goal; warm is the recorded sample result.
Client: The sample is still described as ___ .|warm|The observed warm tone must remain in the record rather than being replaced by the desired tone.
Colorist: The allergy-alert assessment is ___ .|incomplete|The hair-sample result does not complete the separate outstanding assessment or authorize application.""",
        reference=("Wella: distinct purposes of skin-allergy and hair-strand assessments", "https://www.wella.com/international/wella-magazine/hair-color-safety-tests"),
    ),
]
