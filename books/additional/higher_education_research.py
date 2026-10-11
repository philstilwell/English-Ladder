"""Research planning, sponsored-project costing, and publication conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='The smallest p-value was not the primary outcome',
        skill='Distinguish a prespecified analysis from a result selected after inspection.',
        setup='Before collecting data, a fictional team registered one primary outcome and a 0.05 significance threshold. Its planned test gives p = 0.18. Afterward, the team explores twenty other outcomes; the smallest unadjusted p-value is 0.03. No multiple-testing adjustment or independent confirmation has been performed.',
        cast='Alina|Postdoctoral researcher\nDev|Statistical collaborator',
        dialogue='''Alina|The main test was not significant, but I found an outcome with p point zero three. Could we lead with that one instead?
Dev|We can report it, but not replace the [[primary outcome::The primary outcome was specified before data collection; selecting another outcome after viewing results does not make it the original primary test.]] in the account of what we planned. The registered analysis still belongs in the results.
Alina|Its p-value is point one eight against our point zero five threshold. I will show that result rather than remove the table.
Dev|Good. Say that the planned test did not meet that threshold, not that we proved there is no effect.
Alina|For the other outcome, I was going to write that our hypothesis was confirmed. We did discuss it informally before the project.
Dev|This particular test came after inspection. Label it [[exploratory::Exploratory identifies the analysis performed after inspecting the data, rather than presenting it as the prespecified confirmatory test.]]. An earlier informal discussion is not evidence that this analysis was the registered test.
Alina|Should we omit the exploratory work altogether? The pattern might help us design the next study.
Dev|Keep useful exploration. Be clear about the sequence of decisions and what the analysis can support. Transparency does not mean pretending discovery has no value.
Alina|The draft lists only the outcome with point zero three. The other nineteen are in my notebook but not in the manuscript.
Dev|That hides the [[multiple testing::Multiple testing concerns the twenty outcomes examined; reporting only the smallest unadjusted p-value conceals the selection process relevant to interpretation.]] issue. Describe the family of analyses, the selection, and that the reported p-value is unadjusted.
Alina|Could I call point zero three a ninety-seven percent probability that the hypothesis is correct? That wording would be easier for the audience.
Dev|No. A [[p-value::A p-value concerns data under a specified null model and assumptions; subtracting it from one does not give the probability that a hypothesis is true.]] is not the probability that our hypothesis is true. We need the estimate, uncertainty, and modeling assumptions, not that conversion.
Alina|We have the estimate in the output. I will check its units and the interval calculation with you before using either in the summary.
Dev|Yes. And keep the exploratory status visible even if a later analysis uses a different adjustment. A new calculation does not change when we selected the outcome.
Alina|For the follow-up, could we specify this outcome and analysis before collecting new data?
Dev|That would support an [[independent confirmation::Independent confirmation requires a new appropriately planned test, rather than presenting the same inspected data as a fresh confirmatory sample.]] attempt. Define the design and sample-size rationale first; do not promise the new result will agree.
Alina|I will also link the original registration. There was one exclusion change during analysis that the methods section does not currently explain.
Dev|Document the original rule, what changed, when, and why. Readers need to distinguish that deviation from the planned analysis rather than infer it from mismatched sample counts.
Alina|Then we retain the primary result, report the twenty exploratory tests transparently, and propose a separately planned follow-up.
Dev|Exactly. Add a [[deviation statement::The deviation statement records departures from the registered plan, including their timing and reasons, without rewriting the original plan after results are known.]] for the exclusion change. We can present a useful finding without rewriting the study's history.''',
        transfer_title='Keep the planned and discovered results separate',
        transfer_setup='A registered primary test has p = 0.12 against a 0.05 threshold. Twelve unplanned outcomes are explored; the smallest unadjusted p-value is 0.02. The same dataset is used throughout.',
        transfer='''Researcher: "The registered test did not meet the specified ___."|threshold|The primary p-value of 0.12 is above the stated 0.05 threshold.
Collaborator: "The twelve later tests are ___."|exploratory|The tests were not in the registered plan and followed data inspection.
Researcher: "The reported minimum p-value is ___."|unadjusted|The brief explicitly states that the selected 0.02 value has no multiple-testing adjustment.
Collaborator: "Reusing these inspected data is not independent ___."|confirmation|The same inspected dataset is not a new independent test of the selected result.''',
        reference=('Center for Open Science: preregistration', 'https://www.cos.io/initiatives/prereg'),
    ),
    scenario(
        title='The indirect-cost rate applies to the base, not every line',
        skill='Read back a research budget while distinguishing cost totals, exclusions, and commitments.',
        setup='A fictional foundation permits $70,000 total costs. Agreed direct lines are personnel including benefits $40,000, supplies $8,000, equipment $12,000, and travel $4,000. Its specific terms allow 10% indirect costs on direct costs excluding equipment. These are supplied grant terms, not a general funding rule. Internal submission approval remains pending.',
        cast='Mina|Principal investigator\nReuben|Sponsored-projects officer',
        dialogue='''Mina|My budget totals sixty-four thousand in direct costs. I added ten percent to that and got seventy thousand four hundred overall.
Reuben|The addition is arithmetically right, but it uses the wrong [[cost base::The cost base is the amount to which the rate applies; the supplied foundation terms exclude equipment from that amount.]]. This foundation excludes equipment before applying the indirect-cost rate.
Mina|So the twelve-thousand equipment line is removed from the calculation, not removed from the amount we are requesting.
Reuben|Exactly. The equipment remains a direct project cost. Subtract twelve thousand from sixty-four thousand only to calculate the eligible base.
Mina|That leaves fifty-two thousand. Ten percent is five thousand two hundred. I had overstated the indirect amount by twelve hundred.
Reuben|Correct. Those are the [[indirect costs::Indirect costs are $5,200 under the supplied 10% rate and $52,000 base, not 10% of every direct line.]] under these particular terms. Use the foundation's rule here, not a rate copied from another award.
Mina|Then the full request is sixty-four thousand plus five thousand two hundred, or sixty-nine thousand two hundred.
Reuben|Yes. That is eight hundred below the seventy-thousand total-cost ceiling. It is not eight hundred of money already awarded or available to spend.
Mina|Should I use the spare eight hundred as a contingency line? There is no separate contingency category in this call.
Reuben|Do not add an unsupported [[budget justification::The budget justification must connect requested costs to the project and permitted categories; room below a ceiling does not itself justify a new charge.]]. We should request supported project costs, not fill the ceiling merely because space remains.
Mina|For personnel, the forty thousand already includes benefits. I see another benefits percentage on the spreadsheet template. That would count them twice.
Reuben|Remove that duplicate addition. The [[personnel total::The personnel total already includes benefits in this case; applying another benefits charge would double-count the same supplied cost.]] is the agreed forty thousand. Make the inclusion explicit in the explanatory note.
Mina|The foundation template also asks for effort. My commitment is twenty percent of a twelve-month appointment for this project year.
Reuben|That is two point four person-months. Effort describes time committed; it is not automatically an additional budget line beyond the personnel costs already calculated.
Mina|I will show two point four person-months and explain the salary calculation separately. We are not proposing an unpaid contribution in this budget.
Reuben|Good. Do not label the difference below the ceiling [[cost sharing::Cost sharing means project costs supported from another source; the $800 unused ceiling is not an institutional contribution or expenditure.]]. An unused ceiling is not an institutional promise to fund part of the project.
Mina|The totals now reconcile. Can I press submit, or is the internal approval still needed even though we are below the maximum?
Reuben|It is still needed. I will send the corrected budget for the authorized review. This calculation does not commit the university or confirm an award.
Mina|I will keep the submission pending and attach the foundation's costing terms, the line-item budget, and the explanations.
Reuben|Then the [[total request::The total request combines $64,000 direct costs with $5,200 indirect costs, for $69,200 subject to submission approval and the funder's decision.]] is sixty-nine thousand two hundred, subject to internal approval. The direct costs, indirect base, rate, and overall ceiling should each remain visible.''',
        transfer_title='Exclude from the base, retain in the request',
        transfer_setup='A fictional grant has $50,000 direct costs, including $10,000 equipment. Its terms permit 15% indirect costs on direct costs excluding equipment. The total-cost ceiling is $60,000. No award has been made.',
        transfer='''Investigator: "The indirect-cost base is ___ dollars."|40,000|Subtracting the ten-thousand equipment exclusion from fifty thousand leaves forty thousand.
Officer: "The indirect-cost amount is ___ dollars."|6,000|Fifteen percent of the forty-thousand eligible base equals six thousand.
Investigator: "The combined request is ___ dollars."|56,000|All fifty thousand direct costs remain in the request, plus six thousand indirect costs.
Officer: "The unused ceiling is ___ dollars, not an award."|4,000|The sixty-thousand ceiling exceeds the fifty-six-thousand request by four thousand dollars.''',
        reference=('NIH: developing a budget; check the actual award terms', 'https://grants.nih.gov/grants/developing_budget.htm'),
    ),
    scenario(
        title='Which manuscript can the repository release?',
        skill='Identify an article version and explain a specific deposit condition without inventing broader rights.',
        setup='For a fictional article published January 15, 2026, the checked agreement permits repository deposit of the accepted manuscript now, but public release only from October 15, 2026. It does not permit deposit of the publisher PDF. Today is October 1. No conflicting funder requirement applies in this case.',
        cast='Nadia|Researcher\nEllis|Repository librarian',
        dialogue='''Nadia|I have the journal PDF and would like it on my university profile today. Is that the file I should upload to the repository?
Ellis|Not under this agreement. We need the [[accepted manuscript::The accepted manuscript includes the peer-reviewed changes accepted for publication but is distinct from the publisher's formatted PDF.]], including the changes accepted by the journal, before the publisher's typesetting.
Nadia|There are three files in our folder: the original submission, the accepted Word file, and the formatted journal PDF. I can supply the middle one.
Ellis|Please do. Check that it is the actual accepted text, not a later personal edit or a draft that predates the reviewers' changes.
Nadia|The formatted file has the final page numbers and logo. Would using it make the record more accurate?
Ellis|We can link to the [[version of record::The version of record is the formally published article; permission to link to it does not grant permission to deposit its PDF.]] through its identifier. That does not give us permission to deposit the publisher PDF when this agreement excludes it.
Nadia|The article was published January fifteenth. The agreement lists October fifteenth as the public-release date. Today is October first, so I thought we were close enough.
Ellis|The date has not arrived. The checked terms allow deposit now with access closed, then public release on October fifteenth. We should not round the date down.
Nadia|So an item can be in the repository without its full text already being available to every visitor?
Ellis|Yes. The [[embargo::The embargo delays public access to the deposited manuscript until the stated date; it does not prevent the permitted closed deposit in this case.]] controls the full-text release. We will configure the record according to these specific terms rather than assume every deposit is immediately open.
Nadia|I have also attached a chart reproduced from another publisher. The article agreement does not say whether that chart can be included in repository copies.
Ellis|Flag the [[third-party material::Third-party material can have separate permissions; the article's deposit permission does not automatically resolve the rights to the reproduced chart.]] for a rights check before release. We should not infer its status from permission covering your own manuscript text.
Nadia|I can send the chart permission with the agreement. If that permission is limited, you will tell me what version can lawfully be made available?
Ellis|Yes, we will establish the permitted route with the relevant support team. Do not silently alter the accepted paper and label the result as the unmodified accepted version.
Nadia|For the repository description, I will add the article title, author list, journal reference, and persistent identifier.
Ellis|Those [[metadata::Metadata describe and identify the article and its version; they help users find the published work without substituting for full-text permissions.]] help readers identify the work. We will also label the deposited file's version clearly so they know what they are opening.
Nadia|Can I add a Creative Commons license to make it easier for people to reuse? I do not see one granted in the documents we have checked.
Ellis|Not on that basis alone. We need authority for the license applied to the deposited material. Availability and permission to redistribute are not the same thing.
Nadia|I will supply the accepted file and chart permission today. The public full text stays closed until the date and the rights check are satisfied.
Ellis|Correct. I will record the [[release conditions::The release conditions include the October 15 date and resolution of the chart permissions; deposit alone does not satisfy both conditions.]]. We can prepare the record now without promising public access before those conditions are met.''',
        transfer_title='Deposit permission has a version and a date',
        transfer_setup='A fictional checked agreement allows the accepted manuscript to be deposited now and released publicly from December 1. Today is November 20. The publisher PDF is excluded, and no third-party permissions are unresolved.',
        transfer='''Researcher: "The permitted file is the accepted ___."|manuscript|The agreement permits the accepted manuscript rather than the excluded publisher PDF.
Librarian: "Public full-text access remains closed during the ___."|embargo|The public-release date has not arrived, although deposit is permitted now.
Researcher: "The earliest stated public-release date is ___."|December 1|The supplied agreement names December first, not the current November date.
Librarian: "The publisher PDF remains ___."|excluded|The date condition does not expand permission to a file version the agreement excludes.''',
        reference=('NISO: Journal Article Versions', 'https://www.niso.org/publications/niso-rp-8-2008-jav'),
    ),
]
