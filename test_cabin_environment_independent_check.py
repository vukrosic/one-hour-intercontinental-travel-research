import unittest

from cabin_environment_independent_check import compare


class CabinEnvironmentIndependentCheckTests(unittest.TestCase):
    def test_all_summary_metrics_match(self):
        rows = compare()
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(row["pass"] for row in rows))


if __name__ == "__main__":
    unittest.main()
