"""Additional oncology encounters about records, transitions, and practical burdens."""
from books.supplements import scenario

SCENARIOS = [
scenario(title='Preparing a second-opinion record',
    skill='Support a second opinion and distinguish a complete referral packet from a guaranteed recommendation.',
    setup='Patient Mira asks Dr Hart for a second opinion. The receiving service requests the pathology report, relevant imaging, and treatment summary, with authorized transfer arrangements. The clinician supports the request. No new treatment recommendation or review appointment is confirmed.',
    cast='Mira | Patient\nDr Hart | Oncologist',
    dialogue='''Mira | I would like a second opinion, but I worry that asking will sound as though I do not trust you.
Dr Hart | You can ask for another review. Let us discuss the information the receiving service needs and the transfer process.
Mira | They requested a pathology report. Is that different from the short diagnosis line in my appointment letter?
Dr Hart | Yes. The [[pathology report::The pathology report contains the relevant tissue-assessment findings and is more specific than an abbreviated diagnosis in an appointment letter.]] contains the relevant findings, not merely the abbreviated label in a letter.
Mira | They also asked for the images, not only the written scan report. Why would both be requested?
Dr Hart | The reviewing team may need the actual [[imaging studies::Imaging studies include the acquired examinations used for review and are distinct from the written summaries describing them.]] as well as the reports describing them.
Mira | I have had treatment at two sites. I do not want the second team to assume the list from one site is complete.
Dr Hart | We should verify the [[treatment summary::A treatment summary records relevant prior therapy and must be checked across sites rather than assumed complete from one institution's list.]] across the relevant records, including what remains unconfirmed.
Mira | Does sending all the records mean the second team will definitely recommend something different?
Dr Hart | No. A second review may agree, differ, or need further information; we cannot promise its conclusion.
Mira | I would like to know what I am authorizing when the records are transferred.
Dr Hart | The [[record-transfer authorization::Record-transfer authorization defines the appropriate permission for sending specified information to the receiving service through the approved process.]] should identify the relevant information and recipient through the approved process.
Mira | If a specimen is requested for review, is that automatically included with an electronic report?
Dr Hart | Not necessarily. Any specimen or slide request has its own actual handling and transfer arrangements.
Mira | I will ask the receiving service what is still missing instead of assuming that one uploaded file completes everything.
Dr Hart | That is useful. A [[referral packet::A referral packet is the collection of relevant documents and materials required by the receiving service and may need more than one uploaded file.]] can be incomplete even when some documents have arrived.
Mira | Who will tell me whether the review appointment is actually confirmed?
Dr Hart | We should identify the receiving contact and distinguish receipt of records from an accepted appointment.
Mira | Then I can ask for a review without treating the transfer itself as a new treatment plan.
Dr Hart | Exactly. [[Appointment confirmation::Appointment confirmation establishes an actual scheduled review and is separate from a request being sent or records being received.]] and the eventual clinical recommendation remain separate steps.''',
    transfer_title='The images have not arrived',
    transfer_setup='The receiving team has the pathology report and treatment summary but not the imaging studies. No appointment is confirmed.',
    transfer='''Patient: "The imaging studies are still ___." | missing | The receiving service has not yet received the actual imaging studies.
Clinician: "The report and summary have ___." | arrived | The scenario confirms receipt of those two documents only.
Patient: "The referral packet is not ___." | complete | Missing requested imaging means the packet remains incomplete.
Clinician: "The appointment is not yet ___." | confirmed | No scheduled review appointment has been confirmed in this update.'''),
scenario(title='An oncology handoff after hospital discharge',
    skill='Reconcile inpatient changes with the oncology plan and assign unresolved questions.',
    setup='Hospital clinician Dr Sen hands over patient Jules to oncologist Dr Ford after discharge. A medicine list was changed in hospital, but the outpatient record still shows an earlier list. The clinicians will verify the actual discharge instructions and assign follow-up. No medicine names, doses, or authority to restart treatment are supplied.',
    cast='Dr Sen | Hospital clinician\nDr Ford | Oncologist',
    dialogue='''Dr Sen | Jules has been discharged, and the hospital medicine list differs from the earlier outpatient list. We need to reconcile them.
Dr Ford | Please identify the verified changes and their source rather than asking the patient to choose between two conflicting lists.
Dr Sen | The [[discharge summary::The discharge summary records the hospital episode and discharge instructions but must be checked against the actual current plan and medicine information.]] is available, but I want to confirm that the current version reached your team.
Dr Ford | We will acknowledge receipt and review the actual instructions before presenting the earlier list as current.
Dr Sen | Some changes relate to the hospital episode, and the outpatient record has not yet been updated.
Dr Ford | That creates a [[medication discrepancy::A medication discrepancy is a conflict between medicine records or instructions that requires verification rather than a guess about which version applies.]] requiring verification. The language of the handoff must not imply that both lists are simultaneously correct.
Dr Sen | I will distinguish a documented instruction from a suggestion that still needs the responsible clinician's decision.
Dr Ford | Good. We also need the reason for each verified change, where the actual record provides it.
Dr Sen | A note mentions treatment being held, but the wording alone does not authorize restarting it today.
Dr Ford | A [[treatment hold::A treatment hold indicates an interruption under the actual plan and does not itself specify when or whether treatment should resume.]] and a restart decision are different. We need the responsible oncology assessment.
Dr Sen | The patient is worried that discharge means every cancer-care question has already been settled.
Dr Ford | Discharge does not automatically resolve the outpatient plan. We should explain what is confirmed and what remains open.
Dr Sen | One result is still pending, and its reviewing clinician needs to be identified explicitly.
Dr Ford | Let us assign [[result ownership::Result ownership identifies who must review and act on a pending result so it is not lost between inpatient and outpatient services.]] instead of assuming that whichever team sees it first will take responsibility.
Dr Sen | I will include the appropriate contact for questions about the hospital changes.
Dr Ford | And our team will confirm the oncology follow-up arrangements through the actual service process.
Dr Sen | The patient should receive one clear explanation once the conflicting information is resolved.
Dr Ford | A [[reconciled plan::A reconciled plan aligns verified instructions and responsibilities after discrepancies are resolved rather than combining conflicting records without review.]] needs verified instructions, not a merged list that preserves contradictions.
Dr Sen | I will send the current summary and confirm that the outstanding tasks have named owners.
Dr Ford | We will provide [[handoff acknowledgment::Handoff acknowledgment confirms that the receiving team obtained the information and accepted the relevant responsibilities rather than merely receiving a file.]], keeping discharge, pending results, and treatment decisions distinct.''',
    transfer_title='A pending result needs an owner',
    transfer_setup='The discharge summary lists a pending result but no reviewing clinician. The two teams clarify who will review it. No result is yet available.',
    transfer='''Hospital clinician: "The result is still ___." | pending | The result is not yet available in the supplied update.
Oncologist: "The reviewing clinician was not ___." | named | The summary omitted who was responsible for reviewing the result.
Hospital clinician: "We need explicit ___." | ownership | The teams must assign responsibility rather than assume another service will act.
Oncologist: "No conclusion can be drawn from an unavailable ___." | result | A pending result cannot support an interpretation before it exists.'''),
scenario(title='Discussing the financial burden of treatment',
    skill='Invite practical concerns without promising coverage or treating cost-related difficulty as refusal.',
    setup='Patient Rowan tells Dr Bell that transport costs and unpaid time away from work may interfere with appointments. Dr Bell asks permission to involve the support team and discusses verifying actual coverage and assistance options. No insurance approval, eligibility decision, or treatment substitution is supplied.',
    cast='Rowan | Patient\nDr Bell | Oncologist',
    dialogue='''Rowan | I want to keep my appointments, but transport and unpaid time away from work are becoming difficult to manage.
Dr Bell | Thank you for telling me. Those barriers belong in the care discussion, not in a judgment about your commitment.
Rowan | I was afraid that mentioning money would be recorded as refusing the treatment.
Dr Bell | A [[cost-related barrier::A cost-related barrier is a practical difficulty affecting access and is not equivalent to an informed refusal of treatment.]] is different from refusing treatment. We should document what is actually making attendance difficult.
Rowan | The hospital estimate also uses terms I do not understand, and I do not know which amount I might owe.
Dr Bell | The appropriate team can help clarify [[out-of-pocket costs::Out-of-pocket costs are amounts the patient may need to pay under the actual coverage arrangements and cannot be guaranteed from an unverified estimate.]] under your actual coverage, without promising a figure before verification.
Rowan | Could someone help with transport or finding out whether an assistance program is relevant?
Dr Bell | With your permission, we can involve [[patient navigation::Patient navigation helps coordinate practical access and support across services without replacing the clinical plan or guaranteeing eligibility.]] or the relevant support service to explore those options.
Rowan | I would like that, but I do not want my employer contacted automatically.
Dr Bell | We should agree on the information-sharing permissions and recipients rather than treat a support referral as unlimited consent.
Rowan | If an assistance application is submitted, does that mean the cost will definitely be covered?
Dr Bell | No. [[Eligibility review::Eligibility review checks whether the program's actual criteria are met and is separate from submitting an application or receiving approval.]] and approval remain separate steps, and we should be clear about what is still pending.
Rowan | I can provide the documents the team actually needs, but I may need help understanding the forms.
Dr Bell | We can ask what language and administrative support is available through the real service.
Rowan | Does telling you about the cost mean you will change treatment without discussing it with me?
Dr Bell | No. A [[treatment tradeoff::A treatment tradeoff concerns the benefits, harms, and practical implications of actual options and requires an appropriate clinical discussion rather than an automatic cost-based substitution.]] requires a proper clinical discussion; no substitution is being made in this conversation.
Rowan | I would feel better with one contact who can explain what has been applied for and what is confirmed.
Dr Bell | Let us identify that contact and keep applications, estimates, and confirmed arrangements clearly distinguished.
Rowan | Then the practical difficulty can be addressed without assuming that I have chosen to stop care.
Dr Bell | Exactly. [[Financial toxicity::Financial toxicity describes the harmful financial burden associated with care and deserves attention without blaming the patient or promising unverified assistance.]] deserves attention, with honest limits on what we can confirm and a clear next step.''',
    transfer_title='An assistance application is pending',
    transfer_setup='The support team submits an assistance application. Eligibility and coverage are not yet confirmed. The patient has authorized contact with the program, not the employer.',
    transfer='''Patient: "The application has been ___." | submitted | The support team has submitted the application but has no decision yet.
Navigator: "Eligibility remains ___." | unconfirmed | The program has not yet established eligibility or approved coverage.
Patient: "Contact with the program is ___." | authorized | The patient has permitted contact with the assistance program.
Navigator: "That does not authorize contacting your ___." | employer | The supplied permission does not extend to the patient's employer.'''),
]
