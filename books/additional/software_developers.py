"""Original concurrency, query-loading, and decimal-contract conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="The newer tag cannot repair an older payload",
        skill="Explain a rejected conditional update without silently overwriting another person's change.",
        setup='Fictional whole-record PUT replaces price and description. Both clients read $18, "old", strong ETag "v7". A changes price to $20, creating strong tag "v8". B submits $18, "new", If-Match: "v7". B\'s change has not previously succeeded. This service returns 412 without changing data when the condition fails. No later update is approved.',
        cast="Dina|Client developer\nMarco|Service developer",
        dialogue="""Dina|B got a 412 saving the description. Its payload still contains eighteen dollars, because both clients started from the same version.
Marco|That is the [[stale representation::B edited the older v7 representation containing eighteen dollars; the current representation is v8 with twenty dollars, so the submitted full record is stale.]] we need to discuss. A has already changed the price to twenty; B hasn't seen that change.
Dina|The request includes v7. Is the server comparing that with the current version, rather than comparing our description text?
Marco|Yes. The [[If-Match precondition::If-Match requires the supplied entity tag to match the current representation using strong comparison; v7 does not match the current v8 here.]] fails here. The response is 412 with no update, not evidence that B's description was saved.
Dina|Could I fetch just the new tag and resubmit exactly the same body? That would get past the version check.
Marco|It could cause a [[lost update::Sending the stale eighteen-dollar price with a current tag could overwrite A's twenty-dollar change; replacing only the tag does not reconcile the old body.]]. The body still carries eighteen. Passing a version check wouldn't make that overwrite intentional.
Dina|So we need the current record as well as its tag. We should show the price change before preparing another full replacement.
Marco|Exactly. A [[strong ETag::A strong ETag is the representation validator used by this conditional request; it is not permission to submit stale field values or proof of user intent.]] identifies the representation you're checking against. It does not tell us which conflicting fields the user meant to replace.
Dina|The status text says Precondition Failed. Someone called it a server outage, but the service is rejecting our condition as designed.
Marco|Keep the [[HTTP 412::HTTP 412 is the specified precondition-failure response in this case; it does not establish a server outage, a successful save, or a generic authorization failure.]] meaning precise. The price remains twenty and the description remains old after this rejected request.
Dina|For the next attempt, we'll retrieve the current record, review the difference, and preserve twenty if the user only wants to change the description.
Marco|That's [[conflict reconciliation::Conflict reconciliation compares the current record with the intended edit before constructing another request; copying v8 onto the old body would bypass that reasoning.]], not a blind retry. Another update would still need the current condition checked when it reaches the service.
Dina|Meaning someone else could change the record between our fresh read and our next submission. Fetching once doesn't lock it.
Marco|Right. Optimistic concurrency detects a changed version at the conditional write. It doesn't reserve the record while the user is reading it.
Dina|Our error message should preserve the user's unsaved description rather than discard it when we fetch the newer record.
Marco|Agreed as a proposed interface behavior. Show the fresh record and pending edit separately so the user can review what will actually be sent.
Dina|For the test, I'll interleave two clients: A saves twenty first, then B sends the stale condition and gets the specified rejection.
Marco|Check the stored fields afterward too. A status assertion alone wouldn't catch a defective implementation that rejects the request but still changes the data.
Dina|Then the handoff is: B's save rejected, A's twenty preserved, description unchanged, and a reviewed resubmission still pending.
Marco|Yes. Don't label it resolved merely because we know v8. The condition protects the write; the client still has to prepare the right change.""",
        transfer_title="A rejected edit is not a merged edit",
        transfer_setup='Same fictional service. Current strong tag "v12" has quantity 9 and note "old". A stale PUT sends quantity 7, note "new", If-Match: "v11". It has not previously succeeded. The service returns 412 without changing data. No resubmission occurs.',
        transfer="""Developer: The returned status is ___ .|412|The case explicitly specifies precondition failure; the stale v11 tag does not match v12.
Reviewer: The stored quantity remains ___ .|9|The rejected request makes no change, so the current quantity nine is preserved.
Developer: The stored note is still ___ .|old|The requested new note was not applied when the conditional request failed.
Reviewer: Replacing only the tag would leave the payload ___ .|stale|The body would still contain seven rather than the current nine; a newer tag alone does not reconcile those values.""",
        reference=("RFC 9110, section 13.1.1: If-Match and lost-update protection", "https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1"),
    ),
    scenario(
        title="Fifty orders, fifty-one queries",
        skill="Explain query-count growth and a batching proposal without promising an unmeasured response time.",
        setup="Fictional order page: one query loads 50 orders, then one separate query per order loads its lines. All 51 calls are serial; no cache or other queries. A proposed batch implementation uses one order query and one line query for those 50 IDs. For this simplified model, each database round trip contributes exactly 4 ms of network delay. Database work, data transfer, and application work are additional and unmeasured.",
        cast="Jules|Application developer\nAmir|Database specialist",
        dialogue="""Jules|The page has fifty orders, but the trace shows fifty-one queries. The first fetch looks normal; the extra calls appear while we render the lines.
Amir|That matches the [[N+1 query pattern::One initial order query plus one line query for each of fifty orders produces fifty-one queries; the extra work grows with the number of orders.]] in this trace. Loading the orders once doesn't mean their related lines were loaded with them.
Jules|Our object-relational mapper fetches the lines when the template first accesses each collection. I hadn't noticed that property access was issuing SQL.
Amir|That's [[lazy loading::Lazy loading defers fetching related data until access; in this supplied trace each order's line collection triggers another query.]] here. It isn't inherently wrong, but this access pattern produces one database call per order.
Jules|The proposed version fetches the orders, collects their IDs, then fetches all matching lines together. That would be two queries for this page.
Amir|Yes, the proposed [[batched lookup::The proposed implementation uses one related-line query for the fifty selected order IDs, replacing fifty separate line queries while retaining the initial order query.]] reduces this example from fifty-one to two. Check that each line is attached to its correct order afterward.
Jules|At four milliseconds per serial round trip, the old path has two hundred four milliseconds of network delay before we add other work.
Amir|And the new [[round-trip count::The new path has two serial round trips, contributing eight milliseconds in the supplied model; the count is not the complete application response time.]] contributes eight milliseconds under that model. That's a hundred ninety-six milliseconds less modeled network delay.
Jules|I'll put eight milliseconds in the response-time target, then. The arithmetic makes it look very fast.
Amir|Call it the [[network component::Eight milliseconds accounts only for the two modeled network delays; database execution, transferred data, and application processing remain additional and unmeasured.]], not the whole response. We haven't timed query execution, transferred rows, or object construction.
Jules|A larger batch could load more rows at once. Fewer queries don't automatically mean less memory or less database work.
Amir|Exactly. Measure the [[result set::The result set is the data returned by the queries; reducing query count does not establish its size, memory cost, or correct association with each order.]] as well. An order with no lines must still appear if the page contract includes it.
Jules|I'll compare the rendered orders and line associations, not only the query counter. We could get two queries and still show the wrong data.
Amir|Good. Keep ordering and empty collections in that check. The optimization must preserve the page's specified result.
Jules|For a bigger page, is one giant query always the best answer? Some database parameter limits would affect a long list of IDs.
Amir|The batch size needs an implementation decision. Our fifty-ID example isn't a universal limit or a promise that all frameworks use that size.
Jules|Then I'll label fifty as this case's input, with two queries for the proposed version. We still need measurements on representative data.
Amir|Yes. Record query count, total time, and relevant resource use separately. A changed query count is strong evidence about calls, not everything else.
Jules|The review summary will say fifty-one versus two queries, modeled network delay two hundred four versus eight milliseconds, actual total latency not yet measured.
Amir|That is a defensible comparison. It explains the mechanism and arithmetic without turning a simplified calculation into a production guarantee.""",
        transfer_title="Batch size changes the query count",
        transfer_setup="New fictional page: 200 orders, one initial order query, no cache. Old path makes one additional line query per order. New implementation explicitly groups IDs into batches of 50, one line query per batch. All calls are serial at 4 ms network delay each; other work remains unmeasured.",
        transfer="""Developer: The batched path makes ___ total queries.|5|Four groups of fifty IDs require four line queries plus one initial order query, totaling five.
Reviewer: Its modeled network delay is ___ milliseconds.|20|Five serial round trips multiplied by four milliseconds equals twenty milliseconds, excluding all other work.
Developer: The old path makes ___ total queries.|201|One order query plus two hundred individual line queries equals two hundred one.
Reviewer: The modeled network-delay reduction is ___ milliseconds.|784|The old component is 201 times 4, or 804 milliseconds; subtract the new 20 to obtain 784, not a measured total-response improvement.""",
        reference=("SQLAlchemy documentation: lazy loading, N+1 queries, and select-in loading", "https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html"),
    ),
    scenario(
        title="One cent, two different contracts",
        skill="Explain why rounding stage and rounding mode belong in an executable money calculation contract.",
        setup="Fictional checkout test, not tax advice. Three separate line items cost $0.05 each before a fictional 10% charge. The agreed contract calculates the charge on each line, rounds it to two decimal places using half-up, then sums the rounded charges. No discounts or other charges. A proposed implementation instead calculates 10% of the basket subtotal and rounds only that result. Use exact decimal inputs.",
        cast="Rina|Checkout developer\nSol|Reviewer",
        dialogue="""Rina|My checkout total is seventeen cents, but the acceptance example says eighteen. Both calculations use ten percent, so I thought the example had a typo.
Sol|Check the [[rounding stage::The agreed contract rounds each line's charge before summing; rounding once on the basket subtotal is a different calculation even with the same rate.]]. The contract rounds each line's charge before adding the charges together.
Rina|Each five-cent line produces half a cent before rounding. With this rule, that becomes one cent per line, three cents in all.
Sol|Yes. The specified [[half-up rule::For these positive amounts, half-up rounds the exact half-cent tie upward to one cent; it must not be replaced with half-even or an unspecified default.]] sends 0.005 to 0.01. The fifteen-cent subtotal plus three cents gives eighteen.
Rina|My version applies ten percent to fifteen cents, giving one and a half cents, then rounds to two cents. That explains seventeen.
Sol|That's a [[basket-level calculation::The proposed calculation rounds 0.015 once to 0.02 and totals 0.17; it is internally consistent but does not implement the supplied line-level contract.]]. Its arithmetic isn't the agreed algorithm. Equal rates don't make the rounding stages interchangeable.
Rina|Would changing the display to two decimal places fix it? The customer would still see a neatly formatted amount.
Sol|Formatting doesn't establish [[decimal arithmetic::Decimal arithmetic can preserve these exact decimal inputs and the requested rounding operation; merely formatting a binary result does not implement the missing line-level rule.]]. We need the calculation and its rounding decisions to match the contract first.
Rina|I'll construct the decimal values from the original decimal strings. Converting a binary floating-point approximation afterward can preserve the wrong intermediate value.
Sol|And make the [[rounding mode::The rounding mode determines how ties are resolved; the contract explicitly requires half-up rather than relying on a library's possibly different default.]] explicit at the required operation. Don't assume the library default is half-up.
Rina|So the regression example must retain three separate five-cent lines. Combining them into one fifteen-cent line changes the meaning of the fixture.
Sol|Exactly. Preserve the [[line-item boundary::The three separate line items each receive their own rounded charge; merging them into one line would change the supplied contract's calculation unit.]]. The test should catch a future optimization that sums first and rounds later.
Rina|Could we store prices in integer cents instead? That would avoid binary approximations for the original prices.
Sol|It can represent those prices exactly, but the calculated charge still has fractional cents. Integer storage doesn't choose when or how to round them.
Rina|I also shouldn't throw away the half cent before applying the specified rounding. That would make each charge zero in this example.
Sol|Correct. Keep sufficient precision for the rule, then round at the agreed point. Truncating intermediate values would implement another algorithm.
Rina|I'll show the per-line charge, summed charge, subtotal, and total in the test evidence. Then the one-cent difference has a visible source.
Sol|Good. This fictional contract doesn't establish what any jurisdiction requires. A real checkout's approved financial rules must supply that decision.
Rina|The corrected expectation is three one-cent charges and an eighteen-cent total. My seventeen-cent result belongs to the rejected basket-level proposal.
Sol|That's the review conclusion. Fix the algorithm and verify this distinguishing example; don't just change the expected value to whatever the implementation currently returns.""",
        transfer_title="Preserve four separate lines",
        transfer_setup="Same fictional line-level contract and exact decimal inputs, now four separate $0.25 lines. Charge rate 10%; round each charge half-up to two decimal places, then sum. No other amounts. Compare with rounding 10% of the $1.00 subtotal only once.",
        transfer="""Developer: Each rounded line charge is ___ dollars.|0.03|Ten percent of 0.25 is exactly 0.025; half-up to two decimal places yields 0.03.
Reviewer: The sum of the four rounded charges is ___ dollars.|0.12|Four separate charges of 0.03 total 0.12; do not round the basket instead.
Developer: The contract's final total is ___ dollars.|1.12|The four prices total 1.00, to which the line-level charge total of 0.12 is added.
Reviewer: That exceeds the basket-level total by ___ dollars.|0.02|The basket method gives 1.00 plus 0.10, or 1.10; the contract total 1.12 is two cents higher.""",
        reference=("Python documentation: exact decimal inputs, quantize, and rounding modes", "https://docs.python.org/3/library/decimal.html"),
    ),
]
