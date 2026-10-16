# Student resources review

Reviewed October 15, 2026. The owner's Resources spreadsheet tab supplied the starting collection. Only public resource links and original short descriptions were brought into the student page. The spreadsheet was not edited or connected to student browsers.

## Published selection

The 15 destinations in `public/index.html` were opened and checked for relevant learning content, rather than accepting a successful HTTP response alone.

| Resource | Decision and evidence |
| --- | --- |
| British Council A1 listening | Replace the old listen-and-watch address with a current level-specific page containing audio lessons and exercises. |
| ELLLO | Retain; current site has A1–C1 navigation, conversation transcripts and quizzes. Use HTTPS. |
| Randall's Listening Lab | Retain; replace the old index.htm address with the Easy lesson collection. The homepage also introduces new Study Paths. |
| Spotlight English | Retain; active story/audio pages with transcripts, including an October 12, 2026 episode. |
| British Council A1 speaking | Add; short videos, useful phrases and exercises for everyday conversations. |
| ESL Fast Easy Conversations | Repair the malformed spreadsheet address ending in an encoded nonbreaking-space fragment. Link directly to the everyday conversation collection. |
| YouGlish | Add; the live search and official About page explain word/phrase lookup in real video clips. No unlimited-free-use claim. |
| News in Levels | Retain once; duplicate removed. October 15, 2026 stories and three versions were visible. Site levels are not labelled as CEFR levels. |
| Breaking News English | Retain; October 15, 2026 lesson visible, with easier/harder versions and levels 0–6. Site levels are not labelled as CEFR levels. |
| British Council A1–A2 grammar | Add; current free-resource route has explanations and topic exercises, also confirmed in a normal browser. |
| Cambridge English activities | Add; live skill, time and A1–C2 filters, including Basic (A1–A2) exercises. |
| ManyThings Sentences with Audio | Retain and narrow to the sentence collection. English audio and multilingual translations include Japanese. The homepage records February/May 2026 updates. |
| Cambridge Write & Improve | Add the free learner page; official material confirms automatic feedback and use without registration, with a profile needed to save work there. |
| British Council English for emails | Add; direct A2–B1 lesson collection for workplace email writing. |
| The Punctuation Guide | Retain; clean the long text-fragment address. Label its explanations as longer rather than beginner material. |

## Items not carried over

- Flip: the standalone service was retired; see [Microsoft's support response](https://learn.microsoft.com/en-us/answers/a/12837747).
- Duplicate BBC, VOA, News in Levels and Grammarly entries were not copied as separate cards.
- The 2020 online-teaching article is for teachers. General news, entertainment, specialist medical podcasts and academic citation manuals are less direct starting points for this compact student collection.
- Automatic text checkers, paid app promotions and the old explanation bot were not necessary alongside focused exercises and Write & Improve.
- BBC and the old Phil grammar page could not be confirmed through the web reader during this review. They were omitted rather than labelled as broken. Other unselected spreadsheet links were not certified dead.

## Maintenance and boundaries

An additional direct HTTP check returned 200 for ten destinations. British Council and Randall's reject the automated client with 403 responses, while their pages loaded through the web reader; normal-browser checks also confirmed the grammar and Easy listening collections. These automated refusals were not treated as dead links.

This is an intentionally curated snapshot, not a live spreadsheet import or an automatic link-monitoring job. Recheck destination content, redirects and access requirements before changing the displayed review date. A site loading today does not guarantee future availability or every audio/video working in every region.

Descriptions are short, original instructions for adult learners. A1–A2 is a reading-register preference; the page does not infer an individual student's proficiency. Only use provider level labels where confirmed.

External links use HTTPS, open a new tab and suppress the opener/referrer. They contain no profile, lesson, answer or credential data. There are no embeds, automatic visits, progress writes or paid AI calls. Resources is separate from administrator-selected Activities and does not change those selections.

The administrator chooses each student’s visible links using the grouped Student resources checkboxes on registration and Edit account. The stable IDs and administrator labels live in `resources.mjs` and match the cards in `public/index.html`. Choices are saved privately, separate from Activities. Missing choices retain the complete collection; an explicit empty list shows an empty state. Students cannot edit these choices. Their page hides unselected cards and empty categories and reloads choices on reopening or returning to the tab. These settings do not restrict independent visits to the external sites.
