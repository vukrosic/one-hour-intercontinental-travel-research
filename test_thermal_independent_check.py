import unittest

from thermal_independent_check import compare


class ThermalIndependentCheckTests(unittest.TestCase):
    def test_all_reference_rows_match(self):
        rows = compare()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row["pass"] for row in rows))

    def test_deltas_are_below_tolerance(self):
        self.assertLessEqual(max(row["max_absolute_delta"] for row in compare()), 1e-12)


if __name__ == "__main__":
    unittest.main()
