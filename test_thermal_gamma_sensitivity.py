import unittest

from thermal_gamma_sensitivity import calculate, load_inputs


class ThermalGammaSensitivityTests(unittest.TestCase):
    def test_expected_row_count_and_scenarios(self):
        rows = calculate(load_inputs())
        self.assertEqual(len(rows), 12)
        self.assertEqual(sorted({row["gamma_scenario"] for row in rows}), [1.3, 1.4])

    def test_intervals_increase_with_mach_for_each_gamma(self):
        rows = calculate(load_inputs())
        for gamma in (1.3, 1.4):
            subset = [row for row in rows if row["gamma_scenario"] == gamma]
            lows = [row["ideal_total_temperature_low_K"] for row in subset]
            highs = [row["ideal_total_temperature_high_K"] for row in subset]
            self.assertTrue(all(a < b for a, b in zip(lows, lows[1:])))
            self.assertTrue(all(a < b for a, b in zip(highs, highs[1:])))

    def test_mach_three_lower_bound_exceeds_mach_two_upper_bound(self):
        rows = calculate(load_inputs())
        for gamma in (1.3, 1.4):
            subset = {row["mach_bin"]: row for row in rows if row["gamma_scenario"] == gamma}
            self.assertGreater(
                subset[3.0]["ideal_total_temperature_low_K"],
                subset[2.0]["ideal_total_temperature_high_K"],
            )


if __name__ == "__main__":
    unittest.main()
