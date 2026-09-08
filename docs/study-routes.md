# Optional study routes

Implemented 8 September 2026 following the site audit. Editorial calibration and new retrieval/listening work remain deferred. The three inaccurate original grammar graphics retain their existing correction notes; no images were changed in this release.

Students reach `study-routes.html` from Discover or the shared footer. Three goal links lead to three numbered activities per route. Each route states its suggested level, goal, approximate time and what to do. Ordinary browsing remains available.

| Goal | Existing lessons |
| --- | --- |
| My first week in the US | Arrival → Shopping → Transportation |
| Build a reading habit | Food market → City trees → Latest complete news edition, at the chosen level |
| Speak more clearly at work | Project Management modules 1 (clarification), 2 (progress), 7 (requests) |

The route catalog and static guide are built by `study_routes.py`. `study-routes.js` adds a small activity indicator and the next link only when the address contains a recognized `route` value and points to a matching lesson. The normal US-life next-unit link is replaced while following a route so two buttons cannot suggest conflicting next steps. Other units retain ordinary navigation.

Reading level changes preserve the route. The reading route's last link refreshes to the latest complete news edition during the normal offline build. Previously bookmarked news endings remain valid after a later edition publishes. Route navigation does not mark activities complete or introduce any browser storage, service calls or saved answers. Existing level and language preferences are unchanged.

Without JavaScript, the guide's nine lesson links and lesson content remain available; students use the numbered list to choose the next activity. Suggested times are estimates, not measured completion times or a claim of mastery.

Validation: 234 Python tests and 118 JavaScript tests passed, including 10 new route checks. The site audit passed for all 312 pages. Targeted browser checks covered all route destinations at 320, 390 and 1280 pixels, plus complete route navigation, a reading-level change, and guide navigation without JavaScript.
