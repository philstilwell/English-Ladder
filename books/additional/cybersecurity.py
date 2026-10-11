"""Original credential-response, testing-scope, and supplier-assurance dialogues."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title='Deleting the post does not revoke the credential',
        skill='Coordinate credential containment, replacement, and evidence without sharing the secret again.',
        setup='An engineer posted a live service token in a public support snippet, then deleted the post. The token is still active. The response lead can authorize immediate revocation under the local process; the service owner must coordinate replacement. Misuse has not been established.',
        cast='Sofia|Service engineer\nMalik|Response lead',
        dialogue='''Sofia|I deleted the support post as soon as I noticed the token. The page is gone. Can we close the report?
Malik|No. Removing the post does not perform [[revocation::Revocation disables the credential itself; deleting a visible copy does not prevent someone who already obtained it from using it.]]. The token is still active, and someone may already have copied it.
Sofia|It belongs to the nightly integration. I can identify the credential record without pasting its value into this chat.
Malik|Use that [[credential identifier::The credential identifier lets responders locate the relevant record without reproducing the authentication secret in another channel.]]. I am authorizing revocation through our response process now. Notify the owner that dependent work may be interrupted.
Sofia|I have sent the identifier through the restricted case channel. The owner is joining, and the revocation action has been submitted.
Malik|Record when it is actually confirmed. Requested and disabled are different states; we should not claim the token is unusable until the result is verified.
Sofia|Revocation is now confirmed. The owner says a replacement is needed before the next run. Can we put the new value in the configuration ticket?
Malik|No. Use the approved [[secret store::The secret store is the controlled mechanism for holding and delivering sensitive credentials; a general configuration ticket would create another exposed copy.]]. The ticket can reference the controlled record and owner without containing the replacement secret.
Sofia|The integration still has to retrieve it. I will coordinate that change with the owner and verify the approved consumer can authenticate.
Malik|Also confirm that the revoked credential is rejected through the authorized verification process. A successful new connection alone does not establish that the old token stopped working.
Sofia|That gives us two separate checks. Would this complete the credential rotation, even though the investigation stays open?
Malik|The [[rotation::Rotation replaces a credential and moves authorized consumers to the replacement; it does not by itself determine whether the exposed credential was misused.]] can be completed and recorded separately. Do not use that completion to claim there was no earlier unauthorized activity.
Sofia|The owner found another scheduled job using the same credential. It was missing from our first dependency list.
Malik|Add it and assess the interruption. That also changes the [[blast radius::Blast radius is the scope of affected services or access; discovering another dependent job changes the operational impact assessment.]] we understood, so update the impact note rather than leave the first description unqualified.
Sofia|Should the replacement keep all the old permissions? Some were added for a one-off task months ago.
Malik|Review the required permissions with the owner. Do not carry unnecessary access forward merely because it was present before the exposure.
Sofia|The provider records are available for part of the exposure period, but an earlier interval is missing. I found no unexplained use in the available records.
Malik|Keep that limit beside the [[audit log::The audit log provides recorded activity for the available period; missing coverage prevents an unrestricted claim that no misuse occurred.]] result. No unexplained use found in those records is narrower than proof that nobody used the token.
Sofia|The update will separate post removal, confirmed revocation, replacement work, affected jobs, and the investigation gap. I will not include either secret value.
Malik|Good. Preserve the relevant evidence through the approved process and keep the case open for the remaining assessment, even when the integration is running again.''',
        transfer_title='A working replacement is treated as proof of containment',
        transfer_setup='A replacement token works for the approved job, but nobody has verified that the exposed token is disabled. General tickets must not contain secret values.',
        transfer='''Engineer: The successful job confirms the new token works, not the old token's ___.|revocation|A successful replacement connection does not demonstrate that the exposed credential can no longer authenticate.
Lead: Verify rejection through the authorized process and record the ___.|result|The response record needs the actual verification outcome rather than the intended action alone.
Engineer: The ticket will refer to the controlled record, not include the secret ___.|value|Including the replacement value in a general ticket would create another unnecessary copy of the secret.
Lead: Keep the investigation separate from restored service ___.|operation|A running service does not establish whether the exposed credential was misused earlier.''',
        reference=('OWASP: Secrets Management', 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html')),
    scenario(
        title='A linked service is not automatically in the test scope',
        skill='Clarify testing permission, boundaries, and stop conditions before an assessment begins.',
        setup='An authorized assessment covers fictional staging service Lab-A from 22:00 to 23:00 UTC using listed methods. It excludes production and third-party systems. Lab-A redirects to a supplier login. The consultant asks whether that login is included; no permission for it is documented.',
        cast='Kenji|Assessment consultant\nAmara|Service owner',
        dialogue='''Kenji|Before we start, Lab-A redirects to the supplier login. Is that service covered by the authorization, or do we stop at the redirect?
Amara|It is outside the listed [[scope::Scope defines the approved systems and boundaries; a link from an approved staging service does not add the supplier system to the assessment.]]. Our authorization covers Lab-A, not the supplier environment. Do not test the linked service on that basis.
Kenji|Understood. I will record the dependency without sending assessment traffic to it. The product team thought a link made it part of our application.
Amara|The [[rules of engagement::Rules of engagement document the permitted assessment activities, boundaries, timing, and handling conditions; they are more specific than a general request to test the application.]] need to make that boundary clear. I can clarify our requirements, but I cannot grant permission on the supplier's behalf.
Kenji|We also have a list of allowed methods. A stakeholder asked for an availability stress test, which is not on that list.
Amara|That request does not change the agreement. Route any proposed addition through the authorization process and leave it out of the current assessment.
Kenji|The window says twenty-two hundred to twenty-three hundred UTC. My local calendar converted it differently because of the time zone setting.
Amara|Use the stated [[test window::The test window is the authorized time interval in the specified time zone; a calendar conversion does not change the agreed start or end.]] and correct the invitation. Confirm both endpoints with the team before starting, rather than rely on a local display.
Kenji|Who can we reach during the window if an unexpected service issue appears? I have your daytime office number only.
Amara|I will confirm the on-duty contact and escalation route in the approved document. Testing should not begin with an unresolved response contact.
Kenji|If we unexpectedly encounter real customer information in staging, should we collect a sample to prove the finding?
Amara|Follow the agreed [[stop condition::A stop condition requires pausing specified activity when a defined event occurs; unexpected real customer information triggers the handling and escalation process in this case.]]. Pause the affected activity and notify the designated contact. Do not expand access or collect additional customer content to make a stronger demonstration.
Kenji|We can document the minimal observation through the restricted reporting route and let the response owner direct the handling.
Amara|Yes. Preserve necessary evidence under the agreed rules without turning an unexpected exposure into unnecessary copying or wider distribution.
Kenji|And if the system becomes unstable during the approved work, we pause and contact the same on-duty person rather than continue to complete the checklist?
Amara|Correct. The [[point of contact::The point of contact is the designated person for coordination during the assessment; an available, agreed route is necessary for reporting disruption and obtaining instructions.]] must be reachable. Completing the planned steps does not override the agreed interruption procedure.
Kenji|I will send the clarified boundary, UTC window, methods, contacts, and stop conditions for confirmation. We are not starting the new request tonight.
Amara|Any expanded activity needs written [[authorization::Authorization is permission from the appropriate authority for the specific activity; a stakeholder request or technical reachability does not supply it.]] before it happens. That includes resolving permission for any third-party environment involved.
Kenji|The report will separate tested areas from excluded and untested dependencies. I will not describe a clean Lab-A result as a test of the supplier login.
Amara|Good. Keep the limitations visible so the assessment answers what was actually examined, not what someone assumed was included.''',
        transfer_title='The approved window is mistaken for unlimited permission',
        transfer_setup='A consultant has permission to assess a named staging system from 20:00 to 21:00 UTC using listed methods. Production and stress testing are excluded.',
        transfer='''Owner: Approval is limited to the named staging ___.|environment|The authorized target is staging; the permitted time does not add production systems.
Consultant: I will work only within the stated UTC ___.|window|The approved interval limits when the specified assessment activities may occur.
Owner: Keep the activity within the listed ___.|methods|Stress testing is expressly excluded and cannot be added merely because the target and time are approved.
Consultant: Any expansion needs separate ___.|authorization|Changes to targets, time, or activities require the appropriate permission before the expanded work begins.''',
        reference=('NIST: Technical Guide to Information Security Testing and Assessment', 'https://csrc.nist.gov/pubs/sp/800/115/final')),
    scenario(
        title='The supplier has a report, but what does it cover?',
        skill='Read assurance scope critically without treating a report as a blanket security guarantee.',
        setup='A fictional supplier provides a SOC 2 Type 2 report covering its Core service from January 1 to June 30. An August add-on is outside the described system. The report lists customer-side access reviews and excludes a hosting provider under the carve-out method. Purchasing wants immediate approval.',
        cast='Lucia|Procurement manager\nDev|Third-party assurance analyst',
        dialogue='''Lucia|The supplier sent its SOC 2 report. Can I mark the security review complete and issue the order for Core plus the new add-on?
Dev|First check the [[reporting period::The reporting period specifies when the described controls were examined; a January-to-June report does not automatically establish their operation in later months.]]. This Type 2 report covers January through June. It is useful evidence, not a guarantee about every service at every later date.
Lucia|The order includes an add-on introduced in August. The cover has the supplier name, but I do not see that product in the system description.
Dev|Then the [[system boundary::The system boundary identifies the services and components described in the report; the supplier name alone does not bring the later add-on into scope.]] matters. The report covers Core. We need evidence for the add-on rather than assume the company name extends coverage to it.
Lucia|There is a section asking customers to review their own users' access. I thought the supplier's controls covered all access administration.
Dev|Those are [[complementary user entity controls::Complementary user entity controls are controls expected at the customer that the supplier's control design assumes; receiving the report does not perform those customer responsibilities.]]. We need an owner for the applicable customer-side responsibilities, not just a copy of the supplier's report.
Lucia|I will route that to our service owner. Does the report also examine the hosting provider's controls? Its name appears in the description.
Dev|Not in the way you are assuming. The report uses the [[carve-out method::The carve-out method excludes the subservice organization's controls from this examination; naming the hosting provider does not mean those controls were tested by this report's auditor.]] for that provider. We must understand the dependency and the separate assurance needed.
Lucia|So excluded from this examination does not mean the hosting controls failed. It means this report does not supply that examination evidence.
Dev|Correct. Do not turn an evidence boundary into an unsupported failure claim. Equally, do not mark the dependency assessed merely because the provider is named.
Lucia|One test table records a late access review. Should I describe that as proof the supplier suffered a breach?
Dev|No. A [[test exception::A test exception is a deviation identified in the examined control evidence; its nature, context, and implications must be assessed rather than relabeled automatically as a breach.]] needs context: the control, affected scope, test result, response, and implications for us. Read it alongside the auditor's opinion.
Lucia|And an exception is not automatically the same as a qualified opinion? I should not substitute my own label for what the auditor actually concluded.
Dev|Exactly. Record the actual opinion and findings, then assess their relevance to our intended service and information. A headline badge cannot do that work.
Lucia|The supplier offers a letter about changes since June. Can that extend the auditor's examination to the present?
Dev|A management [[bridge letter::A bridge letter provides management's statement about the intervening period; it does not itself extend the independent auditor's examination or add an excluded product.]] is additional information, not a new independent examination. Read who made the statement and what it actually covers.
Lucia|I will request the latest relevant assurance and specific information on the August add-on. That is narrower than asking them to repeat every document they have.
Dev|Good. Also identify our access-review owner and the hosting dependency. Those are different open items, so keep each request connected to its purpose.
Lucia|The purchasing status will say report received, review in progress, Core scope identified, and add-on evidence outstanding. No final security approval yet.
Dev|That accurately separates receiving a document from reaching a risk decision. We can acknowledge the useful evidence without extending its conclusions beyond their scope.''',
        transfer_title='A supplier name is mistaken for coverage of every product',
        transfer_setup='A report describes service Atlas for January-June. The proposed purchase also includes Nova, introduced in August and absent from the system description.',
        transfer='''Buyer: The described service is ___, not every product sold by the supplier.|Atlas|The supplied system description identifies Atlas and does not include the later product.
Reviewer: The examination ends in ___.|June|The stated January-to-June period does not itself cover the later months.
Buyer: We still need evidence relevant to ___.|Nova|Nova is part of the purchase but outside the supplied system description and period.
Reviewer: Report receipt is not the same as final risk ___.|approval|Receiving the document leaves the scope gaps and required decision unresolved.''',
        reference=('AICPA: System and Organization Controls', 'https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services')),
]
