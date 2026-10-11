"""Original curing-system, tool-turnover, and design-map conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Match the system, not the watts",
        skill="Read a product-and-lamp record without confusing electrical power, visible appearance, or a timer with verified curing conditions.",
        setup="Fictional pre-service check: gel system G requires the identified L4 lamp under its current instructions. L4 is unavailable. Borrowed lamp B displays the same 36 W input rating, but no compatibility documentation is available. No product has been applied. Technician Mina and lead Jo review the proposed substitution; this exercise supplies no curing procedure or exposure time.",
        cast="Mina|Nail technician\nJo|Lead technician",
        dialogue="""Mina|Our L4 isn't available, but I can borrow lamp B. Both labels say thirty-six watts. Does that make B a suitable replacement for system G?
Jo|Not from the [[input rating::The 36 W input rating concerns electrical power; matching it does not establish that lamp B meets system G's curing requirements.]] alone. We need the specified product-and-lamp information, not just the same number on the electrical label.
Mina|The current instruction for G names L4. I haven't found any document that lists B for this system.
Jo|Then [[compatibility::Compatibility between the exact lamp and product system is unverified; a shared input rating cannot supply the missing evidence.]] is unverified. Please don't start applying G while we try to resolve that gap.
Mina|Nothing has been applied. I wanted to check first because the client is waiting and B looks very similar.
Jo|Good. The [[model identity::Model identity names the actual lamp; a similar case or display does not make two models interchangeable.]] matters more than the shape of the case. Similar-looking lamps need not deliver the same curing conditions.
Mina|B also has a countdown display. I could select the same time, but that wouldn't prove it's the same exposure, would it?
Jo|Correct. The [[timer::The timer shows elapsed or selected time, not proof that an unspecified lamp supplies the required light conditions.]] doesn't establish the required light conditions. Don't create a substitute protocol by matching seconds or adding extra time.
Mina|I've heard people say that if a gel looks firm, it must be fully cured. Is appearance enough to check that?
Jo|No. A firm-looking [[surface::The surface appearance does not independently verify curing throughout the product or replace the specified system instructions.]] isn't a complete cure check. We follow the actual system instructions and training rather than a visual guess.
Mina|And the word LED on the box doesn't automatically mean there's no ultraviolet light involved?
Jo|Right. LED identifies the light-source technology, not a guarantee of [[UV-free::UV-free cannot be inferred from LED; nail-curing LED systems may emit ultraviolet light.]] output. Use the exact lamp information instead of that shortcut.
Mina|I'll tell reception we're checking equipment suitability before offering this gel service, not that the client has caused a delay.
Jo|Yes. Give a clear update and discuss an appropriate alternative or rebooking through our process. Don't promise that a different service is already suitable or accepted.
Mina|If someone finds another L4, does the model match settle every readiness check automatically?
Jo|No. Its condition, required checks, and correct use still matter. A matching model answers only one part of the equipment question.
Mina|So today's note should say L4 unavailable, B same input rating but compatibility unverified, and no application started.
Jo|Exactly. Do not write lamp B approved or system G completed. We have only reviewed a proposed substitution.
Mina|I'll keep B out of this planned service until the relevant information and approval are obtained. I won't improvise a curing time.
Jo|Thank you. Ask for the actual manufacturer guidance and follow our equipment process. The schedule can't supply the missing technical evidence.""",
        transfer_title="A larger number does not approve a lamp",
        transfer_setup="Fictional system H specifies lamp M2. An available M9 is rated 48 W, while M2 is rated 36 W. No compatibility evidence for M9 is supplied. No product has been applied; no alternative procedure is approved.",
        transfer="""Technician: The lamp named by system H is ___ .|M2|M2 is specified in the supplied instructions; a larger electrical rating does not change that identity.
Lead: The available but unverified model is ___ .|M9|M9 is the proposed substitute, not the documented required lamp.
Technician: Forty-eight watts is the substitute's input ___ .|rating|The input rating describes electrical power, not verified compatibility or the curing conditions at the nail.
Lead: Compatibility with H remains ___ .|unverified|No supporting evidence is supplied, so neither the wattage nor availability approves substitution.""",
        reference=("CND: LED Lamp FAQ, system-specific curing and electrical input", "https://cdn.shopify.com/s/files/1/0794/0010/8323/files/CND-23-0450_ENGFAQ_CND_LED_Lamp_FAQ_F.pdf?v=1715353734"),
    ),
    scenario(
        title="A storage box is not a process",
        skill="Report reusable-tool and single-use-item status without treating tidiness, storage, or a UV cabinet as disinfection.",
        setup="Fictional stock check: reusable metal set A has completed the site's required cleaning, disinfection, and storage checks and is confirmed ready. Set B is cleaned only. Set C is used and unprocessed. A used single-use emery board is also present. The salon's UV cabinet is for storage only. No chemical procedure or sterilization process is supplied.",
        cast="Lena|Nail technician\nRavi|Salon assistant",
        dialogue="""Lena|Before I take a tool set, can you check these labels with me? A says ready, B says cleaned, and C is in the used area.
Ravi|Set A has completed the required [[disinfection::Disinfection is a required process completed for A after cleaning; the cleaned-only label on B does not establish it.]] and the other checks. It's the only set confirmed ready in this record.
Lena|B looks just as shiny as A. I nearly picked it up because I read cleaned as meaning everything was finished.
Ravi|Here, [[cleaned only::Cleaned only means that stage is recorded for B; the remaining required processing and confirmation are not complete.]] is an intermediate status. It doesn't mean the remaining processing or readiness confirmation has happened.
Lena|Could I put B in the UV cabinet and then mark it ready? I thought that cabinet did the next stage.
Ravi|No. This cabinet is [[storage::The supplied UV cabinet is for storage only; placing tools inside cannot replace the required disinfection process.]] only. It isn't a substitute for the required tool processing.
Lena|Then B needs to stay identified as incomplete, and C needs to stay in the used-item area for the correct handling.
Ravi|Yes. Keeping those flows separate helps prevent [[cross-contamination::Cross-contamination can transfer unwanted material or microorganisms between used and prepared items; separate handling preserves the distinction.]]. Don't mix used tools into a ready set because the tray has space.
Lena|What about this emery board? It's marked single use, but it doesn't look worn out. Could it go with B for processing?
Ravi|No. Its [[single-use::Single-use describes the intended use limit; an unworn appearance does not make the used board reusable.]] designation still applies. Handle it under the disposal procedure rather than relabel it as reusable.
Lena|For the metal sets, should I describe A as sterile when I tell the next technician it's ready?
Ravi|No. [[Sterilization::Sterilization is a distinct validated process, including elimination of bacterial spores; no such process is established by this record.]] isn't established here. Say it completed the required cleaning, disinfection, and storage checks, not that it is sterile.
Lena|So ready is a specific process status. It isn't a claim that any item in any box is completely free of every microorganism.
Ravi|Correct. Use the actual completed record and the site's applicable requirements. Don't add a broader claim the record doesn't support.
Lena|If we need B later, should I copy the timing from yesterday's different disinfectant into today's record?
Ravi|No. Follow the current instructions for the actual product, tool, and workplace requirements. This stock conversation doesn't provide a mixing ratio, contact time, or processing method.
Lena|Understood. I'll take A for the planned service, keep B marked cleaned only, and leave C clearly identified as used.
Ravi|And the used single-use board goes through the disposal route, not the reusable-tool route. That keeps all four statuses distinct.
Lena|I'll tell the next person which set is ready by letter, rather than saying the tools on the counter are fine.
Ravi|Good. A is confirmed ready; B and C are not. The cabinet location and a shiny appearance can't replace those specific records.""",
        transfer_title="Keep the tool labels distinct",
        transfer_setup="Reusable set D is used and unprocessed; E is cleaned only; F has completed required cleaning, disinfection, and storage checks and is confirmed ready. A used file is marked single use. The cabinet is storage only; no sterilization is recorded.",
        transfer="""Technician: The only confirmed-ready set is ___ .|F|F has completed all stated requirements; neither used D nor cleaned-only E has that status.
Assistant: Set E is cleaned ___ .|only|Only limits the completed stage and prevents an unsupported readiness claim.
Technician: The used single-use file follows the ___ procedure.|disposal|Its single-use designation excludes the reusable-tool processing route in this case.
Assistant: The cabinet provides ___, not the missing processing.|storage|The supplied cabinet is for storage only and cannot establish disinfection or sterilization.""",
        reference=("OSHA: nail-salon tool processing and UV storage limitations", "https://www.osha.gov/nail-salons/biological-hazards"),
    ),
    scenario(
        title="Which edge gets the accent?",
        skill="Turn style labels into an exact ten-nail design map, keeping tip, base, and blended effects distinct.",
        setup="Three fictional samples: A has a pink base and crisp white French tip; B has a silver crescent near the nail base, labelled reverse French; C blends pink into white with no crisp dividing line. Client Sol selects A on eight nails and B on both ring fingernails. All ten stay short; no extensions or application method are agreed.",
        cast="Sol|Client\nAna|Nail technician",
        dialogue="""Sol|I like the white edge on A, but I'd like the silver detail from B on my ring fingers. Can we combine those looks?
Ana|Yes, let's map the appearance first. A has a crisp [[smile line::The smile line is the curved boundary separating the contrasting tip from the pink area in sample A.]] between the pink area and the white tip.
Sol|That's the line I like. I don't want the white fading gradually into the pink like it does on C.
Ana|Then C's [[ombre::Ombre is a gradual blended transition; Sol instead chooses the crisp division shown in sample A.]] effect isn't part of the request. We'll keep that separate from the sharp-edged tip on A.
Sol|B says reverse French. I mean that silver crescent near the base, not silver at the far end of the nail.
Ana|For this sample, [[reverse French::The label here identifies the base-crescent design in B; the specified location, not the label alone, settles the request.]] labels the base crescent. I'll record its location explicitly because the label alone can be misunderstood.
Sol|Good. On the ring fingers I want B instead of A, not both decorations layered onto the same nail.
Ana|So both [[ring fingernails::The ring fingernails receive B instead of A; one on each hand gives two accent nails.]] get the silver base crescent and no white French tip. Is that right?
Sol|Yes, one on each hand. Every other fingernail gets the pink base and white tip from A.
Ana|That makes [[eight::Ten fingernails minus the two ring-finger exceptions leaves eight receiving sample A.]] with A and two with B. We're counting ten nails in total, not adding two extra decorations to all ten.
Sol|Exactly. Please don't put the silver on the middle fingers by mistake. These two ring fingers are the exceptions.
Ana|I'll make the [[placement map::A placement map assigns the chosen design to specific nails, preventing a correct count from landing on the wrong fingers.]] by hand and finger. The ring finger is between the middle and little fingers.
Sol|And keep them short. I like the pattern, not the longer length of the display pieces.
Ana|Short length remains part of your request. Selecting a design sample doesn't request extensions, and we'll confirm the actual length separately.
Sol|When I hold my hands out to you, my left is on your right. Could that confuse the note?
Ana|We'll use your left and your right throughout. For this design both ring fingers match, but the same habit matters when a design is different on each hand.
Sol|Can you read all of it back before we choose products or start any work?
Ana|Eight pink-and-white French-tip nails with a crisp line; silver base crescents instead on your two ring fingernails; short length, no added extensions requested.
Sol|Yes. No blended C effect and no extra white tip on the ring fingers. That's the combination I want.
Ana|I've recorded those exclusions with the map. We'll discuss the remaining service details from that precise design, without letting a style name replace the placement.""",
        transfer_title="Count the exceptions, not just the hands",
        transfer_setup="For ten fingernails, sample A is selected everywhere except the client's left thumb and the right index and middle fingernails. Those three receive sample B instead, not in addition. No other exceptions are agreed.",
        transfer="""Technician: Sample A appears on ___ nails.|seven|Ten nails minus three exceptions leaves seven for A.
Client: Sample B replaces A on ___ nails.|three|The left thumb, right index, and right middle are three distinct nails.
Technician: The single exception on the left is the ___ .|left thumb|The brief assigns B to the left thumb, not a left ring or index finger.
Client: The index and middle exceptions are on my ___ .|right hand|Both of those named exceptions are on the client's right, not the technician's right.""",
        reference=("OPI: a reverse-French design with a contrasting base crescent", "https://www.opi.com/en-GB/nail-art/glow-with-the-flow"),
    ),
]
