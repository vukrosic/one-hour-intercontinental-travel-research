import unittest

from energy_input_independent_check import compare


class EnergyInputIndependentCheckTests(unittest.TestCase):
    def test_all_rows_match(self):
        rows = compare()
        self.assertEqual(len(rows), 33)
        self.assertTrue(all(row["pass"] for row in rows))

    def test_max_delta_is_below_tolerance(self):
        self.assertLessEqual(max(row["max_absolute_delta"] for row in compare()), 1e-12)


if __name__ == "__main__":
    unittest.main()
