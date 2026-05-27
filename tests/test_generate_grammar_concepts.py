import importlib.util
import sys
import unittest
from pathlib import Path

from bs4 import BeautifulSoup


MODULE_PATH = Path(__file__).resolve().parents[1] / "generate_grammar_concepts.py"
SPEC = importlib.util.spec_from_file_location("generate_grammar_concepts", MODULE_PATH)
ggc = importlib.util.module_from_spec(SPEC)
sys.modules["generate_grammar_concepts"] = ggc
SPEC.loader.exec_module(ggc)


class GenerateGrammarConceptsTests(unittest.TestCase):
    def test_parse_structured_practice_keeps_options_with_prompt(self):
        html = """
        <div>
          <p>Answer the quiz questions below.</p>
          <div>
            <p><b>#1:</b> The professor talked the French economy.</p>
            <details><summary>Answer:</summary>Incorrect. The correct sentence is “The professor talked about the French economy.”</details>
            <ul><li>A. Correct</li><li>B. Incorrect</li></ul>
          </div>
        </div>
        """
        column = BeautifulSoup(html, "html.parser").find("div")

        parsed = ggc.parse_structured_practice(column)
        self.assertIsNotNone(parsed)
        intro, items = parsed
        self.assertEqual("Answer the quiz questions below.", intro)
        self.assertEqual(1, len(items))
        self.assertEqual(
            ["The professor talked the French economy.", "A. Correct", "B. Incorrect"],
            items[0].prompt_lines,
        )
        self.assertEqual(
            ["Incorrect. The correct sentence is “The professor talked about the French economy.”"],
            items[0].answer_lines,
        )

    def test_parse_structured_practice_supports_answer_paragraphs(self):
        html = """
        <div>
          <p>Answer the quiz questions below.</p>
          <div>
            <p><b>#1:</b> The news was alarm-.</p>
            <p>Answer:</p>
            <p>alarming</p>
            <details><summary>Reveal answer</summary><p>See explanation below.</p></details>
          </div>
        </div>
        """
        column = BeautifulSoup(html, "html.parser").find("div")

        parsed = ggc.parse_structured_practice(column)
        self.assertIsNotNone(parsed)
        _, items = parsed
        self.assertEqual(["The news was alarm-."], items[0].prompt_lines)
        self.assertEqual(["alarming"], items[0].answer_lines)

    def test_parse_structured_practice_supports_inline_details_answers(self):
        html = """
        <div>
          <p>Answer the quiz questions below.</p>
          <div>
            <p><b>#1:</b> The news was alarm-. <details><summary>Answer:</summary>alarming</details></p>
          </div>
        </div>
        """
        column = BeautifulSoup(html, "html.parser").find("div")

        parsed = ggc.parse_structured_practice(column)
        self.assertIsNotNone(parsed)
        _, items = parsed
        self.assertEqual(["The news was alarm-."], items[0].prompt_lines)
        self.assertEqual(["alarming"], items[0].answer_lines)

    def test_fragment_answer_rebuilds_full_sentence(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "The house _____ is on the corner is blue.",
                "(a) that",
                "(b) which",
            ],
            answer_lines=["The house", "that", "is on the corner is blue."],
            note_sections=[],
        )

        self.assertEqual(
            ["The house that is on the corner is blue."],
            ggc.derive_correct_answers(item),
        )
        self.assertEqual(["(b) which"], ggc.derive_incorrect_answers(item, ggc.derive_correct_answers(item)))

    def test_quoted_blank_answer_uses_full_sentence(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "My boss suggested ______ take a day off.",
                "A. I",
                "B. me",
                "C. my",
            ],
            answer_lines=[
                'A. “My boss suggested I take a day off.” is correct. The subjunctive mode uses “I” as the subject pronoun.'
            ],
            note_sections=[],
        )

        self.assertEqual(
            ["My boss suggested I take a day off."],
            ggc.derive_correct_answers(item),
        )
        self.assertEqual(
            ["B. me", "C. my"],
            ggc.derive_incorrect_answers(item, ggc.derive_correct_answers(item)),
        )

    def test_boolean_correction_answer_shows_status_and_fix(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "The professor talked the French economy.",
                "A. Correct",
                "B. Incorrect",
            ],
            answer_lines=["Incorrect. The correct sentence is “The professor talked about the French economy.”"],
            note_sections=[],
        )

        self.assertEqual(
            ["B. Incorrect", "The professor talked about the French economy."],
            ggc.derive_correct_answers(item),
        )
        self.assertEqual(
            ["A. Correct"],
            ggc.derive_incorrect_answers(item, ggc.derive_correct_answers(item)),
        )

    def test_override_style_answer_keeps_only_real_correct_option(self):
        item = ggc.PracticeItem(
            number=10,
            prompt_lines=[
                'Which sentence correctly uses "in order to" as an alternative to "so"?',
                "a) I'm studying French in order to that I can read Voltaire.",
                "b) In order to I can read Voltaire, I'm studying French.",
                "c) I'm studying French in order to read Voltaire.",
                "d) In order to read Voltaire, I'm studying French that.",
            ],
            answer_lines=["c) I'm studying French in order to read Voltaire."],
            note_sections=[
                (
                    "Feedback",
                    [
                        'Option c) is correct. "In order to" is followed directly by a verb, not by "that" or a subject. Options a), b), and d) are grammatically incorrect.'
                    ],
                )
            ],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(
            ["c) I'm studying French in order to read Voltaire."],
            correct_answers,
        )
        self.assertEqual(
            [
                "a) I'm studying French in order to that I can read Voltaire.",
                "b) In order to I can read Voltaire, I'm studying French.",
                "d) In order to read Voltaire, I'm studying French that.",
            ],
            ggc.derive_incorrect_answers(item, correct_answers),
        )

    def test_feedback_can_add_second_correct_option(self):
        item = ggc.PracticeItem(
            number=16,
            prompt_lines=[
                'Which sentence demonstrates the correct use of "so" in a question?',
                "a) So, what do you think about the proposal?",
                "b) What do you think about the proposal so?",
                "c) So what do you think about the proposal?",
                "d) What so do you think about the proposal?",
            ],
            answer_lines=[
                'a) So, what do you think about the proposal? Feedback: Both options a) and c) are correct uses of "so" to start a question in informal speech. Option a) uses a comma for a slight pause, while c) is also acceptable without the comma. Options b) and d) are incorrect placements of "so" in a question.'
            ],
            note_sections=[],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(
            [
                "a) So, what do you think about the proposal?",
                "c) So what do you think about the proposal?",
            ],
            correct_answers,
        )
        self.assertEqual(
            [
                "b) What do you think about the proposal so?",
                "d) What so do you think about the proposal?",
            ],
            ggc.derive_incorrect_answers(item, correct_answers),
        )

    def test_correct_answer_label_maps_to_option_and_keeps_note(self):
        item = ggc.PracticeItem(
            number=4,
            prompt_lines=[
                "The car window had been left open. (So it rained on the seats.)",
                "a) The car window was open before it rained on the seats.",
                "b) The car window was closed before it rained on the seats.",
            ],
            answer_lines=[
                "The car window had been left open. Correct answer: a",
                "Feedback: “Had been left open” indicates the window was left open before the rain.",
            ],
            note_sections=[],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(
            ["a) The car window was open before it rained on the seats."],
            correct_answers,
        )
        self.assertEqual(
            ["b) The car window was closed before it rained on the seats."],
            ggc.derive_incorrect_answers(item, correct_answers),
        )

    def test_bare_choice_label_maps_to_full_option(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "I had been living in New York before I moved to Tokyo.",
                "a) I lived in New York after moving to Tokyo.",
                "b) I lived in New York, then I moved to Tokyo.",
            ],
            answer_lines=[
                "Correct answer: b",
                "Feedback: The past perfect shows the New York living happened before the move.",
            ],
            note_sections=[],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(
            ["b) I lived in New York, then I moved to Tokyo."],
            correct_answers,
        )
        self.assertEqual(
            ["a) I lived in New York after moving to Tokyo."],
            ggc.derive_incorrect_answers(item, correct_answers),
        )

    def test_correct_note_section_can_supply_fill_in_answer(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "She ________ finish the report before the deadline because she worked overtime.",
            ],
            answer_lines=[
                "Correct:",
                "was able to",
                "Incorrect:",
                "could",
                'Explanation: "Could" suggests possibility but not a completed action. "Was able to" confirms that she successfully finished the report.',
            ],
            note_sections=[],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(
            ["She was able to finish the report before the deadline because she worked overtime."],
            correct_answers,
        )
        self.assertEqual(
            ["could"],
            ggc.derive_incorrect_answers(item, correct_answers),
        )

    def test_correct_note_section_can_supply_option_answer(self):
        item = ggc.PracticeItem(
            number=1,
            prompt_lines=[
                "The cake is _____ ready.",
                "a) almost",
                "b) most",
            ],
            answer_lines=[
                "Correct:",
                "a) almost",
                "Incorrect: b) most - Most cannot be used here because the sentence refers to something nearly complete.",
            ],
            note_sections=[],
        )

        correct_answers = ggc.derive_correct_answers(item)
        self.assertEqual(["The cake is almost ready."], correct_answers)
        self.assertEqual(
            ["b) most"],
            ggc.derive_incorrect_answers(item, correct_answers),
        )


if __name__ == "__main__":
    unittest.main()
