import unittest

from thermal_sensitivity import calculate, load_inputs


class ThermalSensitivityTests(unittest.TestCase):
    def test_intervals_increase_with_mach(self):
        rows = calculate(load_inputs())
        lows = [row["ideal_total_temperature_low_K"] for row in rows]
        highs = [row["ideal_total_temperature_high_K"] for row in rows]
        self.assertTrue(all(a < b for a, b in zip(lows, lows[1:])))
        self.assertTrue(all(a < b for a, b in zip(highs, highs[1:])))

    def test_each_interval_is_ordered(self):
        for row in calculate(load_inputs()):
            self.assertLess(row["ideal_total_temperature_low_K"], row["ideal_total_temperature_high_K"])

    def test_mach_three_interval_is_separate_from_mach_two(self):
        rows = {row["mach_bin"]: row for row in calculate(load_inputs())}
        self.assertGreater(rows[3.0]["ideal_total_temperature_low_K"], rows[2.0]["ideal_total_temperature_high_K"])


if __name__ == "__main__":
    unittest.main()
