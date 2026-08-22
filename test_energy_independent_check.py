import unittest

from energy_independent_check import compare


class EnergyIndependentCheckTests(unittest.TestCase):
    def test_all_reference_rows_match(self):
        rows = compare()
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(row["pass"] for row in rows))

    def test_deltas_are_below_tolerance(self):
        self.assertLessEqual(max(row["max_absolute_delta"] for row in compare()), 1e-9)


if __name__ == "__main__":
    unittest.main()
