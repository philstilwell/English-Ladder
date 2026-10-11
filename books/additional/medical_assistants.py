"""Original clinic language-access, measurement, and ECG handoff cases."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Book the right language support",
        skill="Confirm spoken and written language preferences separately and distinguish family support from qualified interpreting.",
        setup="Before tomorrow's visit, assistant Mina and coordinator Jo check Mei's recorded preferences: spoken Mandarin, written Traditional Chinese. Mei requests her sister's support. The clinic has booked a qualified video interpreter for Mandarin; a copied appointment note incorrectly says Cantonese. No diagnosis or treatment discussion is taking place here.",
        cast="Mina|Medical assistant\nJo|Language-access coordinator",
        dialogue="""Mina|Jo, the interpreter booking says Mandarin, but tomorrow's appointment note says Cantonese. Both are attached to Mei's visit. Which preference did we actually confirm with her?
Jo|The recorded [[spoken-language preference::Mei stated Mandarin for spoken communication; Cantonese in the copied appointment note conflicts with that confirmed preference.]] is Mandarin. The Cantonese entry was copied incorrectly. Please correct that entry through our record process and preserve the reason.
Mina|Her written preference is Traditional Chinese. I should keep that as a separate field, rather than assume that the spoken language tells me which written materials she wants.
Jo|Exactly. The [[written-language preference::Traditional Chinese is Mei's stated choice for written materials; it should not be inferred from the spoken-language field or replaced by it.]] guides the material request. Check that the available document is the approved version in that form, not just any document labeled Chinese.
Mina|Mei wants her sister in the visit. Should I cancel the interpreter and put family interpreting instead?
Jo|No. Keep our [[qualified interpreter::The clinic has arranged a qualified healthcare interpreter for Mandarin; a relative's presence for support does not replace that booking.]] booking. Mei asked for her sister's support, not for us to withdraw the language service.
Mina|I will tell the team that distinction. We should address Mei directly, rather than asking her sister to answer every question because it seems quicker.
Jo|Yes. The clinician should speak to Mei and allow the interpreter to relay the exchange. The sister can contribute within the arrangement Mei agrees to; she does not automatically speak for her.
Mina|The service is by video. I can check the room equipment and booking connection before the visit, without opening a clinical conversation in a public area.
Jo|Please do. Record that it is [[video interpreting::The booked service uses video for the live spoken exchange; it is not a written translation service or merely a telephone appointment reminder.]], including the appropriate service details. A booking confirmation does not prove the interpreter has joined tomorrow's session.
Mina|For the handoff, I will say Mandarin interpreter booked and Traditional Chinese materials requested. I will not say all language needs are complete before the document and connection checks.
Jo|Good. If the required document is unavailable, bring that back to me. Do not substitute an unreviewed automatic translation for a clinical instruction and mark it approved.
Mina|The clinician asked whether the interpreter could simply summarize a long explanation at the end. Would shorter sections make the exchange easier to check?
Jo|Yes. Use [[short segments::Short segments let the interpreter relay each part accurately and allow the patient to ask questions without relying on a long end-of-explanation summary.]] and pause for interpretation. Preserve the patient's questions too, not just the clinician's instructions.
Mina|Mei may want to discuss something without her sister present. We need to offer that opportunity respectfully, without treating the request as a family disagreement.
Jo|Correct. Follow our private-conversation process and ask Mei about her wishes. The interpreter's confidentiality obligations remain important whether or not a family member is present.
Mina|For checking an explanation, the clinician can ask Mei to describe the plan in her own words through the interpreter, rather than just asking whether she understands.
Jo|That is [[teach-back::Teach-back checks the clarity of an explanation by hearing the patient's understanding in their own words; a yes response or fluent English is not the test.]]. The interpreter relays the response; the clinician resolves any clinical misunderstanding.
Mina|I will correct Cantonese to the confirmed Mandarin preference, keep the written preference separate, retain the interpreter booking, and check the materials and video arrangements.
Jo|Thank you. I will check the approved document request. We will leave the remaining preparation tasks visible rather than mark the visit language support complete prematurely.""",
        transfer_title="Two preferences, two arrangements",
        transfer_setup="Luis confirms spoken Spanish and written English. His adult son will attend for support. The clinic has booked a qualified Spanish telephone interpreter. The connection has not yet occurred; approved English paperwork is available.",
        transfer="""Assistant: Luis's spoken preference is ___ .|Spanish|Luis explicitly chose Spanish for conversation; the English paperwork preference does not override it.
Coordinator: His written preference is ___ .|English|The supplied record separately confirms English for written materials, rather than Spanish by assumption.
Assistant: The booked interpreter will join by ___ .|telephone|The booked service is telephone interpreting, not video or an already completed connection.
Coordinator: The son's attendance is for ___ .|support|The son is attending for support; his presence does not replace the arranged qualified interpreter.""",
        reference=("AHRQ: language preferences and qualified language-access services", "https://www.ahrq.gov/health-literacy/improve/precautions/tool9.html"),
    ),
    scenario(
        title="A number needs its unit",
        skill="Read back a measurement with its unit and explain a traceable correction without inventing a new measurement or clinical conclusion.",
        setup="Fictional record check: today's saved scale output is 160.0 lb at 09:12. A draft entry incorrectly says 160.0 kg. Height was recorded separately as 170 cm. Use 1 lb = 0.45359237 kg; round the converted weight to one decimal place. Nurse Dana reviews the correction; clinical use of the draft is not yet checked.",
        cast="Rosa|Medical assistant\nDana|Nurse",
        dialogue="""Rosa|Dana, I found a mismatch before closing the rooming record. The saved scale output says one hundred sixty point zero pounds, but the draft says kilograms.
Dana|Check the [[source measurement::The saved scale output establishes 160.0 pounds at 09:12; appearance or the patient's previous weight would not establish this measurement's unit.]], including its unit and time. Do not decide which label looks right from the patient's appearance or a remembered earlier weight.
Rosa|The saved output is clear: 160.0 lb at nine twelve today. If our field requires kilograms, multiplying by the supplied factor gives seventy-two point five seven four eight.
Dana|To one decimal place, enter [[72.6::160.0 multiplied by 0.45359237 equals 72.5747792 kilograms, which rounds to 72.6 kilograms at one decimal place.]] kilograms through the correction process. Keep the original pounds reading and the conversion identifiable; those are not two separate weighings.
Rosa|So changing the unit label alone would be wrong. One hundred sixty kilograms is not another way of expressing one hundred sixty pounds.
Dana|Correct. A [[unit conversion::A unit conversion changes the numerical value and unit together while representing the same measured quantity; relabeling 160.0 pounds as kilograms changes its meaning.]] preserves the quantity by changing both number and unit appropriately. Also check whether the system already converts values, so the same reading is not converted twice.
Rosa|The height entry is one hundred seventy centimeters. In meters, that is one point seven zero. It is not one hundred seventy inches.
Dana|Right. Keep [[height::The separate 170-centimeter entry describes height; its conversion to 1.70 meters is unrelated to converting the weight from pounds to kilograms.]] separate from weight. Use the verified value and required unit for each field, not a copied unit from the previous row.
Rosa|Would it help to write that the corrected weight is normal? The number looks more plausible now.
Dana|No. Plausibility is not a clinical assessment. We are correcting a recording error, not assigning a weight category, calculating a treatment dose, or declaring the patient healthy.
Rosa|I will retain the original entry and record what changed and why under our process. I should not delete the history and make it look as if no error occurred.
Dana|Yes. The [[audit trail::The audit trail preserves the original entry, correction, reason, and authorship under the clinic process; an unexplained overwrite would hide the recording error.]] matters if somebody has already used the draft. Tell me which records or workflows may have received it so we can investigate promptly.
Rosa|I have not checked that yet. I will not say no effect just because the error was in a draft field. You need to know the downstream use is unresolved.
Dana|Thank you. I will handle the clinical implications through the appropriate review. Your job is to supply the measurement evidence and report the discrepancy, not estimate harm from the arithmetic alone.
Rosa|Should the converted entry carry the time I make the correction, or nine twelve when the patient was actually weighed?
Dana|Preserve the [[measurement time::The measurement occurred at 09:12; the later correction time is a separate record event and must not make the conversion look like a new weighing.]] as nine twelve and record the correction time separately as required. Converting an existing reading does not mean a new measurement occurred.
Rosa|If the scale record had lacked a unit, I would need clarification through our procedure rather than automatically apply the pounds-to-kilograms factor.
Dana|Exactly. This case gives a verified unit. When the source is uncertain, multiplying by a familiar factor can make an unsupported assumption look precise.
Rosa|Read-back: original 160.0 pounds at 09:12; converted 72.6 kilograms to one decimal; separate height 170 centimeters, or 1.70 meters. Correction history retained; downstream use still being checked.
Dana|Confirmed. Bring the corrected record for the required check. The arithmetic is clear, but it does not by itself close the review of where the incorrect entry may have gone.""",
        transfer_title="Convert once and preserve the source",
        transfer_setup="A verified scale output is 132.0 lb at 10:18. The record requires kilograms to one decimal; use 1 lb = 0.45359237 kg. A separate verified height is 165 cm. The correction is entered at 10:31.",
        transfer="""Assistant: The weight rounds to ___ kilograms.|59.9|132.0 multiplied by 0.45359237 is 59.87419284, which rounds to 59.9 kilograms.
Nurse: The original measurement time remains ___ .|10:18|The patient was weighed at 10:18; 10:31 describes the later correction, not a new weighing.
Assistant: The separate height is ___ meters.|1.65|There are one hundred centimeters in a meter, so 165 centimeters equals 1.65 meters.
Nurse: The record was corrected at ___ .|10:31|The supplied correction time is 10:31 and must remain distinct from the measurement time.""",
        reference=("NIST: Handbook 44, 2026, Appendix C, mass conversion factors", "https://www.nist.gov/document/2026-nist-handbook-44-appendix-c"),
    ),
    scenario(
        title="A clear trace is not a diagnosis",
        skill="Distinguish ECG electrodes, recorded leads, technical warnings, and clinical interpretation during a clinician handoff.",
        setup="Assistant Leo is trained and authorized for ECG acquisition under this fictional clinic's procedure, not interpretation. A 12-lead ECG recorded at 11:06 has a lead-off warning. After the prescribed technical checks, an authorized repeat is recorded at 11:10. Its automated wording is unconfirmed. Dr Shah receives both traces and the patient's question.",
        cast="Leo|Medical assistant\nDr Shah|Receiving clinician",
        dialogue="""Leo|Dr Shah, I have the original eleven-oh-six ECG and the repeat at eleven ten. The first recording showed a lead-off warning. Both are labeled and retained for your review.
Dr Shah|Start with the technical history. A [[lead-off warning::A lead-off warning concerns the recording connection; it is not itself a diagnosis about the patient's heart or proof that all clinical findings are artifact.]] is not a clinical diagnosis. Tell me what was observed and checked, without deciding what the waveform means.
Leo|I completed the prescribed technical checks within my authorized role, then recorded the approved repeat. I have documented those checks; I have not attributed any clinical finding to a loose connection.
Dr Shah|Good. Keep the acquisition history attached. The patient should not be told everything is normal just because the technical warning no longer appears on the second recording.
Leo|The patient asked why a twelve-lead test uses ten sticky patches. I explained that the patches are electrodes and that lead has another meaning in the test name.
Dr Shah|Yes. The [[electrodes::The ten skin electrodes acquire the signals used for a standard twelve-lead ECG; the number of electrodes is not the number of displayed electrical views.]] make contact with the skin. The twelve leads represent different electrical views, not twelve separate adhesive patches.
Leo|I did not give a placement lesson or change the prescribed positions to improve the picture. Any acquisition difficulty follows our equipment instructions and clinic procedure.
Dr Shah|Exactly. Correct patient identification and recording details matter too. A technically clear trace with the wrong patient label would still be an unsafe record.
Leo|The repeat looks easier to read on screen. May I describe that as better signal quality while leaving the clinical meaning to you?
Dr Shah|Report the actual technical observations. [[Signal quality::Signal quality concerns the recording's clarity and interference; it is distinct from whether the patient's ECG has a clinically important finding.]] and clinical interpretation answer different questions. Do not turn easier to read into a normal-heart conclusion.
Leo|The machine also printed an automated statement. I have left it identified as machine-generated and unconfirmed, rather than copying it into a message as your conclusion.
Dr Shah|Correct. [[Automated interpretation::Automated interpretation is the device's analysis, not a completed clinician review; its wording must not be presented as Dr Shah's confirmed conclusion.]] supports the review but does not replace it. I need the actual recordings and patient context, not just a sentence from the device.
Leo|The patient asked whether the repeat means something serious was found. I said you would explain the findings, and that I repeated the recording for the documented technical reason.
Dr Shah|That keeps the explanation within your role without minimizing the question. Pass any current concern through the clinical route promptly; a technical check must not delay necessary care.
Leo|For the record, both recordings retain their own times. I have not overwritten eleven oh six with eleven ten or made the first trace disappear.
Dr Shah|Thank you. Keep the [[repeat acquisition::Repeat acquisition means obtaining a new recording at 11:10; it does not erase the original 11:06 trace or establish a clinical change between them.]] distinguishable from the original. A difference between traces needs review, not an assumption that the patient's condition changed.
Leo|The chart therefore shows the initial warning, documented checks, original and repeat times, and your receipt. It does not say interpreted, normal, or cleared to leave.
Dr Shah|Right. Receipt by the [[reviewing clinician::The reviewing clinician has received the material but must still review it; receipt alone does not establish interpretation or a discharge decision.]] is one stage. The clinical findings and next steps belong in the appropriate clinical record after the actual assessment.
Leo|My handoff is complete: both traces, technical history, and the patient's question are with you. No clinical result has been communicated by me.
Dr Shah|Received. I will review the recordings and speak with the patient. Retain your factual acquisition note without adding a result that I have not provided.""",
        transfer_title="Name the stage that actually occurred",
        transfer_setup="A standard 12-lead ECG uses 10 skin electrodes. The initial trace is timed 14:02 and an authorized repeat 14:07. Dr Malik has received both, but no clinical interpretation is supplied.",
        transfer="""Assistant: This standard twelve-lead recording uses ___ skin electrodes.|10|The standard twelve-lead ECG uses ten electrodes to obtain twelve electrical views.
Clinician: The original trace is timed ___ .|14:02|The first recording retains 14:02 even though a later repeat was obtained.
Assistant: The repeat is timed ___ .|14:07|The repeat is a separate acquisition at 14:07, not a correction to the first trace's timestamp.
Clinician: A clinical interpretation is not yet ___ .|supplied|Receipt of the traces is confirmed, but the facts do not supply a clinical interpretation or clearance.""",
        reference=("Royal Papworth Hospital: standard ECG electrodes and electrical leads", "https://www.royalpapworth.nhs.uk/our-services/cardiology/cardiac-assessment/electrocardiogram-ecg"),
    ),
]
