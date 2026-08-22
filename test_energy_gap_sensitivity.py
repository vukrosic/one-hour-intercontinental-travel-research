import unittest

from energy_gap_sensitivity import calculate


class EnergyGapSensitivityTests(unittest.TestCase):
    def test_expected_occupancy_rows(self):
        self.assertEqual([row["load_factor"] for row in calculate()], [1.0, 0.8, 0.6])

    def test_required_reduction_increases_as_occupancy_falls(self):
        reductions = [row["required_reduction_fraction"] for row in calculate()]
        self.assertTrue(all(a < b for a, b in zip(reductions, reductions[1:])))

    def test_full_load_still_requires_large_reduction(self):
        self.assertGreater(calculate()[0]["required_reduction_fraction"], 0.6)


if __name__ == "__main__":
    unittest.main()
