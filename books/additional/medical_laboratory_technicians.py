"""Original laboratory QC, dilution-record, and reporting-limit conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Three and a half standard deviations, not three and a half percent",
        skill="Explain a control statistic with the correct denominator and a case-specific action rule.",
        setup="Fictional control M: established mean 100 mg/L, standard deviation (SD) 2 mg/L, observed result 107 mg/L. The target statistics apply to this control and lot. Local rule: absolute z-score of 3 or more triggers a hold and authorized review. The affected reports are already withheld and the lead notified. Use z = (result - mean)/SD and coefficient of variation (CV) = SD/mean x 100%. No review outcome or restart permission is supplied.",
        cast="Noor|Laboratory technician\nBen|Quality lead",
        dialogue="""Noor|The worksheet says the control is three-point-five percent high. I think it mixes two different calculations. Can we correct that before the review?
Ben|Yes. The result is seven milligrams per liter above the established mean. Dividing that difference by the two-milligram-per-liter [[standard deviation::Standard deviation is the supplied spread statistic of 2 mg/L; dividing the 7 mg/L difference by it gives 3.5, not 3.5 percent.]] gives three-point-five.
Noor|So the result is three-and-a-half standard deviations above the mean. For percentage difference, the denominator would be the mean of one hundred.
Ben|Exactly. The [[z-score::The z-score is (107 - 100)/2 = +3.5, a unitless standardized distance above the established mean; the percentage difference is separately seven percent.]] is positive three-point-five, while the percentage above the mean is seven percent. Keep both labels with their numbers.
Noor|Our local hold rule includes an absolute score of exactly three. This result is above that boundary, and the hold is already in place.
Ben|Correct. An [[inclusive limit::The supplied local rule includes an absolute z-score equal to three, as well as values greater than three; it is not a universal laboratory rule.]] includes equality. Don't rewrite the rule as greater than three when describing why it applies.
Noor|What does two divided by one hundred tell us? Someone has added two percent next to the control's historical statistics.
Ben|That is the [[coefficient of variation::The supplied established SD divided by its mean, multiplied by one hundred, is two percent; this CV describes those established statistics, not proof that the current run is acceptable.]] for the supplied statistics. It does not make this particular result acceptable or establish a completed review.
Noor|Would it be accurate to call this a trend? We have only this one observation in the exercise, not a sequence moving upward.
Ben|No. A [[trend::A trend requires a pattern across observations; the single supplied high point cannot establish a sustained directional pattern or its cause.]] needs a pattern over time. A single point can trigger the stated rule without telling us why it occurred.
Noor|Then I should not write that calibration caused it, or that recalibration is the solution. Neither is in the evidence we have.
Ben|Right. The [[review outcome::No authorized review outcome is supplied; the hold and correct arithmetic do not establish a cause, technical remedy, or permission to release the affected reports.]] remains pending. Preserve the result and its context rather than replacing an unexplained observation with a guessed cause.
Noor|On the Levey-Jennings display, I would locate this point above the plus-three-standard-deviation line, provided those are the same applicable target statistics.
Ben|Yes. The stated target and lot match here. A graph can make the distance visible, but the picture does not supply a missing investigation.
Noor|I'll revise the note to result one hundred seven, mean one hundred, SD two, all in milligrams per liter, and z positive three-point-five.
Ben|Include the separate seven-percent difference only if you label its denominator. Otherwise readers may mistake it for the CV or standardized score.
Noor|The established CV is two percent. I will not describe that as this run's newly demonstrated precision from one observation.
Ben|Good. Nor should the instrument's ready indicator be treated as cancellation of the report hold. Those are different kinds of status.
Noor|The handoff will preserve the held reports, notification already made, calculation correction, and pending authorized review.
Ben|That gives the next reviewer a usable record without turning a language exercise into instructions to adjust the analyzer or release results.""",
        transfer_title="Equality still triggers this local rule",
        transfer_setup="New fictional control: established mean 200 mg/L, SD 5 mg/L, observed 215 mg/L. Same local rule: absolute z-score of 3 or more triggers a hold and review. The lead is notified; no release is authorized.",
        transfer="""Technician: The result exceeds the mean by ___ mg/L.|15|Subtract the established mean of two hundred from the observed result of two hundred fifteen.
Lead: The z-score is positive ___ .|three|The difference of fifteen divided by the SD of five equals positive three.
Technician: The established CV is ___ percent.|2.5|Five divided by two hundred, multiplied by one hundred, equals two-point-five percent.
Lead: The affected reports remain ___ .|held|The case-specific rule includes equality at an absolute z-score of three, and no release is authorized.""",
        reference=("WHO laboratory quality training, module 7: SD, CV and control-chart terminology; local rule is fictional", "https://extranet.who.int/hslp/who-hslp-download/package/501/material/191"),
    ),
    scenario(
        title="The analyzer already applied the dilution factor",
        skill="Reconcile raw and adjusted values without multiplying an already adjusted result twice.",
        setup="Fictional training record: one sample volume plus four diluent volumes, factor 5. Raw diluted-sample reading: 40 mg/L. Confirmed analyzer flag: factor already applied; adjusted output: 200 mg/L. An unreleased laboratory information system (LIS) draft multiplies by 5 again, showing 1,000 mg/L. This is not a patient report or permission to perform a dilution, alter settings, or release results.",
        cast="Noor|Laboratory technician\nImani|Laboratory systems specialist",
        dialogue="""Noor|The instrument output is two hundred milligrams per liter, but the unreleased information-system draft says one thousand. I want to trace where the extra multiplication happened.
Imani|Start with the recorded [[dilution factor::One volume of sample plus four volumes of diluent gives five final volumes per one sample volume, so the recorded dilution factor is five, not four.]]. One sample volume plus four diluent volumes means a factor of five, not four.
Noor|The raw reading from the diluted material is forty milligrams per liter. Multiplying forty by five gives two hundred for the original-sample equivalent.
Imani|Correct. Keep the [[raw reading::The raw diluted-sample reading is forty mg/L before the factor is applied; it must remain distinguishable from the adjusted two-hundred-mg/L output.]] separate from the adjusted output in the comparison. Both happen to use the same concentration unit.
Noor|The documented analyzer flag confirms that it already applied five. That is stronger evidence than guessing from the size of the displayed number.
Imani|Yes. The [[factor-applied flag::The setup explicitly confirms the analyzer's documented flag, so its output of two hundred mg/L already includes the factor and must not be treated as an unadjusted reading.]] explains what the output represents. Instrument and interface behavior must be checked, not assumed identical across systems.
Noor|Then the draft's second multiplication is the source of one thousand. It is five times the correctly adjusted output, not a different dilution.
Imani|That is [[double application::Multiplying the already adjusted two hundred by five produces one thousand, applying the same dilution factor twice rather than adding new measurement information.]] of the same factor. We need to preserve that distinction in the discrepancy record.
Noor|Could someone describe the difference as a units conversion? Forty, two hundred, and one thousand are all labeled milligrams per liter here.
Imani|No. The [[unit label::All three supplied values use mg/L, so the discrepancy is not an mg/L-to-another-unit conversion; the extra multiplication is the documented difference.]] has not changed. Don't attach a conversion explanation to an arithmetic step that applied a dilution factor again.
Noor|I can identify the mismatch, but that does not mean I should overwrite the draft or change the interface setting during this discussion.
Imani|Exactly. The [[reconciliation record::The reconciliation record should retain the raw value, factor, confirmed flag, adjusted output and discrepant draft for authorized review; identifying the mismatch does not itself authorize edits or release.]] should retain the evidence and go through the authorized review and correction process.
Noor|I'll list raw forty, factor five, adjusted two hundred, draft one thousand, with the same unit alongside each concentration.
Imani|Also identify which field supplied each value. A screenshot of a number alone can lose the distinction between raw and adjusted fields.
Noor|We should keep the original discrepant draft traceable if an authorized correction is made. A clean final value would not explain what changed.
Imani|Agreed. Preserve the applicable change history. Do not remove the evidence needed to understand the repeated multiplication.
Noor|And we should not claim this proves every connected analyzer handles dilution the same way. This flag was verified for this record.
Imani|Right. The historical manufacturer example supports why system-specific handling matters, not a universal setting or current operating procedure.
Noor|My handoff will say the arithmetic is reconciled to two hundred, the draft differs by a repeated factor, and release remains unauthorized.
Imani|That separates a checked calculation from permission to issue a report. The responsible reviewer still needs to resolve the record through the actual laboratory process.""",
        transfer_title="Identify the second multiplication",
        transfer_setup="New fictional record: one sample volume plus nine diluent volumes; raw reading 7 mg/L. The confirmed analyzer flag says the factor was already applied, and output is 70 mg/L. An unreleased draft shows 700 mg/L after multiplying again. Authorized review is not complete.",
        transfer="""Technician: The recorded dilution factor is ___ .|10|One sample volume plus nine diluent volumes gives ten final volumes per sample volume.
Specialist: The once-adjusted concentration is ___ mg/L.|70|Seven multiplied by the factor of ten equals seventy, which is the supplied adjusted analyzer output.
Technician: The twice-adjusted draft incorrectly shows ___ mg/L.|700|Multiplying the already adjusted seventy by ten again produces the discrepant seven hundred.
Specialist: Authorized review is still ___ .|pending|The calculation can be checked, but the setup states that authorized review has not been completed.""",
        reference=("Beckman Coulter REMISOL Advance v1.7, historical section 3.14.4: instrument-specific dilution handling, not current operating instructions", "https://www.beckmancoulter.com/download/file/wsr-188029/UG-ADV-UK-17v1.7?type=pdf"),
    ),
    scenario(
        title="Detected does not mean reliably quantified",
        skill="Preserve analytical qualifiers without converting detection into a diagnosis or precise concentration.",
        setup="Fictional assay M: documented detection limit 0.20 mg/L and quantification limit 0.60 mg/L. A validated positive detection call is confirmed; the internal concentration estimate is 0.35 mg/L. This laboratory's stated reporting rule requires 'detected, below quantification limit' for this case, without publishing the estimate as a numerical result. Clinical decision limits are not supplied. The report remains unreleased.",
        cast="Noor|Laboratory technician\nLeila|Reporting reviewer",
        dialogue="""Noor|The screen displays zero-point-three-five milligrams per liter, but the draft report uses a qualifier. Are we omitting a result that the instrument measured?
Leila|The [[internal estimate::The internal estimate is 0.35 mg/L, below the stated 0.60 mg/L quantification limit; its display does not make it a reportable precise numerical concentration under this case's rule.]] is below the stated quantification limit. The display alone doesn't establish that we may publish that number as a reliable concentration.
Noor|Detection is already confirmed through the validated procedure. I should not infer it merely because the displayed estimate is above zero-point-two-zero.
Leila|Correct. The [[detection limit::The stated detection limit is 0.20 mg/L; the case separately supplies a confirmed detection call, rather than authorizing a positive call from a simple numerical comparison alone.]] and the confirmed detection call provide different information. Use the stated call, not an invented interpretation of a screen.
Noor|The quantification boundary is zero-point-six-zero. So detection can be confirmed even though this case does not meet the requirement for a numerical report.
Leila|Yes. The [[quantification limit::The quantification limit concerns measuring an amount with suitable precision and accuracy; the case gives 0.60 mg/L and requires a qualifier below it, rather than a numerical report of 0.35.]] concerns suitable quantitative performance. It is not another name for the detection limit.
Noor|Would writing zero be clearer for the recipient? It would avoid presenting the uncertain zero-point-three-five value.
Leila|No. The required [[reporting qualifier::The case's reporting rule requires detected, below quantification limit; replacing it with zero or not detected would contradict the confirmed detection call.]] is detected, below quantification limit. Zero would contradict the confirmed detection and erase important information.
Noor|Then I also shouldn't say below the detection limit. That is a different boundary and would confuse why this qualifier is being used.
Leila|Exactly. Nor is an analytical limit a [[clinical decision limit::Clinical decision limits concern clinical interpretation and are not supplied here; analytical detection or quantification limits must not be presented as diagnostic or normal-range cutoffs.]]. We have no supplied basis for calling this evidence of a disease or a normal patient finding.
Noor|The two decimal places on the screen look very precise. But the number of printed digits does not establish measurement precision at that concentration.
Leila|Right. [[Display resolution::Display resolution describes how finely a screen presents values; two decimal places do not establish reliable quantification, measurement precision, or clinical significance.]] and demonstrated analytical performance are not the same thing. Keep that distinction when someone asks why the displayed number is not the report.
Noor|Should the report simply say less than zero-point-six? That would retain the upper quantitative boundary but leave out the confirmed detection.
Leila|Use the complete required wording for this case. A bare less-than statement would drop information that the supplied rule says to retain.
Noor|I'll keep the internal estimate in the appropriate traceable record, not move it into a patient-facing numerical field on my own.
Leila|Yes. Follow the actual reporting procedure and authorized review. This language exercise doesn't grant permission to change report fields.
Noor|The background definitions distinguish detection from quantification. They do not supply this fictional laboratory's reporting policy or a clinical decision threshold.
Leila|Correct. The provided policy is part of the case. Do not attribute it to the pharmaceutical analytical-validation reference as a universal clinical reporting instruction.
Noor|My handoff will retain confirmed detection, the below-quantification qualifier, and unreleased status, with no diagnosis or precise published concentration.
Leila|That gives the next reviewer the important distinctions. A cautious message should preserve what is known, not replace it with either false certainty or a false zero.""",
        transfer_title="Retain the positive detection and its qualifier",
        transfer_setup="New fictional assay: detection limit 0.10 mg/L, quantification limit 0.40 mg/L, internal estimate 0.25 mg/L. Detection is confirmed by the validated procedure. The stated local rule requires detected, below quantification limit; the report is unreleased. No clinical interpretation is supplied.",
        transfer="""Technician: The confirmed analytical call is ___ .|detected|The setup explicitly confirms detection; neither zero nor not detected preserves that finding.
Reviewer: The quantification limit is ___ mg/L.|0.40|The case supplies a quantification limit of zero-point-four-zero, distinct from the detection limit of zero-point-one-zero.
Technician: The required qualifier is below the ___ limit.|quantification|The internal estimate lies below the supplied quantification limit, and the case explicitly requires that qualifier.
Reviewer: Clinical significance remains ___ .|unsupplied|No clinical interpretation or clinical decision threshold is supplied, so analytical detection cannot establish one.""",
        reference=("FDA ICH Q2(R2): background definitions of detection and quantification limits, not a clinical reporting policy", "https://www.fda.gov/media/161201/download"),
    ),
]
