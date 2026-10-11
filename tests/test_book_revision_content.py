"""Focused checks for the expanded conversations and corrected teaching points."""
import re
import unittest

from books.supplements import load_supplements
from work_curriculum import load_tracks


class RevisedTeachingPointTests(unittest.TestCase):
    def test_bookkeeping_periods_bonus_premium_and_due_date_aging_reconcile(self):
        from datetime import date
        scenarios = load_supplements('bookkeeping-payroll')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['600', '200', '1800', 'no'])
        self.assertEqual(answers(scenarios[1]), ['20', '60', '980', 'six'])
        self.assertEqual(answers(scenarios[2]), ['31', '200', 'current', '440'])
        regular = (44 * 20 + 88) / 44
        self.assertEqual(regular, 22)
        self.assertEqual(4 * regular / 2 - 40, 4)
        self.assertEqual(44 * 20 + 88 + 4 * regular / 2, 1012)
        self.assertEqual((date(2026, 11, 30) - date(2026, 10, 30)).days, 31)
        self.assertIn('not the amount to add', scenarios[0]['gaps'][2]['reason'])

    def test_office_expenses_mailing_and_print_counts_keep_distinct_bases(self):
        scenarios = load_supplements('office-administrative-assistants')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['120', '80', '40', 'pending'])
        self.assertEqual(answers(scenarios[1]), ['two', 'pending', '00456', 'unconfirmed'])
        self.assertEqual(answers(scenarios[2]), ['six', '108', '114', 'pending'])
        self.assertEqual(48 + 42 - 50, 40)
        self.assertEqual((30 + 2) * 20 / 4, 160)
        self.assertIn('different people', scenarios[1]['gaps'][1]['reason'])

    def test_automotive_codes_energy_and_angles_are_not_interchangeable(self):
        scenarios = load_supplements('automotive-service')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['225', '45', '17', 'unapproved'])
        self.assertEqual(answers(scenarios[1]), ['20', '25', 'five', 'six'])
        self.assertEqual(answers(scenarios[2]), ['0.15', '0.05', '0.20', 'unrecorded'])
        self.assertEqual(60 * .6 / .9, 40)
        self.assertAlmostEqual(6 / 60 + 12 / 60, .3)
        self.assertIn('not a recommended driving speed', scenarios[0]['gaps'][5]['reason'])

    def test_electrical_energy_ratings_and_power_keep_different_quantities(self):
        scenarios = load_supplements('electricians')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['160', '240', '60', 'three'])
        self.assertEqual(answers(scenarios[1]), ['dust-tight', 'powerful-water-jet', 'temporary-immersion', 'unconfirmed'])
        self.assertEqual(answers(scenarios[2]), ['0.6', '0.8', '1.44', 'unknown'])
        self.assertEqual(12 * (40 - 24) / 1000 * 2500, 480)
        self.assertEqual(480 / (480 * .2), 5)
        self.assertAlmostEqual(1.84 / 2.3, .8)
        self.assertIn('doesn\'t by itself establish', scenarios[1]['dialogue'][7][1])

    def test_carpentry_allowances_matching_and_moisture_preserve_references(self):
        scenarios = load_supplements('carpentry-remodeling')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['2396', 'six', '2402', 'two'])
        self.assertEqual(answers(scenarios[1]), ['P22', 'P23', 'book matching', 'slip matching'])
        self.assertEqual(answers(scenarios[2]), ['15', '10', '13', 'above'])
        self.assertEqual(3000 - (3 * 995 + 3 * 3), 6)
        self.assertEqual(3 * 998 + 3 * 3 - 3000, 3)
        self.assertAlmostEqual((90 - 80) / 80 * 100, 12.5)
        self.assertIn('not every wood product', scenarios[2]['dialogue'][7][1])

    def test_pharmacy_units_and_effective_dates_stay_distinct(self):
        calculation, temperature, packs = load_supplements('pharmacy-technicians')
        answers = [q['options'][q['answer']] for q in calculation['transfer']['lines']]
        self.assertEqual(answers, ['3', '28', '6', 'unknown'])
        self.assertIn('not a prediction', calculation['gaps'][4]['reason'])
        self.assertIn('thirty-five minutes', temperature['gaps'][1]['reason'])
        answers = [q['options'][q['answer']] for q in temperature['transfer']['lines']]
        self.assertEqual(answers, ['30', '10.2', 'vials', 'pending'])
        self.assertIn('not the Monday', packs['gaps'][1]['reason'])
        answers = [q['options'][q['answer']] for q in packs['transfer']['lines']]
        self.assertEqual(answers, ['14', '18', '19', 'completed'])

    def test_dental_notation_and_material_stock_are_not_interchangeable(self):
        notation, history, stock = load_supplements('dental-assistants')
        self.assertIn('upper-left first premolar', notation['dialogue'][1][1])
        self.assertIn('upper-right lateral incisor', notation['dialogue'][2][1])
        answers = [q['options'][q['answer']] for q in notation['transfer']['lines']]
        self.assertEqual(answers, ['12', '7', 'existing', 'audit trail'])
        self.assertIn('cannot substitute', history['dialogue'][12][1])
        self.assertIn('six usable', stock['gaps'][2]['reason'])
        answers = [q['options'][q['answer']] for q in stock['transfer']['lines']]
        self.assertEqual(answers, ['8', '10', '2', 'received'])

    def test_explanations_do_not_refer_to_unshuffled_option_positions(self):
        from build_industry_books import load_book
        from books.cross_cultural_leadership_content import SLUG, UNITS
        for track in load_tracks():
            units = UNITS if track['slug'] == SLUG else load_book(track['slug'])['units']
            for unit in units:
                for item in unit['a'] + unit['d']:
                    with self.subTest(slug=track['slug'], question=item['prompt']):
                        self.assertNotRegex(item['reason'], r'(?i)\b(first|second|third|fourth) option\b')
                        self.assertNotRegex(item['reason'], r'(?i)\bthe first (statement|summary|proposal|response|sentence)\b')
                        self.assertNotRegex(item['reason'], r'(?i)\bthe first (question|request|headline|description|wording|task|aim|message|opening|reply|note|update|announcement|record|item|offer|account|corrects|confirms|distinguishes)\b')

    def test_annual_advice_fee_is_not_charged_four_times(self):
        from books.financial_advice_content import BOOK
        question = BOOK['units'][1]['dialogue'][4][1]
        response = BOOK['units'][1]['dialogue'][5][1]
        self.assertIn('four times', question)
        self.assertTrue(response.startswith('No.'))
        self.assertIn('annual rate, not the rate charged each quarter', response)

    def test_repeatability_is_used_for_same_condition_runs(self):
        from books.pharmaceutical_content import BOOK
        unit = BOOK['units'][0]
        self.assertIn('repeatability', [term for term, _, _ in unit['vocabulary']])
        self.assertNotIn('reproducibility', [term for term, _, _ in unit['vocabulary']])
        self.assertEqual(unit['gaps'][5]['answer'], 'repeatability')
        self.assertIn('same analyst, method, and equipment', unit['dialogue'][11][1])

    def test_containment_does_not_wait_for_root_cause(self):
        from books.pharmaceutical_content import BOOK
        self.assertIn('Keep containment in place now', BOOK['units'][5]['dialogue'][13][1])

    def test_workforce_hours_reconcile_with_headcount_and_fte(self):
        scenario = load_supplements('human-resources')[2]
        self.assertIn('four hundred', scenario['dialogue'][3][1])
        self.assertNotIn('four hundred eighty', scenario['dialogue'][3][1])
        self.assertIn('equals four hundred', scenario['gaps'][1]['reason'])
        self.assertIn('gives ten FTE', scenario['gaps'][2]['reason'])
        self.assertIn('headcount', scenario['gaps'][0]['answer'])

    def test_overtime_example_keeps_gross_and_net_separate(self):
        scenario = load_supplements('human-resources')[0]
        self.assertIn('two hundred sixteen dollars of gross pay', scenario['dialogue'][5][1])
        self.assertIn('eleven hundred seventy-six', scenario['dialogue'][6][1])
        self.assertIn('before deductions', scenario['gaps'][2]['reason'])

    def test_earned_value_example_uses_the_correct_comparisons(self):
        scenario = load_supplements('project-management')[0]
        reasons = {gap['answer']: gap['reason'] for gap in scenario['gaps']}
        self.assertIn('negative $5,000', reasons['cost variance'])
        self.assertIn('equals 0.90', reasons['cost performance index'])
        self.assertIn('negative $15,000', reasons['schedule variance'])

    def test_mix_shift_example_preserves_actual_and_standardized_rates(self):
        item = load_supplements('data-analytics-business-intelligence')[0]
        self.assertAlmostEqual((10 + 270) / 1000, .28)
        self.assertAlmostEqual((108 + 32) / 1000, .14)
        self.assertAlmostEqual(.1 * .12 + .9 * .32, .30)
        self.assertIn('twenty-eight percent', item['dialogue'][4][1])
        self.assertIn('fourteen percent', item['dialogue'][5][1])
        self.assertIn('thirty percent, not the observed fourteen percent', item['dialogue'][12][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers[:3], ['50', '40', 'ten'])

    def test_forecast_errors_keep_ticket_units_and_relative_improvement(self):
        item = load_supplements('data-analytics-business-intelligence')[2]
        self.assertIn('eight tickets per daily forecast', item['dialogue'][11][1])
        self.assertIn('twenty-percent reduction', item['dialogue'][14][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['six', 'eight', 'twenty-five', 'error'])

    def test_examination_extra_time_is_working_time(self):
        item = load_supplements('education-administration')[0]
        self.assertIn('one hundred minutes altogether', item['dialogue'][2][1])
        self.assertIn('ten-forty finish', item['dialogue'][3][1])
        self.assertIn('cannot substitute', item['dialogue'][5][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['thirty', '14:30', 'unchanged', 'extension'])

    def test_research_linear_response_does_not_imply_zero_offset(self):
        from books.higher_education_research_content import BOOK
        unit = BOOK['units'][2]
        terms = {term: definition for term, definition, _ in unit['vocabulary']}
        self.assertIn('nonzero offset', terms['linear response'])
        self.assertIn('repeatability check', terms)
        self.assertIn('background correction', unit['gaps'][2]['reason'])
        self.assertEqual(unit['gaps'][-1]['answer'], 'repeatability check')
        bank = BOOK['units'][3]['transfer']['lines'][0]['options']
        self.assertIn('key', bank)
        self.assertNotIn('on hold', bank)

    def test_research_grant_base_excludes_equipment_not_total_request(self):
        item = load_supplements('higher-education-research')[1]
        reasons = {gap['answer']: gap['reason'] for gap in item['gaps']}
        self.assertIn('$5,200', reasons['indirect costs'])
        self.assertIn('$69,200', reasons['total request'])
        self.assertIn('two point four person-months', item['dialogue'][13][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['40,000', '6,000', '56,000', '4,000'])


    def test_hospitality_routing_changes_payer_not_total(self):
        item = load_supplements('hospitality-tourism')[2]
        self.assertIn('three hundred eighty', item['dialogue'][6][1])
        self.assertIn('not a discount or a refund', item['dialogue'][7][1])
        self.assertEqual(2 * 150 + 2 * 15 + 20 + 30, 380)

    def test_aviation_time_conversion_preserves_previous_local_date(self):
        item = load_supplements('aviation')[1]
        self.assertIn('on the eighth, not the ninth', item['dialogue'][2][1])
        self.assertIn('forty-five minutes', item['dialogue'][5][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['11', '00:40', '40', 'approval'])

    def test_cargo_billing_weight_does_not_replace_actual_mass(self):
        item = load_supplements('aviation')[2]
        self.assertEqual(4 * 60 * 50 * 40 / 6000, 80)
        self.assertIn('actual gross mass', item['gaps'][0]['answer'])
        self.assertIn('Do not substitute', item['dialogue'][13][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['40', '44', '176', '190'])

    def test_progress_payment_deducts_prior_certificates_not_cash(self):
        item = load_supplements('construction-architecture')[2]
        self.assertIn('thirty-five thousand', item['dialogue'][4][1])
        self.assertEqual(item['gaps'][3]['answer'], 'previous certificates')
        self.assertIn('unpaid balance is tracked separately', item['gaps'][3]['reason'])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['80,000', '4,000', '26,000', '5,000'])


    def test_energy_storage_uses_net_energy_without_repeating_losses(self):
        item = load_supplements('energy-utilities')[2]
        self.assertIn('three hours', item['dialogue'][4][1])
        self.assertIn('already allows for losses', item['dialogue'][7][1])
        answers = [q['options'][q['answer']] for q in item['transfer']['lines']]
        self.assertEqual(answers, ['2.5', '150', '75', 'double-count'])
        self.assertEqual(15 / .25 * 12 + 10000 * .1, 1720)
        self.assertEqual(18 / .25 * 12 + 9000 * .1, 1764)


    def test_environmental_reporting_preserves_basis_and_qualifiers(self):
        from books.environmental_consulting_content import BOOK
        terms = {t: d for t, d, _ in BOOK['units'][1]['vocabulary']}
        self.assertIn('qualified estimates', terms['reporting limit'])
        scenarios = load_supplements('environmental-consulting')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['0.60', '10', '9', 'basis'])
        self.assertEqual(answers(scenarios[1]), ['zero', 'detection', '0.0007', 'qualifier'])
        self.assertEqual(answers(scenarios[2]), ['85.30', '84.80', '0.50', 'direction'])
        self.assertAlmostEqual(104.60 - 4.20 - (100.80 - 1.80), 1.40)


    def test_insurance_reconciliation_credits_prior_payment_and_single_deductible(self):
        scenarios = load_supplements('insurance')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['5,400', '4,500', '900', 'payroll'])
        self.assertEqual(answers(scenarios[1]), ['8,000', '3,000', '11,000', 'once'])
        self.assertEqual(answers(scenarios[2]), ['200,000', 'exhausted', '150,000', 'deductible'])
        self.assertIn('not one to every payment', scenarios[1]['dialogue'][9][1])
        self.assertEqual(300000 / 100 * 2.4 - 6000, 1200)


    def test_banking_balances_quotes_and_interest_keep_their_bases(self):
        scenarios = load_supplements('banking-operations')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['550', '480', 'released', 'double-count'])
        self.assertEqual(answers(scenarios[1]), ['2,500', '2,520', '1,990', 'authorization'])
        self.assertEqual(answers(scenarios[2]), ['100', '160', '260', '360'])
        self.assertAlmostEqual(round(100000 * .06 * 20 / 360 + 150000 * .06 * 10 / 360, 2), 583.33)
        self.assertIn('five hundred eighty-three', scenarios[2]['dialogue'][6][1])


    def test_retail_payouts_variants_and_discount_bases_remain_distinct(self):
        from books.retail_ecommerce_content import BOOK
        terms = {t: d for t, d, _ in BOOK['units'][0]['vocabulary']}
        self.assertIn('distinct from units held', terms['assortment depth'])
        scenarios = load_supplements('retail-ecommerce')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['1,850', '1,670', 'unconfirmed', 'sale'])
        self.assertEqual(answers(scenarios[1]), ['RC-L', 'RED-CAP', '0', 'GTIN'])
        self.assertEqual(answers(scenarios[2]), ['150', '135', 'below', '141'])
        self.assertEqual(5000 - 400 - 300 - 200, 4100)
        self.assertEqual(100 * .8 * .9 + 5, 77)
        self.assertIn('Other classes and configurations', scenarios[2]['dialogue'][15][1])


    def test_media_audio_caption_and_rundown_corrections_keep_units(self):
        from books.media_entertainment_content import BOOK
        self.assertIn('shorter, 15-second', BOOK['units'][0]['brief'])
        self.assertIn('fifteen-second', BOOK['units'][0]['dialogue'][12][1])
        scenarios = load_supplements('media-entertainment')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['3', '-4', '2', 'remeasure'])
        self.assertEqual(answers(scenarios[1]), ['0.25', 'earlier', 'not', 'synchronization'])
        self.assertEqual(answers(scenarios[2]), ['120', '18:28:45', '18:29:35', 'start'])
        self.assertEqual(8 / 25, .32)
        self.assertEqual(90 + 60 + 30, 180)
        self.assertIn('move later, not earlier', scenarios[1]['dialogue'][4][1])


    def test_telecommunications_keeps_direction_margin_and_port_scope(self):
        scenarios = load_supplements('telecommunications')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['office', 'audio', 'unchecked', 'T19'])
        self.assertEqual(answers(scenarios[1]), ['16', '12', '4', '1'])
        self.assertEqual(answers(scenarios[2]), ['six', 'four', 'partial', 'requested'])
        self.assertEqual(-3 - (-20) - 15, 2)
        self.assertIn('one decibel', scenarios[1]['dialogue'][6][1])
        self.assertIn('eight moving, four staying', scenarios[2]['dialogue'][19][1])
        self.assertIn('not proof that both audio directions worked', scenarios[0]['dialogue'][1][1])


    def test_government_votes_budget_and_notice_keep_distinct_requirements(self):
        scenarios = load_supplements('government-public-administration')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['five', '5', '3', 'adopted'])
        self.assertEqual(answers(scenarios[1]), ['15', '48', '25', '17'])
        self.assertEqual(answers(scenarios[2]), ['one', 'application', '16:00', 'receipt'])
        self.assertIn('pilot was not approved', scenarios[0]['dialogue'][6][1])
        self.assertEqual(120 - (62 + 12) - (38 - 15), 23)
        self.assertIn('avoid calling the released three thousand a cash refund', scenarios[1]['dialogue'][12][1])
        self.assertIn('two required items', scenarios[2]['dialogue'][1][1])


    def test_nonprofit_matching_full_cost_and_consent_respect_their_limits(self):
        from books.nonprofit_ngo_content import BOOK
        pledge = next(d for t, d, _ in BOOK['units'][7]['vocabulary'] if t == 'pledge')
        self.assertIn('promise', pledge)
        self.assertIn('not merely an expression of interest', pledge)
        self.assertEqual(BOOK['units'][7]['gaps'][5]['answer'], 'prospective gift')
        scenarios = load_supplements('nonprofit-ngo')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['5', '11.2', '6.2', 'zero'])
        self.assertEqual(answers(scenarios[1]), ['5', '45', '47', '2'])
        self.assertEqual(answers(scenarios[2]), ['newsletter', 'quote', 'stopped', 'services'])
        self.assertEqual(60000 * .1, 6000)
        self.assertIn('not a hidden subsidy', scenarios[1]['dialogue'][8][1])
        self.assertIn('will not affect your services', scenarios[2]['dialogue'][3][1])


    def test_consulting_reuse_benefit_bases_and_model_handover_are_bounded(self):
        scenarios = load_supplements('consulting')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['template', 'confidential', 'report', 'authorized'])
        self.assertEqual(answers(scenarios[1]), ['32', '12', '5', 'double-count'])
        self.assertEqual(answers(scenarios[2]), ['16', '6,000', '2,000', 'forecast'])
        self.assertEqual(20000 - 15000, 5000)
        self.assertEqual(1800 * (30 - 18) - 15000, 6600)
        self.assertIn('not manufacture a forty-thousand noncash residual', scenarios[1]['dialogue'][16][1])
        self.assertIn('does not settle', scenarios[0]['dialogue'][3][1])


    def test_sales_release_tender_and_channel_metrics_use_the_stated_scope(self):
        scenarios = load_supplements('sales-business-development')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['650', '200', '50', 'unconfirmed'])
        self.assertEqual(answers(scenarios[1]), ['staffed', '3', '10', 'permitted'])
        self.assertEqual(answers(scenarios[2]), ['60', 'two', '15', '12'])
        self.assertEqual(40 + 240 - 160, 120)
        self.assertAlmostEqual(round(160 / (40 + 240) * 100, 1), 57.1)
        self.assertIn('twenty is the most', scenarios[2]['dialogue'][10][1])
        self.assertIn('nine hundred not yet released', scenarios[0]['dialogue'][17][1])


    def test_customer_success_retention_proration_and_exit_states_stay_distinct(self):
        scenarios = load_supplements('customer-success')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['80', '160', '90', '230'])
        self.assertEqual(answers(scenarios[1]), ['1,200', '180', '1,020', 'co-termination'])
        self.assertEqual(answers(scenarios[2]), ['attachments', '16:00', 'extension', 'unconfirmed'])
        self.assertEqual((100 - 20 - 10 + 35) / 100, 1.05)
        self.assertEqual(15 * 20 * 3 * .9, 810)
        self.assertEqual(115 * 20 * 12, 27600)
        self.assertIn('not in the retention numerator', scenarios[0]['dialogue'][1][1])
        self.assertIn('not make export assistance depend', scenarios[2]['dialogue'][1][1])


    def test_legal_operations_billing_preservation_and_notice_keep_separate_states(self):
        scenarios = load_supplements('legal-operations-compliance')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['200', '400', '1700', 'approval'])
        self.assertEqual(answers(scenarios[1]), ['email', 'chat', 'records', 'release'])
        self.assertEqual(answers(scenarios[2]), ['non-renewal', '12:00', 'receipt', 'reminder'])
        self.assertEqual(12 * 300 + 3 * 500 + 150, 5250)
        self.assertEqual(12 * 325 + 4 * 500 + 150 - 5250, 800)
        self.assertIn('does not authorize its disclosure', scenarios[1]['dialogue'][13][1])
        self.assertIn('not proof of', scenarios[2]['dialogue'][9][1])


    def test_home_care_records_actual_support_and_checks_accessible_details(self):
        from books.home_care_caregivers_content import BOOK
        mar = next(d for t, d, _ in BOOK['units'][3]['vocabulary'] if t == 'MAR')
        self.assertIn('different types of medicines support', mar)
        self.assertIn('yogurt with berries', BOOK['units'][4]['brief'])
        scenarios = load_supplements('home-care-caregivers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['22.40', '2', '7.60', '30'])
        self.assertEqual(answers(scenarios[1]), ['10:15', '6 June', 'large print', 'me'])
        self.assertEqual(answers(scenarios[2]), ['16:00', 'unconfirmed', 'delivered', 'emergency'])
        self.assertAlmostEqual(50 - 34.70 - 13.30, 2)
        self.assertIn('not two thirty', scenarios[1]['dialogue'][6][1])
        self.assertIn('no care delivered', scenarios[2]['dialogue'][18][1])


    def test_medical_assisting_checks_language_units_and_actual_clinical_receipt(self):
        from books.medical_assistants_content import BOOK
        call = BOOK['units'][6]
        self.assertEqual(call['cast'], [('Noor', 'Medical assistant'), ('Dana', 'Receiving nurse')])
        self.assertIn('does not delay the live clinical call', call['brief'])
        scenarios = load_supplements('medical-assistants')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['Spanish', 'English', 'telephone', 'support'])
        self.assertEqual(answers(scenarios[1]), ['59.9', '10:18', '1.65', '10:31'])
        self.assertEqual(answers(scenarios[2]), ['10', '14:02', '14:07', 'supplied'])
        self.assertEqual(round(160 * .45359237, 1), 72.6)
        self.assertEqual(round(132 * .45359237, 1), 59.9)
        self.assertIn('not two separate weighings', scenarios[1]['dialogue'][3][1])
        self.assertIn('not a clinical diagnosis', scenarios[2]['dialogue'][1][1])


    def test_childcare_confirms_names_sources_and_safeguarding_actions(self):
        from books.childcare_early_education_content import BOOK
        dll = next(d for t, d, _ in BOOK['units'][5]['vocabulary'] if t == 'dual language learner')
        self.assertIn('two or more', dll)
        scenarios = load_supplements('childcare-early-education')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(scenarios[0]), ['seven', 'two', 'nine', 'occurred'])
        self.assertEqual(answers(scenarios[1]), ['French', 'English', 'song', 'Tuesday'])
        self.assertEqual(answers(scenarios[2]), ['10:12', 'exact', 'Leena', 'confirmed'])
        self.assertIn('eleven with us and one with Leena', scenarios[0]['dialogue'][4][1])
        self.assertIn('neither proves nor rules out', scenarios[1]['dialogue'][15][1])
        self.assertIn('must not delay protective action', scenarios[2]['brief'])
        self.assertIn("own reporting duties", scenarios[2]['dialogue'][17][1])


    def test_restaurant_stock_charges_and_guest_choice_remain_distinct(self):
        from books.restaurant_servers_content import BOOK
        self.assertEqual([name for name, _ in BOOK['units'][0]['cast']], ['Lena', 'Cam'])
        stock, charge, access = load_supplements('restaurant-servers')
        self.assertIn('including the three', stock['dialogue'][1][1])
        self.assertIn('$47', stock['gaps'][3]['reason'])
        answers = [q['options'][q['answer']] for q in stock['transfer']['lines']]
        self.assertEqual(answers, ['two', 'chicken', '80', 'unavailable'])
        self.assertEqual(150 + 150 * .18 + 12, 189)
        answers = [q['options'][q['answer']] for q in charge['transfer']['lines']]
        self.assertEqual(answers, ['12', '98', 'zero', 'unspecified'])
        self.assertIn('speak directly with you', access['dialogue'][17][1])
        self.assertEqual(access['gaps'][1]['answer'], 'Parmesan')


    def test_kitchen_recipe_yield_and_recall_trace_are_consistent(self):
        from books.cooks_kitchen_staff_content import BOOK
        rotation = dict((term, meaning) for term, meaning, _ in BOOK['units'][7]['vocabulary'])
        self.assertIn('First expiring', rotation['FEFO'])
        scaling, yield_case, recall = load_supplements('cooks-kitchen-staff')
        self.assertEqual((30 * 200) / (12 * 250), 2)
        self.assertIn('not the count-only ratio 2.5', scaling['gaps'][1]['reason'])
        answers = [q['options'][q['answer']] for q in scaling['transfer']['lines']]
        self.assertEqual(answers, ['3', '4.5', '1.5', '900'])
        self.assertEqual(10 / .8, 12.5)
        self.assertIn('0.4 kg shortfall', yield_case['gaps'][3]['reason'])
        answers = [q['options'][q['answer']] for q in yield_case['transfer']['lines']]
        self.assertEqual(answers, ['12', '36', '4', '0.80'])
        self.assertIn('empty fourth bottle is not a full bottle', recall['gaps'][1]['reason'])
        answers = [q['options'][q['answer']] for q in recall['transfer']['lines']]
        self.assertEqual(answers, ['R6', 'three', 'S4', 'unresolved'])


    def test_barista_ratios_strength_and_overlapping_orders_are_distinct(self):
        ratio, strength, order = load_supplements('baristas-cafe-staff')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(ratio), ['20', '1:2', '1:2.5', 'unmeasured'])
        self.assertEqual(answers(strength), ['5', '20', '500', '1.00'])
        self.assertEqual(answers(order), ['two', 'one', 'four', 'requested'])
        self.assertEqual(500 * 1.35 / 30, 22.5)
        self.assertAlmostEqual(6.75 / 600 * 100, 1.125)
        self.assertIn('beverage-based estimate', strength['brief'])
        self.assertIn('two plus two plus one plus seven', order['dialogue'][7][1].lower())


    def test_cleaning_checks_contact_conditions_sample_scope_and_labor_time(self):
        contact, marker, workload = load_supplements('housekeeping-commercial-cleaning')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(contact), ['three', '14:13', '14:12', 'not met'])
        self.assertIn('four minutes wet followed by one dry minute', contact['dialogue'][3][1].lower())
        self.assertEqual(answers(marker), ['seven', '70%', 'three', 'not established'])
        self.assertIn('not a percentage of the room disinfected', marker['dialogue'][5][1])
        self.assertEqual(answers(workload), ['3', '60', '14:15', '3.75'])
        self.assertEqual(600 / 200 + 2 * 15 / 60, 3.5)
        self.assertEqual((600 / 200) / 2 * 60 + 15, 105)


    def test_hairdressing_keeps_visible_length_guard_labels_and_tests_distinct(self):
        from books.hairdressers_barbers_content import BOOK
        self.assertIn('away from the basin', BOOK['units'][4]['brief'])
        self.assertIn('must not wait', BOOK['units'][4]['brief'])
        curl, guard, color = load_supplements('hairdressers-barbers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(curl), ['chin', 'stretched', 'coarse', 'low'])
        self.assertEqual(answers(guard), ['ten', 'three', 'removed', 'unagreed'])
        self.assertEqual(answers(color), ['six', 'neutral', 'warm', 'incomplete'])
        self.assertIn('fine strands with high density', curl['dialogue'][7][1])
        self.assertIn('nominal length, not a guarantee', guard['dialogue'][17][1])
        self.assertIn('different starting record', color['dialogue'][7][1])


    def test_nail_services_keep_lamp_tool_and_design_records_distinct(self):
        lamp, tools, design = load_supplements('nail-technicians')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(lamp), ['M2', 'M9', 'rating', 'unverified'])
        self.assertEqual(answers(tools), ['F', 'only', 'disposal', 'storage'])
        self.assertEqual(answers(design), ['seven', 'three', 'left thumb', 'right hand'])
        self.assertIn("doesn't establish the required light conditions", lamp['dialogue'][7][1])
        self.assertIn("isn't established here", tools['dialogue'][11][1])
        self.assertIn('instead of A, not both', design['dialogue'][6][1])


    def test_retail_receipts_locations_and_tare_do_not_double_count(self):
        payment, shelf, weight = load_supplements('retail-associates-cashiers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(payment), ['50.25', '9.75', '12', 'zero'])
        self.assertEqual(answers(shelf), ['ten', 'six', 'three', 'thirteen'])
        self.assertEqual(answers(weight), ['1200', '9.00', '0.45', 'once'])
        self.assertAlmostEqual(50 - (42.60 - 15), 22.40)
        self.assertEqual(7 + 6 + 5, 12 + 6)
        self.assertAlmostEqual((.845 - .035) * 12, 9.72)
        self.assertIn('including the front unit', shelf['dialogue'][1][1])
        self.assertIn('already the product-only amount', weight['dialogue'][11][1])


    def test_driver_times_billing_and_clearance_preserve_their_basis(self):
        zone, detention, route = load_supplements('truck-delivery-drivers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(zone), ['15:45', '20:45', 'fifteen', 'unconfirmed'])
        self.assertEqual(answers(detention), ['13:10', '51', 'four', '80'])
        self.assertEqual(answers(route), ['20', '4.20', '15', 'unverified'])
        self.assertEqual(10 * 60 + 35 - (7 * 60 + 40), 175)
        self.assertEqual((35 + 14) // 15 * 20, 60)
        self.assertAlmostEqual((4.12 - 3.90) * 100, 22)
        self.assertIn('Rounding belongs in the calculation', detention['dialogue'][11][1])
        self.assertIn("doesn't approve the route", route['dialogue'][7][1])
        self.assertIn('one appointment, not two slots', zone['dialogue'][4][1])


    def test_warehouse_dates_identifiers_and_cutoffs_keep_their_basis(self):
        from datetime import date
        shelf, scan, count = load_supplements('warehouse-distribution')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(shelf), ['nineteen', 'F', 'four', 'two'])
        self.assertEqual(answers(scan), ['two', 'T', 'R', 'unchecked'])
        self.assertEqual(answers(count), ['92', 'zero', '14:30', '104'])
        delivery = date(2026, 11, 12)
        self.assertEqual([(d - delivery).days for d in (
            date(2026, 11, 30), date(2026, 12, 31), date(2026, 12, 15))],
            [18, 49, 33])
        self.assertEqual(100 - 6, 94)
        self.assertIn('same reduction twice', count['dialogue'][11][1])
        self.assertIn("doesn't mean Q is physically missing", scan['dialogue'][16][1])
        self.assertIn('not a claim that anything has been picked', shelf['dialogue'][18][1])


    def test_landscape_quantities_plant_labels_and_irrigation_measures(self):
        volume, plants, water = load_supplements('landscaping-grounds')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(volume), ['720', '756', 'nineteen', 'four'])
        self.assertEqual(answers(plants), ['six', 'container size', 'cultivar', 'ten'])
        self.assertEqual(answers(water), ['nine', 'eighteen', 'six', '66.7'])
        self.assertAlmostEqual((12 * 2 + 4 * 3 - 4) * .05, 1.6)
        self.assertAlmostEqual(1600 * 1.1, 1760)
        self.assertEqual(36 * 50 - 1760, 40)
        self.assertEqual(sum([10, 12, 14, 16] * 4) / 16, 13)
        self.assertAlmostEqual(round(10 / 13 * 100), 77)
        self.assertIn("doesn't change the approved fifty-millimeter", volume['dialogue'][13][1])
        self.assertIn("That's not an", water['dialogue'][11][1])
        self.assertIn('not a height measurement', plants['dialogue'][7][1])


    def test_plumbing_flow_delivery_and_levels_keep_their_units(self):
        flow, heater, drain = load_supplements('plumbers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(flow), ['12', '0.2', '320', '110'])
        self.assertEqual(answers(heater), ['D', '50', 'two', 'unapproved'])
        self.assertEqual(answers(drain), ['150', '12.650', '1.67', 'inside bottom'])
        self.assertEqual(6 / 30 * 60, 12)
        self.assertEqual(68 - 66, 2)
        self.assertEqual(62 - 66, -4)
        self.assertAlmostEqual(50.300 - 12 / 80, 50.150)
        self.assertIn('not a diagnosis', flow['dialogue'][11][1])
        self.assertIn('part of that delivery', heater['dialogue'][5][1])
        self.assertIn("isn't itself a depth-of-cover", drain['dialogue'][15][1])


    def test_hvac_capacity_air_source_and_blend_references(self):
        cooling, air, blend = load_supplements('hvac-refrigeration')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(cooling), ['1.6', '0.4', 'D', '0.7'])
        self.assertEqual(answers(air), ['three', '0.75', '25', '50'])
        self.assertEqual(answers(blend), ['dew', 'seven', 'bubble', 'six'])
        self.assertAlmostEqual(13 - 10.4, 2.6)
        self.assertEqual(9 / 12, .75)
        self.assertEqual(150 / 300, .5)
        self.assertEqual(150 / 600 * 100, 25)
        self.assertEqual(12 - 5, 7)
        self.assertEqual(40 - 35, 5)
        self.assertIn('extra latent capacity', cooling['dialogue'][5][1])
        self.assertIn('count the outdoor flow twice', air['dialogue'][15][1])
        self.assertIn('No applicable targets', blend['dialogue'][15][1])
        from books.hvac_refrigeration_content import BOOK
        self.assertIn('already alerted', BOOK['units'][5]['brief'])
        self.assertIn("we've alerted", BOOK['units'][5]['dialogue'][0][1])


    def test_developer_conditional_writes_queries_and_decimal_contracts(self):
        from decimal import Decimal, ROUND_HALF_UP
        edit, queries, money = load_supplements('software-developers')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(edit), ['412', '9', 'old', 'stale'])
        self.assertEqual(answers(queries), ['5', '20', '201', '784'])
        self.assertEqual(answers(money), ['0.03', '0.12', '1.12', '0.02'])
        cent = Decimal('.01')
        line_charge = (Decimal('.05') * Decimal('.1')).quantize(cent, rounding=ROUND_HALF_UP)
        basket_charge = (Decimal('.15') * Decimal('.1')).quantize(cent, rounding=ROUND_HALF_UP)
        self.assertEqual(line_charge * 3, Decimal('.03'))
        self.assertEqual(basket_charge, Decimal('.02'))
        self.assertEqual((51 - 2) * 4, 196)
        self.assertIn('body still carries eighteen', edit['dialogue'][5][1])
        self.assertIn("isn't a universal limit", queries['dialogue'][15][1])
        self.assertIn("doesn't establish what any jurisdiction requires", money['dialogue'][17][1])
        from books.software_developers_content import BOOK
        self.assertIn("haven't established that", BOOK['units'][1]['dialogue'][2][1])


    def test_qa_combinations_mutation_denominators_and_keyboard_evidence(self):
        rule, mutation, focus = load_supplements('software-quality-assurance')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(rule), ['A', '10', 'membership', 'unexecuted'])
        self.assertEqual(answers(mutation), ['5', '9', '55.6', '71.4'])
        self.assertEqual(answers(focus), ['passed', 'unchecked', 'failed', 'untested'])
        self.assertEqual(2 ** 3, 8)
        self.assertEqual(2 / 8 * 100, 25)
        self.assertEqual(round(8 / 11 * 100, 1), 72.7)
        self.assertEqual(8 / 10 * 100, 80)
        self.assertIn('before discount', rule['dialogue'][8][1])
        self.assertIn('excludes compile error', mutation['dialogue'][1][1])
        self.assertIn('blanket approval', focus['dialogue'][19][1])
        self.assertIn('screen reader', focus['dialogue'][10][1])
        from books.software_quality_assurance_content import BOOK
        self.assertEqual(BOOK['units'][1]['gaps'][4]['answer'], 'reproduction run')
        self.assertIn('not confirmation testing', BOOK['units'][1]['dialogue'][9][1])


    def test_laboratory_statistics_dilution_and_reporting_qualifiers(self):
        qc, dilution, limits = load_supplements('medical-laboratory-technicians')
        answers = lambda s: [q['options'][q['answer']] for q in s['transfer']['lines']]
        self.assertEqual(answers(qc), ['15', 'three', '2.5', 'held'])
        self.assertEqual(answers(dilution), ['10', '70', '700', 'pending'])
        self.assertEqual(answers(limits), ['detected', '0.40', 'quantification', 'unsupplied'])
        self.assertEqual((107 - 100) / 2, 3.5)
        self.assertEqual(2 / 100 * 100, 2)
        self.assertEqual(40 * (1 + 4), 200)
        self.assertEqual(200 * 5, 1000)
        self.assertIn('not a universal', qc['gaps'][2]['reason'])
        self.assertIn('not an mg/L', dilution['gaps'][4]['reason'])
        self.assertIn('false zero', limits['dialogue'][19][1])
        from books.medical_laboratory_technicians_content import BOOK
        self.assertIn('Correction: six point four, not six point one', BOOK['units'][6]['dialogue'][2][1])
        self.assertIn('That read-back is correct', BOOK['units'][6]['dialogue'][4][1])


    def test_leadership_clearance_is_not_review_completion(self):
        from books.cross_cultural_leadership_content import UNITS
        exchange = UNITS[3]['transfer']
        self.assertIn('clearance has not been granted', exchange['setup'])
        self.assertEqual([q['options'][q['answer']] for q in exchange['lines']],
                         ['internal', 'until', 'review pending', 'clears'])
        self.assertIn('compliance grants clearance', exchange['lines'][1]['prompt'])

    def test_ai_rehearsals_preserve_metric_bases_and_unknown_scope(self):
        from books.ai_development_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('33,000 against a 32,000', BOOK['units'][1]['rehearsal'][0])
        question = BOOK['units'][5]['d'][2]
        self.assertEqual(question['options'][question['answer']],
                         'How serious are the newly failing cases for users?')
        self.assertIn('50-percent reduction', BOOK['units'][6]['rehearsal'][0])


    def test_it_inventory_overlap_and_health_checks_remain_distinct(self):
        from books.general_it_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('subset of the installed group', BOOK['units'][4]['dialogue'][15][1])
        q = BOOK['units'][3]['d'][2]
        self.assertEqual(q['options'][q['answer']],
                         'How far back may the recovered data point be relative to the disruption?')
        self.assertIn('constrained capacity', BOOK['units'][7]['gaps'][7]['reason'])
        self.assertIn('pending account-owner confirmation', BOOK['units'][5]['rehearsal'][1])


    def test_law_proposals_and_evidence_are_not_treated_as_agreements(self):
        from books.law_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        negotiation = BOOK['units'][5]
        self.assertIn('complete', negotiation['gaps'][1]['reason'].lower())
        self.assertIn('not', negotiation['gaps'][1]['reason'].lower())
        metadata = next(q for q in BOOK['units'][3]['d'] if 'example of metadata' in q['prompt'])
        self.assertIn('creation', metadata['options'][metadata['answer']].lower())


    def test_finance_rehearsals_keep_balances_and_authority_separate(self):
        from books.finance_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('separate reviewer', BOOK['units'][6]['dialogue'][14][1])
        self.assertEqual(1200 - 700 - 500, 0)
        self.assertIn('three items open', BOOK['units'][6]['rehearsal'][1])
        self.assertIn('December service and January payment', BOOK['units'][1]['rehearsal'][0])
        material_weakness = next(v for v in BOOK['units'][6]['vocabulary'] if v[0] == 'material weakness')
        self.assertIn('reasonable possibility', material_weakness[1])


    def test_advice_rehearsals_preserve_client_choice_and_model_limits(self):
        from books.financial_advice_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertTrue(BOOK['units'][1]['dialogue'][13][1].startswith('No, it does not'))
        self.assertIn('fixed date', BOOK['units'][2]['transfer']['setup'])
        self.assertIn('no withdrawal instruction', BOOK['units'][3]['dialogue'][19][1])
        self.assertIn('no trade is authorized', BOOK['units'][4]['dialogue'][19][1])
        q = next(q for q in BOOK['units'][3]['d'] if 'sequence risk' in q['prompt'])
        self.assertIn('order of investment returns', q['options'][q['answer']])


    def test_marketing_comparisons_keep_time_rate_and_outcome_bases(self):
        from books.marketing_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('task rate rises 25%', BOOK['units'][1]['precision'])
        self.assertAlmostEqual((50 - 40) / 50, .2)
        self.assertAlmostEqual(50 / 40 - 1, .25)
        self.assertTrue(BOOK['units'][6]['precision'].startswith('The observed rates'))
        self.assertIn('Monitoring is not itself proof of a problem', BOOK['units'][6]['dialogue'][9][1])
        self.assertIn('temporary copy', BOOK['units'][2]['dialogue'][1][1])


    def test_real_estate_comparisons_and_known_access_obstacles(self):
        from books.real_estate_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('before discussing', BOOK['units'][0]['a'][0]['prompt'])
        self.assertNotIn('verified step-free', BOOK['units'][1]['transfer']['lines'][2]['prompt'])
        self.assertIn('Forty thousand less', BOOK['units'][2]['dialogue'][5][1])
        self.assertEqual((470000 + 540000 + 430000) / 3, 480000)
        self.assertIn('not a repair-completion promise', BOOK['units'][7]['dialogue'][9][1])


    def test_strategy_models_preserve_capacity_and_forward_decisions(self):
        from books.corporate_strategy_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('forty weeks is enough', BOOK['units'][1]['dialogue'][13][1])
        self.assertIn('would create', BOOK['units'][4]['transfer']['lines'][1]['prompt'])
        self.assertEqual(120 + 100 - 160, 60)
        q = next(q for q in BOOK['units'][3]['d'] if 'monthly bridge' in q['prompt'])
        self.assertIn('declined by $7,500', q['options'][q['answer']])
        self.assertIn('no', BOOK['units'][5]['dialogue'][17][1])
        self.assertNotIn('resources', next(v[1] for v in BOOK['units'][1]['vocabulary'] if v[0] == 'cannibalization'))


    def test_pharmaceutical_intake_precedes_follow_up_and_claims_stay_limited(self):
        from books.pharmaceutical_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        safety = BOOK['units'][4]
        self.assertIn('sent the message', safety['dialogue'][2][1])
        self.assertIn('confirm receipt', safety['dialogue'][3][1])
        self.assertIn('inpatient hospitalization', safety['precision'])
        self.assertIn('persistent or significant disability', safety['precision'])
        self.assertIn('Keep containment in place now', BOOK['units'][5]['dialogue'][13][1])
        self.assertIn('same target question', BOOK['units'][3]['dialogue'][17][1])


    def test_healthcare_handoffs_require_acceptance_not_just_receipt(self):
        from books.healthcare_administration_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        handoff = next(v for v in BOOK['units'][5]['vocabulary'] if v[0] == 'handoff acceptance')
        self.assertIn('responsibility', handoff[1])
        self.assertIn('identity', BOOK['units'][5]['brief'])
        self.assertEqual(12 + 8, 20)
        self.assertEqual(12 / 20, .6)
        self.assertEqual(12 / 100, .12)

    def test_nursing_reports_preserve_evidence_and_event_times(self):
        from books.nursing_allied_health_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('I am taking', BOOK['units'][2]['dialogue'][15][1])
        self.assertIn('does not establish the cause', BOOK['units'][2]['dialogue'][7][1])
        self.assertIn('neither', BOOK['units'][4]['d'][3]['reason'])
        self.assertIn('2:20', BOOK['units'][5]['d'][3]['reason'])
        self.assertIn('2:45', BOOK['units'][5]['d'][3]['reason'])
        self.assertIn('already', BOOK['units'][1]['rehearsal'][2])


    def test_biotech_percentage_bases_and_scale_stages_remain_explicit(self):
        from books.biotechnology_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('reverse decrease', BOOK['units'][1]['dialogue'][11][1])
        self.assertIn('one hundred twenty-five', BOOK['units'][1]['dialogue'][10][1])
        self.assertAlmostEqual((125 - 100) / 100, .25)
        self.assertAlmostEqual((125 - 100) / 125, .2)
        self.assertIn('conditional harvest estimate', BOOK['units'][4]['dialogue'][3][1])
        self.assertIn('Six', BOOK['units'][6]['precision'])


    def test_device_intake_routes_early_and_observation_does_not_invent_cause(self):
        from books.medical_devices_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('routed the account now', BOOK['units'][5]['dialogue'][2][1])
        self.assertIn('received it for assessment', BOOK['units'][5]['dialogue'][3][1])
        self.assertIn('misreading', BOOK['units'][3]['a'][1]['reason'])
        self.assertIn('compromised care', next(v[1] for v in BOOK['units'][3]['vocabulary'] if v[0] == 'critical task'))
        self.assertIn('three hundred held, two sampled failures', BOOK['units'][6]['dialogue'][18][1])


    def test_manufacturing_keeps_batch_disposition_and_drawing_basis_distinct(self):
        from books.manufacturing_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertEqual(900 + 60 + 40, 1000)
        self.assertAlmostEqual(12.18 - 12.10, .08)
        self.assertIn('responsibility', next(v[1] for v in BOOK['units'][7]['vocabulary'] if v[0] == 'acknowledgment'))

    def test_supply_chain_keeps_order_cohorts_and_capacity_gaps_distinct(self):
        from books.supply_chain_logistics_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('80 to 130', BOOK['units'][3]['d'][2]['reason'])
        self.assertIn('deferred', BOOK['units'][7]['dialogue'][16][1])
        self.assertEqual(12000 - 11000, 1000)
        self.assertNotEqual(12000 - 10500, 12000 - 11000)


    def test_hr_keeps_pay_measures_and_reported_accounts_distinct(self):
        from books.human_resources_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertAlmostEqual(72000 / 80000, .9)
        self.assertAlmostEqual((72000 - 60000) / (100000 - 60000), .3)
        self.assertIn('does not place it at a meeting', BOOK['units'][3]['d'][1]['reason'])
        self.assertIn('pending', BOOK['units'][2]['d'][1]['options'][BOOK['units'][2]['d'][1]['answer']])


    def test_project_reviews_do_not_turn_float_or_checkpoints_into_approval(self):
        from books.project_management_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertIn('Unrelated flexibility', BOOK['units'][1]['d'][1]['reason'])
        handoff = ' '.join(text for _, text in BOOK['units'][6]['dialogue'])
        self.assertIn('14:00', handoff)
        self.assertIn('14:30', handoff)
        self.assertIn('not a promise', handoff)
        self.assertEqual(8 + 2 + 1 - (5 + 2 + 1), 3)

    def test_engineering_preserves_cost_basis_and_unit_conversion(self):
        from books.engineering_content import BOOK
        self.assertEqual(len({tuple(u['rehearsal']) for u in BOOK['units']}), 8)
        self.assertEqual((14 * 3000 + 1000) - (12 * 3000 + 5000), 2000)
        self.assertEqual(100 * .01, 1)
        self.assertIn('Multiply', BOOK['units'][7]['dialogue'][9][1])
        self.assertIn('changed conditions', next(v[1] for v in BOOK['units'][2]['vocabulary'] if v[0] == 'reproducibility'))


class PrintedBlankTests(unittest.TestCase):
    def test_contiguous_glyphs_form_one_printed_blank(self):
        from audit_work_books import blank_runs
        chars = [dict(text='_', x0=100 + 5 * i, x1=105 + 5 * i, top=200, size=10)
                 for i in range(32)]
        self.assertEqual([len(run) for run in blank_runs(chars)], [32])
        self.assertEqual(blank_runs(chars)[0][-1]['x1'] - blank_runs(chars)[0][0]['x0'], 160)

    def test_wrapping_and_horizontal_gaps_do_not_hide_split_blanks(self):
        from audit_work_books import blank_runs
        chars = [dict(text='_', x0=100 + 5 * (i % 16), x1=105 + 5 * (i % 16),
                      top=200 + 14 * (i // 16), size=10) for i in range(32)]
        self.assertEqual([len(run) for run in blank_runs(chars)], [16, 16])
        for i, char in enumerate(chars):
            char['top'] = 200
            char['x0'] = 100 + 5 * i + (4 if i >= 16 else 0)
            char['x1'] = char['x0'] + 5
        self.assertEqual([len(run) for run in blank_runs(chars)], [16, 16])


class ExpandedConversationTests(unittest.TestCase):
    def test_complete_collection_has_726_distinct_extended_conversations(self):
        from work_books import book_units
        scripts = []
        for track in load_tracks():
            scenarios = book_units(track['slug']) + load_supplements(track['slug'])
            self.assertEqual(len(scenarios), 11)
            scripts.extend(re.sub(r'\s+', ' ', ' '.join(text for _, text in item['dialogue'])).casefold()
                           for item in scenarios)
        self.assertEqual(len(scripts), 726)
        self.assertEqual(len(set(scripts)), len(scripts))

    def test_every_book_has_three_distinct_extended_scenarios(self):
        scripts = set()
        for track in load_tracks():
            with self.subTest(slug=track['slug']):
                extras = load_supplements(track['slug'])
                self.assertEqual(len(extras), 3)
                for item in extras:
                    self.assertEqual(len(item['dialogue']), 20)
                    self.assertEqual(len(item['gaps']), 6)
                    self.assertEqual(len(item['transfer']['lines']), 4)
                    text = ' '.join(speech for _, speech in item['dialogue'])
                    normalized = re.sub(r'\s+', ' ', text).casefold()
                    self.assertNotIn(normalized, scripts)
                    scripts.add(normalized)
                    self.assertGreaterEqual(len(text.split()), 220)
                    self.assertLessEqual(len(text.split()), 550)


if __name__ == '__main__':
    unittest.main()
