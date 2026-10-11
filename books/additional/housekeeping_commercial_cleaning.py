"""Original contact-time, cleaning-assessment, and workload conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The clock is not the whole check",
        skill="Read a product-use requirement accurately and explain why elapsed time alone does not establish compliance.",
        setup="Fictional record review, not chemical-use instructions: the approved product directions for the specified hard, nonporous surface require five minutes continuously visibly wet. The recorded application was 07:42; the surface was observed wet until it dried at 07:46. At 07:47, worker Farah asks whether the requirement was met. No correction or release is recorded.",
        cast="Farah|Cleaner reviewing the record\nBen|Cleaning supervisor",
        dialogue="""Farah|The timer reached five minutes at seven forty-seven, but the surface had dried a minute before that. Can I mark the contact-time requirement complete?
Ben|No. Check the [[directions for use::Directions for use specify the relevant surface and application conditions; the timer alone does not establish that they were met.]], not only the timer. What exact condition is attached to those five minutes?
Farah|The specified hard, nonporous surface has to stay visibly wet continuously. The recorded start was seven forty-two, and it dried at seven forty-six.
Ben|Then the stated [[five minutes::The fictional directions require five continuous wet minutes; four wet minutes plus one dry minute do not satisfy that requirement.]] were not achieved in that record. Four minutes wet followed by one dry minute is not the same condition.
Farah|If it had stayed wet continuously from seven forty-two, the five-minute point would have been seven forty-seven.
Ben|Yes, [[07:47::07:42 plus five minutes is 07:47, but that clock time would meet the duration only if the required wet condition had continued.]] is the arithmetic endpoint. It does not override what actually happened to the surface before then.
Farah|I wrote the drying time in my notes. I should retain that rather than change the entry to match what the timer was meant to show.
Ben|Exactly. The [[application record::The application record must retain the actual start and drying times rather than being edited into an unsupported successful result.]] needs the observed facts. We can then arrange the required correction under the actual product directions and site procedure.
Farah|Would a photograph at the start be enough to prove that the surface stayed wet throughout?
Ben|No. It shows that moment only. The requirement is [[visibly wet::Visibly wet describes the required surface condition throughout the contact period, not merely at the start or the final photograph.]] throughout the specified period, not just for one photograph.
Farah|Someone suggested using the same timing on the upholstered chair beside it. Is that covered by the hard-surface instruction?
Ben|Not from this information. Check [[surface compatibility::Surface compatibility and approved use must be established for the actual material; hard-nonporous directions do not automatically cover upholstery.]] and the approved use for that material. The hard-surface instruction is not permission to treat upholstery the same way.
Farah|The product's safety data sheet is available too. Should I take a remembered time from that instead of this use instruction?
Ben|Use the current applicable directions for the exact product and task, with the matching hazard information and training. Do not replace them with a remembered number.
Farah|And I should not improvise a stronger concentration or combine products to try to shorten the time.
Ben|Correct. This record review does not authorize a new mixture or application method. Any correction must follow the real instructions and workplace controls.
Farah|I will report application at seven forty-two, drying at seven forty-six, and the five-minute wet condition not met. No correction has yet been recorded.
Ben|That is accurate. The issue is the unmet condition, not a claim that the timer malfunctioned or that the surface was never cleaned.
Farah|Once the authorized correction is performed, I will record it separately with its actual observations rather than erase the earlier result.
Ben|Good. Keep the original record and follow-up linked. A planned correction, an elapsed five minutes, and an approved return to use are separate facts.""",
        transfer_title="Retain the wet-condition failure",
        transfer_setup="Fictional directions require three continuous wet minutes on the specified surface. Application was 14:10; it remained wet until drying at 14:12. No later correction is recorded. Calculate time and report status only; do not invent treatment instructions.",
        transfer="""Cleaner: The required continuously wet period is ___ minutes.|three|The supplied directions require three minutes, not the two minutes actually observed wet.
Supervisor: With continuous wetness, the arithmetic endpoint would be ___ .|14:13|Adding three minutes to 14:10 gives 14:13, conditional on the stated wet requirement being maintained.
Cleaner: The recorded drying time was ___ .|14:12|The surface dried at 14:12, before the required endpoint.
Supervisor: The stated wet-time requirement was ___ .|not met|Only two continuous wet minutes are recorded; waiting while dry does not supply the missing wet minute.""",
        reference=("US EPA: product directions, surface types, and wet contact time", "https://www.epa.gov/pesticide-registration/selected-epa-registered-disinfectants"),
    ),
    scenario(
        title="What the marker result proves",
        skill="Report sampled cleaning performance without converting tracer removal into a claim of disinfection or universal cleanliness.",
        setup="Fictional staff training audit: eight predetermined high-touch spots were marked with an approved fluorescent tracer. Six marks were fully removed after cleaning; two remained partly visible. This site's scoring counts only fully removed marks as passes. After authorized re-cleaning, both remaining marks were fully removed. No microbial culture or ATP test was performed.",
        cast="Ravi|Cleaner\nElena|Quality supervisor",
        dialogue="""Ravi|The panels looked clean under normal light, but your check showed part of a mark on two of the eight spots. How should I report that?
Elena|Start with the [[fluorescent marker::A fluorescent marker is a tracer placed before cleaning; checking its removal evaluates the marked cleaning process, not the presence of specific pathogens.]] results. Six marks were fully removed and two were partially removed under the stated scoring rule.
Ravi|So the partial ones do not count as passes, even though some of the mark disappeared?
Elena|Correct. The [[first-pass result::Six fully removed marks out of eight sampled spots equals a 75% first-pass result under this site's rule.]] is six out of eight, or seventy-five percent. Do not turn partially removed into fully removed.
Ravi|Could I describe the room as seventy-five percent disinfected? That sounds like the same proportion, but I am not sure it means the same thing.
Elena|It does not. This is a [[process check::The marker exercise checks physical removal at selected spots; it is not a measurement of the percentage of a room disinfected.]] at selected spots, not a percentage of the room disinfected or a count of germs killed.
Ravi|Then my message should name the eight sampled spots and the two that needed more attention, rather than say a quarter of the whole room was missed.
Elena|Exactly. Keep the [[sample scope::Eight predetermined marked spots are the sample; their result cannot establish the condition of every surface in the room or building.]] visible. We did not test every surface, and this marker result cannot prove their condition.
Ravi|After the approved re-cleaning, you checked the two remaining marks again and found both fully removed. Does the report now say eight out of eight at first pass?
Elena|No. Record the [[recheck::The recheck records the later removal of both remaining marks after corrective work; it does not rewrite the original six-of-eight result.]] separately. Keep the original six out of eight and the later two successful corrections.
Ravi|That way the report shows improvement without hiding that some work needed repeating. The first result remains useful for training.
Elena|Yes. We can discuss the actual missed locations and work pattern, then agree a practical improvement instead of treating a percentage as a personal accusation.
Ravi|Someone asked whether our lamp was detecting bacteria. It only detects the tracer used for this check, correct?
Elena|Correct. The marker result does not measure [[microbial contamination::Microbial contamination concerns microorganisms; fluorescent-tracer removal does not directly measure them or establish their absence.]]. There was no microbial culture or other organism-specific test in this exercise.
Ravi|I have also heard of ATP testing. Is that simply another name for this fluorescent mark?
Elena|No. ATP is adenosine triphosphate, and those tests indicate organic material through a different method. They are not a direct count of a particular pathogen either.
Ravi|So a low result on an ATP instrument would not automatically prove that every disinfection requirement had been followed.
Elena|Right. Interpret each method within its limits and the approved program. Instrument readings, visible appearance, tracer removal, and required product-use conditions are different evidence.
Ravi|My summary is six of eight fully removed initially, two partial; both partial marks fully removed after re-cleaning. I will not claim the whole room is germ-free.
Elena|That is a useful report. Retain the sampled locations, scoring rule, original result, and follow-up so the next review compares like with like.""",
        transfer_title="Keep first pass and recheck separate",
        transfer_setup="Ten marked spots are assessed. Seven marks are fully removed and three partly remain; only fully removed marks count as passes. After authorized correction, all three remaining marks are removed. No microbial test is supplied.",
        transfer="""Cleaner: The initial fully removed count is ___ .|seven|Seven spots pass the stated full-removal rule; partial removal does not count as a pass.
Supervisor: The first-pass percentage is ___ .|70%|Seven divided by ten equals 70%, not the later post-correction total.
Cleaner: The number successfully corrected at recheck is ___ .|three|The three initially partial marks are removed after correction and recorded as a separate follow-up.
Supervisor: Absence of pathogens is ___ by this marker result.|not established|Tracer removal assesses the sampled cleaning process, not the absence of microorganisms.""",
        reference=("CDC: assessment methods and limitations of fluorescent-marker and ATP checks", "https://www.cdc.gov/healthcare-associated-infections/hcp/cleaning-global/procedures.html"),
    ),
    scenario(
        title="Two people do not erase setup",
        skill="Convert a task rate into labor-hours and elapsed time while retaining preparation, closeout, and the actual scope.",
        setup="Fictional planning exercise: 600 square meters of identified cleanable floor at 200 square meters per labor-hour for the defined task. Two trained cleaners can divide the work equally without interference. Each needs ten minutes of setup and five of closeout, done concurrently. Both start at 09:00. Rates exclude these tasks, breaks, delays, and any drying or release time.",
        cast="Malik|Cleaning team lead\nJo|Scheduling coordinator",
        dialogue="""Malik|The client wants the floor task finished by ten thirty. We have two people starting at nine. Can we check whether the plan actually fits?
Jo|First, confirm the [[cleanable area::The calculation covers 600 square meters of identified cleanable floor, not the total building area or unspecified extra tasks.]]. We have six hundred square meters for this defined task, not every surface in the building.
Malik|Yes. The planning rate is two hundred square meters per labor-hour. That is one person's productive task time, not a whole crew's rate.
Jo|Then six hundred divided by two hundred gives three [[labor-hours::At 200 square meters per labor-hour, 600 square meters requires three person-hours of the defined floor task.]] for the floor task itself.
Malik|With two people sharing it equally, each handles three hundred square meters. That would take each person one and a half hours at this assumed rate.
Jo|Correct. Under the equal-work assumption, the floor work takes [[ninety minutes::Three labor-hours divided equally between two cleaners gives 1.5 hours, or 90 elapsed minutes, for floor work alone.]] of clock time. But that does not include getting ready or putting equipment away.
Malik|Both need ten minutes before floor work starts and five minutes afterwards. Those activities happen at the same time for the two workers.
Jo|So add fifteen minutes to the [[elapsed time::Concurrent ten-minute setup and five-minute closeout add fifteen elapsed minutes, making 105 minutes from the shared start.]]. Ninety plus fifteen is one hundred five minutes from their shared start.
Malik|Starting at nine, setup ends at nine ten; floor work ends at ten forty; closeout ends at ten forty-five.
Jo|Yes, the planned finish is [[10:45::09:00 plus ten setup minutes, ninety floor-work minutes, and five closeout minutes is 10:45, before any unmodeled delay or release time.]]. That is fifteen minutes later than the client's requested finish, even before any unmodeled delay.
Malik|For labor budgeting, each person's fifteen minutes still counts. Together that adds thirty person-minutes, or half a labor-hour.
Jo|Right. The total [[labor budget::Three floor-task labor-hours plus two workers at fifteen minutes each gives 3.5 labor-hours, not three hours or 105 person-minutes.]] is three and a half hours: three productive task hours plus half an hour of combined setup and closeout.
Malik|Could I call ten forty-five the time the floor is definitely ready for everyone to walk on?
Jo|No. This calculation excludes drying and any required inspection or release. It estimates the stated work, not an all-clear for access.
Malik|And if the two workers cannot divide the area cleanly, the simple halving of task time may not hold.
Jo|Exactly. Shared equipment, obstructions, access limits, and different work conditions can change the plan. The fictional rate is not a universal speed requirement.
Malik|I will tell the client that the current plan misses ten thirty by at least fifteen minutes. We need a revised arrangement rather than asking people to skip setup.
Jo|Yes. Check an earlier authorized start, suitable staffing, or an agreed scope or deadline change. None is already approved by this arithmetic.
Malik|The summary is six hundred square meters, three floor-task labor-hours, three and a half total labor-hours, and an estimated ten forty-five finish under these assumptions.
Jo|That makes the decision clear. Keep the scope and exclusions beside the estimate so an optimistic number does not silently replace the actual work plan.""",
        transfer_title="Budget people and clock time",
        transfer_setup="A fictional 900-square-meter task has a planning rate of 300 square meters per labor-hour. Three workers can divide it equally. Each has ten minutes setup and five closeout concurrently, outside that rate. All start at 13:00; no other time allowances are included.",
        transfer="""Lead: The productive floor task requires ___ labor-hours.|3|Nine hundred divided by three hundred equals three labor-hours before the separate allowances.
Planner: Dividing the task equally gives ___ minutes of productive clock time.|60|Three labor-hours divided among three workers gives one hour each, or sixty elapsed minutes.
Lead: The calculated work finish is ___ .|14:15|From 13:00, add ten minutes setup, sixty minutes floor work, and five minutes closeout.
Planner: Including each worker's allowances, the total is ___ labor-hours.|3.75|Three task hours plus three workers times fifteen minutes equals 3.75 labor-hours; the elapsed time is only 1.25 hours.""",
        reference=("ISSA: calculating cleaning time from task area and production rate", "https://www.issa.com/articles/how-to-calculate-cleaning-times/"),
    ),
]
