import unittest

from energy_intensity import calculate, load_inputs


class EnergyIntensityTests(unittest.TestCase):
    def test_lower_load_factor_increases_intensity(self):
        rows = calculate(load_inputs())
        intensities = [row["concorde_proxy_btu_per_passenger_mile"] for row in rows]
        self.assertTrue(all(a < b for a, b in zip(intensities, intensities[1:])))

    def test_energy_and_co2_ratios_match_for_same_fuel(self):
        for row in calculate(load_inputs()):
            self.assertAlmostEqual(row["energy_ratio_vs_modern_long_haul"], row["co2_ratio_vs_modern_long_haul"])

    def test_full_load_proxy_exceeds_modern_long_haul(self):
        full_load = calculate(load_inputs())[0]
        self.assertGreater(full_load["energy_ratio_vs_modern_long_haul"], 1.0)

    def test_expected_rows(self):
        self.assertEqual([row["load_factor"] for row in calculate(load_inputs())], [1.0, 0.8, 0.6])


if __name__ == "__main__":
    unittest.main()
