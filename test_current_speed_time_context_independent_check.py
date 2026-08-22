import unittest

from current_speed_time_context_independent_check import compare


class CurrentSpeedTimeContextIndependentCheckTests(unittest.TestCase):
    def test_all_summary_metrics_match(self):
        rows = compare()
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(row["pass"] for row in rows))


if __name__ == "__main__":
    unittest.main()
