import unittest

from current_speed_basis_time_context import calculate, summarize


class CurrentSpeedBasisTimeContextTests(unittest.TestCase):
    def test_basis_rows_are_explicitly_partitioned(self):
        rows = calculate()
        self.assertEqual(len(rows), 7)
        summary = summarize(rows)
        self.assertEqual(summary["top_or_max_basis_rows"], 3)
        self.assertEqual(summary["explicit_cruise_basis_rows"], 4)

    def test_top_speed_does_not_equal_high_speed_cruise(self):
        summary = summarize(calculate())
        self.assertAlmostEqual(summary["highest_top_or_max_mach"], 0.95)
        self.assertAlmostEqual(summary["highest_explicit_cruise_mach"], 0.90)
        self.assertGreater(summary["g700_top_or_max_saving_percent"], summary["g700_high_speed_cruise_saving_percent"])


if __name__ == "__main__":
    unittest.main()
