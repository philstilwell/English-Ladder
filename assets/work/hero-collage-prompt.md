# English for Work directory artwork

Revised 10 October 2026 with OpenAI's native image generator. Two image-edit
requests, no API fallback. The existing collage was the first edit reference;
the first result was the second edit reference. The final generated PNG is
`industry-collage-66.png`. The WebP is a quality-88 format conversion with the
original dimensions (1196 x 1315) and transparency preserved.

The generator preserved all 66 subjects but did not produce exact row spacing.
The directory therefore displays the generated artwork in a CSS grid of 66 equal
cells, six columns by eleven rows. `work_icons.py` records each illustration's
bounds and centers it within the same 80% width/height envelope without stretching.
The source bitmap itself is not a mathematically regular atlas. Existing course
card illustrations and PDF artwork are unchanged.

## First edit prompt

Use case: precise-object-edit.
Asset type: transparent hero illustration for the English Ladder English for Work directory.
Edit the supplied image, not a website screenshot. The ONLY intended change is the layout: make all 66 existing occupational icon groups receive EXACTLY EQUAL AMOUNTS OF SPACE. Preserve all recognizable subjects, their existing left-to-right/top-to-bottom order, the crisp colorful cartoon drawing style, dark navy outlines, and blue, teal, coral and gold palette. Do not introduce new subjects or remove any existing subjects.

CRITICAL GEOMETRY: produce a near-square portrait canvas, approximately 1200 x 1320 pixels, subdivided invisibly into exactly SIX equal-width columns and ELEVEN equal-height rows. All 66 cells are identical rectangles, with no exception for the bottom rows. Each icon group is centered horizontally and vertically within its own cell, with consistent generous clear padding. Think of center positions x = 100, 300, 500, 700, 900, 1100 and y = 60, 180, 300, 420, 540, 660, 780, 900, 1020, 1140, 1260 on a 1200 x 1320 canvas; preserve these proportions if output dimensions differ. Use the same maximum artwork envelope (about 160 x 90 pixels) for EVERY cell. Keep native silhouette aspect ratios without stretching. Normalize apparent visual size so the final three rows have the same presence and spacing as the first three rows. The bottom row must not be compressed, smaller, cut off, or pushed against the edge. Fully draw each icon inside its assigned cell. No visible grid, separators, frames, labels, words, numbers or watermark. Genuine transparent background, not a checkerboard.

Verify the exact following 6 x 11 row-major ordering:
Row 1: cross-cultural leadership conversation; AI laptop with neural network and chip; IT server and monitor; legal scales and gavel; finance calculator and coins; financial advisor consultation.
Row 2: marketing megaphone and target; real-estate house and key; strategy chess knight with directional arrows; pharmaceutical pills and clinical clipboard; hospital administration building with clipboard; nursing stethoscope with medical chart.
Row 3: biotechnology DNA and pipette; medical monitor device; manufacturing robotic arm; supply-chain truck with packages; HR candidate cards; project planning calendar and clock.
Row 4: engineering gear and caliper; semiconductor wafer and chip; software product phone and interface cards; cybersecurity shield and padlock; analytics chart and magnifying glass; education administration school and clipboard.
Row 5: academic research graduation cap, book, microscope; hospitality suitcase, bell, key; aviation passenger airplane and control tower; construction hardhat and plans; energy transmission tower and wind turbine; environmental soil sampler, vial, leaf.
Row 6: insurance umbrella over house and car; banking bank building, card, transfer arrows; ecommerce cart and phone; entertainment film camera and clapperboard; telecom antenna and fiber cable; government capitol building with seal.
Row 7: nonprofit hands holding earth and heart; consulting presenter and chart; sales handshake with growth chart; customer success headset and approved profile; legal compliance folders, checklist, shield; home caregiver armchair, walker, caring hand and heart.
Row 8: dental tooth and dental tools; pharmacy medicine bottle, pills, tray; medical assistant blood pressure cuff and chart; early childcare picture book and blocks; restaurant serving tray with meal and drink; chef hat and frying pan.
Row 9: barista espresso machine and coffee cups; housekeeping mop, bucket, spray bottle; barber scissors, comb, barber pole; nail technician manicured hand, polish, file; retail cash register and scanner; delivery truck, parcel, handheld device.
Row 10: warehouse shelves, pallet, barcode scanner; landscaping lawnmower, shrub, rake; carpentry hammer, timber, plane, square; electrician pliers, cable, plug, lightbulb; plumbing wrench, tap, pipes; heating and air-conditioning unit, snowflake, thermostat.
Row 11: automotive car with open hood and wrench; office assistant phone, calendar, folders; bookkeeping calculator, spreadsheet, check; software developer laptop with abstract colored code lines; software QA bug on monitor, magnifier, checklist; medical laboratory microscope, pipette, test tubes.

Success means EXACTLY 66 complete icon groups, 6 per row, in equally spaced rows and columns with equal cell padding. Keep the first row and last row at equal distances from their respective outer edges. Do not repeat the reference image's top-heavy spacing or progressively shrinking bottom rows.

## Final edit prompt

Use case: precise-object-edit.
Edit target: supplied 66-icon occupational collage.
This is a STRICT SPACING CORRECTION, not a redesign. Preserve all 66 occupational subjects exactly once, in the same six-column, eleven-row order, the same colors, and the same crisp outlined illustration style. Transparent background.

The supplied picture has uneven row spacing: the top rows are about 125 pixels apart, while the bottom rows are only about 102 pixels apart. FIX THAT. First construct an INVISIBLE mathematically regular SIX-COLUMN ELEVEN-ROW table covering the image. Every cell is exactly the same width and exactly the same height. Reposition AND rescale each complete icon group to fit the uniform cells. Never place the icons by eye in a progressively compressed stack. The last three rows must receive exactly as much vertical space as the first three rows.

Target canvas 1200 by 1320. Each invisible cell is 200 pixels wide by 120 pixels high. All icon groups should fit a maximum 156-pixel-wide by 88-pixel-high envelope centered in their cell, with balanced optical scale. The center of the FIRST ROW must be at y=60, the SECOND at y=180, THIRD y=300, FOURTH y=420, FIFTH y=540, SIXTH y=660, SEVENTH y=780, EIGHTH y=900, NINTH y=1020, TENTH y=1140, ELEVENTH y=1260. Use proportional coordinates if canvas dimensions differ.
Column centers x=100,300,500,700,900,1100.
There must be at least 30 pixels of clear vertical air between successive icon groups, everywhere from first to last row. The first row artwork must be smaller than it is in the reference so that the bottom row artwork can be equally large. The bottom row must NOT be shorter, smaller or squeezed. Top and bottom outer margins must match. Do NOT draw the table, grid, cells, frames, numbers, labels or any typography. Nothing cropped, stretched, duplicated, missing or reordered. This picture must look as though each entire icon were centered in a perfectly regular 6-by-11 CSS grid with identical padding, not an organic collage.

Order to preserve:
1 leadership meeting | AI laptop | IT server | legal scales | finance calculator | financial advisor
2 marketing target | house and key | strategy chess | pharmaceutical pills | hospital administration | nursing stethoscope
3 biotechnology DNA | medical monitor | manufacturing robot | supply-chain truck | HR candidates | project calendar
4 engineering caliper | semiconductor wafer | software product phone | cybersecurity lock | analytics charts | school administration
5 academic research | hospitality luggage | aviation airplane | construction helmet | energy tower and turbine | environmental sampler
6 insurance umbrella | banking bank | ecommerce cart | film camera | telecom antenna | government capitol
7 nonprofit globe | consulting presenter | sales handshake | customer-support headset | legal compliance folders | home-care armchair
8 dental tooth | pharmacy tray | medical assistant cuff | childcare blocks | restaurant tray | cook pan
9 cafe espresso machine | housekeeping bucket | barber scissors | nail polish | retail register | delivery truck
10 warehouse shelves | landscaping mower | carpenter tools | electrician tools | plumber tools | HVAC air conditioner
11 automotive car | office phone | bookkeeping calculator | software laptop | QA monitor | medical laboratory microscope
