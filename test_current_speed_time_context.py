import unittest

from current_speed_time_context import calculate, summarize


class CurrentSpeedTimeContextTests(unittest.TestCase):
    def test_current_rows_and_mach_two_comparison_exist(self):
        rows = calculate()
        self.assertEqual(len(rows), 4)
        self.assertEqual(summarize(rows)["current_reference_rows"], 3)
        self.assertEqual(summarize(rows)["mach2_comparison_rows"], 1)

    def test_speed_only_savings_are_monotonic(self):
        rows = calculate()
        savings = [row["speed_only_time_saving_vs_airline_percent"] for row in rows]
        self.assertEqual(savings[0], 0.0)
        self.assertTrue(all(a < b for a, b in zip(savings, savings[1:])))
        self.assertAlmostEqual(savings[1], 8.1081081081081)
        self.assertAlmostEqual(savings[2], 9.0909090909091)
        self.assertAlmostEqual(savings[3], 57.5)


if __name__ == "__main__":
    unittest.main()
