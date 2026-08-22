import unittest

from airport_compatibility_close_read_independent_check import compare


class AirportCompatibilityCloseReadIndependentCheckTests(unittest.TestCase):
    def test_all_summary_metrics_match(self):
        rows = compare()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row["pass"] for row in rows))


if __name__ == "__main__":
    unittest.main()
