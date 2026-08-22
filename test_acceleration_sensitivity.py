import unittest

from acceleration_sensitivity import calculate


class AccelerationSensitivityTests(unittest.TestCase):
    def test_expected_scenario_count(self):
        self.assertEqual(len(calculate()), 12)

    def test_higher_acceleration_reduces_phase_distance(self):
        rows = calculate()
        for start in range(0, 12, 3):
            fractions = [row["accel_decel_distance_fraction"] for row in rows[start : start + 3]]
            self.assertTrue(all(a > b for a, b in zip(fractions, fractions[1:])))

    def test_time_overhead_is_nonnegative(self):
        self.assertTrue(all(row["acceleration_time_overhead_fraction"] >= 0 for row in calculate()))

    def test_no_cruise_regime_is_explicit_if_reached(self):
        self.assertTrue(all(row["profile_regime"] in {"accelerate-cruise-decelerate", "no-cruise-lower-bound"} for row in calculate()))


if __name__ == "__main__":
    unittest.main()
