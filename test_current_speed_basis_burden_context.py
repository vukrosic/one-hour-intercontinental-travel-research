import unittest

from current_speed_basis_burden_context import calculate, summarize


class CurrentSpeedBasisBurdenContextTests(unittest.TestCase):
    def test_proxy_rows_and_basis_counts(self):
        rows = calculate()
        self.assertEqual(len(rows), 7)
        summary = summarize(rows)
        self.assertEqual(summary["top_or_max_rows"], 3)
        self.assertEqual(summary["explicit_cruise_rows"], 4)

    def test_top_speed_proxy_exceeds_explicit_cruise_proxy(self):
        summary = summarize(calculate())
        self.assertGreater(summary["highest_top_or_max_ke_proxy"], summary["highest_explicit_cruise_ke_proxy"])
        self.assertGreater(summary["highest_top_or_max_temperature_ratio"], summary["highest_explicit_cruise_temperature_ratio"])
        self.assertGreater(summary["g700_top_ke_proxy"], summary["g700_high_cruise_ke_proxy"])


if __name__ == "__main__":
    unittest.main()
