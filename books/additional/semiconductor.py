"""Original wafer-test, timing-signoff, and moisture-handling conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A failing wafer map may also tell a contact story',
        skill='Discuss wafer-test evidence while distinguishing a test result, a contact hypothesis, and approved retest.',
        setup='A wafer-sort run shows repeated failures at one probe site. The test program is unchanged, but contact-resistance information and probe-card history have not yet been reviewed. The test and yield engineers investigate. No cause, retest disposition, or shipment decision is established.',
        cast='Luca|Test engineer\nNari|Yield engineer',
        dialogue='''Nari|The wafer map has a repeated pattern at one probe site. Can we tell the fab that this is a process defect?
Luca|Not yet. First separate the [[test bin::A test bin classifies the recorded test outcome; it does not by itself identify the physical cause of a failure.]] from the cause. The bin tells us which test outcome was recorded, not why it happened.
Nari|The pattern seems to follow the same site in successive touchdowns. That could be different from a defect following a physical wafer region.
Luca|Exactly. Compare the [[site correlation::Site correlation examines whether the outcome follows a particular parallel test site, helping distinguish that pattern from the wafer's physical geography.]] with the die coordinates. Keep both views so we do not mistake the test arrangement for a wafer-location effect.
Nari|The program revision is unchanged. Does that rule out the test system as a contributor?
Luca|No. The [[probe card::The probe card provides the electrical interface to wafer contacts; its condition and history can matter even when the test-program revision is unchanged.]], tester configuration, connections, and conditions still need review. A matching program name does not establish identical test behavior.
Nari|The operations note mentions intermittent contact. I would like to see the actual measurements rather than use that phrase as the explanation.
Luca|I will retrieve the [[contact resistance::Contact resistance concerns the electrical resistance at the probing connection; relevant measurements can help investigate a contact hypothesis without proving it from a label.]] records and the card history. At present, contact is a hypothesis, not a confirmed cause.
Nari|Please preserve the first-pass results too. If the team reruns selected die later, I do not want the original failures to vanish from the dataset.
Luca|Agreed. Any [[retest::Retest repeats testing under the applicable authorized conditions; it must preserve the first-pass record and identify the basis for interpreting a changed result.]] needs the authorized plan, traceable conditions, and a separate result. Repeating until something passes is not a justified investigation.
Nari|Would a higher pass count after an intervention establish that every first-pass failure was only a contact problem?
Luca|No. We would need to compare the relevant evidence and understand the intervention. A changed result is useful, but it does not assign one cause to every failing die.
Nari|We should show first-pass yield and any later disposition separately. Otherwise the apparent improvement could simply reflect a different reporting rule.
Luca|Yes. Keep the [[denominator::The denominator identifies the population used in a yield calculation; first-pass and selected-retest populations must not be silently interchanged.]] and population explicit, especially if only selected die are retested.
Nari|I can compare the pattern across coordinates, sites, and lots. Is there anything you need from yield analysis before the equipment review?
Luca|The exact failing test identifiers and map references. That will let the equipment team connect its records to the same observations instead of a screenshot without context.
Nari|I will send those and keep the lot status unchanged. The customer update can say a site-associated pattern is under investigation.
Luca|Good. Do not say the fab caused it or the test system cleared it while those conclusions remain open.
Nari|Once the review establishes the next authorized work, we can report what was checked, what changed, and which conclusions the evidence supports.
Luca|Exactly. A useful wafer map leads to a focused investigation, not an immediate choice between blaming the process and discarding the test result.''',
        transfer_title='A selected retest is reported as the whole wafer yield',
        transfer_setup='Only 20 initially failing die are retested. Fifteen pass on that retest. The complete first-pass wafer results remain available.',
        transfer='''Yield engineer: Fifteen of twenty describes the selected retest ___.|population|The retest population contains only selected initially failing die, not the whole wafer.
Test engineer: Preserve the original first-pass ___.|results|Later testing must not erase the original observations or their reporting basis.
Yield engineer: Do not label seventy-five percent as the whole-wafer ___.|yield|Fifteen divided by twenty is the selected retest pass rate, not overall wafer yield.
Test engineer: Interpret any changed result under the authorized retest ___.|plan|The authorized plan determines the conditions and basis for using the retest evidence.''',
        reference=('FormFactor: Wafer Probing and Test Community', 'https://compass.formfactor.com/2023-virtual/')),
    scenario(
        title='Nominal timing passes, but signoff still has an open corner',
        skill='Explain a timing violation and challenge an unjustified exception without confusing analysis scopes.',
        setup='A digital design passes the reviewed nominal setup analysis. One required slow-corner scenario reports setup slack of -0.08 ns, and required hold analysis is incomplete. A schedule note says timing clean. The timing lead and design engineer review the claim; no exception or signoff decision has been approved.',
        cast='Rhea|Timing lead\nJon|Design engineer',
        dialogue='''Jon|Nominal timing passes, so I marked the design timing clean. You flagged the note. Which part of the signoff package is still open?
Rhea|The required slow-corner scenario has negative [[setup slack::Setup slack compares the required and actual arrival timing for the setup check; negative slack means the stated constraint is not met in that scenario.]] of zero point zero eight nanoseconds. Required hold analysis is also incomplete.
Jon|So the nominal result is useful, but it does not cover all the required operating assumptions. We need to show the failing scenario separately.
Rhea|Yes. A [[PVT corner::A PVT corner specifies process, voltage, and temperature assumptions for analysis; a pass at one corner does not automatically establish a pass at others.]] defines process, voltage, and temperature assumptions. Those conditions are part of the result, not a footnote we can drop.
Jon|The path is only used in a special mode. Could I declare it a false path to remove the violation from the report?
Rhea|Only with a valid, reviewed [[timing exception::A timing exception changes how specified paths are analyzed and requires a justified functional basis; it is not a way to hide an inconvenient violation.]]. The fact that a path is inconvenient or infrequent does not prove it cannot be exercised under the relevant mode.
Jon|I will check the mode and constraints with verification. A false-path claim needs support from actual functional behavior, not the launch date.
Rhea|Exactly. Keep the endpoint, mode, and constraint reference with the question. We need to know whether the analysis is appropriate before deciding what design change is needed.
Jon|If we improve this setup path, can the same change affect a hold check elsewhere?
Rhea|It can. The [[hold analysis::Hold analysis checks minimum-delay timing requirements and is distinct from setup analysis; a setup improvement does not automatically establish hold correctness.]] must be assessed on its own required basis. We should not assume one favorable change resolves every timing concern.
Jon|The latest report uses an updated netlist, but I am not sure the extracted interconnect data belongs to that revision.
Rhea|Confirm the [[parasitic extraction::Parasitic extraction provides modeled interconnect effects such as resistance and capacitance; its configuration must match the design being analyzed.]] and other inputs before relying on the result. A precise slack number is not meaningful if the input configuration is inconsistent.
Jon|Then the next update needs the exact netlist, constraints, libraries, extraction, modes, and corners. That is more useful than another screenshot of a green summary.
Rhea|Yes. It also needs the open checks and reviewed exceptions. [[Timing closure::Timing closure is the process of meeting the defined timing requirements across the required analysis scope, not merely obtaining one favorable nominal report.]] is against the required scope, not whichever report happens to be most favorable.
Jon|I will remove timing clean and report nominal setup passed, one required setup violation open, and hold checks incomplete.
Rhea|That preserves the completed work without implying signoff. We can then assign the constraint review and the technical investigation to the right owners.
Jon|Should I promise a frequency reduction as the solution? It would change the customer requirement, so I think that belongs in a separate trade-off discussion.
Rhea|Correct. Do not quietly change the requirement to make the report pass. Any proposed specification change needs its own assessment and authorization.
Jon|I will bring the reviewed path evidence to the next meeting. We will distinguish a real design issue from a justified constraint correction rather than assume either one.
Rhea|Good. The final decision needs consistent inputs, completed required checks, and a supported treatment of exceptions, not a nominal pass expanded into a blanket claim.''',
        transfer_title='A negative slack is hidden by an unsupported exception',
        transfer_setup='A required timing scenario has negative slack. An engineer proposes excluding the path without evidence that the exception is functionally valid.',
        transfer='''Reviewer: Keep the violation visible until the exception has a justified ___.|basis|An exception needs a valid functional rationale rather than merely a desire to remove the violation.
Engineer: Check the path against the relevant operating ___.|mode|Functional behavior in the applicable mode matters when deciding whether an exception is appropriate.
Reviewer: Preserve the actual analysis inputs and configuration ___.|revision|The timing result must remain linked to the precise configuration analyzed.
Engineer: Do not call timing closed while required checks remain ___.|open|Incomplete required checks prevent a blanket claim that the defined timing scope is complete.''',
        reference=('Synopsys: Static Timing Analysis', 'https://www.synopsys.com/glossary/what-is-static-timing-analysis.html')),
    scenario(
        title='A resealed bag does not explain the exposure history',
        skill='Clarify moisture-handling records and distinguish shelf life, floor life, and disposition.',
        setup='A reel of moisture-sensitive packaged devices arrives at assembly in a resealed bag. The original opening time and cumulative exposure record are missing. The package label identifies the part and moisture sensitivity level, but no approved disposition is recorded. A materials coordinator asks a packaging engineer how to describe the status.',
        cast='Sora|Materials coordinator\nCaleb|Packaging engineer',
        dialogue='''Sora|The reel is back in a sealed bag. Can I mark it ready for assembly, or do you still need the missing opening-time record?
Caleb|We need the history. The [[moisture sensitivity level::The moisture sensitivity level identifies a package's classification for moisture-related handling; it is not evidence that this reel's actual exposure stayed within its requirements.]] on the label does not tell us how this particular reel was handled after opening.
Sora|The bag has a recent resealing date. Someone suggested using that as a fresh start for the clock.
Caleb|Resealing alone does not establish a reset of [[floor life::Floor life concerns the permitted exposure under specified conditions before the relevant assembly process; a new bag seal alone does not establish a fresh exposure allowance.]]. We must follow the applicable product and handling requirements, not invent a new allowance.
Sora|I will look for the material movement records and ask the previous shift when the bag was first opened.
Caleb|Please distinguish a confirmed record from an estimate. We need the [[cumulative exposure::Cumulative exposure concerns the relevant accumulated time and conditions after opening; an undocumented interval cannot be treated as zero simply because the reel was resealed.]] and storage conditions, including any interval we cannot account for.
Sora|There is a humidity indicator card in the bag. Does its current appearance prove that the reel was always stored correctly?
Caleb|No. The [[humidity indicator card::A humidity indicator card provides an indication relevant to humidity within the package under its specified interpretation; it does not reconstruct the complete historical exposure record.]] is one part of the applicable assessment. It is not a complete time history of every earlier handling event.
Sora|The supplier also gives shelf-life information. I should not use the remaining months there as an answer to the missing floor-life record.
Caleb|Correct. [[Shelf life::Shelf life concerns storage over a defined period under stated conditions; it is a different question from post-opening floor life before assembly.]] and post-opening exposure are different questions. Keep the packaging and storage conditions attached to either statement.
Sora|Could the team simply choose a baking cycle from a similar component? I do not want a language misunderstanding to become an improvised process instruction.
Caleb|No. Any conditioning must follow the applicable approved requirements for the actual part, package, and materials. This conversation does not prescribe a temperature or duration.
Sora|Then I will keep the reel identified and unavailable for routine issue while the responsible team reviews the missing history under our procedure.
Caleb|Yes. The [[disposition::Disposition is the authorized decision about the material's next route after reviewing the relevant evidence and requirements; resealing does not supply that decision.]] must be recorded. A neat bag and a current label are not the same as an authorized material decision.
Sora|I can give production an update now: exact reel identified, exposure history incomplete, review requested. I should not call the devices damaged either.
Caleb|That is accurate. Missing evidence means the status is unresolved; it does not establish a physical failure in every device.
Sora|If we find the original records, I will send them with their source and timestamps rather than replacing the unknown interval with a recollection.
Caleb|Good. Preserve the difference between the recovered record and anyone\'s estimate so the reviewer can assess the actual basis.
Sora|I will also ask the team to improve the handover field for opening time. We should not face the same missing-history question on the next reel.
Caleb|Agreed. Resolve this reel through the approved process, then address the record gap without claiming that a better form retrospectively proves its handling was acceptable.''',
        transfer_title='Shelf life is used to dismiss an unknown exposure interval',
        transfer_setup='A device reel is within its stated storage shelf life, but its post-opening exposure history is incomplete.',
        transfer='''Coordinator: Storage shelf life does not resolve the missing exposure ___.|history|The storage period and post-opening handling record address different requirements.
Engineer: Identify the actual part, package, and applicable handling ___.|requirements|The assessment must use the requirements for the specific material rather than a similar component.
Coordinator: Keep unknown time separate from a confirmed ___.|record|An undocumented interval must not be treated as a verified value.
Engineer: Await the authorized material decision before routine ___.|issue|The unresolved handling status needs the applicable disposition before normal production issue.''',
        reference=('Texas Instruments: Product Shelf Life', 'https://www.ti.com/quality-reliability/quality/product-shelf-life.html')),
]
