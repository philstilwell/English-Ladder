"""Original consulting conversations on reusable knowledge, benefits, and model handover."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Reuse the method responsibly",
        skill="Distinguish reusable methods from protected client material while keeping a proposal moving.",
        setup="Fictional policy permits a generic diagnostic template, but not a former client's confidential deck without permission. Nia created that deck using unpublished site economics and a distinctive operating model. Removing names is not clearance. The prospect permits use of its own supplied public report. A knowledge manager verifies reusable assets.",
        cast="Nia|Consultant\nArun|Engagement partner",
        dialogue="""Nia|The prospect needs a proposal tomorrow. I have a strong diagnostic deck from my last engagement. Could I remove the client name and use its operating-model slides?
Arun|Not on that basis. The [[confidential information::The unpublished site economics and distinctive operating-model details are protected former-client information under the supplied policy; removing a name does not give permission to reuse them.]] includes the site economics and the way the operation is configured, not just the name on the cover.
Nia|I built those slides myself. I thought that made them our method rather than the client's information. The visual structure would save us a lot of time.
Arun|Your authorship does not settle [[reuse rights::Reuse rights determine what material may be used again and on what terms; creating a slide does not automatically authorize reuse of the client information it contains.]]. We need to separate the general method from client data, protected analysis, and engagement-specific restrictions.
Nia|What if I change the labels and round the figures? The prospect would not see the exact numbers or the locations.
Arun|That is not reliable [[de-identification::De-identification reduces identifying details, but distinctive combinations may still reveal the former client; it also does not independently establish permission to reuse confidential material.]]. Someone who knows the market could recognize the combination. More importantly, disguising the material would not itself grant permission to use it.
Nia|Then I should not attach the old deck to the proposal workspace while we decide. The prospect and its advisers have access there.
Arun|Correct. Keep it within its authorized access boundary. Ask the knowledge manager which [[approved asset::An approved asset is material cleared for the intended reuse, such as the stipulated generic diagnostic template; its status must be checked rather than inferred from convenience.]] we can use. The generic diagnostic template is permitted under our policy.
Nia|We can use that structure and populate it from the prospect's public report. They supplied it for this proposal, so we can identify the actual source.
Arun|Yes. Preserve the [[source provenance::Source provenance records where an input came from; using the prospect's identified public report is different from silently importing another client's unpublished figures.]] for each factual statement. Do not carry across the former client's numbers and describe them as an industry benchmark.
Nia|For the proposed analysis, I can describe the questions we would test rather than show a worked result from somebody else's business.
Arun|That is useful to the buyer. Show the decision, work stages, and intended outputs. A credible proposal does not need confidential proof from another engagement.
Nia|May we mention that our team has done a similar engagement? I do not want to imply that the former client endorses this proposal.
Arun|Check the [[client-reference permission::Client-reference permission governs using a client identity or engagement as a reference; it is separate from permission to reuse a method or confidential working materials.]] separately. An approved generic description may be possible, but a named logo, testimonial, or reference contact needs the applicable clearance.
Nia|I will ask the knowledge manager for a cleared example. If none is available tonight, I can still show the planned approach without the old client's details.
Arun|Exactly. We should not make tomorrow's deadline a reason to assume permission. Use material we can substantiate and are authorized to share.
Nia|I will also remove the old-deck shortcut from this proposal's working folder. It points to the restricted engagement and could invite accidental sharing.
Arun|Good. Follow the access and records process without deleting the former engagement's required records. We are correcting the proposal workspace, not erasing the underlying work.
Nia|The revised proposal will use the approved template, the prospect's identified public figures, and a clearly labeled proposed method. No borrowed client economics or implied endorsement.
Arun|Send that version for review. We can demonstrate relevant experience while keeping methods, evidence, permissions, and client confidentiality clearly separated.""",
        transfer_title="Choose material cleared for this pitch",
        transfer_setup="An approved generic process template is reusable. A former client's confidential pricing table is not cleared. A new prospect has supplied its own published annual report for the pitch. No named client reference is authorized.",
        transfer="""Consultant: We can reuse the approved generic ___.|template|The policy explicitly permits this generic asset, unlike the confidential pricing table.
Partner: The old pricing table remains ___.|confidential|Its protected status does not disappear when client labels are removed.
Consultant: New factual inputs can come from the prospect's published annual ___.|report|The prospect supplied that report for this use, so its facts can be attributed to the identified source.
Partner: A named client reference is not ___.|authorized|The facts expressly state that no permission for a named reference has been granted.""",
        reference=("Institute of Management Consultants USA: enforceable code of ethics", "https://www.imcusa.org/about/ethics/code-of-ethics/"),
    ),
    scenario(
        title="Saved time is not all saved cash",
        skill="Explain a benefits bridge without adding overlapping measures or presenting estimates as achieved savings.",
        setup="Fictional forecast: 1,200 hours released annually, valued at $50/hour; regular payroll unchanged. Within this improvement, approved overtime reductions should cut annual spending $20,000. Setup costs $15,000 once. Assume a full first year of benefits and no other cost changes. No benefit has yet been realized.",
        cast="Mina|Consultant\nJon|Client finance lead",
        dialogue="""Mina|The benefits slide says sixty thousand of time savings plus twenty thousand less overtime. Before I use eighty thousand as the headline, can we check the bridge?
Jon|Yes, because those measures overlap. Your [[capacity value::Capacity value converts released time into a monetary indicator, here 1,200 hours times 50 dollars equals 60,000; it is not by itself a reduction in spending.]] is twelve hundred hours at fifty dollars. That describes resource capacity, not sixty thousand coming out of the payroll budget.
Mina|The regular team will stay employed on the same pay. They would use the released time to handle the backlog and reduce the extra hours.
Jon|Then the identified [[cash-releasing benefit::The cash-releasing benefit is the expected 20,000 reduction in overtime spending; unchanged regular payroll cannot be presented as another realized cash reduction.]] is the twenty-thousand overtime reduction. It is part of the same improvement, not an unrelated saving to stack on the time valuation.
Mina|So the headline must not be eighty thousand. Nor should I call the whole sixty thousand cash saved when the regular salary payments stay the same.
Jon|Right. Avoid [[double counting::Double counting would add the overlapping time valuation and overtime saving as if they were independent benefits; the stated facts do not support an 80,000 combined saving.]]. We can report released hours and the separate spending effect, with a clear explanation of their relationship.
Mina|For year one, the spending reduction is twenty thousand and implementation costs fifteen thousand. On our full-year assumption, that leaves five thousand.
Jon|That is the projected [[net cash benefit::Net cash benefit for the stipulated first year is 20,000 expected spending reduction minus 15,000 one-off implementation cost, or 5,000, before any other changes excluded by the exercise.]]. Keep the timing assumption beside it. Starting halfway through the year would not automatically produce a full year's reduction.
Mina|The following year's comparison would show twenty thousand before other changes, since the fifteen-thousand setup cost does not repeat under these assumptions.
Jon|Describe that as the annual [[run-rate benefit::The run-rate benefit expresses the recurring annual spending reduction at the assumed operating level; here it is 20,000, distinct from first-year net cash benefit after setup costs.]], not guaranteed cash in every future year. Workload, staffing arrangements, and sustained adoption could change the result.
Mina|Who should confirm the overtime reduction after launch? The project team can count released hours, but it does not own payroll spending.
Jon|Name a [[benefits owner::The benefits owner is accountable for tracking and supporting realization of the defined benefit; project completion alone does not establish that overtime spending has actually fallen.]] in operations, with finance checking the spending evidence. We need the baseline, measurement period, and treatment of changes in workload.
Mina|Could a quiet month make the result look better even if the process had little effect? We should not attribute every payroll movement to this project.
Jon|Exactly. Compare like periods and document material changes. The bridge needs evidence of what changed and why, not just two totals with a saving label between them.
Mina|I will label the figures forecast, because the process has not gone live. Approval to reduce overtime is not proof that the lower spending has happened.
Jon|Good. When actual results arrive, reconcile them to the forecast and explain differences. Keep the released-capacity measure even if it is useful without becoming cash.
Mina|And we should not manufacture a forty-thousand noncash residual simply by subtracting twenty from sixty. The blended time valuation is not a payroll reconciliation.
Jon|Correct. The two indicators use different bases. Show the hours, valuation assumption, expected overtime reduction, and setup cost without pretending they form an additive accounting total.
Mina|The revised headline will be twelve hundred hours of projected capacity, with twenty thousand expected annual spending reduction and five thousand net cash benefit in the stipulated first year.
Jon|That is a decision-useful comparison. Attach the assumptions and owner, then let the client judge the benefit without an inflated total.""",
        transfer_title="Reconcile a second business case",
        transfer_setup="A proposed change releases 800 hours, valued at $40 per hour. Within the same change, annual contractor spending is expected to fall $12,000. One-off setup costs $7,000. Assume full-year realization and no other changes. Regular payroll is unchanged.",
        transfer="""Consultant: The capacity valuation is $___ thousand.|32|Eight hundred hours multiplied by forty dollars equals thirty-two thousand in time value, not automatically cash saved.
Finance: The annual spending reduction is $___ thousand.|12|The identified cash effect is the contractor-spending reduction, not the full time valuation.
Consultant: First-year net cash benefit is $___ thousand.|5|Twelve thousand less the seven-thousand one-off setup cost leaves five thousand on the stated assumptions.
Finance: Adding the overlapping time and spending indicators would ___ the benefit.|double-count|The contractor reduction arises within the same improvement, so the two indicators cannot be treated as independent additive savings.""",
        reference=("HM Treasury: Government Efficiency Framework; cash and non-cash distinctions", "https://www.gov.uk/government/publications/the-government-efficiency-framework/the-government-efficiency-framework--2"),
    ),
    scenario(
        title="Hand over a usable model",
        skill="Walk a client through a reproducible model, controlled updates, and clearly bounded acceptance.",
        setup="Fictional model v1.4: monthly contribution = units times (price minus variable unit cost), less fixed cost. Baseline: 2,000 units, $30 price, $18 variable cost, $15,000 fixed cost; tax and financing excluded. Omar will maintain it. Handover tests reproduce the baseline and a 1,800-unit sensitivity, other inputs unchanged. Future enhancements are excluded.",
        cast="Cass|Consultant\nOmar|Client analyst",
        dialogue="""Omar|Before we sign off, I want to run the spreadsheet myself. Which version should I use, and what result should I reproduce?
Cass|Start from approved version one point four. The [[baseline case::The baseline case uses 2,000 units, price 30, variable unit cost 18, and fixed cost 15,000, giving 2,000 times 12 minus 15,000 equals 9,000.]] returns nine thousand: two thousand units at a twelve-dollar unit contribution, less fifteen thousand fixed cost.
Omar|I get nine thousand too. The inputs are separate from the calculation sheet. Are the pale cells values I may change, or are some calculated outputs?
Cass|Use the input guide, not color alone. The [[input register::The input register identifies the model's editable inputs, sources, units, and dates so an update can be traced rather than inferred from a cell's appearance.]] identifies sources, units, dates, and which values are assumptions rather than observations.
Omar|For the test, I will change volume to eighteen hundred and leave price, variable unit cost, and fixed cost untouched. That gives six thousand six hundred.
Cass|Correct. This is a [[sensitivity test::The sensitivity test varies volume alone to 1,800 units while holding the other inputs constant, producing 1,800 times 12 minus 15,000 equals 6,600.]], not a forecast that demand will fall. It shows the output under one specified input change.
Omar|If the commercial team changes the price next month, I should enter the approved assumption in its input cell, not type over the contribution result.
Cass|Exactly. Overwriting the output would [[hard-code::To hard-code the output here means replacing the calculation with a fixed value, breaking the model's ability to respond consistently to changed inputs.]] the result and break the calculation. Keep formulas intact and check that updated inputs use the same units and period.
Omar|Where should I record who approved a new price assumption? The source report alone might not explain why we used a particular estimate.
Cass|Use the [[assumptions log::The assumptions log records the basis, owner, approval, and limitations of assumed inputs; it complements the source records and allows later users to understand choices.]]. Record the basis, owner, approval, and known limitations. An assumption should not become a historical fact simply because it appears in a spreadsheet.
Omar|I also see the notes exclude tax and financing. We must not label the nine-thousand baseline as net profit after all business costs.
Cass|Right. Call it the defined monthly contribution after the included fixed cost. The scope note explains what it includes and excludes; preserve that wording in extracted charts.
Omar|After testing, I will save the next working version separately. We need to be able to return to the approved baseline without guessing which file is current.
Cass|That is the purpose of [[version control::Version control preserves identifiable model versions and a record of changes, allowing an approved baseline and subsequent updates to be distinguished and reviewed.]]. Follow your team's naming and access process, with the change, date, author, and review status recorded.
Omar|Does signing the handover mean finance has approved the investment recommendation? I want the acceptance record to be precise about what we tested.
Cass|No. It confirms the agreed model delivery and handover checks, not approval of an investment or certainty about future results. Record the two reproduced outputs and any unresolved issues.
Omar|I can maintain the specified inputs. Adding another product and a different cost structure would need a design change, not just another column copied across.
Cass|Agreed. That enhancement is outside this handover. Route it through the agreed change process; do not assume ongoing development is included because the file is editable.
Omar|I will attach the baseline and sensitivity results, confirm ownership, and retain the input guide, assumptions log, limitations, and version history with the model.
Cass|Then the handover shows that you can operate the agreed model, not merely that an attachment arrived. We can record acceptance of that defined scope.""",
        transfer_title="Reproduce another contribution model",
        transfer_setup="A model calculates monthly contribution as units times (price minus variable unit cost), less fixed cost. Inputs are 1,500 units, $40 price, $24 variable cost, and $18,000 fixed cost. The sensitivity changes only units to 1,250. Tax and financing are excluded.",
        transfer="""Analyst: Unit contribution is $___ before fixed cost.|16|Forty dollars selling price minus twenty-four dollars variable unit cost gives sixteen dollars per unit.
Consultant: The baseline monthly result is $___.|6,000|Fifteen hundred units times sixteen dollars less eighteen thousand fixed cost equals six thousand.
Analyst: The sensitivity result is $___.|2,000|Twelve hundred fifty units times sixteen dollars less eighteen thousand gives two thousand, with other inputs unchanged.
Consultant: This sensitivity is not a demand ___.|forecast|The exercise changes one input to test its effect; it does not predict which demand level will occur.""",
        reference=("HM Government: AQuA Book; assumptions, documentation, assurance, and version control", "https://www.gov.uk/guidance/the-aqua-book"),
    ),
]
