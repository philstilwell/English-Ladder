# Campaign tracking for English Ladder and Slugfester

Current daily promotion runs were paused at Phil's request on November 1, 2026. Setting up tracking is not permission to resume them. Keep that hold until Phil authorizes future publishing.

## Reading the results

The private Cloudflare D1 database **promotion-campaigns** holds `campaign_dashboard`, a compact lifetime-per-post report, and `campaign_results`, the full details including source, community, link and verified permalink. Open [Explore Data](https://dash.cloudflare.com/35f54f15edb91fa1d38da7b8eb7583f5/workers/d1/databases/7198c22f-cba8-401e-8389-f26d7835a8de/studio), select `campaign_dashboard` for the overview or `campaign_results` for details. Cloudflare sign-in is required. There is no public analytics endpoint.

* `browser_arrivals`: a campaign landing page remained visible for at least one second.
* `engaged_visits`: the same load remained visible for at least ten seconds and received a browser-reported trusted pointer, keyboard or scroll interaction.
* `internal_arrivals`, `test_arrivals`, `bot_arrivals`: excluded categories, never added to audience or engagement totals.
* `unclassified_link_requests`: audience-bucket fetches before browser confirmation. These may include undetected bots. Never describe this as human visitors.

These are page loads, not unique people. Engagement is evidence of likely readership, not proof of a human. Repeat loads count again. Bots running real browsers may still qualify. Referrer stripping no longer prevents attribution because the unique link identifies the source post. A copied link remains attributed to its original campaign. Existing untagged posts cannot be attributed retrospectively.

## Exclude administration and verification

On every browser/device used by Phil or an agent, open both:

* https://englishladder.com/campaign/traffic
* https://slugfester.com/campaign/traffic

Choose **Mark this browser internal**. Verify that the page says `internal` on each site before checking campaign links. The first-party exclusion cookie lasts one year; clearing cookies or using another profile/device requires setting it again. Automation used for verification must also append `?traffic=test` to campaign links. That parameter is for checks only and must never appear in published copy. Draft/test campaign rows are always excluded. Do not clear the exclusion to manufacture audience data.

General Cloudflare traffic reports still include administrative requests. Use this campaign view for post-attributed audience counts. This worker does not change broad site analytics or collect unrelated visits.

## Every future authorized post gets a new link

1. Freshly check permission, audience fit, posting location, intervals and shared history under the standing promotion instructions. Do not reuse a pending, removed or previously posted item.
2. Reserve a new row using `node campaign-tracking/campaign.mjs new SITE SOURCE COMMUNITY TITLE TARGET`. SITE is `englishladder.com` or `slugfester.com`; SOURCE is `facebook` or `reddit` (English Ladder only). TARGET is a verified public HTML resource path. The command prints the unique link and SQL; it never publishes or writes remotely.
3. Run the generated SQL in the private D1 Console. It starts as `draft`, so checks cannot inflate audience totals. Keep the ID, target, exact proposed copy and source/community in the shared register. Do not include private information in titles or IDs. Do not reuse links across different posts, comments or platforms.
4. Verify the full landing page, assets, internal links and intended resource through the campaign link, with internal mode confirmed and `?traffic=test`. For PDF resources link to their public HTML lesson/course page. Never link `/backend`, admin routes, private pages or malformed paths.
5. Immediately before the authorized submission, execute SQL from `node campaign-tracking/campaign.mjs activate ID`. `active` means counting is enabled; it does **not** claim the post was published. Publish the clean campaign link without `traffic=test` or punctuation joined to it. The landing page adds standard `utm_source`, `utm_medium=social`, `utm_campaign=post-outreach` and `utm_content=ID` parameters automatically.
6. Verify publication independently according to the platform rules. Only after verification use `node campaign-tracking/campaign.mjs published ID POST_URL ISO_TIME` and run that SQL. Record pending/removed/unknown/blocked statuses in the shared channel register; never mark those as published. Keep the link and counters even if a post is later removed. Do not delete history or resubmit automatically.
7. During authorized reporting, compare browser arrivals and engaged visits by post and check continuing public visibility. Record removals and promptly notify Phil of failed promotions. No scheduled publishing resumes until Phil asks.

If current credentials lack D1 scope, use the signed-in Cloudflare Console/Explore Data UI. Do not expand credentials or use browser-cookie extraction. Replace newlines with spaces when pasting multi-line SQL into Console's single-line input.

## Implementation and privacy

The independent `promotion-tracking` Worker intercepts **only** `/campaign/*` on the two apex domains. It does not replace either site's main deployment. It fetches an allowlisted public resource without forwarding visitor cookies, authorization or query data, adds a same-origin measurement script, and restores the resource URL before deferred site scripts run. Unknown links return 404. Raw fetches and browser confirmation are deliberately separate.

The database stores random references for individual page loads for up to 30 days. A daily scheduled cleanup removes those references while retaining aggregate campaign counts. No visitor IP, full user-agent, names, practice answers, persistent visitor identifiers or cross-site fingerprints are stored in this database. Browser Do Not Track and Global Privacy Control preferences disable browser-event collection. Raw requests still increment a counter. The only persistent cookie is the explicit internal/test exclusion choice. Privacy details are at `/campaign/privacy` on both sites.

## Validation and deployment

Run `node --test campaign-tracking/test.mjs` and `python3 campaign-tracking/test-schema.py`. Also build with `wrangler deploy --dry-run --outdir /tmp/promotion-tracking-built --config campaign-tracking/wrangler.jsonc`, then run `node campaign-tracking/test-built.mjs /tmp/promotion-tracking-built/worker.js`. This catches browser script serialization failures in the actual bundle. Keep `keep_names: false`; bundled name helpers cannot be serialized into a standalone browser function. Use the existing English Ladder Wrangler installation, not a new dependency install. `wrangler deploy --config campaign-tracking/wrangler.jsonc` deploys this independent Worker. Existing sites continue their own publication workflows.

The database schema is `schema.sql`. Schema creation is additive/idempotent; edits after initial deployment require a deliberate migration (do not assume `IF NOT EXISTS` updates definitions). The two `qa-*-20261101` rows are verification records, not public promotions. Never include them in campaign success claims.

Expected extra cost at present volume is $0 using existing Cloudflare Workers/D1 free allowances. D1's free daily read/write limits are hard caps, not permission to upgrade. Do not buy capacity or change the account plan without Phil's authorization. If collection fails, report the gap and do not count missing events as zero audience.

Rollback: remove only this Worker's two `/campaign/*` routes or redeploy a previous known-good version. Preserve D1 history and the source files. Do not alter the sites' root routes, scheduled content generation or existing promotion records.
