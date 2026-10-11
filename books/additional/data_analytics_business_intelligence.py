"""Original mix-shift, historical-dimension, and forecasting review conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Both segments improve, but the overall rate falls',
        skill='Explain weighted rates and changing composition without inventing a causal explanation.',
        setup='Two periods each contain 1,000 eligible visits. Segment A changes from 10 conversions in 100 visits to 108 in 900. Segment B changes from 270 in 900 to 32 in 100. Definitions are unchanged. The team must explain segment improvement alongside an overall decline.',
        cast='Nadia|BI analyst\nPaul|Commercial director',
        dialogue='''Paul|Your segment chart shows improvement in both groups, but the headline says conversion fell. Have the charts used different data?
Nadia|They use the same records. Start with each [[denominator::The denominator is the eligible visit count for the corresponding segment and period; those counts change substantially even though each period totals one thousand visits.]]. A changes from one hundred to nine hundred visits; B changes from nine hundred to one hundred.
Paul|A goes from ten out of one hundred to one hundred eight out of nine hundred. That is ten percent to twelve percent.
Nadia|Yes, up two [[percentage points::Percentage points express the difference between the percentage values; both segment rates rise by two points, not by the same relative percentage.]]. B goes from thirty percent to thirty-two percent. Both segment-level comparisons are favorable.
Paul|The first total is ten plus two hundred seventy conversions: two hundred eighty out of one thousand, or twenty-eight percent.
Nadia|And the later total is one hundred eight plus thirty-two: one hundred forty out of one thousand, or fourteen percent. Those calculations reconcile.
Paul|So the later period has many more visits in the lower-converting segment. Its better rate does not offset that change in composition.
Nadia|Exactly. This [[mix shift::The mix shift moves a much larger share of visits into lower-converting segment A; changing weights can reverse the direction seen in the separate segment rates.]] explains why the aggregate comparison moves differently from the segment comparisons. An unweighted average would answer another question.
Paul|Could we just show the average of the two segment rates? That would be twenty percent before and twenty-two percent after.
Nadia|Only with an explicit equal-weight interpretation. It would not be the actual share of these visits that converted, because the segment sizes are not equal.
Paul|For a like-for-like composition comparison, could we apply the earlier visit proportions to the later segment rates?
Nadia|Yes, if we label the calculation. Use the earlier [[reference weights::The reference weights are the earlier ten-percent share for A and ninety-percent share for B; keeping them fixed creates a separate composition-standardized comparison.]]: ten percent for A and ninety percent for B.
Paul|That gives point one times twelve percent plus point nine times thirty-two percent. The result is thirty percent, not the observed fourteen percent.
Nadia|Correct. It shows what that weighted calculation produces using the earlier mix. Keep the observed result alongside it; do not replace actual performance with the adjusted figure.
Paul|The commercial team might call thirty percent the performance we would certainly get if we changed our traffic allocation back.
Nadia|That overstates the [[standardization::Standardization applies a common weighting basis to improve comparability; it does not prove that an intervention changing traffic would leave every segment's rate unchanged.]]. It is a descriptive comparison, not proof that a future allocation change would preserve those rates.
Paul|Then we still need evidence about why the mix changed and whether different visitors within each segment would behave similarly.
Nadia|Yes. We have not estimated a [[causal effect::A causal effect concerns what an intervention changes; these aggregate and standardized comparisons alone do not isolate the effect of changing traffic allocation.]] of reallocating traffic. The arithmetic explains the apparent contradiction without settling the intervention decision.
Paul|I will show actual conversion, segment rates, and segment sizes together. The standardized comparison can be separate and clearly labeled.
Nadia|That lets the audience see both the real aggregate decline and the improvement within each segment, without choosing whichever chart tells the preferred story.''',
        transfer_title='An equal-weight average hides the actual visit mix',
        transfer_setup='Earlier: A converts 20 of 100 visits; B converts 180 of 300. Later: A converts 90 of 300; B converts 70 of 100. Definitions match. Each period has 400 visits.',
        transfer='''Analyst: The earlier overall rate is ___ percent.|50|Twenty plus one hundred eighty equals two hundred conversions from four hundred visits, or fifty percent.
Director: The later overall rate is ___ percent.|40|Ninety plus seventy equals one hundred sixty conversions from four hundred visits, or forty percent.
Analyst: Each segment improved by ___ percentage points.|ten|A rises from twenty to thirty percent and B from sixty to seventy percent, each a ten-point increase.
Director: Show the segment sizes so the changing ___ is visible.|composition|More visits belong to the lower-converting segment later, so the overall rate can fall despite both within-segment improvements.'''),
    scenario(
        title='The customer moved regions. Did the old sale move too?',
        skill='Agree historical attribution and distinguish business identity from a versioned dimension record.',
        setup='Customer C17 belonged to North in February and moved to South effective March 1. Its February order is $500; its April order is $700. A current-region join assigns both to South. The requested report must use the region in effect on each order date.',
        cast='Iris|Analytics engineer\nMateo|Sales operations analyst',
        dialogue='''Mateo|South has gained five hundred dollars in February, even though nobody entered a new order. Could the customer-region update explain it?
Iris|Yes. The report joins both orders to the [[current record::The current record contains the customer's latest region, South; using it for every order reclassifies earlier sales instead of preserving their original regional attribution.]]. It now says South, so the February order moves with the customer in that view.
Mateo|Our requested view is region at the time of sale. February should remain North and April should be South.
Iris|Then we need a [[historical attribution::Historical attribution assigns each fact using the relevant state at its event time; it differs from regrouping all facts under today's customer attributes.]] rule. Neither view should be labeled simply sales by region without telling readers which basis it uses.
Mateo|We have the approved March first effective date. Does the warehouse need two customer records, or would that duplicate the customer?
Iris|Two versions can represent one business customer. A [[Type 2 dimension::A Type 2 dimension preserves successive versions of descriptive attributes so facts can be related to the version valid at the relevant time.]] preserves the region history instead of overwriting every previous state.
Mateo|C17 remains the business identifier in both versions. How do we distinguish the rows if that identifier is no longer unique in the history table?
Iris|Each version gets a [[surrogate key::A surrogate key identifies the particular warehouse dimension row; the stable customer business identifier can appear on several historical versions.]]. Facts can then reference the correct version while we still group those versions under the same customer when needed.
Mateo|For the boundary, the North version ends when the South version starts. We must avoid matching the March first order to both.
Iris|Exactly. Define the effective intervals consistently. In this model the start is inclusive and the end exclusive, so March first belongs to South only.
Mateo|What does the loading process use to assign the version to each order? A current flag would give the same wrong answer again.
Iris|Use a [[time-based lookup::A time-based lookup matches the fact's relevant date to the dimension version's effective interval, rather than selecting the current version for every fact.]] against the effective interval for C17. Then test the boundary date, missing intervals, and overlapping versions.
Mateo|The expected result for these two orders is North five hundred, South seven hundred, total twelve hundred. The total alone would not expose the original error.
Iris|Right. The current-region report also totals twelve hundred. Check the regional allocation as well as the grand total, and retain both labeled views if both are required.
Mateo|Suppose the source team later corrects the move date. We should not silently replace an already issued regional report without a record.
Iris|Follow the agreed [[restatement::Restatement revises previously reported figures under a documented correction policy; the changed attribution and its reason must remain traceable.]] policy. Record the corrected source evidence, affected periods, and what changed in the published figures.
Mateo|Could we infer the old region from today's address if the earlier version is missing? That would make the chart complete.
Iris|Not without supporting evidence. Flag the unresolved history and route it to the source owner. A complete-looking chart is not a reason to invent an earlier state.
Mateo|I will confirm the requested historical basis with Sales, then check the two orders and the March first boundary in the revised output.
Iris|I will preserve C17's business identity, assign the appropriate version keys, and document the interval rule so future refreshes do not silently move old sales.''',
        transfer_title='The grand total passes while the regional split is wrong',
        transfer_setup='Customer D8 moves from East to West effective May 1. It has a $300 April order and a $400 June order. The report requires order-date region, not current region.',
        transfer='''Analyst: The April order belongs to ___.|East|April precedes the May first move, so the order-date region is East.
Engineer: The June order belongs to ___.|West|June follows the effective move date, making West the relevant historical version.
Analyst: The unchanged grand total is ___ dollars.|700|Three hundred plus four hundred equals seven hundred under either allocation, so the total alone cannot verify the regional split.
Engineer: Verify the effective-date intervals and the selected version ___.|keys|Version keys must identify the dimension rows valid on each order date rather than merely the current customer row.''',
        reference=('Microsoft Learn: Star Schema and Slowly Changing Dimensions', 'https://learn.microsoft.com/en-us/power-bi/guidance/star-schema')),
    scenario(
        title='The forecast used information from tomorrow',
        skill='Challenge an evaluation shortcut and explain forecast error in the correct units.',
        setup='An old next-day ticket-volume model used next-day resolved-ticket counts, unavailable when forecasting. A separate rebuilt model uses archived, time-appropriate inputs. On a fixed ten-day holdout unused for training or tuning, its total absolute error is 80 tickets; the agreed baseline totals 100.',
        cast='Farah|Forecast analyst\nLewis|Operations planner',
        dialogue='''Lewis|The old forecast was remarkably accurate. Why have you taken its performance figure out of the planning presentation?
Farah|One input was unavailable at the [[forecast origin::The forecast origin is the time when the prediction is issued; information generated afterward cannot be treated as an available input to that prediction.]]. It used tomorrow's resolved-ticket count to predict tomorrow's incoming volume.
Lewis|That count was in the historical export, so it looked like an ordinary column. But we would not have known it when making the forecast.
Farah|Exactly. That is [[data leakage::Data leakage introduces information unavailable for the intended prediction into model development or evaluation, making the reported performance unrepresentative of the real forecasting task.]]. A field being present in today's historical file does not mean it existed at the earlier decision time.
Lewis|You rebuilt the model without it. Have you also checked when the remaining fields became available, rather than just when their events occurred?
Farah|Yes. This rebuilt evaluation uses archived inputs available at each prediction time, including the actual publication delays. It does not backdate a later data delivery.
Lewis|How did you test it? A random mixture of past and future dates would not look like our daily planning process.
Farah|We used a chronological [[backtest::A backtest evaluates predictions against historical outcomes while recreating the information and timing of the intended forecasting task.]]. Training precedes the evaluated predictions, and each forecast uses only the information available at its issue time.
Lewis|The comparison sheet also names a final ten-day block. Was that block used to choose the model settings?
Farah|No. It is the fixed [[holdout period::The holdout period is reserved for evaluation and was not used to fit or tune this model; repeatedly tuning against it would undermine that separation.]]. The model and comparison rule were settled before those results were examined.
Lewis|Across those ten days the absolute errors add to eighty tickets. What should I call the average, rather than just saying eighty errors?
Farah|The [[mean absolute error::Mean absolute error averages the magnitudes of prediction errors without cancellation; eighty tickets of total absolute error over ten days gives eight tickets per daily forecast.]] is eight tickets per daily forecast. It is in ticket units, not eight percent, and opposite signed errors do not cancel.
Lewis|Our agreed simple forecasting method has total absolute error of one hundred over the same ten days, so its mean is ten tickets.
Farah|Yes. That [[baseline::The baseline is the agreed reference forecasting method evaluated on the same days and outcome definition; it gives the new model's error a meaningful comparison.]] is essential. A model can look sophisticated while failing to improve on a simple alternative.
Lewis|Eight instead of ten is a twenty-percent reduction in mean absolute error for this period. It does not mean eighty-percent forecast accuracy.
Farah|Correct. Also inspect individual days and the operational cost of underestimation versus overestimation. The mean alone does not describe every planning consequence.
Lewis|Can we promise the same improvement next month? Staffing needs a practical expectation, not just the historical result.
Farah|No guarantee. This is a bounded historical evaluation. Changes in demand or input availability can alter performance, so the approved deployment plan needs monitoring.
Lewis|I will present the eight-versus-ten-ticket comparison, name the ten-day period, and explain why the earlier figure was withdrawn.
Farah|Good. Keep the corrected evaluation traceable and the future claim modest. The result supports considering the rebuilt model, not pretending we can use tomorrow's information today.''',
        transfer_title='A ticket error is mislabeled as a percentage',
        transfer_setup='Over eight held-out days, a model has 48 tickets of total absolute error. The reference method has 64 over the same days. No percentage-error metric was calculated.',
        transfer='''Analyst: The model mean absolute error is ___ tickets per forecast.|six|Forty-eight divided by eight gives six tickets of mean absolute error.
Planner: The reference method averages ___ tickets.|eight|Sixty-four divided by eight gives eight tickets of mean absolute error.
Analyst: That is a ___ percent reduction in this error metric.|twenty-five|The reduction is two tickets relative to the eight-ticket reference error: two divided by eight equals twenty-five percent.
Planner: Do not relabel a six-ticket error as six-percent ___.|error|The metric is in ticket units, and no percentage-error calculation is supplied.''',
        reference=('scikit-learn: Common Pitfalls and Data Leakage', 'https://scikit-learn.org/stable/common_pitfalls.html')),
]
