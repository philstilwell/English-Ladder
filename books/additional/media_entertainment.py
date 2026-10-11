"""Additional original production, accessibility, and transmission conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Loudness is not the peak reading",
        skill="Discuss an audio rejection using the correct measurements and agree a testable delivery correction.",
        setup="Fictional stereo delivery requires integrated loudness -23 LUFS and maximum true peak no higher than -1 dBTP. The complete exported program measures -19 LUFS and -0.2 dBTP. The team considers a uniform 4 dB reduction with no other processing change. Predicted readings must be checked on the final export; these are this delivery's requirements, not every outlet's.",
        cast="Marta|Sound mixer\nRavi|Post-production supervisor",
        dialogue="""Ravi|The delivery failed audio review. The note says minus nineteen LUFS and minus zero point two dBTP. Which of those should we fix first?
Marta|They measure different things. The [[integrated loudness::Integrated loudness measures the program over the relevant duration in LUFS; the supplied -19 reading is four loudness units above this delivery's -23 target.]] is four units above the target. The peak reading also exceeds the separate permitted maximum.
Ravi|Minus zero point two is higher than minus one, even though the number looks smaller without its sign. That explains the second flag.
Marta|Right. The [[true peak::True peak is measured in dBTP and addresses peak level rather than average program loudness; -0.2 dBTP exceeds the stipulated -1 dBTP ceiling by 0.8 dB.]] is zero point eight decibels above the ceiling. Do not relabel that reading as the program's loudness.
Ravi|Would reducing the entire mix by four decibels be a reasonable first pass, without changing the balance between speech and music?
Marta|Yes. Uniform [[attenuation::Attenuation reduces the signal level; a uniform four-decibel reduction predicts a four-unit loudness decrease and a four-decibel peak decrease before final remeasurement.]] should bring the loudness near minus twenty-three and predict a peak of minus four point two, if nothing else changes.
Ravi|That predicted peak is below the minus-one ceiling. We do not need to push it back up merely to touch the limit.
Marta|Exactly. A maximum is not a target we must hit. Raising the whole signal again would also raise loudness and could undo the correction.
Ravi|The current mix sounds balanced creatively. I would prefer not to squash the dynamics just because the delivery was rejected.
Marta|Then start with gain, not a new compression treatment. We have predicted [[headroom::Headroom is the remaining level margin below the applicable limit; a predicted -4.2 dBTP is 3.2 dB below this -1 dBTP ceiling.]] below the peak ceiling after that reduction. Listen and measure before deciding whether further processing is needed.
Ravi|Will the final encoded file necessarily have exactly the same peak as the mix export? Delivery will create another file.
Marta|Not necessarily. Export or encoding can affect the measured result. The prediction helps select a correction; it does not replace checking the actual delivered file.
Ravi|The first report covered the entire program, not only the loud introduction. I will make sure the new measurement uses the same intended content.
Marta|Also verify the [[channel mapping::Channel mapping assigns the intended audio to delivery channels; a loudness pass does not prove that left, right, or other required tracks are correctly assigned.]]. A passing loudness number would not reveal that someone exported the wrong track pair.
Ravi|The requested version is stereo. I will compare the file identifier and delivery manifest so we do not measure the commentary mix by mistake.
Marta|Good. I will listen for dialogue intelligibility, clipping, and unexpected changes as well. Two passing numbers cannot certify every aspect of the soundtrack.
Ravi|Please keep the original failure report and the corrected file's results together. The distributor needs to know which version was rechecked.
Marta|I will attach the [[QC report::The quality-control report records the tested file, measurements, specification, and remaining findings; results for an earlier version do not establish the delivered version's status.]] to that exact export. If either measurement still misses the requirement, we investigate before submitting again.
Ravi|Our proposed correction is four decibels down, preserving the mix balance, then a complete measurement and listening pass on the delivery file.
Marta|Agreed. Report the measured result, not the predicted one. That gives the distributor a traceable correction and keeps the creative and technical decisions separate.""",
        transfer_title="Keep the signs and units",
        transfer_setup="Fictional file: -20 LUFS integrated, -1 dBTP true peak. Required integrated target -23 LUFS; peak ceiling -2 dBTP. Consider only uniform gain reduction, with no other processing change. Predict first, then remeasure the final file.",
        transfer="""Supervisor: The initial gain reduction to target is ___ decibels.|3|Moving from minus twenty toward minus twenty-three calls for three decibels of reduction, not an increase.
Mixer: That predicts a true peak of ___ dBTP.|-4|Subtracting three decibels from the initial minus-one peak predicts minus four dBTP.
Supervisor: The predicted peak is ___ decibels below the ceiling.|2|Minus four is two decibels below the specified minus-two maximum.
Mixer: Before delivery, we must ___ the final export.|remeasure|The calculated shift is a prediction; the actual final file must be measured against the delivery requirements.""",
        reference=("European Broadcasting Union: loudness and true-peak terminology", "https://tech.ebu.ch/docs/r/r128.pdf"),
    ),
    scenario(
        title="Captions that preserve the meaning",
        skill="Give precise caption corrections for synchronization, speaker identity, and information lost from the soundtrack.",
        setup="Fictional review of approved master V7 at 25 frames per second. Three checked caption cues appear eight frames early; the rest of the file is not yet checked. One caption omits 'not' from the spoken sentence 'We did not approve the sale.' An off-screen speaker is unclear, and an audible doorbell relevant to the scene is omitted. Correct text must follow the actual soundtrack.",
        cast="Lin|Accessibility editor\nOmar|Online editor",
        dialogue="""Lin|The captions imported, but I found a meaning error and a timing problem. Which picture version did you use for the final check?
Omar|V7 is the approved [[reference master::The reference master is the identified picture and sound version used for caption review; using an earlier edit could produce incorrect timing and content judgments.]]. I have it open now at twenty-five frames per second. Let us compare the same export before changing anything.
Lin|At three checked cues, the text appears eight frames before the corresponding speech. I have logged each cue number and its first spoken word.
Omar|That suggests a [[constant offset::A constant offset is the same timing difference at checked points; three matching observations suggest it but do not prove the entire file shares it.]] at those points. It does not yet prove that one shift will fix the whole file; another section could drift or contain an edit.
Lin|At twenty-five frames per second, eight frames is zero point three two seconds. The checked captions would need to move later, not earlier.
Omar|Correct. Keep the [[frame rate::The frame rate converts the observed frame difference into time: eight frames divided by twenty-five frames per second equals 0.32 seconds.]] with that calculation. Eight frames is not eight hundredths of a second, and another frame rate would change the conversion.
Lin|I will check the remaining cues before proposing a file-wide shift. Moving the whole video to match a caption file would change the approved master.
Omar|Agreed. The caption timing is what we are investigating. We should not alter the picture or audio synchronization to make an unchecked text file fit.
Lin|The more serious text error is in the sale discussion. The soundtrack says we did not approve the sale, but the caption says we did approve it.
Omar|Restore the [[negation::Negation is the negative meaning carried here by 'not'; omitting it reverses the speaker's statement rather than merely shortening the sentence.]]. That missing word reverses the meaning. We cannot treat it as an acceptable shortening just because the line is easier to fit.
Lin|I will preserve the spoken meaning and adjust the timing or line break within the delivery guidelines. The dialogue must not become a different claim.
Omar|There is also a reply from off screen. The current caption gives the words but leaves it unclear who is speaking in that exchange.
Lin|I will add appropriate [[speaker identification::Speaker identification tells the viewer who speaks when that is not clear from the image and context; it should use established information without inventing or prematurely revealing identity.]] using what the scene establishes. I will not introduce a character name before the story reveals it.
Omar|Good. And the doorbell is what makes the character turn toward the entrance. A viewer without the audio currently loses that reason.
Lin|That needs a concise [[sound cue::A sound cue represents relevant non-speech audio such as the audible doorbell driving the character's reaction; captions need more than spoken words when sound carries meaning.]]. I will identify the audible doorbell, not add a theory about who is outside or what will happen next.
Omar|Once the text is corrected, can we review it in the actual player? A valid file can still display badly against the picture.
Lin|Yes. I will check readability, placement, cue timing, and whether text covers important on-screen information. Successful import is only the start of that review.
Omar|I will keep V7 fixed and give the corrected caption file its own revision identifier. The old file will not remain the default attachment.
Lin|Then we can record which cues were checked and any remaining issues, instead of claiming the entire file passed after three timing samples.
Omar|Agreed. We will verify the whole corrected track against V7, including the negative sentence, off-screen reply, and doorbell, before sending the final package.""",
        transfer_title="A late cue and a missing word",
        transfer_setup="At 24 frames per second, a checked caption appears six frames LATE. The soundtrack says 'The permit has not expired,' but the caption omits 'not.' Other cues remain unchecked.",
        transfer="""Editor: Six frames at this rate equal ___ seconds.|0.25|Six frames divided by twenty-four frames per second equals one quarter of a second.
Reviewer: This checked caption needs to move ___.|earlier|The caption is late relative to its speech, so the correction direction is earlier rather than later.
Editor: Restore the missing word ___.|not|The supplied soundtrack includes not; omitting it falsely changes an unexpired permit into an expired one.
Reviewer: A single checked cue does not establish whole-file ___.|synchronization|The remaining cues have not been checked, so one timing observation cannot certify synchronization throughout the track.""",
        reference=("W3C: accurate and synchronized captions", "https://www.w3.org/WAI/media/av/captions/"),
    ),
    scenario(
        title="A live rundown that fits",
        skill="Negotiate a shorter live rundown and use concise read-backs to prevent the wrong package or timing from reaching air.",
        setup="Fictional pre-transmission review: at the planned 20:07 checkpoint, 180 seconds remain before a fixed 20:10 end. Remaining items currently total 240 seconds: interview 120, package 90, close 30. An approved 60-second package exists. The producer may shorten the interview to 90 seconds while retaining the essential question. No further links or transitions sit outside these durations.",
        cast="Bea|Producer\nAnton|Director",
        dialogue="""Bea|At the seven-minute checkpoint, this version of the show still has four minutes left to run. We only have three before the fixed end.
Anton|The [[hard out::The hard out is the fixed 20:10 ending in this plan; at 20:07 it leaves 180 seconds, not enough for the current 240-second sequence.]] remains twenty ten. We need to remove sixty seconds from the remaining sequence, not hope the presenter reads faster.
Bea|I can take thirty seconds from the interview by dropping the optional follow-up. The essential question and answer must stay intelligible.
Anton|Then the [[rundown::The rundown lists the ordered program items and durations; changing the interview from 120 to 90 seconds removes thirty seconds from its current total.]] needs ninety seconds for that interview. We still need another thirty seconds; the package and close have not changed yet.
Bea|We have an approved sixty-second version of the package. It carries the same essential story and ends on the same shot.
Anton|Use that [[cutdown::The cutdown is the approved shorter package, sixty seconds instead of ninety; selecting it removes the remaining thirty seconds without inventing a live edit.]]. Confirm its asset identifier, though. The same final shot does not mean the two files have the same duration.
Bea|The identifier is RIVER-60. RIVER-90 is the longer original. I will put the short identifier and duration into the revised item.
Anton|And retain the [[out cue::The out cue is the identifiable ending used to coordinate the next item; it must match the selected package rather than be guessed from its file name.]]. Playback and the presenter need the correct ending so we can move cleanly into the close.
Bea|With ninety for the interview, sixty for the package, and thirty for the close, we have exactly one hundred eighty seconds.
Anton|Correct. From twenty oh seven, the package starts at twenty oh eight thirty and the close at twenty oh nine thirty. The hard out stays twenty ten.
Bea|Please give me a [[read-back::A read-back repeats the critical instruction so the sender can check understanding; here it should confirm the short package identifier and the revised item durations.]] before I circulate it. We changed two items, and I do not want someone applying only one of the changes.
Anton|Interview ninety; RIVER-60 for sixty; close thirty. Package at twenty oh eight thirty, close at twenty oh nine thirty, out at twenty ten.
Bea|That matches. I will update the presenter notes to remove only the optional follow-up, not shorten the essential answer into a misleading fragment.
Anton|The closing script also needs to fit its allocated thirty seconds. We cannot discover during the show that it contains an extra uncounted link.
Bea|All links and transitions are included in these supplied durations. I will still check the revised script against that assumption before the show.
Anton|Good. And when you call [[stand by::Stand by instructs the operator to prepare, not to start playback; a separate execution cue is needed under the agreed control-room procedure.]] for the package, make it clear that playback prepares but does not roll until the agreed execution cue.
Bea|Understood. I will use our established cue sequence and keep the production talkback separate from anything the audience should hear.
Anton|We also need confirmation that playback has actually loaded RIVER-60. A corrected rundown row alone does not prove the right file is cued.
Bea|I will collect that confirmation and brief the presenter on the shorter interview. Any later timing change comes back through this same coordinated update.
Anton|Then we have a workable plan: both approved reductions applied, the essential story retained, and every department working from the same durations and identifiers.""",
        transfer_title="Backtime a shorter sequence",
        transfer_setup="Fictional plan: at 18:28, 120 seconds remain before an 18:30 hard out. The approved sequence is a 45-second interview, a 50-second package, and a 25-second close. All links are included; no extra time is available.",
        transfer="""Producer: The three durations total ___ seconds.|120|Forty-five plus fifty plus twenty-five equals the full one-hundred-twenty seconds available.
Director: The package begins at ___.|18:28:45|The forty-five-second interview begins at 18:28, so the package follows at 18:28:45.
Producer: The close begins at ___.|18:29:35|Adding the fifty-second package to 18:28:45 gives 18:29:35 for the final twenty-five seconds.
Director: Stand by means prepare, not ___ playback.|start|The preparation cue does not itself instruct the operator to execute playback under the stated distinction.""",
        reference=("Avid: rundown timing, backtime, and hard-out clocks", "https://mediacentral.avid.com/mccux/Content/MCUX_Users_Guide/Show%20Timing.htm"),
    ),
]
