import unittest

from airport_compatibility_close_read import load_rows, summarize


class AirportCompatibilityCloseReadTests(unittest.TestCase):
    def test_rows_are_unique(self):
        rows = load_rows()
        self.assertEqual(len(rows), 6)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))

    def test_framework_historical_and_prospective_states_are_separate(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["current_framework_rows"], 4)
        self.assertEqual(summary["historical_precedent_rows"], 1)
        self.assertEqual(summary["prospective_standard_rows"], 1)

    def test_no_current_generic_high_speed_pass(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["current_generic_high_speed_pass_rows"], 0)
        self.assertGreaterEqual(summary["candidate_characteristics_required_rows"], 4)


if __name__ == "__main__":
    unittest.main()
