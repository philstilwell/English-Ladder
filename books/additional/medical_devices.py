"""Original software-change, field-action, and sterile-packaging conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='A small software patch still needs an impact assessment',
        skill='Explain the evidence and decisions required before a device-software update.',
        setup='A device team has corrected a software defect in a test build. The fix passes its targeted test, but wider regression work and regulatory assessment are incomplete. The product manager wants to send the update to customers. No release is authorized.',
        cast='Ari|Software quality engineer\nSofia|Device product manager',
        dialogue='''Sofia|The targeted test passes. Can we send the patch to customers this afternoon and finish the remaining paperwork afterward?
Ari|Not yet. The [[change-impact assessment::The change-impact assessment examines the consequences of the modification, including affected functions, risks, evidence, and regulatory questions.]] is incomplete. A passing defect test covers one question, not the whole release.
Sofia|It is only a few lines of code. I thought that made it a minor maintenance change.
Ari|Code size does not establish clinical or functional impact. We need to trace the changed behavior and anything that depends on it.
Sofia|Which evidence should I expect besides repeating the test that originally exposed the defect?
Ari|The justified [[regression testing::Regression testing examines whether the change adversely affects behavior that should still work, beyond the targeted defect correction.]] and other required checks, tied to the affected functions and risk review.
Sofia|The dashboard still shows green results from the previous version. Those should not appear to cover the new build automatically.
Ari|Correct. Confirm the [[configuration baseline::The configuration baseline identifies the controlled hardware and software versions to which the evidence applies.]] for every relevant report so the release package refers to what was actually tested.
Sofia|Does any software change require a new submission, or can we assume a bug fix never does?
Ari|Neither blanket statement is appropriate. Regulatory affairs must document the [[submission assessment::The submission assessment determines the regulatory implications of the actual change; its outcome is not established by calling the change a bug fix.]] for this device and change.
Sofia|We should also consider what customers will need to do and how the update reaches the installed devices.
Ari|Yes. The [[deployment plan::The deployment plan defines the authorized update process, affected configurations, communication, and confirmation of implementation.]] needs the affected configurations, customer instructions, and confirmation steps reviewed.
Sofia|Support proposed a simple message saying the update has no effect on existing workflows. We have not evaluated that claim yet.
Ari|Then do not include it as fact. Explain the verified change and any reviewed user implications without adding reassurance the evidence does not support.
Sofia|What happens if installation does not complete? Customers will need an approved route for that situation.
Ari|The relevant [[recovery procedure::The recovery procedure defines the assessed response to an unsuccessful update; it must not be improvised by customers or support staff.]] and support arrangements must be established through the controlled process.
Sofia|I will change today's milestone from customer release to completion of the review package. The targeted test result can stay visible.
Ari|That is accurate. Keep the open regression and regulatory items beside it, with owners and the evidence needed to close them.
Sofia|Once those are complete, I will ask for the authorized release decision rather than infer approval from a green dashboard.
Ari|And the customer communication must identify the approved version. A corrected defect, a completed review, and an installed update are different milestones.''',
        transfer_title='Old test results are attached to a new build',
        transfer_setup='A release package links test results from build 4.1 to a modified build 4.2 without an impact assessment.',
        transfer='''Engineer: These results identify build 4.1, not the modified ___.|version|The test evidence applies to the identified build rather than automatically covering its successor.
Manager: Assess which conclusions remain applicable after the ___.|change|The modification needs an impact assessment before earlier conclusions are reused.
Engineer: Keep the open work visible in the review ___.|package|The package should show the unfinished assessment instead of implying complete evidence.
Manager: Do not communicate release until the authorized decision is ___.|recorded|A release claim requires the actual authorized decision, not an assumed dashboard status.''',
        reference=('FDA: Software Changes to an Existing Device', 'https://www.fda.gov/regulatory-information/search-fda-guidance-documents/deciding-when-submit-510k-software-change-existing-device')),
    scenario(
        title='A field notice reaches the hospital, but not every affected unit',
        skill='Track a device field action using identifiers and confirmed completion rather than email counts.',
        setup='An approved fictional field notice identifies a particular model and serial-number range. A distributor has emailed ten hospitals, but no device-level responses have been received. The field-action coordinator and service lead must establish implementation status under the authorized plan. They are not determining the notice\'s clinical instructions or regulatory classification.',
        cast='Lena|Field-action coordinator\nOmar|Service lead',
        dialogue='''Omar|The distributor emailed all ten hospitals. Can the dashboard show the field action as complete?
Lena|It can show notifications sent. We still need the [[affected population::The affected population is the set of devices within the notice's specified scope, not simply the number of customer emails sent.]] reconciled to the model and serial-number range in the approved notice.
Omar|Some hospitals have several units, and devices may have moved between departments since purchase.
Lena|Then use the [[distribution records::Distribution records identify where devices were supplied and support follow-up when their current locations need confirmation.]] to begin the trace, followed by the required customer confirmation.
Omar|The hospital contact may acknowledge the email without checking every unit. We need that distinction in the response form.
Lena|Exactly. [[Acknowledgment::Acknowledgment confirms receipt or recognition of the communication; it does not establish that every required device action has been completed.]] is a communication milestone, not proof that the instructions were carried out.
Omar|One customer asks whether an older unit of the same model is included. Its serial number is outside the notice's range.
Lena|Check the exact identifier against the approved scope. Do not expand or narrow the notice casually; route any ambiguity to the responsible team.
Omar|Another contact asks what to do with a device currently in clinical use. I should not improvise a recommendation during the service call.
Lena|Use the approved instructions and the designated clinical or technical escalation route. Our coordination must not alter the authorized message.
Omar|For each affected unit, we should capture the action status and the supporting confirmation required by the plan.
Lena|Yes. That is [[device-level reconciliation::Device-level reconciliation accounts for each relevant device and its action status rather than relying on a customer-level email total.]]. Keep unknown locations and unanswered requests visible as open items.
Omar|Can a nonresponse be treated as no affected stock? The distributor says silence usually means there is nothing to report.
Lena|No. Silence is not a verified inventory result. Follow the plan's contact and escalation steps and record the attempts accurately.
Omar|How do we judge whether the notification process itself has worked?
Lena|The plan includes [[effectiveness checks::Effectiveness checks assess whether the field communication and required response achieved their intended purpose, rather than merely counting messages.]]. Their results must be evaluated, not replaced by the number of emails in the sent folder.
Omar|I will keep receipt, device identification, and action completion as separate fields in the worklist.
Lena|Good. Any formal [[closure::Closure is the authorized conclusion of the field action after its required evidence and conditions are satisfied.]] must follow the responsible team's review and applicable requirements.
Omar|Today's update will say ten hospitals contacted, responses pending, and no device-level completion yet confirmed.
Lena|That gives us a reliable starting point for follow-up without suggesting the safety communication has reached every device or been fully implemented.''',
        transfer_title='One hospital reply is counted as six completed devices',
        transfer_setup='A hospital with six potentially affected devices acknowledges a notice. Its reply does not identify the devices or confirm the required action.',
        transfer='''Service lead: The reply confirms receipt, not device-level ___.|completion|Acknowledging the notice does not show that the required action was completed for each device.
Coordinator: Obtain the required device identifiers and action ___.|status|Device identifiers and status are needed to reconcile the potentially affected population.
Service lead: Keep the six units pending until the evidence is ___.|verified|The reply lacks the evidence needed to establish each unit's position.
Coordinator: Route unresolved cases through the approved follow-up ___.|plan|The approved plan determines the next contact and escalation steps for unresolved cases.''',
        reference=('FDA: Recalls, Corrections and Removals for Devices', 'https://www.fda.gov/medical-devices/postmarket-requirements-devices/recalls-corrections-and-removals-devices')),
    scenario(
        title='A new carton does not automatically preserve a sterile package',
        skill='Explain packaging-system evidence and distinguish barrier integrity from a cosmetic change.',
        setup='A device manufacturer proposes a smaller shipping carton for a terminally sterilized product. The inner sterile package is unchanged, but the fit and protective inserts will change. Existing distribution and shelf-life evidence relates to the old packaging configuration. No change is approved.',
        cast='Keira|Packaging engineer\nNoah|Operations manager',
        dialogue='''Noah|The smaller carton reduces shipping volume, and the inner pouch is unchanged. Can we classify this as a purely cosmetic change?
Keira|Not from that fact alone. The [[packaging system::The packaging system includes the sterile barrier and relevant protective packaging; changing the outer configuration can affect protection.]] includes how the barrier is protected during handling, transport, and storage.
Noah|The new insert holds the device more tightly. That could change where loads are applied to the pouch.
Keira|Exactly. We need an impact assessment for the [[sterile barrier::The sterile barrier is the packaging that maintains the sterile condition until the intended point of use, within its established conditions.]] and the product, not just a comparison of carton dimensions.
Noah|We already have a transport report. Why would its conclusions need review if the same carrier handles the shipment?
Keira|The tested [[configuration::Configuration identifies the actual combination of packaging components and arrangement covered by the evidence.]] was different. The carrier's identity does not show that the new arrangement behaves the same way.
Noah|Would a photograph after a trial shipment be enough to show that the pouch still looks intact?
Keira|Visual observations may contribute, but the plan needs justified [[package-integrity::Package-integrity evidence addresses whether the barrier remains intact; a photograph alone does not establish every relevant performance requirement.]] evidence and the other applicable performance checks.
Noah|The commercial team also wants to keep the same shelf-life claim. The carton change should not become an automatic extension.
Keira|Correct. Review the [[shelf-life::Shelf-life evidence supports the claimed storage period under defined conditions; a packaging change does not automatically preserve or extend that support.]] support and determine what remains applicable. Keep the claim tied to the assessed configuration and conditions.
Noah|Could a passing seal-strength result cover everything? It would be easier to explain one number than several reports.
Keira|No single number automatically covers the whole system. Seal strength, integrity, product protection, and opening performance answer related but different questions.
Noah|Opening matters too. A tighter insert could make removal harder even if transport protection improves.
Keira|Yes, consider [[aseptic presentation::Aseptic presentation concerns making the sterile product available at use without compromising its sterile condition, not just surviving transport.]] and the intended handling sequence through the appropriate evaluation.
Noah|I will tell procurement this is a proposal under review. They should not replace the approved carton merely because the new one is available.
Keira|Good. We also need the exact component specifications and suppliers tied to the change record so the evaluation matches what would be purchased.
Noah|Can you give the review team a list of existing evidence, the gaps, and the proposed basis for any additional work?
Keira|Yes. We will justify the plan rather than automatically discard every earlier result or assume it all transfers unchanged.
Noah|Then the savings case will remain conditional on the quality, performance, and regulatory review required for the change.
Keira|That is the right status. Smaller shipping volume is a business benefit, not evidence that the revised packaging protects sterility and function.''',
        transfer_title='A packaging test covers an earlier insert',
        transfer_setup='A distribution-test report identifies insert A. The proposed package uses insert B, and no impact assessment has been completed.',
        transfer='''Engineer: The report covers the earlier packaging ___.|configuration|The named insert is part of the tested configuration and differs from the proposal.
Manager: Assess the effect of the new insert before reusing the ___.|conclusion|The earlier conclusion cannot automatically be applied to a changed package.
Engineer: Keep the change pending while the required evidence is ___.|reviewed|The impact assessment and evidence review are incomplete, so approval is not established.
Manager: Do not substitute components before the authorized change ___.|decision|A proposed component replacement requires the appropriate authorized decision before implementation.''',
        reference=('FDA: Recognized ISO 11607-1 Packaging Standard', 'https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?standard__identification_no=44769')),
]
