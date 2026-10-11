"""Additional original retail and e-commerce conversations."""
from books.supplements import scenario

SCENARIOS = [
    scenario(
        title="Sales are not the bank payout",
        skill="Reconcile marketplace receipts, refunds, fees, and reserved funds without calling every difference a loss.",
        setup="Fictional marketplace statement: $5,000 captured item sales, $400 refunds, $300 nonrefundable fees, and $200 newly reserved. No opening balance, tax, shipping, currency conversion, or other adjustments. The resulting payout has been issued but is not yet confirmed received by the bank. The reserve release date is unspecified.",
        cast="Nora|Marketplace manager\nFelix|Finance analyst",
        dialogue="""Nora|The marketplace shows five thousand in sales, but the payout is only four thousand one hundred. Have we lost nine hundred dollars somewhere?
Felix|Let us follow the [[settlement statement::The settlement statement connects the captured sales to refunds, fees, reserved funds, and the issued payout; the difference is not automatically missing money.]]. Four hundred went back to customers, three hundred is fees, and two hundred has been reserved.
Nora|After the refunds, that leaves four thousand six hundred. I had treated that as the amount we should see in the bank.
Felix|That is sales less the supplied refunds, before the other statement adjustments. The [[processing fees::The processing fees are the stated $300 deduction; unlike the reserve, they are nonrefundable under this fictional statement's terms.]] reduce the amount available for payout by another three hundred.
Nora|So we are at four thousand three hundred before the reserve. Is the reserved two hundred another fee?
Felix|No. The [[reserve hold::The reserve hold sets aside $200 rather than paying it out now; it is distinct from the nonrefundable $300 fee and has no supplied release date.]] is money set aside under these terms. It is not the same as a nonrefundable charge.
Nora|Then the reconciliation is five thousand, less four hundred, less three hundred, less two hundred: four thousand one hundred issued.
Felix|Exactly. Keep the four lines visible. If we label the entire nine-hundred difference as marketplace commission, both the refund and reserve explanations disappear.
Nora|The dashboard says the payout has been issued. Can I mark it received in our cash report now?
Felix|Check the [[bank receipt::Bank receipt confirms the funds actually reached the bank; an issued marketplace payout is a different processing stage and is not sufficient evidence of receipt.]] first. The bank has not confirmed it in our supplied record, so keep the transfer outstanding for reconciliation.
Nora|I will match the payout reference against the bank entry when it appears. An equal amount alone might not identify the right transfer.
Felix|Good. Retain the reference, amount, currency, and dates. Also make sure the refund rows belong to this settlement rather than subtracting them a second time elsewhere.
Nora|If the two hundred is released next month, should the sales report show another two hundred of sales?
Felix|No. A [[reserve release::A reserve release makes previously held funds available; it does not create a new customer sale, and any later deductions still need reconciliation.]] concerns existing funds. We would reconcile the later statement and its actual deductions rather than record a new sale.
Nora|Can I put the release in next month's cash forecast as certain? I would like to use that money for a supplier payment.
Felix|We have no release date here. Show any forecast assumption explicitly and check the applicable reserve terms before making a commitment against it.
Nora|I will keep captured sales, refunds, fees, and held funds in separate columns. The payout column will remain separate from confirmed bank receipts.
Felix|That gives us a usable [[reconciliation trail::A reconciliation trail preserves how each adjustment connects the source statement to the payout and bank record, making later differences traceable.]]. Finance can then apply the appropriate accounting treatment without trying to reconstruct the statement from one net figure.
Nora|For today's trading call: four thousand one hundred issued, two hundred reserved, and bank receipt still outstanding. Not nine hundred in unexplained losses.
Felix|That is clear. Attach the statement reference and leave the receipt check assigned to me; the commercial team can use the sales measures without confusing them with cash.""",
        transfer_title="Trace a smaller payout",
        transfer_setup="Fictional statement: $2,000 captured sales, $150 refunds, $100 fees, and $80 reserved. No other adjustments. The payout is issued, but bank receipt is unconfirmed. Any later reserve release relates to these existing funds.",
        transfer="""Manager: Sales less the refunds equal ___ dollars.|1,850|Two thousand captured sales less one hundred fifty refunded leaves one thousand eight hundred fifty.
Analyst: After fees and the reserve, the issued payout is ___ dollars.|1,670|Subtracting the one-hundred-dollar fee and eighty-dollar reserve from 1,850 gives 1,670.
Manager: Bank receipt is still ___.|unconfirmed|The statement establishes issuance only; no bank record of receipt has been supplied.
Analyst: Releasing the reserve would not create a new ___.|sale|The reserve contains existing transaction funds, so its later release is not another customer purchase.""",
        reference=("Shopify: payment reserves and releases", "https://help.shopify.com/en/manual/payments/shopify-payments/payouts/reserves"),
    ),
    scenario(
        title="The right shirt, the wrong variant",
        skill="Resolve a catalog mismatch by reading back identifiers and distinguishing variant data from product-group data.",
        setup="Fictional Harbor Tee variants: blue/medium SKU HT-BL-M has zero available; blue/large SKU HT-BL-L has twenty. Both belong to group HARBOR-TEE. The large variant's shopping-feed title incorrectly says medium and its link preselects medium. Its size field and manufacturer-assigned GTIN are verified as large. No customer order has been placed.",
        cast="Sana|Catalog specialist\nJoel|Digital merchandiser",
        dialogue="""Joel|The shopping result says blue, medium, twenty available. Our medium shelf is empty. Is this another inventory-feed problem?
Sana|The twenty belongs to large. The [[variant SKU::The variant SKU identifies the specific internal item: HT-BL-L is blue/large, while HT-BL-M is blue/medium with no available units.]] ends in L, and the size field says large. The title has been copied from medium.
Joel|Both rows use HARBOR-TEE as their group. Should I change the large row to a completely different group to separate them?
Sana|No. The shared [[item group ID::The item group ID groups genuine variants of the same product; it does not replace each variant's distinct identifier or merge their stock quantities.]] connects variants of the same shirt. Keep distinct item IDs and the correct size on each row.
Joel|Then the parent group is not a stock pool. Twenty large shirts cannot support a promise of twenty medium shirts.
Sana|Exactly. The [[size attribute::The size attribute must describe the offered variant; here large is correct and medium in the title is the mismatch needing correction.]] is already correct for large. Fix the misleading title rather than changing that accurate field to match it.
Joel|The image shows the blue shirt. It would look the same in medium and large. That may be why the mistake survived the visual check.
Sana|Yes. An image can confirm color and style without proving size. Check the identifiers and supplied product data, not the thumbnail alone.
Joel|The link also opens medium by default. If we change only the title, the shopper could still land on the wrong selection.
Sana|We need the [[landing-page selection::The landing-page selection must correspond to the advertised variant; a large listing linked to a preselected medium option still creates a mismatch.]] to match the large offer. Test the actual feed link, not just navigation from the main product page.
Joel|The barcode field is verified as large. Should I copy medium's barcode so all the grouped rows share one?
Sana|No. Preserve the verified [[GTIN::The Global Trade Item Number is a product identifier assigned under the applicable system; the verified large-variant GTIN must not be replaced with medium's merely to make grouped rows match.]]. Sharing a product group does not make different trade-item identifiers interchangeable. Do not invent a replacement number either.
Joel|I will leave the correct stock, size, and identifier alone. The title and the link selection are the two confirmed corrections.
Sana|Right. Then preview both variants separately. A fix for large should not change medium's zero availability or turn the group record into a purchasable extra item.
Joel|Can I tell the trading team the listing is fixed as soon as I save the source file?
Sana|Not yet. Check the [[processed feed::The processed feed shows what the destination accepted after ingestion; saving the source file alone does not establish the final displayed offer.]] and the displayed offer after ingestion. Record any delay or rejection instead of assuming the update has propagated.
Joel|I will test the large shopping result through to the selected large item and confirm the stock still shows twenty.
Sana|And test medium separately: correct medium title, medium selection, and zero availability. That second check catches accidental changes to the sibling variant.
Joel|My handoff will list both SKUs, their size and stock, the corrected title and link, and the destination check. No inventory adjustment is needed from these facts.
Sana|Good. We are repairing the offer mapping, not manufacturing stock or changing the shirt. That is the distinction the support team needs when answering the next query.""",
        transfer_title="Read the variant, not just the group",
        transfer_setup="Fictional red cap: medium SKU RC-M has 0 available; large SKU RC-L has 12. Both share group RED-CAP. The large feed row wrongly says medium in its title; its size field and verified GTIN correctly identify large.",
        transfer="""Merchandiser: The twelve available units belong to SKU ___.|RC-L|The supplied inventory assigns all twelve units to the large variant, identified internally as RC-L.
Specialist: The shared group identifier is ___.|RED-CAP|Both genuine variants belong to RED-CAP, while retaining their own distinct item identities.
Merchandiser: Medium's available quantity remains ___.|0|Correcting a title does not move or create stock for the medium variant.
Specialist: Correct the large row's title, not its already verified ___.|GTIN|The case verifies the large identifier, so changing it merely to match an erroneous title would introduce another error.""",
        reference=("Google Merchant Center: grouping product variants", "https://support.google.com/merchants/answer/6324507?hl=en"),
    ),
    scenario(
        title="Two discounts, two calculation bases",
        skill="Explain an offer using its actual combination order and eligibility threshold, then agree precise customer-facing wording.",
        setup="Fictional tested offer: a $100 product gets a 20% product discount, followed by a combinable 10% order discount on the reduced merchandise subtotal. Free shipping requires at least $75 AFTER both discounts; otherwise shipping is $5. No tax or other charge. These rules are supplied for this offer, not every platform or combination.",
        cast="Emil|Promotions executive\nGrace|Trading quality analyst",
        dialogue="""Emil|The banner says thirty percent off with free shipping. We have twenty percent off the product and another ten percent at checkout. Does that wording work?
Grace|Not for this setup. The [[product discount::The product discount takes twenty percent from the original $100 product price, leaving $80 before the order discount is calculated.]] reduces the hundred-dollar item to eighty. The next ten percent uses eighty as its base.
Emil|So the checkout discount is eight dollars, not another ten. That leaves seventy-two for the merchandise.
Grace|Yes. This [[order discount::The order discount is ten percent of the already reduced $80 merchandise subtotal, so it removes $8 under the supplied combination rules.]] follows the product discount. The combined merchandise saving is twenty-eight dollars, or twenty-eight percent of the original price.
Emil|I added the percentages because both messages used percent off. The different bases are what make that calculation wrong here.
Grace|Exactly. We should say twenty percent off the product, then an extra ten percent off the reduced subtotal. Show the final example price as well.
Emil|What about free shipping? The original price is a hundred, and even the first discounted amount is eighty. Both are above seventy-five.
Grace|The [[shipping threshold::The shipping threshold is assessed after both discounts in this fictional offer; the relevant subtotal is $72, below the $75 minimum.]] is checked after both discounts. Seventy-two falls below seventy-five, so the five-dollar shipping charge applies.
Emil|That makes the payable total seventy-seven, with no tax or other charge in this test. It is not seventy dollars delivered.
Grace|Correct. The [[merchandise subtotal::The merchandise subtotal is $72 after both discounts, while the final payable total is $77 after adding the separate $5 shipping charge.]] and final total need separate labels. A shipping charge is not a reversal of the product discount.
Emil|Can we increase the free-shipping threshold calculation to the pre-discount price instead? That would make the banner easier to keep.
Grace|That would be a different commercial rule requiring an approved change and retest. Do not change the interpretation simply to rescue wording already drafted.
Emil|Fair. I will correct the banner to match the approved offer. We can show the free-shipping condition beside it rather than imply everyone qualifies.
Grace|Also confirm [[combination eligibility::Combination eligibility determines whether the two offers may apply together; the supplied test allows this combination, but that does not establish other discount pairings.]] in the actual checkout. An entered code is not proof that its discount applied successfully.
Emil|Should our support script say percentages always apply one after another? That would be a quick explanation for agents.
Grace|No. Other classes and configurations can use the same base or disallow combining. Explain this product-then-order sequence without turning it into a universal rule.
Emil|For the test record, I will capture the starting hundred, twenty off, eight off, seventy-two subtotal, five shipping, and seventy-seven total.
Grace|Include the [[checkout summary::The checkout summary records the applied discounts, shipping basis, and payable total; it allows the displayed offer to be checked against the actual calculation.]] and the approved conditions. Test a qualifying basket separately instead of assuming this below-threshold basket covers both outcomes.
Emil|Then the revised message can give the seventy-two merchandise price and state that this basket has five-dollar shipping. No thirty-percent or free-shipping claim for it.
Grace|That works. Send the corrected copy and the captured calculation together so merchandising, support, and the checkout team all explain the same offer.""",
        transfer_title="Check the threshold after both reductions",
        transfer_setup="Fictional offer: $200 product, 25% product discount, then 10% order discount on the reduced subtotal. Free shipping starts at $140 AFTER both discounts; otherwise $6. No tax or other charges.",
        transfer="""Executive: After the product discount, the subtotal is ___ dollars.|150|Twenty-five percent off two hundred removes fifty dollars, leaving one hundred fifty.
Analyst: After the order discount, merchandise costs ___ dollars.|135|Ten percent of the reduced one-hundred-fifty subtotal is fifteen, leaving one hundred thirty-five.
Executive: Shipping is charged because that subtotal is ___ the threshold.|below|The post-discount subtotal of 135 is below the stated 140-dollar free-shipping threshold.
Analyst: Including shipping, the total is ___ dollars.|141|The one-hundred-thirty-five merchandise subtotal plus six-dollar shipping equals one hundred forty-one.""",
        reference=("Shopify: discount classes and combination rules", "https://help.shopify.com/en/manual/discounts/discount-combinations"),
    ),
]
