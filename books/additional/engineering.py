"""Original simulation, substitution, and experimental-design conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A smoother plot is not a convergence study',
        skill='Challenge a simulation claim by asking about the quantity of interest, model assumptions, and supporting evidence.',
        setup='Three finite-element runs use progressively finer meshes. Displacement changes little, but peak stress at an idealized sharp corner keeps increasing. The design lead wants a green pass label. No acceptance threshold or release conclusion is supplied.',
        cast='Yara|Structural analyst\nFinn|Design lead',
        dialogue='''Finn|The latest plot looks much smoother. Can we call the model converged and put the result into the release review?
Yara|We need to name the [[quantity of interest::The quantity of interest is the specific output used for the intended assessment; different outputs may behave differently under refinement.]]. Displacement changes little between these runs, but the peak stress keeps rising.
Finn|I assumed a finer mesh improved every result in the same way. Does the stable displacement not settle the whole model?
Yara|No. [[Mesh convergence::Mesh convergence concerns the behavior of a specified result as the discretization is refined; stability of one output does not establish it for every output.]] concerns the relevant output and purpose. One stable measure does not establish stability for every value.
Finn|The rising stress is at that sharp inside corner. Could the model geometry itself explain why the local maximum does not settle?
Yara|A [[stress singularity::A stress singularity can occur at an idealized geometric or loading feature, producing a local stress that does not converge to a finite value with refinement.]] is one possibility to investigate. We must assess the idealization rather than automatically interpret each higher peak as a new physical measurement.
Finn|But we should not simply delete the red area from the plot and call the design satisfactory either.
Yara|Exactly. We need a justified assessment of the actual feature and intended failure criterion, with the limitations visible. Changing the display is not solving the engineering question.
Finn|What should the review package show about the supports and loads? The slide currently only has the colored result.
Yara|The [[boundary conditions::Boundary conditions define how the modeled system is constrained or interacts with its surroundings; they must represent the intended assessment adequately.]], load case, material assumptions, geometry, and relevant solution settings. The picture alone does not tell reviewers what physical problem we solved.
Finn|The supplier says their model uses the same material name. Should we expect identical results when we compare them?
Yara|Not without checking the actual properties, formulations, geometry, and conditions. A shared label does not establish equivalent inputs or methods.
Finn|We have also checked the implementation against a known calculation. Is that the same as showing that the model represents the real assembly?
Yara|No. [[Verification::Verification addresses whether the model implementation and numerical solution are correct for the specified model; it is distinct from assessing representation of reality.]] and comparison with relevant physical evidence answer different questions. Passing a numerical check does not automatically validate the intended real-world use.
Finn|Then the hardware comparison still matters. We need to say which measurements and conditions support the use we are proposing.
Yara|Yes, and include [[sensitivity analysis::Sensitivity analysis examines how outputs change when selected inputs or assumptions vary; it helps identify which uncertainties matter to the conclusion.]] where appropriate. A conclusion that changes sharply with an uncertain input needs that sensitivity explained.
Finn|For today, I will remove the blanket green label. We can report stable displacement in these runs and the unresolved local-stress interpretation separately.
Yara|That is accurate. I will provide the refinement results and the model assumptions for review, without treating the visual smoothness as acceptance evidence.
Finn|Please also identify what further work is needed for the release question. The reviewers need an actionable gap, not just a warning that models have limitations.
Yara|I will link each open question to the intended claim. That lets us decide what the analysis can support and what still requires assessment.''',
        transfer_title='One stable output is used to approve every output',
        transfer_setup='A thermal model gives a stable average temperature under mesh refinement, but its local peak is still changing materially.',
        transfer='''Lead: Stability of the average does not establish the local ___.|peak|Different outputs may converge at different rates, so one stable measure cannot settle the other.
Analyst: State the specific quantity of interest for the ___.|assessment|The intended assessment determines which output requires adequate supporting evidence.
Lead: Keep the remaining numerical limitation visible in the ___.|report|The report must disclose the unresolved behavior instead of hiding it behind an average.
Analyst: A smooth image is not an acceptance ___.|criterion|Visual appearance does not replace the defined technical basis for accepting the result.''',
        reference=('COMSOL: Finite Element Mesh Refinement', 'https://www.comsol.com/multiphysics/mesh-refinement')),
    scenario(
        title='The replacement fits, but is it an approved alternate?',
        skill='Evaluate a proposed component substitution across requirements and product configuration.',
        setup='A proposed replacement sensor has the same connector and envelope dimensions as the unavailable original. Its output scale, accuracy over temperature, and environmental rating remain unassessed. The bill of materials lists only the original. A buyer asks about production use.',
        cast='Milo|Buyer\nSerena|Design engineer',
        dialogue='''Milo|The usual sensor is unavailable. This one fits the same space and connector, and the supplier calls it a drop-in replacement. Can I order it for production?
Serena|Send me the exact part number and datasheet. A matching envelope establishes part of the [[form-and-fit::Form-and-fit concerns physical characteristics and compatibility at the mounting or connection interface; it does not establish equivalent function or performance.]] comparison, not the complete engineering equivalence.
Milo|The connector looks identical in the photograph. I have not compared the pin assignments or electrical characteristics yet.
Serena|We need the actual [[interface requirements::Interface requirements define the relevant mechanical, electrical, and information connections; a similar connector appearance does not demonstrate compliance.]], including those details. A photograph cannot establish that two connected parts behave compatibly.
Milo|What about the output? The supplier lists the same measured quantity, but the scale is on a different page of the datasheet.
Serena|Compare the [[transfer function::The transfer function here describes the relationship between the measured input and the sensor output; a changed scale can affect downstream interpretation.]]. Measuring the same quantity does not mean the receiving system can interpret the output without a change.
Milo|I also see an accuracy figure measured at room temperature. Our existing requirement covers a wider operating range.
Serena|Then we need evidence across the applicable conditions. A favorable room-temperature value does not automatically meet an accuracy-over-temperature requirement.
Milo|The supplier says they sell it to several similar customers. I can ask for supporting information, but that is not our product assessment.
Serena|Right. We should compare our requirements, including environmental and reliability needs, and identify the gaps. Other customers may have different configurations and use conditions.
Milo|Could I add the part to the purchasing list while engineering finishes the comparison? That would make it easier to place the order quickly later.
Serena|Keep it as a candidate. The controlled [[bill of materials::The bill of materials identifies the parts belonging to the defined product configuration; listing a candidate as approved would misstate its status.]] must not show it as a production-approved part before the required decision.
Milo|Understood. Any samples for evaluation would need their own purchase purpose and handling so they are not mistaken for production stock.
Serena|Exactly. An [[approved alternate::An approved alternate has completed the applicable assessment and approval for its defined use; a supplier recommendation or evaluation sample does not establish that status.]] has a specific assessed use. We should not let a convenient stock code imply approval across every product.
Milo|If the comparison supports a change, do we also need to identify which units or builds can use it?
Serena|Yes. The [[effectivity::Effectivity defines where or when an approved change applies, such as specified builds or serial ranges, avoiding an uncontrolled mix of configurations.]] needs to be clear, along with any associated documentation, software, test, or service implications.
Milo|I will give you the shortage timing, exact candidate details, and what the supplier can provide. I will not promise production availability yet.
Serena|I will return a requirement-by-requirement comparison and the required review steps. We can show which checks are complete and which still block a decision.
Milo|That gives planning a real status: candidate found, equivalence under assessment, no production substitution approved.
Serena|Yes. The goal is a workable alternative with a documented basis, not merely a part that can be plugged into the same connector.''',
        transfer_title='A sample order becomes an apparent production approval',
        transfer_setup='A buyer orders a candidate component for engineering evaluation. The purchasing record mistakenly labels it an approved production alternate.',
        transfer='''Engineer: These parts were ordered for evaluation, not production ___.|use|The order's stated purpose is assessment and does not authorize installation in production products.
Buyer: Correct the status without losing the purchase ___.|history|The record should accurately show the correction while preserving what was ordered and why.
Engineer: Complete the comparison against the applicable ___.|requirements|Equivalence must be assessed against the relevant product requirements, not assumed from availability.
Buyer: Keep the candidate separate from approved ___.|alternates|An unassessed candidate must not appear to have the same status as an authorized substitute.'''),
    scenario(
        title='Two settings changed, so which one improved the result?',
        skill='Negotiate an experiment that separates factors and measures variation without overstating a pilot result.',
        setup='One bench run uses fan setting A and vent X; another uses fan B and vent Y. The second records a lower temperature, but ambient conditions also differ. The team discusses a follow-up design, not authorized test settings or a release decision.',
        cast='Harper|Engineering lead\nDae|Test engineer',
        dialogue='''Harper|The second prototype ran cooler. Can we say vent design Y is responsible and recommend it to the design review?
Dae|Not from these two runs. We changed two [[factors::Factors are the input variables being studied; both fan setting and vent design changed between these runs, so their separate effects are not established.]] together, and the ambient temperature was different as well.
Harper|Then the fan setting could explain some of the difference. We have not tested A with Y or B with X.
Dae|Exactly. The [[design matrix::The design matrix identifies the planned combinations of factor settings; it exposes missing combinations needed for the intended comparison.]] should show the combinations needed to address our question, rather than only the two configurations that happened to be available.
Harper|Would looking at both factors together help us see whether the effect of the vent depends on the fan setting?
Dae|Yes. That is an [[interaction::An interaction means the effect of one factor depends on the level of another; separate single-change conclusions may miss that relationship.]] question. We should choose a reviewed design capable of examining it instead of assuming the two effects simply add together.
Harper|We also need to define cooler. Are we comparing the same sensor location, the same elapsed point, and the same summary of the temperature data?
Dae|We need a precise [[response variable::The response variable is the measured outcome of the experiment, with its location, timing, and calculation defined so results are comparable.]]. Otherwise the runs might use different summaries while the slide presents them as one measure.
Harper|The team suggests taking several readings from the same run and treating them as several independent tests. That would give us a larger count.
Dae|Repeated readings help describe that run, but they are not automatically independent [[replicates::Replicates repeat the experimental treatment on appropriate independent experimental units or runs; multiple readings within one run do not automatically provide them.]]. The plan must distinguish within-run readings from independently repeated runs.
Harper|How should we handle changing ambient conditions? We cannot assume the laboratory stays identical throughout the work.
Dae|Record the relevant conditions and consider them in the design. Depending on the constraints, blocking may help account for known variation rather than let it follow one design option systematically.
Harper|Could we run all X configurations first and all Y configurations afterward to make setup easier?
Dae|That may confound design with time. Consider appropriate [[randomization::Randomization varies the allocation or order to reduce systematic association with uncontrolled effects; practical restrictions must be handled explicitly in the design.]] or a justified restricted design, while preserving the applicable safety and test controls.
Harper|I will not prescribe the run order in the review meeting. Please bring a plan showing the comparisons, repeated runs, and practical constraints.
Dae|I will also show what conclusions the proposed design can and cannot support. A limited pilot may identify a useful direction without establishing every operating condition.
Harper|For the existing result, we can say the B-and-Y run recorded a lower temperature under its stated conditions. We cannot assign that difference solely to the vent.
Dae|Correct. Preserve both runs and the ambient data. The first comparison is informative, but its limitations need to travel with the result.
Harper|Once the plan is reviewed, we can decide the work and resources. Until then, this discussion should not be read as permission to change the bench procedure.
Dae|Agreed. We are defining a better question and evidence plan, not converting an uncontrolled comparison into an approved design choice.''',
        transfer_title='Repeated readings are counted as independent trials',
        transfer_setup='One prototype undergoes one test run. Ten sensor readings from that run are described as ten independent trials.',
        transfer='''Lead: Ten readings from one run are not automatically ten independent ___.|trials|Measurements within a single run do not automatically represent independent repetitions of the experiment.
Engineer: Identify the experimental unit and the source of ___.|variation|The design must establish what is independently repeated and which variation the evidence captures.
Lead: Keep the measurement count distinct from the run ___.|count|The number of readings and the number of test runs answer different questions.
Engineer: Limit the conclusion to what the design actually ___.|supports|A conclusion must reflect the experimental design rather than an inflated apparent sample size.''',
        reference=('NIST: Choosing an Experimental Design', 'https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm')),
]
