"""Additional original telecommunications coordination conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The call connects, but audio is one-way",
        skill="Describe voice-call evidence by protocol, direction, and observation point without closing the fault prematurely.",
        setup="Fictional authorized test S42: an office agent hears the external caller, but the caller reports no agent audio. SIP INVITE receives 200 OK and is acknowledged. An approved office-edge trace shows outbound RTP packets; remote receipt and playback are unverified. No cause is established. This is a coordination discussion, not configuration instructions or an emergency-call test.",
        cast="Dina|Enterprise voice engineer\nMarco|Carrier support engineer",
        dialogue="""Dina|S42 connects, but the caller cannot hear our agent. Our agent can hear the caller. The ticket was marked successful because the setup trace looked normal.
Marco|The [[SIP signaling::SIP signaling establishes and manages the session; the supplied INVITE, 200 OK, and acknowledgment do not prove intelligible audio reaches both people.]] completed for this call. That is useful evidence about setup, not proof that both audio directions worked.
Dina|Then please keep the fault open. I want the summary to say which person hears which, rather than just audio problem.
Marco|Agreed. We have [[one-way audio::One-way audio describes the reported asymmetry: the office agent hears the caller, while the caller cannot hear the agent; it does not itself identify a failed component.]] from the user's perspective. Caller to office is audible; office to caller is reported inaudible.
Dina|At the office edge, the approved trace shows outbound packets for the test. Does that establish that our voice reached the caller?
Marco|It establishes packets at that observation point. [[RTP::Real-time Transport Protocol carries media such as audio in this session; observing outbound RTP at one point does not establish remote delivery or audible content.]] traffic leaving the edge is not the same as confirmed receipt and successful playback at the far end.
Dina|So we still need to correlate that stream with the carrier-side evidence. I will include the exact test time and the local call reference.
Marco|Please include the time zone and trace point as well. If clocks differ or we compare another attempt, the packet observations may appear inconsistent for the wrong reason.
Dina|The report should not say zero packet loss at the caller. We have not measured the caller's receiving side at all.
Marco|Correct. The [[media path::The media path is the route taken by the audio packets; it must be investigated separately from the signaling exchange and at identified points in the relevant direction.]] needs investigation in the affected direction. We cannot infer every hop from a successful setup exchange.
Dina|Someone has suggested a firewall issue. I have left that as a hypothesis, because we have not located where the useful audio stops.
Marco|That is appropriate. Address translation, media negotiation, endpoint behavior, and other causes may need checking under the approved process. Naming a familiar cause is not isolation.
Dina|Would a stream of packets also be consistent with silence or an endpoint failing to render audio, rather than packets disappearing in transit?
Marco|Yes. Packet presence does not prove the intended speech was encoded or played. The negotiated [[codec::A codec encodes and decodes the audio; successful signaling or packet presence alone does not prove the intended speech was correctly encoded, transported, and rendered.]] and endpoint behavior may matter, but neither is established as the fault here.
Dina|We should avoid copying customer audio or full account details into the general ticket. The authorized technical record should contain only what the investigation needs.
Marco|Agreed. Use the approved access and retention process. I will ask the carrier team for correlated observations, not a blanket assertion that everything beyond our boundary is fine.
Dina|My update will say setup completed, caller-to-office audio works in this test, and the opposite direction still needs investigation beyond the local packet observation.
Marco|That is an accurate [[fault summary::A fault summary combines the observed symptom, verified protocol events, observation points, and open questions without turning a partial test into an end-to-end success claim.]]. Include the test reference so the next engineer does not merge it with a different customer attempt.
Dina|Once a correction is made, we should repeat the agreed ordinary test and verify speech in both directions, not just look for another 200 OK.
Marco|Yes. The closure record needs the actual end-to-end result and any remaining limitations. For now, S42 is connected at the signaling level but not a verified successful voice conversation.""",
        transfer_title="Reverse the affected direction",
        transfer_setup="Fictional test T19: the external caller hears the office agent, but the agent cannot hear the caller. Call setup succeeds. Packets are observed at the caller-side edge only; office receipt and playback are unchecked.",
        transfer="""Engineer: The reported inaudible direction is caller to ___.|office|The agent cannot hear the external caller, so caller-to-office audio is the affected direction.
Support: Successful setup establishes signaling, not end-to-end ___.|audio|The scenario explicitly distinguishes call establishment from whether both participants hear speech.
Engineer: Office-side receipt is still ___.|unchecked|Only the caller-side observation is supplied, and the office receiving side has not been checked.
Support: Keep the record tied to test ___.|T19|The stated identifier is T19, which links the direction report to the correct test attempt.""",
        reference=("IETF RFC 3261: signaling and session establishment", "https://datatracker.ietf.org/doc/html/rfc3261"),
    ),
    scenario(
        title="Enough light, but not enough margin",
        skill="Explain a fiber power calculation while distinguishing absolute power, link loss, and the required design reserve.",
        setup="Fictional matching optical equipment: minimum transmit power -3 dBm; receiver sensitivity -20 dBm at the specified performance. Planned path loss totals 15 dB, with a required 3 dB reserve under this project's design rule. Ignore other penalties only for this calculation. These figures are not equipment recommendations or a complete acceptance test.",
        cast="Ivo|Optical network planner\nNadia|Deployment manager",
        dialogue="""Nadia|The spreadsheet predicts minus eighteen dBm at the receiver. That is above its minus-twenty sensitivity. Can I mark the design as meeting our margin requirement?
Ivo|Not yet. The [[power budget::The power budget is the difference between minimum transmit power and receiver sensitivity: -3 minus -20 equals 17 dB before reserving design margin.]] is seventeen decibels before reserve. Subtracting the planned fifteen-decibel loss leaves only two decibels of margin.
Nadia|The project requires three. So a result above the receiver's threshold is not enough to satisfy the specified reserve.
Ivo|Correct. The [[path loss::Path loss is the stipulated 15 dB reduction between transmitter and receiver; it is a relative level difference, unlike the absolute dBm power values.]] must be fourteen decibels or less for this seventeen-decibel budget to retain the three-decibel reserve.
Nadia|I want to check the signs aloud. Minus three, less fifteen, gives minus eighteen dBm. We do not subtract minus fifteen and get positive twelve.
Ivo|Exactly. That is the predicted [[received power::Received power is the absolute optical level at the receiver, here predicted as -3 dBm minus 15 dB, or -18 dBm; it is not a measured field result.]]. The loss is a positive fifteen-decibel reduction, not a negative power reading.
Nadia|Then the current design is short of our required reserve by one decibel. It is not three decibels short and not completely without signal.
Ivo|Right. Call it insufficient [[engineering margin::Engineering margin is the remaining allowance above receiver sensitivity after path loss; two decibels remains here, one decibel below the stipulated three-decibel requirement.]] under the stated rule. Do not turn that calculation into a claim that the installed service has already failed.
Nadia|Could the team simply use a stronger typical transmitter value from another sheet? It would make the result look better.
Ivo|We need the applicable minimum and conditions for the chosen equipment. Replacing the agreed basis with a favorable typical value would hide the shortfall rather than resolve it.
Nadia|The receiver figure also needs to apply at the specified performance, not merely show the faintest light the device can detect.
Ivo|Yes. [[Receiver sensitivity::Receiver sensitivity is the minimum input associated with specified performance and conditions; a detection indication alone is not the same criterion.]] belongs with its performance criterion. The calculation needs compatible equipment assumptions, not whichever two numbers produce the largest budget.
Nadia|We have only checked the low-power side here. A complete design also needs to consider whether maximum input could overload the receiver.
Ivo|Correct. More optical power is not automatically better. The receiver's permitted maximum, other penalties, and actual operating conditions require their own checks.
Nadia|Before I ask for a revised route estimate, what needs to stay attached to the loss figure so we compare like with like?
Ivo|Keep the [[wavelength::Wavelength identifies the optical operating or test condition; losses and equipment specifications must be compared on a compatible basis rather than mixing values from different conditions.]], fiber type, component assumptions, and reference endpoints. A result for another test condition is not automatically interchangeable with this one.
Nadia|I will return the design for a documented revision rather than edit the reserve down to two. The three-decibel requirement remains unchanged.
Ivo|Good. The responsible engineer can assess a suitable design change. This conversation does not authorize swapping components or changing an operating link.
Nadia|My planning note will say seventeen budget, fifteen planned loss, two remaining, and three required: one decibel short of the stipulated margin.
Ivo|That is the useful summary. Keep predicted and measured results separate, and leave final acceptance to the specified engineering and testing process.""",
        transfer_title="Calculate the remaining reserve",
        transfer_setup="Fictional link: minimum transmit power -2 dBm, receiver sensitivity -18 dBm, planned path loss 12 dB. Required reserve is 3 dB. Ignore other penalties for this arithmetic only.",
        transfer="""Planner: The power budget before reserve is ___ dB.|16|Minus two minus negative eighteen gives a sixteen-decibel difference between transmit power and sensitivity.
Manager: The stipulated path loss is ___ dB.|12|The separate path-loss input is twelve decibels, not an absolute power in dBm.
Planner: The margin remaining after that loss is ___ dB.|4|Sixteen decibels of budget minus twelve of loss leaves four decibels of margin.
Manager: That exceeds the required reserve by ___ dB.|1|Four available decibels of margin minus the three-decibel requirement leaves one decibel above the required reserve.""",
        reference=("Fiber Optic Association: power and loss budgets", "https://www.thefoa.org/tech/lossbudg.htm"),
    ),
    scenario(
        title="Eight numbers move; four must stay",
        skill="Clarify a partial number transfer using explicit scope, carrier records, and distinct authorization and completion milestones.",
        setup="Fictional U.S. account: twelve numbers, abbreviated by endings 0100-0111. Authorization covers 0100-0107 only; 0108-0111 must stay. The draft wrongly selects a full port. Billing number 0100 is moving. The requested 22 October date has no carrier commitment. Complete identifiers are in the approved record; actual requirements are provider-specific.",
        cast="Yara|Porting coordinator\nScott|Customer telecom administrator",
        dialogue="""Yara|Before I submit the transfer, the form says full port, but your signed list names eight of twelve numbers. Should the other four remain with the current provider?
Scott|Yes. Our [[number inventory::The number inventory identifies all twelve services and their intended disposition; eight endings 0100-0107 move, while four endings 0108-0111 remain with the current provider.]] is clear: endings zero-one-zero-zero through zero-one-zero-seven move; zero-one-zero-eight through zero-one-one-one stay. The form is wrong.
Yara|That is eight moving and four staying. I will reconcile the complete verified numbers in the actual request; these shortened endings are only for this discussion.
Scott|The [[letter of authorization::The letter of authorization records the customer's specified permission; here it covers eight named numbers and does not authorize transferring the remaining four.]] covers those eight only. Please do not expand it to all twelve to make the full-port field agree with the draft.
Yara|Agreed. This is a [[partial port::A partial port moves only some numbers from the current account; the remaining services must be addressed explicitly rather than treated as included in a full transfer.]], so the retained services need explicit handling in the request and with the current provider.
Scott|The retained numbers are still in use. I also see that zero-one-zero-zero is the billing reference for the current account, even though that number is moving.
Yara|That [[billing telephone number::The billing telephone number identifies the account for carrier processing; moving that number may require an agreed replacement or account arrangement to preserve retained services.]] needs attention. Confirm the provider's required arrangement for retaining those four services before we submit the request.
Scott|I can contact the current provider through our authorized channel and confirm the retained-service details. I will not choose a replacement billing number from memory.
Yara|Keep that response with the order. Also check any bundled-service dependencies; moving the numbers does not automatically resolve those arrangements.
Scott|The business wants the move on October twenty-second. Has the carrier accepted that date, or is it still just our preference?
Yara|We have no [[firm order commitment::A firm order commitment is the carrier's accepted scheduling milestone under its process; the requested 22 October date is not such a commitment in this record.]] yet. Correcting the scope and supplying the required records must not be reported as confirmation of the requested date.
Scott|I will keep the user notice provisional. They need a confirmed plan before changing their published contact arrangements or assuming the new routing is active.
Yara|And please do not cancel the existing services as a way to start the transfer. Coordinate the actual port and any later service changes through the providers' processes.
Scott|Understood. The four retained numbers are not a cancellation request, and the eight moving numbers still need their transfer coordinated.
Yara|When the scheduled work occurs, [[completion confirmation::Completion confirmation records that the transfer has actually reached its completed state; a scheduling commitment alone does not establish completed routing or all service checks.]] is another milestone. A commitment date alone will not tell us every number is routing correctly.
Scott|We will use the agreed ordinary calling checks for the moved and retained numbers. A successful call to the main number should not close all twelve checks.
Yara|Exactly. Follow the applicable service validation process and handle any emergency-calling requirements through qualified, coordinated procedures, not unplanned emergency test calls.
Scott|I will return the retained-service arrangement and complete number list through the approved channel. Credentials and transfer security codes do not belong in a widely shared email.
Yara|I will correct the draft to the authorized partial scope, verify the remaining requirements, and report the actual carrier response with its date and status.
Scott|Thank you. Our handoff is eight moving, four staying, billing-reference handling pending, and October twenty-second requested only. No wider transfer or cancellation is authorized by this conversation.""",
        transfer_title="A partial request is not a full-account move",
        transfer_setup="Fictional account: ten verified numbers. Signed authorization covers six; four must remain. The draft says full port, and the preferred 5 November date has no carrier commitment. Complete identifiers are held in the approved record.",
        transfer="""Administrator: The authorized number of transfers is ___.|six|The signed scope names six numbers, not all ten on the account.
Coordinator: The number of services that must remain is ___.|four|Ten total numbers minus six authorized to move leaves four explicitly retained services.
Administrator: The corrected request must describe a ___ port.|partial|Only some account numbers move, so a full-port designation conflicts with the authorized scope.
Coordinator: The 5 November date remains ___.|requested|No carrier commitment is supplied, so the preferred date cannot be described as confirmed or completed.""",
        reference=("Bandwidth: partial ports, billing numbers, and commitment milestones", "https://www.bandwidth.com/support/en/articles/12822975-bandwidth-porting-guide"),
    ),
]
