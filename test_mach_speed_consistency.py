import unittest

from mach_speed_consistency import calculate, load_inputs


class MachSpeedConsistencyTests(unittest.TestCase):
    def test_expected_row_counts(self):
        speed_rows, acceleration_rows = calculate(load_inputs())
        self.assertEqual(len(speed_rows), 16)
        self.assertEqual(len(acceleration_rows), 12)

    def test_nominal_bins_are_inside_declared_intervals(self):
        _, rows = calculate(load_inputs())
        self.assertTrue(all(row["nominal_within_derived_interval"] for row in rows))

    def test_phase_distance_increases_with_speed(self):
        _, rows = calculate(load_inputs())
        for acceleration in (0.05, 0.10, 0.20):
            subset = [row for row in rows if row["acceleration_fraction_g"] == acceleration]
            lows = [row["accel_decel_distance_fraction_low"] for row in subset]
            highs = [row["accel_decel_distance_fraction_high"] for row in subset]
            self.assertTrue(all(a < b for a, b in zip(lows, lows[1:])))
            self.assertTrue(all(a < b for a, b in zip(highs, highs[1:])))

    def test_mach_five_has_largest_phase_distance_fraction(self):
        _, rows = calculate(load_inputs())
        subset = [row for row in rows if row["acceleration_fraction_g"] == 0.05]
        self.assertEqual(max(subset, key=lambda row: row["accel_decel_distance_fraction_high"])["mach"], 5.0)


if __name__ == "__main__":
    unittest.main()
