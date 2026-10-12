"""Twenty-four short patent-practice conversations with separate practical situations."""
from books.patent_law_content import BOOK
from books.specialist_support import short_lesson

LESSONS = {}
LESSONS['module-1'] = short_lesson(BOOK['units'][0], '''
The test engineer also proposed a feature | Counsel checks development contributions. | Counsel | Engineer
The project report calls Dana a tester. Did Dana also propose any changes to the design?
Yes. Dana suggested moving the inlet after observing uneven flow during the first trial.
Please identify that suggestion separately from the work of running the trial itself.
I have the dated meeting notes and the drawing showing the proposed inlet location.
Those records will help us understand the contribution without assigning inventorship from the job title.
We should also distinguish the suggestion from the final arrangement the team later adopted.
Exactly. Describe who proposed what and how the design developed, without rewriting the history.
I will preserve the original notes and explain the sequence in the confidential disclosure.
Then we can assess the relevant contributions against the claimed subject matter and applicable law.
I will not reduce Dana's role to testing merely because that is the title in the project plan.

An expected effect is not measured data | A patent professional reviews an invention summary. | Engineer | Reviewer
The summary says the new channel reduces energy use, but that version has not been tested.
Then describe the proposed mechanism and expected effect without presenting a measurement that does not exist.
We predict lower resistance because the path is smoother, although the actual result remains unknown.
That explanation is useful when clearly separated from the data for the earlier prototype.
I can label the earlier graph with the configuration actually used in that test.
Please do, and keep the later drawing from appearing to be the tested configuration.
Should the disclosure still mention the alternative even though we have no measurements for it?
Describe the technical proposal accurately so the patent professional can assess the relevant disclosure questions.
I will remove the unsupported numerical claim and retain the factual design explanation.
That improves accuracy without pretending the alternative was built, tested, or legally assessed already.

The conference slide is still a disclosure | Counsel discusses a proposed presentation. | Researcher | Counsel
I removed the patent title from the conference slide, so I assumed there is no disclosure concern.
The title is not the only issue; the technical content and circumstances need review before presentation.
The diagram still shows the channel arrangement, and the audience would not be under our internal confidentiality process.
Then send the actual slide and event details through the approved channel for prompt assessment.
We have not presented it or posted it online, and the event is next month.
Good. Preserve that status rather than reporting a disclosure as though it already occurred.
I should not assume that a general grace-period statement applies to every planned jurisdiction.
Correct. Real consequences depend on the actual facts and law, so do not rely on a universal shortcut.
I will hold the proposed technical slide for the required review and identify the responsible contact.
That lets the team address the issue before an intended presentation becomes an irreversible public event.
''')
LESSONS['module-2'] = short_lesson(BOOK['units'][1], '''
The translation changed a search term | An analyst reviews multilingual search coverage. | Analyst | Counsel
The translated abstract calls the component a sleeve, but our original search used only the term housing.
That may explain a coverage gap; add relevant variants without assuming the words always describe identical structures.
I will compare the full document and figures before mapping the translated term to our feature.
Good. The translation can help locate material, but the actual technical disclosure still needs assessment.
The machine translation also changes the direction of flow in one sentence.
Flag that discrepancy for appropriate language review rather than relying on the fluent version alone.
I can preserve the source passage and the translation used during the search.
That makes the uncertainty traceable and prevents the report from hiding a material language issue.
The revised report will state which terms and language sources were covered.
Then readers can understand the search expansion without mistaking it for an unlimited completeness guarantee.

A later family member has different claims | A search reviewer checks grouped results. | Reviewer | Analyst
You grouped these documents as one family, but the later member appears to contain a different claim set.
I used the family grouping to reduce duplicate results, not to establish identical claim scope.
Keep that purpose clear and identify the actual document supporting each relevant finding.
I will separate the publication numbers, dates, and claim versions in the comparison.
We also need the current legal status where the review concerns rights affecting a product.
Yes. A family relationship alone does not say which claims are pending, granted, or no longer in force.
The technical disclosure can still be relevant, but its legal use depends on the question.
I will distinguish a prior-art discussion from any separate freedom-to-operate assessment.
That distinction will stop the commercial team from treating one consolidated row as complete clearance.
The report will retain the family link while preserving each material document's identity and status.

The search found nothing close in one database | An analyst reports a negative result. | Manager | Analyst
Your search found no close match. Can the presentation say that no relevant prior art exists?
No. It can say that no close result was located within the scope we actually searched.
The current search used one database and only the English terms supplied by engineering.
Then both limits should stay visible rather than disappear from the executive summary.
Could you identify the next coverage questions without promising a complete search of every possible source?
Yes. We can review relevant classifications, term variants, language coverage, and non-patent literature.
I also should not describe the result as permission to launch the product.
Correct. That is a separate question involving the actual configuration, rights, territory, and review scope.
I will keep the summary short but retain the phrase within the stated search scope.
That gives the team a useful finding without turning limited evidence into a universal assurance.
''')
LESSONS['module-3'] = short_lesson(BOOK['units'][2], '''
A method step became a component | A drafter checks an engineering paraphrase. | Engineer | Drafter
My summary lists the pump, housing, and cooling step together as though they were all components.
The cooling step describes an action, while the pump and housing describe physical elements.
We should separate the apparatus explanation from the sequence performed during operation.
Yes, and check the actual claim type instead of changing operative wording through the summary.
I can explain that fluid passes through the channel before returning to the reservoir.
That sequence is useful technical information, provided it matches the disclosed operation.
The diagram alone does not tell us whether the draft requires that exact order.
Correct. We need the actual wording and proper legal analysis for the claim-scope question.
I will label the sequence as an engineering explanation rather than a definitive claim construction.
Then the discussion stays clear without converting a teaching diagram into a legal conclusion.

The replacement word changed the relationship | Counsel reviews a proposed stylistic edit. | Editor | Counsel
I replaced connected to with adjacent to because the second phrase sounded less repetitive.
Those phrases describe different relationships; proximity does not necessarily establish a connection.
The component can be near the housing without being attached in the way the drawing shows.
Exactly. A wording change needs technical and legal review, not just a judgment about style.
I will restore the original wording in the working comparison and mark my suggestion separately.
Please preserve the change history so reviewers can see what was proposed and why.
We should ask the engineer whether the connection is direct or through another component.
That can clarify the intended mechanism, while the patent professional reviews support and scope.
I will not silently use a smoother synonym in the operative claim text.
That is the right distinction between improving readability and altering a substantive requirement.

A dependent claim cannot be read alone | A product manager asks about a claim chart. | Manager | Counsel
The chart shows the sensor only in claim 4. Does claim 4 cover any sensor we sell?
Not from that observation. We need to read its dependency and all inherited requirements.
Claim 4 depends on claim 2, which already refers back to claim 1.
Then the claim tree matters; the sensor is not automatically protected in isolation.
I can expand the chart to show which earlier limitations carry into the combination.
That will help the engineering team understand the structure without changing the actual claim language.
Should we also identify the precise version, since the claim numbering changed during drafting?
Yes. Numbering alone is unreliable when different versions circulate in the same meeting.
I will use the dated draft and label the chart as a working explanation.
Then everyone can discuss the same combination without mistaking an isolated feature for the entire claim.
''')
LESSONS['module-4'] = short_lesson(BOOK['units'][3], '''
The old draft was never filed | A reviewer checks a support citation. | Engineer | Counsel
I found the controller in an early draft, so I cited that paragraph as original filing support.
Was that wording actually included in the application as filed, or removed before submission?
It was removed during review. The filed copy describes only the mechanical arrangement.
Then the unfiled draft does not establish what the filed application disclosed.
I will preserve both versions and correct the support table to identify the actual filed text.
Good. We can then assess the real support question without treating drafting history as filed content.
The engineering team still wants protection for the controller developed later.
That request needs qualified advice on available options, not a retrospective change to the historical record.
I will mark the controller issue as unresolved and supply the development dates.
That gives the review the facts it needs without promising an earlier date or an available filing route.

The figure labels are inconsistent | A drafter checks an application drawing. | Drafter | Engineer
The text calls element twelve an inlet, but the figure legend calls the same number an outlet.
The drawing direction shows fluid entering there; the legend appears inconsistent with the intended design.
Please identify the source of that explanation and the relevant original materials.
I can provide the dated engineering drawing and explain the intended flow direction.
We still need to distinguish a proposed correction from a conclusion that the legal change is permissible.
Agreed. The patent professional should assess the actual filed record and available correction process.
I will mark both references rather than quietly replace every occurrence with inlet.
That will let reviewers see the discrepancy and the proposed resolution clearly.
The revised working copy will remain labeled as proposed until the review is complete.
Good. A clearer diagram should not conceal the fact that the filed text needs its own assessment.

Possible is not necessarily disclosed | Counsel asks about an asserted inherent feature. | Engineer | Counsel
The original device could use a wireless controller, so I assumed wireless control was inherently disclosed.
Could use describes a possibility; it does not establish that the feature was necessarily present.
The filed example can also work with a mechanical connection and no wireless component.
Then we cannot support your conclusion simply by saying the later wireless version is technically feasible.
I should explain the original mechanism and the alternative versions separately.
Yes. The applicable disclosure analysis needs the actual facts, not a stronger modal word inserted in summary.
I will change necessarily includes to could be implemented with in the technical note.
That is more accurate technically, but it still does not settle legal support for an amendment.
We will leave that conclusion to the patent review and preserve the original documents.
Exactly. Precise language helps the assessment without deciding it in advance.
''')
LESSONS['module-5'] = short_lesson(BOOK['units'][4], '''
An interview note overstated agreement | A coordinator reviews a meeting summary. | Coordinator | Counsel
The examiner said the distinction was clearer after our explanation, so I wrote that the claim was allowed.
That overstates the discussion. Clarity during an interview is not a formal allowance.
I should record what was discussed and whether any specific next step was identified.
Yes. Keep the actual interview outcome separate from the status of the application.
The examiner asked us to submit the supported argument in the response for review.
Then report that request rather than claiming the later review has already been completed.
I will revise the note and preserve the original meeting record for the responsible professional.
Also ensure the actual response requirements and deadlines remain properly tracked.
The update will say the issue was discussed and a response remains to be submitted.
That gives the client a useful progress report without turning an encouraging exchange into a grant decision.

The technical disagreement needs a pinpoint | Counsel reviews an engineer's response comments. | Engineer | Counsel
My comment says the reference is completely wrong, but I have not identified the disputed passage.
Please show the specific mapping you disagree with and explain the technical difference.
The cited figure places the channel beside the enclosure, while our claim describes a different relationship.
That is a focused point we can assess against the actual wording and disclosure.
I will avoid attacking the examiner or implying that every part of the reference is irrelevant.
Good. A firm response should address the reasoning, not speculate about the person's motives.
We also need to keep the separate clarity issue visible in the response plan.
Exactly. Success on one argument would not automatically resolve every issue raised in the notice.
I will provide a marked comparison and the supporting technical explanation for your review.
Then we can evaluate a properly supported response without promising that the examiner will agree.

Final is a procedural label | A client asks about a later notice. | Client | Counsel
This notice says final rejection. Does that mean there is nothing left to discuss and no deadline to track?
No. The label has procedural consequences, and the actual options and timing need prompt review.
We should not treat it as the ordinary word finished and simply close the internal file.
Correct. Nor should we assume that any particular amendment, appeal, or extension is available without checking.
I can send the full notice and confirm the current authorized client contact.
That will help us explain the actual posture and obtain instructions on the appropriate options.
Management needs a concise account of what changed since the previous update.
We can describe the procedural status, issues, verified timing, and options requiring a decision.
I will avoid promising either automatic success or that every possible route is closed.
That preserves the distinction between a procedural designation and an unsupported conclusion about the entire matter.
''')
LESSONS['module-6'] = short_lesson(BOOK['units'][5], '''
The estimate excludes translation review | A coordinator compares local filing estimates. | Manager | Coordinator
The lower estimate looks attractive, but its total does not mention translation review or local filing fees.
Then it is not directly comparable with the estimate that includes those items.
I will ask each provider to identify inclusions, exclusions, currency, and the assumptions behind the amount.
Good. We also need to distinguish an estimate from authority to incur the expense.
The client has not yet approved the market list or the budget.
Then the status should remain evaluation pending rather than filing instructed.
We can collect the information now while the responsible professionals verify actual timing.
Yes. Budget uncertainty should not hide a real deadline that needs prompt attention.
The comparison will show equivalent categories instead of ranking unrelated headline totals.
That will support a clearer decision without suggesting that a lower estimate guarantees the same service or outcome.

The written opinion sounds favorable | Counsel explains an international-stage report. | Manager | Counsel
The written opinion is encouraging. May we call it a successful patent grant in the press summary?
No. It is an international-stage assessment, not a grant from every office we may approach.
We can describe receipt of the report and the next portfolio decisions instead.
Yes, with suitable review of any public statement and the actual scope of the findings.
The report does not decide whether we should enter every possible market.
Correct. Business priorities, costs, local advice, and the actual findings all matter to that decision.
I will keep national or regional grant status separate from the report's conclusions.
That prevents a favorable assessment from becoming a claim of territorial rights that do not yet exist.
The board update will identify which decisions are authorized and which remain under evaluation.
Good. Clear status language is more useful than a headline that collapses the entire application process.

The instruction names the wrong applicant | A coordinator verifies filing particulars. | Associate | Coordinator
Your instruction names the group brand, but the application documents identify a specific legal entity.
Thank you for flagging it. We should verify the actual applicant details before treating the names as equivalent.
The local forms also need consistent information rather than an informal commercial abbreviation.
I will check the approved records and obtain the necessary clarification through the responsible professional.
Please preserve the existing document version while that verification takes place.
Agreed. I will not silently substitute an entity merely because the brand is familiar.
We also need to keep the real filing timetable visible during the correction.
Yes. I will route the discrepancy promptly with the exact documents and unresolved question.
The revised instruction should clearly identify what has been verified and by whom.
Then the local action can proceed on accurate authorized particulars rather than an assumption about corporate identity.
''')
LESSONS['module-7'] = short_lesson(BOOK['units'][6], '''
The redesigned housing is not merely cosmetic | Counsel checks a production change. | Engineer | Counsel
We changed the housing for manufacturing, but the sales team says it is only a cosmetic update.
The label is not enough. What components and relationships changed in the actual production configuration?
The channel now connects through a different fitting, and the flow path is slightly longer.
Please provide the controlled drawing and a comparison with the version previously reviewed.
That will let you decide whether the earlier assessment needs to be revisited.
Yes. Do not assume the conclusion applies automatically simply because the product name stayed the same.
I will also identify the intended market and commercial activity in the request.
Those details help define the relevant scope instead of asking for an unbounded assurance.
The launch note will say the changed configuration is awaiting the appropriate review.
That keeps a manufacturing update from silently becoming an unsupported clearance conclusion.

An expired record does not settle the family | A product lead asks about search status. | Lead | Counsel
One database entry says expired. Can we remove the entire patent family from the review?
Not on that observation alone. We need the relevant records, territory, claims, and current legal status.
The grouped results include another application that appears to remain pending.
Then distinguish the individual documents rather than applying one member's status to every related filing.
I will send the exact identifiers and the date of the database check.
Good. The responsible review can then verify the actual information and its significance.
We should also avoid treating a search database label as a complete legal opinion.
Correct. It is a source to assess, not a substitute for the scoped analysis.
The revised table will retain the family relationship while separating each material status.
That makes the finding usable without erasing a potentially relevant record through overgeneralization.

The opinion covered manufacture, not every transaction | Counsel clarifies an assessment request. | Manager | Counsel
The earlier report reviewed manufacturing in A. Sales now wants to rely on it for imports into B.
Those are different activities and territories, so we need to check the actual opinion scope.
The product configuration is unchanged, but the proposed commercial route is new.
That still matters. An unchanged design does not automatically make every legal question identical.
I will supply the intended activities and locations rather than ask whether the product is simply safe.
Please do. A specific request allows the relevant rights and assumptions to be assessed.
The earlier conclusion should remain attached to its stated facts and limitations.
Exactly. Do not remove those qualifications when preparing the commercial summary.
I will mark the new route as requiring review and identify the business decision it supports.
That gives the team a practical next step without expanding the old opinion beyond its basis.
''')
LESSONS['module-8'] = short_lesson(BOOK['units'][7], '''
Distributor rights are not manufacturing rights | Two negotiators clarify a proposed license. | Licensee | Licensor
Our distributor wants to manufacture a local version, so we assumed the distribution arrangement covers that too.
Those activities need to be distinguished against the actual rights proposed in the license.
The draft currently describes resale of finished products, not an onward manufacturing permission.
Then we should raise the manufacturing request explicitly rather than treat it as an implied extension.
We also need to identify the relevant territory and whether a sublicense would be required.
Yes. The parties should negotiate the actual scope and conditions with the appropriate legal review.
I will add the request as an open item in the marked-up term sheet.
Please keep the existing proposal and the requested expansion separately visible.
Our commercial summary will not say the distributor already has those rights.
That avoids converting a business preference into a permission that has not been granted.

A milestone needs an observable trigger | Negotiators discuss a payment provision. | Licensee | Licensor
The draft says payment is due when development is substantially complete, but our teams interpret that differently.
Then the trigger needs a more precise definition rather than relying on a shared-sounding phrase.
Our engineering group means completion of the prototype, while finance assumes commercial production has begun.
Those are materially different events and could lead to different payment dates.
We should identify the agreed event and the evidence used to confirm it.
Yes, together with the actual payment terms and any review process the parties agree.
I will not replace the phrase unilaterally with our preferred interpretation.
Good. Mark the proposed wording so both sides can assess the change.
The term sheet should keep that payment provision open until the issue is resolved.
That makes the remaining negotiation concrete instead of hiding it inside an ambiguous milestone label.

Improvements are a separate negotiation | A licensee raises a development concern. | Licensee | Licensor
Our team may develop a new connector, and we want to know how later improvements would be treated.
The current heading does not settle ownership, access, or licensing of those later developments.
We should identify the particular rights each side is requesting rather than use improvements as one broad label.
Agreed. The definitions and obligations need to be clear enough for both technical and commercial teams.
We also want to distinguish our existing background technology from work developed during the relationship.
That distinction belongs in the actual negotiated provisions, with appropriate legal review.
I will provide a marked proposal showing those separate categories and the requested treatment.
Please keep proposed terms separate from rights already held or granted under another agreement.
The next meeting can address the identified differences without assuming that exclusivity answers everything.
Exactly. A precise open-item list is more useful than a broad assurance neither side intended to give.
''')
