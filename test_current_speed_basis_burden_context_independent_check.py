import unittest

from current_speed_basis_burden_context_independent_check import compare


class CurrentSpeedBasisBurdenContextIndependentCheckTests(unittest.TestCase):
    def test_all_summary_metrics_match(self):
        rows = compare()
        self.assertEqual(len(rows), 9)
        self.assertTrue(all(row["pass"] for row in rows))


if __name__ == "__main__":
    unittest.main()
