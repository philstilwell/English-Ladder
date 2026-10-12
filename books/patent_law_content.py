"""Original patent-practice English: technical precision and legal scope."""
from books.specialist_support import specialist_unit as unit, source, FICTION

BOOK = dict(slug='patent-law', title='Patent Law English', category='Business & professional services',
    balanced_answer_columns=True,
    cover_label='ENGLISH FOR PATENT PRACTICE', cover_title='Patent Law', cover_size=34,
    tagline='Describe the invention. Define the legal question.',
    audience='For patent lawyers, patent agents, intellectual-property specialists, and technical professionals working with patent counsel.',
    roles='patent attorneys, patent agents, intellectual-property specialists, invention reviewers',
    summary='Patent-practice English for invention interviews, prior-art discussions, claims, drafting support, office actions, international filing, freedom-to-operate reviews, and licensing.',
    map_intro='Eight matters move from an invention disclosure to a licensing discussion, separating technical facts from legal conclusions that require qualified review.',
    notes_title='Small wording changes can change the question.',
    notes_intro='Patent teams move between engineering detail, legal analysis, and commercial priorities. Effective English makes a component relationship, an unresolved claim issue, or a territorial limitation clear without overstating protection.',
    field_notes=[
        ('Ask how it works', 'A benefit such as faster cooling does not identify the structure or steps that produce it. Ask about the mechanism and alternatives.', '"Which feature produces that result, and what changes if we remove it?"'),
        ('Identify the document', 'An invention disclosure, application, publication, and granted patent have different functions. Identify the actual document and status.', '"This is the published application, not a granted claim set."'),
        ('Separate the analyses', 'Patentability, ownership, infringement, and freedom to operate are different questions. An encouraging result in one does not settle the others.', '"That search addressed patentability, not clearance for commercial launch."'),
        ('Keep scope visible', 'Territory, claim wording, product configuration, dates, and legal status can determine the relevance of an assessment.', '"The review concerns this configuration in the named market."')],
    scope_note=FICTION + 'Language practice, not patent or legal advice. Examples simplify documents and do not establish inventorship, patentability, validity, infringement, priority, filing deadlines, licensing rights, or freedom to operate. Real matters require qualified patent professionals, current law and office practice, and the actual documents. Protect confidential inventions and observe applicable filing, disclosure, security, and export requirements.',
    sources=[
        source('USPTO. MPEP 2109: Inventorship.', 'https://www.uspto.gov/web/offices/pac/mpep/s2109.html', 'US terminology concerning contribution to conception of claimed subject matter; not a universal inventorship test.'),
        source('USPTO. MPEP 301: Ownership and assignability.', 'https://www.uspto.gov/web/offices/pac/mpep/s301.html', 'Distinguishes patent ownership and exclusion rights from permission to commercialize.'),
        source('WIPO. Introduction to the Patent Cooperation Treaty.', 'https://www.wipo.int/en/web/pct-system/introduction', 'International filing, search, and national or regional examination terminology.'),
        source('USPTO. Manual of Patent Examining Procedure.', 'https://www.uspto.gov/web/offices/pac/mpep/index.html', 'Primary US examination terminology; sections 608, 706, 714, and 2163 inform the claim, response, and disclosure distinctions. Actual matters require current rules and qualified review.')], units=[])

BOOK['units'].append(unit(
    title='Interviewing inventors without leading their answers', scene='The improvement is a channel, not simply faster cooling',
    skill='Elicit the mechanism, alternatives, and individual contributions behind an invention disclosure.',
    brief='Engineer Amira describes a prototype battery enclosure with a curved coolant channel. Technician Leo built it from drawings and suggested a detachable connector. One internal test reports a shorter cooling time, but the test conditions have not been compared. Patent professional Daniel is gathering facts, not deciding inventorship or patentability.',
    cast='Amira | Engineer\nDaniel | Patent professional',
    culture=('Curiosity before characterization', 'Ask about contributions and evidence without assigning legal labels based on seniority, job title, or who presents the invention.'),
    a='''What change is described in the enclosure? | A curved coolant channel | A different battery chemistry | A larger enclosure with no channel change | A connector that replaces the channel | The supplied mechanism concerns a curved coolant channel in the prototype enclosure.
What is known about Leo? | He built the prototype and suggested a connector | He only supplied funding | He conceived every proposed claim | His contribution has already been legally classified | The brief identifies construction and a connector suggestion without deciding inventorship.
What limits the cooling-time comparison? | The test conditions have not been compared | No prototype exists | The result is a commercial guarantee | The connector has been patented | A single internal result cannot establish a controlled comparison without checking conditions.''',
    vocabulary='''invention disclosure | Internal account of a proposed invention and its development. | submit an invention disclosure
technical problem | Practical technical difficulty the proposed invention addresses. | define the technical problem
technical effect | Technical result attributed to a feature or process. | substantiate a technical effect
conception | Formation of the inventive idea under the applicable legal test. | investigate contribution to conception
reduction to practice | Implementation or legally relevant realization of an invention. | document reduction to practice
inventorship | Legal identification of the inventor or inventors. | assess inventorship
contribution record | Account of who contributed what and when. | preserve the contribution record
prototype | Preliminary implementation used to explore or test a design. | evaluate the prototype
embodiment | Particular implementation described for an invention. | describe an embodiment
alternative configuration | Different arrangement of components or steps. | disclose an alternative configuration
coolant channel | Passage through which cooling fluid moves. | trace the coolant channel
detachable connector | Connection component designed to be separated. | specify a detachable connector
causal mechanism | Process explaining how a feature produces a result. | explain the causal mechanism
comparative test | Test comparing implementations under stated conditions. | conduct a comparative test
baseline configuration | Reference arrangement used for comparison. | identify the baseline configuration
laboratory notebook | Contemporaneous record of experimental work. | preserve the laboratory notebook
confidential disclosure | Communication within the relevant confidentiality arrangements. | control confidential disclosure
public disclosure | Making information available outside the relevant confidential setting. | review public disclosure''',
    precision='Describe each contribution before assessing its legal significance. Building a prototype and conceiving a claimed feature are not interchangeable descriptions.',
    precision_extra='An inventor interview gathers facts. Seniority does not establish inventorship, and a promising test result does not establish patentability.',
    phrases='''Elicit the mechanism | What does the curved channel change in the flow path?
Probe an alternative | Would the same effect occur with a straight channel?
Trace a contribution | Who first proposed that feature, and what records support the account?
Separate result from explanation | The test reports a shorter time; it does not yet establish why.
Clarify implementation | Did Leo follow the drawings or propose a different arrangement?
Preserve uncertainty | We have not compared the test conditions yet.
Protect disclosure | Please use the approved confidential channel for the drawings.
Summarize evidence | We have a prototype, a reported result, and contribution details to verify.''',
    notes='''Designed versus built | Designed concerns the arrangement; built concerns implementation. A person may have done either or both.
Because versus after | Because asserts causation; after identifies sequence without establishing the cause.
Could versus did | Could describes a possible alternative; did describes what actually happened.''',
    d='''Which question is least leading? | Who proposed the connector, and when? | Leo merely followed instructions, correct? | Amira must be the only inventor, correct? | The manager owns the idea, so is he the inventor? | The neutral question elicits contribution facts without suggesting the desired legal conclusion.
Which test summary is supported? | A shorter cooling time was reported in one test | Faster cooling is guaranteed in all conditions | The connector caused the improvement | Comparable conditions have been confirmed | The brief supplies a reported result but no verified causal or controlled comparison.
What should the interview capture about alternatives? | How a straight channel would change the mechanism | Only the preferred marketing benefit | A guarantee that all alternatives are patentable | An assumption that undisclosed alternatives are already supported | Explaining alternatives identifies technical relationships without inventing evidence or legal conclusions.
Which status is accurate? | Inventorship remains for qualified assessment | All contributors are automatically inventors | The presenter is necessarily the sole inventor | Prototype construction alone settles the issue | The interview gathers facts without establishing the applicable legal inventorship outcome.''',
    dialogue='''Amira | Our enclosure cools faster. I would like the application to focus on that benefit rather than the shape of the tubing.
Daniel | Let us identify the [[technical problem::The technical problem identifies the difficulty addressed rather than substituting a marketing benefit for the mechanism.]] first. What limits cooling in the reference design, and which feature changes that behavior?
Amira | Fluid bypasses part of the enclosure. The curved channel takes it around that area instead of directly to the outlet.
Daniel | That describes a [[causal mechanism::The causal mechanism connects the arrangement to the proposed effect while leaving performance evidence open to review.]]. We should distinguish that explanation from the measurements supporting it.
Amira | One internal test showed a shorter cooling time. I have not checked whether both tests used the same starting temperature.
Daniel | Then we need the [[baseline configuration::The baseline configuration is the reference arrangement needed to interpret the comparison rather than assuming comparable conditions.]] and test conditions before describing the result as a controlled improvement.
Amira | Leo built the enclosure from my drawings, but he suggested making the connector detachable for easier assembly.
Daniel | Record that in the [[contribution record::The contribution record preserves who proposed each feature without prematurely deciding the legal inventorship question.]]. Construction work and a new design suggestion should not be collapsed into one description.
Amira | Should I list only senior engineers as inventors? Leo is a technician and did not present the project to management.
Daniel | Job title does not settle [[inventorship::Inventorship requires the applicable legal assessment of contributions, not a ranking by seniority or presentation role.]]. We need the relevant facts and proposed claims before reaching that conclusion.
Amira | I also sketched a straight channel with a baffle, although we have not built that version yet.
Daniel | Describe the [[alternative configuration::An alternative configuration is another arrangement that should be identified accurately, including whether it was constructed or tested.]] and explain whether you expect it to address the same flow problem.
Amira | The curved version is the one we built. The straight version remains a drawing, with no performance measurements.
Daniel | Identify each [[embodiment::An embodiment is a particular implementation, so the tested version must remain distinct from an untested proposed arrangement.]] separately and avoid implying that the untested version produced the reported data.
Amira | The notebook contains dated sketches and build notes. I can collect those without rewriting the original entries.
Daniel | Preserve the [[laboratory notebook::The laboratory notebook contains contemporaneous development evidence and should be preserved rather than rewritten to fit a preferred account.]] and provide copies through the approved confidential process.
Amira | Marketing wants to show the prototype at a public event next month. I have not approved that request.
Daniel | Flag the proposed [[public disclosure::Public disclosure can have patent consequences under actual law and facts, so the plan requires prompt qualified review.]] for prompt legal review before anyone assumes the timing is harmless.
Amira | I will supply the drawings, contribution details, test conditions, and event request as separate items for your review.
Daniel | That gives the [[invention disclosure::The invention disclosure organizes the technical facts and development history without itself establishing patentability or inventorship.]] a factual foundation without promising protection or treating an initial result as a verified product claim.''',
    rehearsal=['Read the corrected interview and stress designed, built, suggested, and tested where their meanings differ.', 'Switch roles and deliver the final document list using only the supplied development facts.'],
    transfer_title='A drawing was mistaken for a test result', transfer_setup='A second enclosure appears only in a dated sketch. It has not been built or tested. The team wants to include it in the confidential disclosure.',
    transfer='''Engineer: "This is an alternative ___." | configuration | The sketch depicts another arrangement, not an established test outcome.
Reviewer: "Its performance remains ___." | untested | The brief states that no construction or testing has occurred.
Engineer: "I will preserve the dated ___." | sketch | The dated drawing is the supplied development record for this version.
Reviewer: "Describe the expected effect as a ___." | hypothesis | An expected untested effect is a proposition to investigate, not a measured result.'''))

BOOK['units'].append(unit(
    title='Discussing prior art without overstating the search', scene='One reference matches two features, not the entire claim',
    skill='Explain a search result using feature mapping, dates, and the limits of the search scope.',
    brief='Analyst Noor finds Reference R describing a housing and curved channel. The draft claim also requires a detachable connector, which Noor has not located in R. Reference S mentions a detachable connector in a different device. Dates and legal relevance need review. Counsel Ethan must distinguish the references and search limitations.',
    cast='Noor | Search analyst\nEthan | Patent counsel',
    culture=('A useful finding can still be incomplete', 'Describe what a reference discloses before calling it decisive. Make uncertainty usable instead of hiding it behind a yes-or-no label.'),
    a='''Which feature has not been located in R? | The detachable connector | The housing | The curved channel | Every feature in the draft | Noor found the housing and channel but has not located the connector in R.
Where is a connector mentioned? | S, in a different device | Only in the client grant | In an identified passage of R | In no document at all | The facts place the connector in S without establishing its presence in R.
What remains to be reviewed? | Dates and legal relevance | Whether R has been found | Whether the draft requires a connector | Whether Noor performed a search | The case expressly leaves dates and legal significance unresolved for review.''',
    vocabulary='''prior art | Earlier material relevant under the applicable patent law. | assess prior art
novelty | Requirement that claimed subject matter be new under the applicable test. | analyze novelty
inventive step | Requirement addressing whether an invention exceeds the applicable obviousness threshold. | assess inventive step
nonobviousness | US patentability requirement concerning obviousness under applicable law. | evaluate nonobviousness
reference document | Identified source considered in a patent analysis. | retrieve the reference document
feature mapping | Comparison linking claimed features to disclosed material. | prepare feature mapping
disclosure passage | Specific text or figure describing relevant subject matter. | cite the disclosure passage
publication date | Date a document was published. | verify the publication date
priority date | Claimed earlier date whose legal effect requires assessment. | check the priority date
search scope | Boundaries of databases, terms, subject matter, and dates searched. | define the search scope
classification code | Patent-search category identifying technical subject matter. | search by classification code
keyword variant | Alternative term used to locate related material. | include keyword variants
citation trail | Chain of references connected through citations. | follow the citation trail
patent family | Related filings linked through specified priority relationships. | review the patent family
non-patent literature | Relevant material outside patent documents. | search non-patent literature
single-reference analysis | Examination of what one identified reference discloses. | distinguish single-reference analysis
combination rationale | Reasoning for combining teachings under the applicable legal test. | assess the combination rationale
search limitation | Constraint affecting search completeness or interpretation. | disclose the search limitation''',
    precision='Not located is a search finding, not proof of absence. A reference describing some features does not automatically disclose the whole combination.',
    precision_extra='Novelty and obviousness or inventive-step analyses have jurisdiction-specific tests. Do not combine references casually and call the result a single-reference disclosure.',
    phrases='''Locate support | Which passage discloses the connector?
Qualify the finding | I have not located that feature in this reference.
Separate references | R describes the channel; S discusses a connector in another device.
Check dates | Publication and priority information still need verification.
Define search limits | The search covered these databases and keyword variants.
Avoid a guarantee | No close result in this search is not a guarantee of patentability.
Frame the legal issue | Any proposed combination needs the applicable legal analysis.
Report next steps | I will add pinpoint citations and document the remaining search gaps.''',
    notes='''Not found versus absent | Not found reports a search result; absent makes a stronger statement about the material.
Discloses versus suggests | Discloses attributes material to a source; suggests often introduces an inference needing explanation.
Relevant versus decisive | Relevant warrants review; decisive claims that the material resolves the issue.''',
    d='''Which report sentence is supported? | R describes two features; its connector remains unlocated | R conclusively discloses the entire draft | S proves the connector appears in R | No connector exists anywhere in prior art | The findings support a limited account of R, not a universal legal conclusion.
What makes feature mapping traceable? | Pinpoint passages or figures for each feature | Titles without passages | One group label replacing both references | Removing uncertainty from the table | Pinpoint support lets reviewers check each proposed mapping against the actual source.
What must an R-plus-S argument address? | Applicable combination analysis and its factual basis | Only whether both documents are downloadable | Whether the client prefers the title | Automatic combination of all similar documents | A combination argument requires appropriate legal reasoning rather than automatic aggregation.
Which statement fairly describes an unsuccessful search? | No close result was located within the stated scope | No relevant prior art exists | Every claim is patentable worldwide | Commercial launch has been cleared | A search result is bounded by coverage and does not establish universal patentability or clearance.''',
    dialogue='''Noor | Reference R looks close. It shows a housing and curved channel, which are both in our current draft claim.
Ethan | Start with [[feature mapping::Feature mapping links each claimed element to identified source material instead of equating overall similarity with complete disclosure.]] so we can see exactly which passages support each comparison.
Noor | The housing is in paragraph twelve and the channel in figure three, but I have not located the detachable connector.
Ethan | Preserve that [[search limitation::The search limitation states what has not been established and prevents an incomplete finding from becoming proof of absence.]]. Not located in your review is more precise than declaring that the reference cannot disclose it.
Noor | Reference S mentions a detachable connector, although its device is different and the function is not described in the same way.
Ethan | Keep the [[reference document::Each reference document must remain separately identified so that a feature from S is not silently attributed to R.]] identities separate. We should not move a feature from S into the column describing R.
Noor | Could the two documents still raise a problem if neither appears to describe the entire draft combination alone?
Ethan | That calls for the applicable [[nonobviousness::Nonobviousness concerns a distinct patentability analysis under US law, not automatic treatment of multiple documents as one disclosure.]] or inventive-step analysis, including the facts and reasoning supporting any proposed combination.
Noor | I will describe the potential combination without saying that it automatically defeats the claim under every legal system.
Ethan | Identify a possible [[combination rationale::A combination rationale supplies reasoning for considering teachings together and must be assessed under the relevant legal test.]] for counsel to assess rather than treating shared subject matter as sufficient by itself.
Noor | The database gives several dates. I copied the earliest number without identifying what that date represents.
Ethan | Distinguish the [[publication date::The publication date identifies publication and must not be confused with other dates whose legal effect may differ.]] from claimed priority information, and verify the relevant legal timing separately.
Noor | Some results are related filings with different claims. I grouped them together to keep the report shorter.
Ethan | A [[patent family::A patent family groups related filings but does not establish identical claims or legal status for every member.]] can organize results, but the actual document and claim version must remain identifiable.
Noor | We covered two databases, three classification groups, and synonyms for coolant routing, but not every technical publication.
Ethan | State that [[search scope::Search scope identifies actual coverage and makes the limits visible to readers interpreting the findings.]], including limits on non-patent literature and any language coverage.
Noor | The team wants the conclusion changed to no blocking prior art found, which sounds broader than the report supports.
Ethan | Keep the [[novelty::Novelty is a specific patentability question, so the search summary must not become a broad commercial-clearance conclusion.]] discussion tied to the examined features; do not imply freedom to operate or a guarantee of grant.
Noor | I will revise the table, separate documents and dates, and flag the connector question for further review.
Ethan | Add the exact [[disclosure passage::The disclosure passage allows direct verification of each proposed feature mapping rather than reliance on an unsupported summary.]] for every positive mapping. That gives us a report we can analyze, challenge, and update.''',
    rehearsal=['Read the corrected dialogue, stressing not located, separate, and within the stated scope.', 'Switch roles and distinguish R alone from a proposed R-plus-S argument using the printed facts.'],
    transfer_title='The abstract hides a useful figure', transfer_setup='A reviewer finds a potentially relevant figure after the abstract search. The feature and legal date still need verification against the full document.',
    transfer='''Reviewer: "The abstract search did not identify this ___." | figure | The new finding is a figure, not a completed legal conclusion.
Counsel: "Check the complete ___ before mapping the feature." | disclosure | The mapping needs actual disclosed material rather than an abstract-only impression.
Reviewer: "The relevant date remains to be ___." | verified | The brief expressly leaves the relevant legal timing unresolved.
Counsel: "Update the report and preserve its stated ___." | scope | The new finding improves the report without creating an unlimited search guarantee.'''))

BOOK['units'].append(unit(
    title='Explaining claim structure to a technical colleague', scene='The dependent claim adds a feature',
    skill='Translate claim relationships into plain English without changing their scope.',
    brief='For this simplified drafting discussion, claim 1 requires a housing and channel. Claim 2 depends on claim 1 and adds a detachable connector. Engineer Priya thinks claim 2 covers a connector by itself. Patent professional Marcus explains the dependency and checks the draft term the valve, which has no clear earlier introduction. These are unfiled examples, not legal claim-construction conclusions.',
    cast='Priya | Engineer\nMarcus | Patent professional',
    culture=('Explain the relationship before the terminology', 'Technical colleagues may read claim lists as separate product options. Explain what carries forward before introducing drafting labels.'),
    a='''What does claim 2 add in this example? | A detachable connector to the inherited requirements | A connector instead of the housing and channel | A new cooling-time guarantee | A valve replacing every earlier feature | The simplified dependency expressly carries forward claim 1 and adds the connector.
What is unclear about the valve wording? | Which earlier element the term identifies | Whether claim 2 has a connector | Whether claim 1 mentions a housing | Whether the draft has been published | The definite phrase has no clear earlier introduction identifying the intended element.
What is the document status? | An unfiled drafting example | A granted patent with settled scope | An issued infringement judgment | A signed license | The case explicitly describes unfiled examples rather than granted or adjudicated claims.''',
    vocabulary='''claim | Statement defining the subject matter for which protection is sought or granted. | review the claim
independent claim | Claim that does not depend on another claim. | draft an independent claim
dependent claim | Claim incorporating a referenced claim and adding a further limitation. | review a dependent claim
claim dependency | Relationship linking a dependent claim to another claim. | check claim dependency
claim limitation | Requirement expressed in a claim. | identify each claim limitation
claim scope | Extent of subject matter covered under the applicable interpretation. | assess claim scope
antecedent basis | Earlier identification supporting a later reference to an element. | check antecedent basis
preamble | Introductory portion of a claim. | review the preamble
transitional phrase | Wording connecting claim introduction and body with legal significance. | select the transitional phrase
claim body | Portion stating substantive elements or steps. | analyze the claim body
apparatus claim | Claim directed to a device or system. | distinguish an apparatus claim
method claim | Claim directed to steps of a process. | draft a method claim
functional language | Wording describing what an element does. | evaluate functional language
structural limitation | Requirement describing physical structure or arrangement. | identify a structural limitation
further limitation | Additional restriction in a dependent claim. | introduce a further limitation
claim construction | Legal interpretation of claim terms and scope. | address claim construction
claim tree | Diagram or list showing claim dependencies. | check the claim tree
fallback position | Narrower supported position available for appropriate consideration. | preserve a fallback position''',
    precision='In the supplied example, claim 2 contains the housing, channel, and connector requirements. It is not a claim to the connector alone.',
    precision_extra='A plain-English explanation helps the discussion but does not replace the actual claim language or the applicable legal construction.',
    phrases='''Explain inheritance | Claim 2 carries forward the requirements of claim 1.
Identify the addition | The connector is an added limitation, not a replacement.
Check the referent | Which valve does the later phrase refer to?
Locate the first mention | We need to check where that element is introduced.
Separate claim types | This version describes an apparatus rather than a sequence of steps.
Limit the paraphrase | That is a working explanation, not a legal construction.
Discuss narrowing | Adding a requirement narrows this simplified combination.
Keep alternatives distinct | A connector-only concept would need separate drafting and support review.''',
    notes='''In addition to versus instead of | In addition to adds a requirement; instead of substitutes one and changes the relationship.
A versus the | A can introduce an element; the ordinarily refers to an identified element. Exact drafting consequences require review.
Comprising versus consisting of | These can have materially different legal effects. Do not exchange them as ordinary stylistic synonyms.''',
    d='''Which paraphrase matches the supplied claim 2? | A housing and channel with the added connector | A connector with no housing requirement | Either a housing or a connector | A channel only if no connector is present | The stated dependency retains claim 1 requirements and adds the connector.
Which question addresses antecedent basis? | Where is the valve first identified? | Is the cover illustration attractive? | Which client prefers the title? | Has the product achieved commercial sales? | Antecedent basis concerns the earlier identification of the later referenced element.
What should a plain-language paraphrase avoid? | Silently dropping inherited limitations | Naming the added feature | Explaining the dependency | Identifying that the document is a draft | Dropping inherited limitations would change the supplied combination and mislead the technical reader.
Which change requires substantive review rather than casual editing? | Replacing comprising with consisting of | Correcting a page-number typo | Aligning a heading without changing text | Fixing an extra space in a cover label | Transitional phrases can affect legal scope and are not interchangeable stylistic choices.''',
    dialogue='''Priya | Claim 2 says the enclosure of claim 1 has a detachable connector. Does that mean we now have protection for any connector?
Marcus | No. In this draft, the [[dependent claim::A dependent claim retains the referenced requirements and adds a limitation rather than protecting the added element in isolation.]] includes the requirements it inherits from claim 1.
Priya | So the housing and channel remain part of the combination, even though their wording is not repeated on that line?
Marcus | Exactly. The [[claim dependency::Claim dependency identifies the relationship that carries the earlier requirements into the dependent claim.]] carries them forward, and the connector adds another requirement to that combination.
Priya | I had treated the numbered claims like a menu where the reader chooses one component and ignores the others.
Marcus | Think in terms of each [[claim limitation::A claim limitation is a requirement of the claimed combination, not a menu item that can be omitted at will.]]. We must identify all the requirements in the particular claim under discussion.
Priya | Would a claim covering only the connector need to be drafted differently and checked against the original disclosure?
Marcus | Yes. A separate [[independent claim::An independent claim does not depend on another claim, but its drafting and legal support still require assessment.]] would raise its own drafting and support questions; the current dependency does not accomplish that.
Priya | I also noticed the phrase the valve near the end, but I could not find a valve introduced earlier.
Marcus | That is an [[antecedent basis::Antecedent basis concerns the earlier identification needed to make the later reference to the valve clear.]] issue to review. We need to establish which element the phrase is intended to identify.
Priya | The engineer meant a flow-control valve, not the detachable connector. I can point to the relevant drawing.
Marcus | Good. We should check the [[structural limitation::A structural limitation describes the physical element or arrangement, which must match the intended supported feature.]] and its support rather than guessing that two different component names mean the same thing.
Priya | Could I simplify comprising to consisting of? The second phrase sounds more natural to me in ordinary English.
Marcus | Do not change that [[transitional phrase::A transitional phrase can affect legal scope, so these expressions must not be exchanged as stylistic synonyms.]] for style alone. The legal effect needs deliberate review under the applicable law.
Priya | I will leave the operative wording intact and add a separate plain-English explanation for the engineering meeting.
Marcus | That helps, provided you label it as a paraphrase rather than a definitive [[claim construction::Claim construction is the legal interpretation of scope, not an informal engineering paraphrase.]] that settles every possible interpretation.
Priya | I can show claim 1 at the top and claim 2 below it, with the connector marked as an addition.
Marcus | A [[claim tree::A claim tree displays dependencies and helps readers see which requirements are inherited by later claims.]] will make the relationship visible without dropping the inherited housing and channel requirements.
Priya | Then our summary is a housing and channel with a detachable connector, not a connector standing alone.
Marcus | Correct for this example. That narrower combination may be a [[fallback position::A fallback position is a narrower supported position for consideration, not a guarantee of patentability or protection.]] to assess, but it is not a promise of grant or an infringement conclusion.''',
    rehearsal=['Read claim 1 and claim 2 aloud using the supplied paraphrases, emphasizing in addition to rather than instead of.', 'Swap roles and explain the valve-reference problem without guessing which component the draft legally covers.'],
    transfer_title='A different dependency changes the inherited features', transfer_setup='Claim 3 depends on claim 2 and adds a pressure sensor. In this simplified example, claim 2 already includes the housing, channel, and connector.',
    transfer='''Engineer: "Claim 3 inherits the earlier ___." | requirements | The stated dependency retains the requirements already included in claim 2.
Reviewer: "The sensor is an additional ___." | limitation | The new sensor adds a requirement to the inherited combination.
Engineer: "It does not replace the ___." | connector | The connector remains part of claim 2 and is inherited by claim 3.
Reviewer: "Show that relationship in the claim ___." | tree | A claim tree represents the dependency relationship described in the example.'''))

BOOK['units'].append(unit(
    title='Checking drafting support before amending', scene='The new controller was developed after filing',
    skill='Distinguish filed disclosure from later engineering developments when discussing an amendment.',
    brief='The filed application describes a mechanical bypass. A later prototype uses an electronic controller. Engineer Sofia wants to insert the controller into the pending application as a clarification. Patent counsel Ravi has not located support for it in the filed text or drawings. The team must preserve both versions and obtain qualified advice on available filing options.',
    cast='Sofia | Engineer\nRavi | Patent counsel',
    culture=('Accuracy can slow an attractive shortcut', 'A later improvement may be valuable without belonging in the earlier filing. Explain the document boundary without dismissing the engineering work.'),
    a='''Which feature appears in the filed disclosure as described? | A mechanical bypass | The later electronic controller | A tested wireless interface | Every future control system | The brief identifies a mechanical bypass as the feature described at filing.
What is Sofia proposing? | Adding the later controller as a clarification | Deleting the whole application | Withdrawing every drawing | Reporting an existing grant | She wants to insert the later controller while describing the change as clarification.
What has Ravi established? | He has not located support in the filed materials | The amendment is legally permissible | The later prototype has an earlier filing date | A new filing has already been approved | The supplied finding is lack of located support, not a final legal or filing decision.''',
    vocabulary='''specification | Written disclosure forming part of a patent application. | review the specification
application as filed | Application content in its originally filed form. | compare the application as filed
written description | Disclosure supporting the claimed subject matter under the applicable requirement. | assess written description
enablement | Sufficiency of teaching under the applicable legal standard. | evaluate enablement
new matter | Added subject matter not permitted by the applicable disclosure rules. | identify potential new matter
amendment | Proposed or entered change to application documents. | prepare an amendment
support citation | Pinpoint reference to material supporting proposed wording. | provide a support citation
filed drawing | Drawing contained in the relevant filed application. | inspect the filed drawing
later-developed feature | Feature developed after the earlier document or filing. | distinguish a later-developed feature
original disclosure | Content disclosed in the original application. | locate original disclosure
explicit support | Support stated directly in the relevant material. | identify explicit support
inherent disclosure | Feature necessarily present under the applicable analysis rather than merely possible. | assess inherent disclosure
draft history | Record of successive drafting versions. | preserve the draft history
marked-up copy | Version visibly identifying proposed changes. | circulate a marked-up copy
clean copy | Version showing text without visible change markings. | compare the clean copy
support matrix | Table linking proposed wording to source disclosure. | maintain a support matrix
priority entitlement | Right to rely on an earlier date under applicable requirements. | assess priority entitlement
filing strategy | Plan for pursuing protection through appropriate filings. | review the filing strategy''',
    precision='Calling a substantive addition a clarification does not supply support. Compare the proposed wording with the actual filed disclosure.',
    precision_extra='Later development, earlier disclosure, and priority entitlement are separate questions. This scenario does not prescribe a filing route or deadline.',
    phrases='''Locate the basis | Where does the filed application disclose that controller?
Separate versions | That feature appears in the later prototype, not the cited filed passage.
Challenge a label | Calling it a clarification does not answer the support question.
Request precision | Please provide the exact paragraph or drawing reference.
Avoid hindsight | We should not read later knowledge back into the earlier document.
Preserve the record | Keep the filed version separate from the working draft.
Route the decision | We need advice on the available filing options.
Summarize the limit | The proposed addition remains under review; it is not approved for filing.''',
    notes='''As filed versus as amended | As filed identifies original content; as amended identifies content after a change.
Disclosed versus developed | A feature can have been developed without being disclosed in a particular application.
Necessarily versus possibly | Necessarily asserts an unavoidable feature; possibly states only a potential one.''',
    d='''What would most directly support the proposed wording? | A verified relevant passage or drawing in the filed disclosure | A later marketing slide alone | A new prototype photo with no earlier support | The engineer calling it obvious | Support must be assessed against the relevant original disclosure, not supplied by a label.
Which summary avoids hindsight? | The controller is later developed and support is unlocated | The original filing automatically includes later improvements | Every possible controller was necessarily disclosed | The new prototype changes the historical filing contents | The supplied facts distinguish later development from the unresolved original-support question.
Why keep a marked-up copy? | To make proposed wording changes visible for review | To establish patentability by formatting | To replace the original filed record | To give the new feature an earlier date | Visible changes help reviewers assess additions without altering the historical filed document.
Which action is appropriate now? | Review support and available filing options with counsel | File the addition because it is called clarification | Promise the earlier date to every new feature | Delete the filed version from the record | Qualified review must resolve support and options before the team assumes a permissible filing step.''',
    dialogue='''Sofia | The latest prototype uses an electronic controller. Can we add it to the pending application as a clarification of the bypass?
Ravi | First compare it with the [[application as filed::The application as filed is the historical disclosure against which the proposed addition must be assessed.]]. The version I have describes a mechanical bypass, not this later controller.
Sofia | The controller performs a related purpose, but we developed its arrangement after the filing and drew a new circuit diagram.
Ravi | Then identify it as a [[later-developed feature::A later-developed feature must remain distinguishable from what was actually disclosed in the earlier filing.]] while we investigate whether the proposed wording has support in the earlier disclosure.
Sofia | I found a broad sentence saying that flow may be controlled. Would that automatically support any electronic implementation?
Ravi | Not automatically. We need a proper [[written description::Written description asks whether the relevant disclosure supports the claimed subject matter under the applicable legal standard.]] analysis rather than assuming a general result discloses every way of achieving it.
Sofia | I can show the exact sentence and the drawing it references, instead of sending only the revised paragraph.
Ravi | Please provide that [[support citation::A support citation points to the specific original material on which the proposed wording relies.]] so we can evaluate the proposed wording against the actual text and figures.
Sofia | The new diagram is clearer. I was going to replace the old drawing in our shared folder to avoid confusion.
Ravi | Preserve the [[filed drawing::The filed drawing is part of the historical application record and must not be overwritten by a later engineering version.]]. Keep the new diagram separately labeled so that the historical record remains intact.
Sofia | I understand. Describing the addition as clarification does not establish that the original application taught this arrangement.
Ravi | Correct. We must assess potential [[new matter::New matter concerns impermissible added subject matter under applicable rules and cannot be avoided merely by calling an addition clarification.]] and the other disclosure requirements before deciding what can be changed.
Sofia | Would a table listing each proposed phrase beside its original source help you identify the unsupported parts?
Ravi | Yes. A [[support matrix::A support matrix links each proposed phrase to its claimed original basis and exposes missing or disputed support.]] makes both positive citations and unresolved gaps visible without concealing them in a clean draft.
Sofia | I will also keep a version showing insertions and deletions, so the technical and legal reviewers see the same changes.
Ravi | Circulate the [[marked-up copy::A marked-up copy visibly identifies proposed changes so reviewers can assess their substance against the existing text.]] alongside the clean version, with neither described as approved for filing.
Sofia | Management asked whether the electronic version would automatically receive the earlier date because it improves the same product.
Ravi | We cannot promise [[priority entitlement::Priority entitlement depends on the applicable requirements and supported subject matter, not merely on improving the same product.]] on that basis. The relevant subject matter and actual disclosure need assessment.
Sofia | I will report that the later improvement is valuable, but the support and filing route remain unresolved.
Ravi | That is accurate. We can discuss [[filing strategy::Filing strategy evaluates appropriate available routes after considering the actual disclosure, dates, jurisdictions, and legal requirements.]] once we have the records, without inventing a deadline or assuming that every route is available.''',
    rehearsal=['Read the corrected exchange, stressing as filed, later developed, and proposed.', 'Switch roles and state the three records to preserve: original documents, support matrix, and marked-up draft.'],
    transfer_title='The new diagram is not the original diagram', transfer_setup='A reviewer receives a clean drawing labeled revised. The original filed drawing and a change comparison have not been attached.',
    transfer='''Reviewer: "Please attach the original ___ drawing." | filed | The historical filed drawing is needed to compare the proposed changes.
Engineer: "I will also supply the change ___." | comparison | A change comparison makes the differences visible for review.
Reviewer: "The clean version alone does not establish ___." | support | A revised drawing does not itself prove support in the original disclosure.
Engineer: "The proposed revision remains under ___." | review | No approval or completed support assessment is supplied in the scenario.'''))

BOOK['units'].append(unit(
    title='Explaining an office action and agreeing on a response', scene='The examiner raised two different issues',
    skill='Separate the examiner position, proposed response, and procedural status in a client update.',
    brief='A fictional US non-final office action rejects claim 1 over Reference R and separately questions the clarity of the term substantially aligned. The client wants to say the examiner rejected the product. Counsel Elise proposes reviewing the cited mapping and the unclear term before selecting a response. The actual notice controls all dates; no deadline or guaranteed outcome is supplied.',
    cast='Jon | Client engineering lead\nElise | Patent counsel',
    culture=('Challenge reasoning, not the person', 'A firm response can identify a disputed mapping without portraying the examiner as hostile or promising that disagreement will secure allowance.'),
    a='''What does the notice address? | A prior-art rejection and a separate clarity issue | Product safety approval | A final infringement judgment | A granted license | The case identifies a claim rejection and a separate concern about a term.
How should the examiner position be attributed? | The examiner states the cited mapping | The patent office proved the product cannot work | The company admitted every point | The customer rejected the design | The position comes from the office action and should not be turned into a different conclusion.
Which source controls the response timing? | The actual notice and applicable procedure | A guessed deadline from another case | The engineering meeting calendar alone | A standard date invented for the exercise | The brief supplies no date and directs timing to the actual notice and procedure.''',
    vocabulary='''office action | Official communication from a patent examiner or office. | review the office action
non-final action | Procedural action not designated final in the relevant examination process. | respond to a non-final action
ground of rejection | Stated legal basis for rejecting a claim. | address each ground of rejection
examiner position | View or reasoning expressed by the examiner. | summarize the examiner position
response deadline | Time limit governing the required response. | verify the response deadline
docket entry | Recorded matter and deadline information in a tracking system. | verify the docket entry
claim amendment | Proposed or entered change to claim wording. | assess a claim amendment
argument on the record | Reasoning formally submitted in the examination record. | develop an argument on the record
examiner interview | Discussion with an examiner under the applicable procedure. | request an examiner interview
interview summary | Record of the substance and outcome of an examiner discussion. | review the interview summary
allowance | Office determination permitting claims to proceed toward grant subject to requirements. | distinguish allowance from issuance
final rejection | Procedural designation affecting available response routes. | review a final rejection
appeal | Request for review under the applicable review procedure. | assess an appeal
prosecution history | Record of proceedings during patent examination. | review the prosecution history
clarity issue | Concern that wording does not identify its meaning sufficiently. | resolve a clarity issue
distinguishing feature | Feature relied on to differentiate claimed subject matter from cited material. | identify a distinguishing feature
response strategy | Plan for addressing the actual issues raised. | agree on a response strategy
client instruction | Authorized direction from the client on the matter. | obtain client instructions''',
    precision='The notice addresses claims and wording, not whether customers may buy the product. Examiner arguments, client disagreements, amendments, and allowance are separate statuses.',
    precision_extra='Non-final and final are procedural terms. They do not justify ignoring a notice or assuming that a particular response route, extension, or outcome is available.',
    phrases='''Attribute the position | The examiner maps that passage to the channel limitation.
Separate issues | The clarity concern needs a response apart from the prior-art argument.
Disagree precisely | We do not read that passage as disclosing the stated relationship.
Discuss options | An amendment and an argument have different implications.
Avoid a promise | We can explain our position without guaranteeing allowance.
Confirm authority | Please confirm instructions after reviewing the proposed response.
Preserve timing | We will verify the actual deadline and docket entry.
Summarize status | The response is proposed; it has not yet been approved or filed.''',
    notes='''Rejects versus prohibits | A claim rejection is not a general prohibition on making or selling a product.
Proposed versus entered | Proposed describes a requested change; entered indicates the relevant procedural acceptance into the record.
Final versus finished | Final is a procedural designation, not an ordinary-language guarantee that every possible step has ended.''',
    d='''Which client update is accurate? | The office action raises prior-art and clarity issues for response | The product has been banned | The patent has already been granted | An interview guarantees allowance | The notice concerns examination issues, not product prohibition, grant, or a promised result.
Which disagreement is professionally precise? | The cited passage does not appear to disclose that relationship | The examiner is hostile and incompetent | Every citation is irrelevant because we disagree | The client wants protection, so the objection must disappear | This statement challenges the reasoning with an identifiable issue rather than attacking the examiner.
What must happen before calling the response filed? | The actual filing must occur and be verified | The engineer must read a draft | The team must prefer one option | Counsel must open the notice | Draft review and preference do not establish that a response has actually been filed.
Which summary keeps the issues separate? | Check the mapping and independently address the unclear term | Ignore clarity once a reference is disputed | Treat both issues as a product defect | Rename the notice to remove the rejection | Each stated issue needs appropriate attention rather than being erased by disagreement on another point.''',
    dialogue='''Jon | The examiner rejected our product. Management wants a quick assurance that your reply will reverse that decision.
Elise | The [[office action::The office action concerns patent examination issues and should not be misreported as a general rejection or prohibition of the product.]] addresses the claims and their wording, not whether the product can be sold or will succeed commercially.
Jon | The notice points to Reference R for claim 1 and also questions the phrase substantially aligned.
Elise | Those are separate issues. We need to address the [[ground of rejection::The ground of rejection is the stated basis for rejecting the claim, distinct from a separate wording concern.]] and examine the clarity concern rather than assume one answer resolves both.
Jon | Our engineer thinks the channel in R runs beside the housing instead of through the relationship described in our draft.
Elise | That may identify a [[distinguishing feature::A distinguishing feature identifies the particular claimed difference to analyze, not a generalized assertion that the whole reference is irrelevant.]]. Please show the relevant passages and explain the technical relationship precisely.
Jon | We can provide a side-by-side diagram, but it should not introduce details that are missing from the filed application.
Elise | Correct. Any proposed [[claim amendment::A claim amendment changes operative claim wording and requires support and scope review rather than being treated as an informal explanatory note.]] needs support and scope review, while our argument must stay consistent with the actual disclosure.
Jon | Could we first ask the examiner how that passage is being read instead of guessing the intended mapping?
Elise | We can assess an [[examiner interview::An examiner interview can clarify issues under the applicable procedure but does not itself guarantee agreement or allowance.]] under the applicable procedure. A discussion may clarify the issue without guaranteeing agreement.
Jon | If the conversation sounds encouraging, may I tell management that the application has been approved?
Elise | No. An encouraging discussion is not [[allowance::Allowance is a formal examination status and must not be inferred from an encouraging informal discussion.]]. We need an accurate record of what was discussed and the actual subsequent procedural status.
Jon | I will describe the response as proposed until we have reviewed the alternatives and authorized the next step.
Elise | That preserves [[client instruction::Client instruction identifies the authorized direction needed for the matter and must not be assumed from informal interest in an option.]]. We should explain the consequences of an amendment and an argument before confirming the chosen response.
Jon | The notice is labeled non-final. Does that mean we can leave it until the next quarterly engineering meeting?
Elise | No. Verify the [[response deadline::The response deadline comes from the actual notice and procedure and cannot be postponed based on the word non-final.]] and tracking record promptly; the label is not permission to disregard timing.
Jon | I also want the team to understand that a formal response becomes part of the examination record.
Elise | Yes. The [[prosecution history::The prosecution history preserves examination proceedings and submissions, so formal arguments require careful, consistent review.]] matters, so we should review technical explanations and legal arguments carefully before submitting them.
Jon | I will send the mapping and wording comments, then review your proposed alternatives with the authorized client contact.
Elise | We can then agree on the [[response strategy::Response strategy coordinates the distinct issues, supported options, authority, and actual procedure without promising a favorable outcome.]], keeping the notice, instructions, deadline, and eventual filing confirmation separate in the status report.''',
    rehearsal=['Read the corrected update and distinguish the examiner position from the team response.', 'Switch roles and deliver the final action sequence without supplying a deadline or promising allowance.'],
    transfer_title='A draft reply was marked filed', transfer_setup='The response draft has been approved internally, but no submission or office receipt has been verified.',
    transfer='''Coordinator: "The draft is internally ___." | approved | Internal approval is the completed step supplied in the scenario.
Counsel: "That does not establish that it was ___." | filed | Approval alone does not prove submission to the patent office.
Coordinator: "I will check the actual submission ___." | record | The actual filing record is needed to verify the event.
Counsel: "Keep the deadline ___ until its status is verified." | visible | Unverified filing requires continued attention to the real timing obligation.'''))

BOOK['units'].append(unit(
    title='Coordinating international patent filing decisions', scene='An international report is not a worldwide grant',
    skill='Explain the PCT process and obtain specific instructions without promising universal protection.',
    brief='Coordinator Hana has received an international search report and written opinion for a PCT application. Manager Luis calls it a world patent. The company is evaluating markets A, B, and C but has authorized none for the national or regional stage. Local requirements, costs, translations, and actual deadlines remain for verification with the responsible professionals.',
    cast='Luis | IP portfolio manager\nHana | Filing coordinator',
    culture=('Translate the process into decision points', 'A manager needs to know what has happened, what still requires a decision, and who is responsible. Avoid turning a process diagram into a promise of grant.'),
    a='''What documents have arrived? | An international search report and written opinion | A grant covering every country | All national patents for A, B, and C | A signed license for every market | The case supplies international-stage reports, not national or worldwide grants.
Which markets are authorized for the next stage? | None has yet been authorized | All three automatically | Only A by implication | Every PCT country | The brief expressly says no market has been authorized for national or regional action.
Which matters need verification? | Requirements, costs, translations, and actual deadlines | Whether the reports exist | Whether the manager spoke | Whether any market is being evaluated | These implementation and timing matters remain unresolved in the supplied case.''',
    vocabulary='''Patent Cooperation Treaty | Treaty providing an international patent application procedure. | use the Patent Cooperation Treaty route
international application | Application filed under the relevant international procedure. | identify the international application
receiving Office | Office receiving a PCT application under the applicable rules. | identify the receiving Office
International Searching Authority | Authority conducting the relevant PCT international search. | identify the International Searching Authority
international search report | Report identifying relevant search results in the PCT process. | review the international search report
written opinion | Written international-stage assessment under the relevant PCT procedure. | review the written opinion
international phase | International stage of the PCT application process. | complete international-phase tasks
national phase | Stage before national offices under the applicable PCT framework. | plan national-phase entry
regional phase | Stage before a regional office under the applicable framework. | coordinate regional-phase entry
designated Office | Office associated with a designation under the PCT procedure. | verify designated Office requirements
national requirements | Requirements applicable before the relevant national office. | verify national requirements
translation specification | Requirements for the language version needed in a filing. | confirm the translation specification
filing instruction | Authorized direction identifying a requested filing action. | obtain filing instructions
jurisdiction budget | Planned expenditure for pursuing protection in a territory. | approve the jurisdiction budget
local associate | Local patent professional assisting with a jurisdictional matter. | instruct the local associate
grant decision | Decision by the competent office on granting patent rights. | distinguish the grant decision
territorial protection | Rights limited to the relevant territory and legal scope. | explain territorial protection
portfolio review | Assessment of filings and rights against organizational priorities. | conduct a portfolio review''',
    precision='A PCT application is not a world patent. International-stage reports inform further decisions; national or regional offices determine grant under their applicable systems.',
    precision_extra='This exercise provides no filing deadline or route-specific instruction. Actual dates, offices, translations, fees, and procedures require current verification.',
    phrases='''Correct the label | We have a PCT application, not a worldwide grant.
Explain the report | The written opinion is an assessment, not a patent certificate.
Identify the decision | Which markets are authorized for the next stage?
Separate interest from instruction | Evaluating a country is not an instruction to file there.
Confirm responsibilities | Who verifies the local requirements and deadline?
Clarify costs | Does this estimate include translation and local professional fees?
Preserve territorial scope | Any resulting rights must be identified by territory and status.
Close the loop | We need explicit instructions and confirmation of the action taken.''',
    notes='''Application versus patent | An application seeks rights; a granted patent has the actual status and scope established by the relevant system.
Designated versus entered | Designation in a treaty procedure and completion of national-stage actions are different concepts.
Estimate versus authorization | An estimate informs a decision; it does not authorize expenditure or filing.''',
    d='''Which description corrects world patent accurately? | A PCT application with international-stage reports | A guaranteed grant in all selected markets | One patent automatically enforceable everywhere | A license to sell in every country | The supplied process is an application route, not universal grant or commercial permission.
What converts market interest into a filing instruction? | Explicit authorized direction for the specified action | A market appearing on a discussion slide | A translation estimate alone | A search report mentioning a country | A specific authorized instruction is distinct from exploratory discussion and cost information.
What should a budget comparison identify? | What each estimate includes and excludes | Only the smallest headline number | A guarantee that grants cost the same everywhere | An assumption that translations are always included | Comparable budgets require clear coverage of local fees, translation, and other stated items.
Which status remains unresolved? | National or regional action for the evaluated markets | Receipt of the international reports | The existence of the PCT application | Management interest in A, B, and C | No market authorization or completed next-stage action is supplied in the brief.''',
    dialogue='''Luis | The search report has arrived. Can I tell the board that our world patent now covers markets A, B, and C?
Hana | Please call it an [[international application::An international application under the PCT is a filing procedure, not a worldwide granted patent.]] under the PCT. We do not have a worldwide grant from receiving those reports.
Luis | I see an international search report and a separate assessment discussing the claims. Do they perform the same function?
Hana | The [[written opinion::The written opinion provides an international-stage assessment and must not be presented as a certificate granting patent rights.]] gives an assessment under that procedure; neither document itself grants patents in the markets on our list.
Luis | The reports will still help us decide whether the commercial opportunity justifies further work in each market.
Hana | Yes. They inform the [[portfolio review::Portfolio review compares the filings and available information with business priorities without treating an assessment as a grant.]], alongside business priorities and qualified advice on the actual findings.
Luis | The market slide lists A, B, and C. I assumed that putting them on the slide authorized your next steps.
Hana | We need a specific [[filing instruction::A filing instruction is an authorized direction for a specified action and cannot be inferred from a list of markets under evaluation.]]. Evaluation and authorization are different statuses, especially where costs and timing are involved.
Luis | Should the board expect exactly the same requirements in each place once the international stage is complete?
Hana | No. The relevant [[national requirements::National requirements are office-specific and need verification rather than being assumed identical across markets.]] or regional requirements must be checked with the responsible professionals using current information.
Luis | I have three estimates, but one includes translation and another mentions only the local professional fee.
Hana | Then the [[jurisdiction budget::A jurisdiction budget must identify included and excluded costs so that figures for different territories can be compared meaningfully.]] comparison needs clearer assumptions before anyone treats those totals as equivalent.
Luis | We also need to know who checks the language and format of each version, not just who places the order.
Hana | Confirm the [[translation specification::The translation specification identifies the actual language and filing requirements that the prepared version must satisfy.]] and review responsibility. A completed translation is not proof that every filing requirement has been met.
Luis | The local firms can confirm the requirements and actual dates, but the central team must send consistent instructions.
Hana | Each [[local associate::The local associate provides the relevant local professional coordination, while the central team must preserve clear instructions and accountability.]] should receive the authorized scope, documents, and a request for confirmation of the action taken.
Luis | Once the national-stage actions are completed, should the status report say protection is granted in each place?
Hana | No. Entry and the [[grant decision::The grant decision belongs to the competent office and remains distinct from completing national or regional entry actions.]] are separate. Report each application or right using its actual territory and procedural status.
Luis | I will revise the board slide to show reports received, market decisions pending, and local requirements under review.
Hana | Good. That explains [[territorial protection::Territorial protection requires identifying where rights exist and their actual scope and status, rather than implying universal coverage.]] without promising grants, inventing deadlines, or treating the application as permission to commercialize everywhere.''',
    rehearsal=['Read the corrected conversation and distinguish application, report, entry, and grant.', 'Switch roles and state what the three estimates need before the board can compare them.'],
    transfer_title='An estimate was mistaken for an instruction', transfer_setup='A local associate sends an estimate for market B. The client has not authorized filing or approved the budget.',
    transfer='''Associate: "This document is an ___." | estimate | The document describes expected cost rather than an authorized filing action.
Coordinator: "Client authorization is still ___." | pending | The brief says no client filing or budget approval has been given.
Associate: "Please send an explicit filing ___." | instruction | The associate needs an authorized direction for the actual requested action.
Coordinator: "We will also verify the applicable ___." | deadline | The scenario supplies no date, so the real deadline requires verification.'''))

BOOK['units'].append(unit(
    title='Explaining freedom to operate and design-around questions', scene='Our own patent does not answer the launch question',
    skill='Clarify the product, territory, claim status, and scope of a commercial-clearance review.',
    brief='Product lead Mei says the company can launch its enclosure because it owns a patent. Counsel Arun explains that a separate freedom-to-operate review concerns third-party rights and the actual product configuration in market A. The engineers propose moving a connector but have not supplied revised drawings. No clearance opinion, infringement finding, or design-around conclusion has been issued.',
    cast='Mei | Product lead\nArun | Patent counsel',
    culture=('Separate encouragement from clearance', 'Acknowledge the value of the company patent while explaining why it does not settle rights held by others. Avoid letting launch pressure broaden an uncompleted review.'),
    a='''Why does ownership not settle the launch question? | Third-party rights may require separate review | Ownership always prohibits launch | Every patent automatically expires at launch | The company has no patent | The brief distinguishes the company patent from possible third-party rights affecting the actual product.
What is missing for the proposed connector change? | Revised drawings | The name of the proposed market | Any suggestion of a design change | The product lead role | The engineers propose a change but have not provided the revised configuration.
Which conclusion has been issued? | None of the stated legal conclusions | A clearance opinion | An infringement judgment | A confirmed design-around assessment | The brief expressly says that no such opinion, finding, or conclusion has been issued.''',
    vocabulary='''freedom to operate | Assessment of relevant rights affecting specified commercial activity in a territory. | commission a freedom-to-operate review
right to exclude | Patent right to prevent specified acts within its legal scope. | explain the right to exclude
third-party patent | Patent belonging to another party. | review third-party patents
commercial clearance | Qualified assessment addressing specified launch or commercial risks. | define commercial-clearance scope
product configuration | Particular design and components being evaluated. | freeze the reviewed product configuration
territory of interest | Geographic jurisdiction relevant to the proposed activity. | identify the territory of interest
legal status | Current procedural or rights status of a patent or application. | verify legal status
claim chart | Structured comparison of claim requirements with relevant features. | prepare a claim chart
literal infringement | Infringement analysis based on the claim requirements under applicable interpretation. | assess literal infringement
doctrine of equivalents | Jurisdiction-specific doctrine addressing certain equivalents beyond literal wording. | review the doctrine of equivalents
design-around | Product change intended to avoid relevant patent scope, requiring assessment. | evaluate a design-around
blocking patent | Patent whose relevant scope may constrain proposed commercial activity. | investigate a potential blocking patent
expired patent | Patent whose term or rights have ended subject to actual legal status. | verify an expired patent
pending application | Application not yet resolved by the relevant final status. | monitor a pending application
continuing application | Related further application under an applicable filing system. | review continuing applications
clearance opinion | Professional opinion within a defined commercial-clearance scope. | obtain a clearance opinion
residual risk | Risk remaining after the stated review or action. | communicate residual risk
review trigger | Change or event requiring reassessment. | define a review trigger''',
    precision='A patent confers exclusion rights within its scope; it is not a universal permission to commercialize. Patentability and freedom to operate ask different questions.',
    precision_extra='Moving one feature does not automatically establish a successful design-around. The actual configuration, claims, status, territory, and applicable law need review.',
    phrases='''Separate ownership from permission | Our own patent does not settle third-party rights.
Define the review | Which product version and market does the assessment cover?
Request the configuration | Please provide the revised drawings before we assess the change.
Avoid a shortcut | A different appearance does not by itself establish a design-around.
Check the record | We need the current claims and legal status.
Qualify the conclusion | Any opinion must state its scope, assumptions, and limits.
Control changes | A material design change should trigger reassessment.
Report accurately | Clearance is under review, not already confirmed.''',
    notes='''Own versus may use | Own identifies a property relationship; may use can imply permission that requires separate analysis.
Looks different versus falls outside | Visual difference and legal scope are not equivalent tests.
For this version versus for every version | The first limits the assessment; the second expands it beyond the reviewed configuration.''',
    d='''Which launch statement is supported? | Third-party-rights review remains incomplete | Our patent guarantees launch clearance | Moving the connector eliminates every risk | The draft review is an infringement judgment | The case provides no completed clearance or design-around assessment.
What is necessary to assess the proposed change? | The actual revised configuration and relevant claims | Only a statement that it looks different | A sales target without drawings | The company patent cover page alone | Assessment requires the changed design and relevant legal material rather than appearance or ownership alone.
Which scope statement is appropriately bounded? | This product configuration in market A | Every future product worldwide | All affiliates regardless of design | Any market named in a later slide | The brief identifies a specific configuration and market, not universal future clearance.
Which event should be flagged for reassessment? | A material change to the reviewed product | Correcting a non-substantive slide typo | Reordering an internal meeting agenda | Reprinting the same approved cover page | A material product change can affect the basis of the actual review.''',
    dialogue='''Mei | We own a patent on the enclosure, so I told the launch team that the product is clear to sell in market A.
Arun | Ownership gives us a [[right to exclude::The right to exclude concerns specified acts within patent scope and does not itself authorize commercialization free of other rights.]] within the patent scope. It does not settle whether third-party rights affect our product.
Mei | Then the patentability search we commissioned earlier answered a different question from the one the launch team is asking now.
Arun | Correct. A [[freedom to operate::Freedom to operate concerns relevant rights affecting specified commercial activity, distinct from whether the company invention may be patentable.]] review needs a defined product, activity, territory, and current legal information.
Mei | Our first market is A, and the production design has changed since the version used in the earlier review.
Arun | Please identify the current [[product configuration::The product configuration is the actual design being assessed, so an earlier version cannot silently stand in for the changed production design.]] rather than assuming that an earlier drawing still represents what will be sold.
Mei | Engineering proposes moving the connector to the opposite side. The team thinks that should avoid the competitor patent.
Arun | We need the revised drawings before assessing that [[design-around::A design-around is an intended avoidance change whose legal effectiveness requires assessment rather than being established by intent or visual difference.]]. A different appearance does not by itself answer the claim-scope question.
Mei | I can obtain a controlled drawing and a list of changed components, with the old version retained for comparison.
Arun | Good. We can use a [[claim chart::A claim chart compares relevant claim requirements with the product features and helps expose where the actual scope questions arise.]] to organize the relevant comparison, subject to proper claim interpretation and legal analysis.
Mei | The search result includes a granted patent and a related application. Can we treat both as the same right?
Arun | No. Verify the [[legal status::Legal status distinguishes granted rights, pending applications, and other relevant conditions rather than equating related documents.]] and actual claims for each relevant record. Related filings can differ in scope and procedural position.
Mei | We should also make clear that the report is about market A, not every country in the sales forecast.
Arun | Exactly. The [[territory of interest::The territory of interest bounds the jurisdictional review and cannot be expanded merely because another country appears in a sales forecast.]] matters, along with the specified activities and the applicable law.
Mei | Management would like a short answer before the launch meeting, even if several factual questions remain unresolved.
Arun | We can give a concise status, but not label it a completed [[clearance opinion::A clearance opinion is a professional assessment within a defined scope, not a substitute label for an unfinished status update.]] while the configuration and relevant rights are still under review.
Mei | I will replace clear to sell with review ongoing and identify the missing drawing as the engineering team's next action.
Arun | That is accurate. The eventual assessment should also explain any [[residual risk::Residual risk identifies what remains after the stated review and should not be hidden behind an absolute assurance.]] within its stated scope rather than promising that no claim can ever arise.
Mei | Once the design is reviewed, I will flag any further connector or channel change before relying on the same conclusion.
Arun | Make that a [[review trigger::A review trigger is a change requiring reassessment because it may alter the factual basis of the previous conclusion.]]. A scoped assessment stays useful only when the team knows when its underlying facts have changed.''',
    rehearsal=['Read the corrected exchange and distinguish patentability, ownership, and freedom to operate.', 'Switch roles and restate the missing information without promising that the connector change avoids any claim.'],
    transfer_title='The sales team adds another market', transfer_setup='A completed assessment concerns one specified product in market A. Sales now proposes market B, which is outside that assessment.',
    transfer='''Sales: "We want to add another ___." | market | The proposed change is expansion to a different geographic market.
Counsel: "B is outside the existing review ___." | scope | The supplied assessment concerns market A only, not market B.
Sales: "We need the relevant local rights ___." | checked | The new territory requires the appropriate rights assessment rather than automatic reuse.
Counsel: "Do not describe the earlier opinion as ___ clearance." | worldwide | The prior assessment is expressly limited and cannot support universal coverage.'''))

BOOK['units'].append(unit(
    title='Negotiating a patent-license term sheet', scene='Exclusive in one field is not exclusive everywhere',
    skill='Clarify grant scope, economic terms, and unresolved conditions during a licensing discussion.',
    brief='Licensor representative Nia and prospective licensee Ben review a draft term sheet. It proposes exclusivity for industrial cooling in territory A, with other fields excluded. A royalty percentage is discussed, but the net-sales definition and treatment of returns are unresolved. Sublicensing requires a separately negotiated provision. No agreement has been executed.',
    cast='Ben | Prospective licensee\nNia | Licensor representative',
    culture=('Narrow the disagreement', 'Negotiations move forward when each side identifies the specific right or economic assumption it needs. Avoid treating a headline percentage as a complete commercial agreement.'),
    a='''What exclusivity is proposed? | Industrial cooling in territory A | Every use worldwide | All fields in A and B | Only an internal evaluation with no commercial rights | The draft limits proposed exclusivity to the named field and territory.
Which economic issue remains unresolved? | Net-sales definition and returns treatment | Whether any percentage was discussed | Whether Ben is interested | Whether the draft names a territory | The royalty base and return treatment are open even though a percentage has been discussed.
What is the agreement status? | Unexecuted draft terms | A completed worldwide assignment | An executed unrestricted license | A court-imposed license | The brief states that no agreement has been executed and important terms remain open.''',
    vocabulary='''licensor | Party granting rights under a license. | identify the licensor
licensee | Party receiving rights under a license. | identify the licensee
license grant | Provision specifying licensed rights and limits. | negotiate the license grant
exclusive license | License granting exclusivity as defined by the actual agreement. | define the exclusive license
nonexclusive license | License without the specified exclusivity. | distinguish a nonexclusive license
field of use | Defined application area within a license. | restrict the field of use
licensed territory | Geographic scope of licensed rights. | define the licensed territory
sublicense | Permission granted onward under rights allowed by the primary license. | negotiate sublicense rights
royalty base | Amount or measure to which the royalty rate applies. | define the royalty base
net sales | Contract-defined sales measure after specified adjustments. | negotiate net sales
upfront payment | Payment due at the initial contractual stage. | agree an upfront payment
milestone payment | Payment linked to a specified event or achievement. | define a milestone payment
minimum royalty | Contractual minimum payment under the stated terms. | negotiate a minimum royalty
audit right | Contractual ability to verify relevant records. | agree audit rights
improvement rights | Contractual treatment of later improvements. | clarify improvement rights
termination trigger | Event allowing or requiring termination under the agreement. | define a termination trigger
term sheet | Document recording proposed or preliminary commercial terms. | revise the term sheet
execution | Formal signing or completion under the applicable agreement process. | confirm execution''',
    precision='Exclusive must be read with its field, territory, rights, and conditions. A percentage has limited meaning without the agreed royalty base.',
    precision_extra='A term sheet can have legal consequences depending on its actual wording and law. This fictional draft is not executed, and no binding effect or negotiation protection is determined.',
    phrases='''Clarify exclusivity | Exclusive for which field and territory?
Define the economics | Which deductions are included in the net-sales definition?
Separate rate and base | We have discussed the percentage, not settled the amount it applies to.
Check onward rights | Sublicensing needs its own agreed provision.
Trade a specific term | We can discuss that minimum alongside the defined commercial commitment.
Keep versions aligned | Please mark the revised grant language in the next draft.
Preserve open items | The royalty base and returns treatment remain unresolved.
Confirm status | These are proposed terms, not an executed license.''',
    notes='''Exclusive versus unrestricted | Exclusivity can be limited to a defined field or territory and does not imply unlimited rights.
Rate versus base | Rate is the percentage or multiplier; base is the measure to which it applies.
Agreed in principle versus executed | Preliminary agreement on a point and formal completion are distinct statuses; actual legal effect requires review.''',
    d='''Which description matches the proposed exclusivity? | Industrial cooling in A, subject to final terms | Every commercial use in every territory | All improvements automatically owned by Ben | Unlimited sublicensing in every field | The supplied proposal is limited by field and territory and remains unexecuted.
Why is the percentage alone insufficient? | The royalty base and return treatment are unresolved | Percentages cannot be used in licenses | Territory always determines net sales automatically | A draft percentage establishes every payment date | The amount payable depends on the agreed base and adjustments, not only the rate.
Which request requires separate negotiation here? | Permission to sublicense | Confirmation that a draft exists | Repeating the named field | Recording that returns remain open | The brief states that sublicensing requires a separately negotiated provision.
Which closing summary is accurate? | Proposed grant discussed; economics and sublicensing remain open | All rights granted and payment terms settled | Exclusivity automatically extends outside the field | The term sheet has no possible legal relevance | This summary preserves the specific unresolved terms without assuming execution or legal effect.''',
    dialogue='''Ben | The heading says exclusive license. Our sales team reads that as permission to use the technology in any product we develop.
Nia | The proposed [[field of use::The field of use defines the permitted application area and prevents exclusive from being mistaken for unrestricted use.]] is industrial cooling. The heading must be read with that limitation and the rest of the grant.
Ben | We also plan to sell in market B. I assumed the same exclusivity would follow the product wherever it travels.
Nia | The draft [[licensed territory::The licensed territory defines geographic scope, which does not automatically expand with the licensee sales plans.]] is A. Any request to include B needs explicit negotiation rather than an assumption from the word exclusive.
Ben | Understood. We have discussed the percentage, but our finance team cannot calculate the expected payment from the current wording.
Nia | We still need to settle the [[royalty base::The royalty base is the amount or measure to which the percentage applies, so an agreed rate alone does not determine payment.]], including which sales and adjustments the definition actually covers.
Ben | Returns matter for our business. We need the calculation to distinguish invoiced sales from products later returned by customers.
Nia | That belongs in the [[net sales::Net sales is a contract-defined measure whose deductions and adjustments need explicit agreement rather than assumed standard treatment.]] definition. We should agree the treatment and timing rather than rely on an undefined accounting shorthand.
Ben | A regional partner would distribute the product and may want rights to manufacture a version for local customers.
Nia | Distribution and a [[sublicense::A sublicense grants onward rights only as permitted by the primary agreement and must not be inferred from distribution arrangements alone.]] are not interchangeable. Any onward manufacturing rights need the appropriate negotiated provision.
Ben | Could we discuss a lower initial payment if we accept a payment when the first approved product enters commercial production?
Nia | We can discuss a [[milestone payment::A milestone payment depends on a specifically defined event, which needs precise terms rather than an informal expectation of progress.]], but the event, evidence, and payment obligation would need precise agreement.
Ben | Our finance team also wants to know what records we would need to maintain for royalty verification.
Nia | The proposed [[audit right::An audit right defines contractual verification access and conditions, which should be agreed rather than assumed from the royalty obligation alone.]] should address the relevant records and conditions, with appropriate confidentiality and practical arrangements.
Ben | We expect to develop improved connectors. I do not want either side to assume ownership or access without discussing it.
Nia | Then include [[improvement rights::Improvement rights address contractual treatment of later developments and must not be inferred from the original license heading.]] as a separate open item, alongside the licensed patents and any other defined subject matter.
Ben | I will send a marked-up version showing our requests on territory, returns, sublicensing, and later improvements.
Nia | Please keep the [[term sheet::The term sheet records the proposed terms and open issues; its actual legal effect depends on its wording and applicable law.]] status clear. A discussion of those points does not mean the license has been completed.
Ben | Our closing summary should say that the commercial proposal is progressing, with several specified provisions still unresolved.
Nia | Agreed. Do not describe [[execution::Execution refers to formal completion or signing under the actual agreement process, which has not occurred in the supplied case.]] as complete. We need the final terms, proper review, and authorized completion before reporting an executed license.''',
    rehearsal=['Read the corrected negotiation, stressing field, territory, rate, and base.', 'Switch roles and list the four requested revisions without treating proposed terms as completed rights.'],
    transfer_title='The rate is unchanged but the base differs', transfer_setup='Two draft royalty provisions use the same percentage. Draft A permits specified returns deductions; draft B does not. Neither is approved.',
    transfer='''Analyst: "The two drafts use the same ___." | rate | The supplied percentage is identical in both draft provisions.
Counsel: "Their royalty ___ differs." | base | The return deduction changes the amount to which the rate applies.
Analyst: "We must compare the permitted ___." | deductions | The stated difference concerns whether returns may reduce the calculation.
Counsel: "Both provisions remain ___." | proposed | Neither draft has been approved, so neither is a completed agreed term.'''))
