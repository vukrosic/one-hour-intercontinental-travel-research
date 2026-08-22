import unittest

from energy_input_sensitivity import calculate, load_inputs


class EnergyInputSensitivityTests(unittest.TestCase):
    def test_expected_row_count(self):
        self.assertEqual(len(calculate(load_inputs())), 33)

    def test_all_favorable_stress_still_exceeds_modern_benchmark(self):
        rows = calculate(load_inputs())
        favorable = [row for row in rows if row["scenario"] == "all_favorable_10pct"]
        self.assertEqual(len(favorable), 3)
        self.assertTrue(all(row["historical_proxy_co2_ratio_vs_modern"] > 1.0 for row in favorable))

    def test_baseline_ratio_matches_energy_gap(self):
        rows = calculate(load_inputs())
        baseline = [row for row in rows if row["scenario"] == "baseline"]
        self.assertEqual([round(row["historical_proxy_co2_ratio_vs_modern"], 3) for row in baseline], [3.017, 3.772, 5.029])


if __name__ == "__main__":
    unittest.main()
