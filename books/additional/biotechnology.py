"""Original biotechnology evidence, sample-identity, and data-use conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A familiar cell-line label is not an identity check',
        skill='Discuss cell-bank identity and contamination status without overstating what a test establishes.',
        setup='A research team wants to compare a newly received human cell stock with its existing working stock. Labels look similar, but the identity records and passage history have not been reconciled. A negative mycoplasma result is available only for the existing stock. This discussion concerns research readiness, not a laboratory protocol.',
        cast='Inez|Cell-platform scientist\nCaleb|Project scientist',
        dialogue='''Caleb|The new stock has the same cell-line name as ours. Can we combine its results with the current study?
Inez|Not on the label alone. We need the [[cell-line authentication::Cell-line authentication establishes identity through appropriate evidence; a matching label alone is not an identity check.]] records and a clear link to the material we actually received.
Caleb|Our current stock tested negative for mycoplasma. I assumed that covered the comparison.
Inez|That result concerns the tested stock and sampling point. It does not establish the new stock's identity or contamination status.
Caleb|Then identity testing and [[mycoplasma testing::Mycoplasma testing checks for a particular contamination concern; it is not interchangeable with establishing the cell line's identity.]] answer different questions, even when both appear in the quality package.
Inez|Exactly. We need the relevant results, methods, dates, and material identifiers, with their limits intact.
Caleb|The old stock's label also has a passage number. The incoming paperwork lists a different number without explaining the counting convention.
Inez|Reconcile the [[passage history::Passage history records the sequence of cell subculturing and relevant lineage information; inconsistent counting needs clarification.]]. Do not assume two identical numbers describe equivalent histories or that different numbers necessarily prove a problem.
Caleb|The supplier refers to a master bank, while our experiments use a working bank. Can you explain the relationship in the project summary?
Inez|The [[working cell bank::A working cell bank supplies routine work from a defined cell-bank lineage; its relationship to the source bank must remain traceable.]] should have a traceable relationship to the source bank under our system.
Caleb|Could normal-looking cells be enough reassurance while we wait for the records?
Inez|No. Appearance may be an observation, but it does not rule out misidentification or [[cross-contamination::Cross-contamination introduces material from another source and may not be excluded by normal-looking morphology alone.]].
Caleb|We have not used the incoming stock yet. Should I tell the team the comparison is awaiting the readiness review?
Inez|Yes. Follow the site's handling and status controls, and keep the two stocks and their records distinct while the questions are resolved.
Caleb|I will request the missing information rather than rewrite the incoming label to match our familiar name.
Inez|Good. Preserve the [[provenance::Provenance identifies the material's origin and history; relabeling without resolving the discrepancy would hide that information.]] and record any authorized correction with its basis.
Caleb|Once the records are reconciled, we still need to decide whether pooling the datasets answers the study question.
Inez|Correct. Confirmed identity does not by itself establish that all experimental conditions are comparable.
Caleb|I will separate the material-readiness question from the data-combination decision in the update.
Inez|That gives the team two clear checks instead of one reassuring but unsupported statement that the stocks are the same.''',
        transfer_title='A result from the old stock is attached to the new one',
        transfer_setup='A spreadsheet links an existing stock\'s contamination-test result to a newly received stock. The new stock has not been assessed.',
        transfer='''Scientist: This result belongs to the previously tested ___.|stock|The record identifies the old stock and does not assess the new material.
Reviewer: Restore the correct link and retain the correction ___.|history|Traceable correction preserves how the wrong association was identified and fixed.
Scientist: Mark the new stock's test status as ___.|unestablished|No assessment of the new stock has been supplied, so its status cannot be inferred.
Reviewer: Keep identity and contamination as separate review ___.|questions|Material identity and a specific contamination result are distinct evidence questions.''',
        reference=('ATCC: Cell Line Authentication Test Recommendations', 'https://www.atcc.org/resources/technical-documents/cell-line-authentication-test-recommendations')),
    scenario(
        title='The sequencing batches also separate every study group',
        skill='Explain confounding and challenge a confident biological interpretation of a batch-aligned result.',
        setup='A fictional RNA-sequencing study placed every case sample in batch A and every control sample in batch B. The expression plot separates the groups. No batch-independent confirmation exists. The analyst and study scientist are discussing the interpretation and a possible follow-up design, not a validated diagnostic test.',
        cast='Ruth|Bioinformatics analyst\nDev|Study scientist',
        dialogue='''Dev|The expression plot separates cases and controls cleanly. Can we call this a disease signature in the report?
Ruth|Not yet. The groups also separate by processing batch, so a [[batch effect::A batch effect is systematic variation associated with processing groups rather than necessarily the biology under study.]] could contribute to the pattern.
Dev|Every case was in A and every control in B. I thought the analysis could simply adjust for that afterward.
Ruth|Here we have complete [[confounding::Confounding means the biological group and processing batch vary together, preventing their separate effects from being identified from this design alone.]] between group and batch. An adjustment cannot create the missing independent comparison.
Dev|Would sequencing each sample again count as more independent evidence for the disease difference?
Ruth|That would add [[technical replicates::Technical replicates repeat measurement of the same biological material; they do not create additional independent biological samples.]], depending on what is repeated. It would not create new independent biological samples by itself.
Dev|Then we need to distinguish the number of samples from the number of times each was measured.
Ruth|Yes. [[Biological replicates::Biological replicates are independent biological samples that capture relevant biological variation rather than repeated readings of one sample.]] provide a different kind of information. The sample structure must stay visible in the analysis.
Dev|The plot is still useful for spotting the problem, even if we cannot interpret the separation as purely biological.
Ruth|Exactly. Keep the plot, annotate the batch assignment, and explain the design limitation rather than hide the uncomfortable grouping.
Dev|Could we remove genes that seem batch-sensitive until the case-control separation looks more convincing?
Ruth|Not as an outcome-driven cleanup. Filtering needs a defensible basis, and it cannot establish which part of a perfectly confounded pattern is biological.
Dev|For follow-up, I want the study team and analysis team to agree the assignments before sample processing begins.
Ruth|We should review a [[balanced design::A balanced design distributes relevant biological groups across processing conditions so those factors are not automatically identical.]] and the relevant constraints before generating more data.
Dev|We will also need enough metadata to reconstruct how every sample moved through processing.
Ruth|Correct. The [[sample metadata::Sample metadata describe origin, grouping, processing, and other relevant characteristics needed to understand the analysis design.]] must link reliably to the expression data, including any changes or exclusions.
Dev|What can we state now without implying the study is worthless?
Ruth|That the observed separation aligns with both disease group and batch, so this dataset alone cannot separate those explanations.
Dev|I will revise the headline and request review of the follow-up design. We will not present this plot as a validated disease classifier.
Ruth|Good. The limitation identifies what the next study needs to resolve; it does not require pretending we observed no pattern at all.''',
        transfer_title='Repeated readings are counted as new donors',
        transfer_setup='Samples from five donors are each measured twice. A summary reports ten independent donors. No additional donors were recruited.',
        transfer='''Scientist: We have five donors, not ten independent biological ___.|replicates|Repeating measurements of the same five donors does not add new independent donors.
Analyst: The extra measurements provide technical repeat ___.|readings|The repeated measurements add readings of existing biological material rather than new donor sources.
Scientist: Keep the donor-to-measurement links in the ___.|metadata|Metadata must preserve which measurements came from the same donor or sample.
Analyst: Correct the sample-size claim before interpreting the ___.|analysis|The analysis must reflect the real dependence and number of independent samples.''',
        reference=('EMBL-EBI: Experimental Design for RNA-seq', 'https://www.ebi.ac.uk/training/materials/introduction-to-rna-seq-materials/intro-fundamentals/experimental-design-for-rna-seq/')),
    scenario(
        title='The dataset is coded, but the proposed use has changed',
        skill='Clarify research-use permissions and data-sharing boundaries before a new collaboration.',
        setup='A team has authorized access to coded human research data for a named study. A partner proposes a different analysis and requests a copy. The new purpose, partner access, and applicable consent limitations have not been reviewed. No transfer has occurred.',
        cast='Farah|Translational scientist\nBen|Research-governance lead',
        dialogue='''Farah|The partner can run the new analysis next week. Since the files have study codes rather than names, may I send a copy?
Ben|Not yet. [[Coded data::Coded data use identifiers such as study codes; coding does not by itself make every use or transfer unrestricted.]] are not automatically unrestricted. What purpose and recipients does our current authorization cover?
Farah|It names our existing study. The partner wants to investigate a different outcome using the same records.
Ben|Then we need a [[secondary-use::Secondary-use review assesses a further research purpose beyond the initially authorized use, rather than assuming access covers every question.]] review before treating the proposal as covered.
Farah|The scientific question is related. Does that make it close enough to proceed while the paperwork catches up?
Ben|Related scientifically does not settle the permission. Check the [[consent scope::Consent scope defines the relevant uses participants agreed to and any limits that must be respected in the proposed research.]] and the applicable institutional and repository conditions.
Farah|Some records may have different restrictions. I had planned to send one combined file for convenience.
Ben|Map the [[data-use limitations::Data-use limitations specify restrictions attached to the records or consent groups; combining files does not remove those restrictions.]] before combining or transferring anything. We cannot erase differences by exporting them together.
Farah|The partner has a secure system and experienced analysts. Would security approval be sufficient?
Ben|Security is necessary, but it does not authorize the purpose or recipients. We also need the appropriate [[data-use agreement::A data-use agreement records permitted handling and use between parties; it must align with the governing permissions rather than replace them.]] and access decisions.
Farah|Could I give them my login so they can inspect the fields without receiving a separate copy?
Ben|No. Use the approved access process with named authorized users. Sharing credentials would bypass the controls we are trying to verify.
Farah|I will prepare the proposed question, required fields, analysts, and planned outputs for review.
Ben|Include whether any new linkage is proposed and how outputs will be checked. We need the actual workflow, not just the project's title.
Farah|There is also a recent participant request concerning further use. I do not know how it affects copies or completed analyses.
Ben|Route that [[withdrawal request::A withdrawal request requires review under the relevant consent, policy, and legal framework; its effects should not be invented or ignored.]] through the responsible team. Do not promise universal deletion or assume it has no effect.
Farah|For now, the partner gets no files or credentials. I can explain that the new analysis needs its own review.
Ben|Yes. Preserve the current access boundaries while the reviewers establish which records and uses, if any, are permitted.
Farah|Once the decision arrives, I will confirm the exact approved dataset and recipient list before arranging the transfer.
Ben|And retain the authorization with the transfer record. Scientific enthusiasm is valuable, but the permitted scope must remain traceable.''',
        transfer_title='A new collaborator requests an existing login',
        transfer_setup='A collaborator is not yet an approved user of a controlled-access research dataset and asks to borrow a team member\'s login.',
        transfer='''Scientist: Existing access does not authorize sharing our ___.|credentials|Credentials identify authorized access and must not be lent to bypass user approval.
Governance lead: Submit the collaborator through the named-user access ___.|process|The collaborator needs the applicable review and authorization for their own access.
Scientist: We must also confirm that the proposed question is a permitted ___.|use|User approval and permitted research purpose are related but separate requirements.
Governance lead: Keep the data within the current authorized ___ meanwhile.|scope|The unresolved proposal does not expand the existing authorization while review is pending.''',
        reference=('NIH dbGaP: Data Access Requests and Data-Use Limitations', 'https://dbgap.ncbi.nlm.nih.gov/FAQs/data-access-requests/')),
]
