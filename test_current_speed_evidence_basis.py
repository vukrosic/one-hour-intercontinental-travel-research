import unittest

from current_speed_evidence_basis import load_rows, summarize


class CurrentSpeedEvidenceBasisTests(unittest.TestCase):
    def test_current_rows_and_evidence_roles(self):
        rows = load_rows()
        self.assertEqual(len(rows), 4)
        summary = summarize(rows)
        self.assertEqual(summary["rows_with_top_or_max_speed"], 3)
        self.assertEqual(summary["rows_with_explicit_high_speed_cruise"], 1)
        self.assertEqual(summary["rows_with_top_and_high_speed_cruise"], 1)

    def test_top_and_cruise_frontiers_are_distinct(self):
        summary = summarize(load_rows())
        self.assertAlmostEqual(summary["highest_top_or_max_mach"], 0.95)
        self.assertAlmostEqual(summary["highest_explicit_cruise_mach"], 0.90)
        self.assertAlmostEqual(summary["largest_top_minus_high_speed_cruise_gap"], 0.035)


if __name__ == "__main__":
    unittest.main()
