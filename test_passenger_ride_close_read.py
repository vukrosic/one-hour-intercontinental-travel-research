import unittest

from passenger_ride_close_read import load_rows, summarize


class PassengerRideCloseReadTests(unittest.TestCase):
    def test_rows_are_unique_and_nonempty(self):
        rows = load_rows()
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))
        self.assertEqual(len(rows), 6)

    def test_frequency_and_multi_factor_evidence_are_recorded(self):
        summary = summarize(load_rows())
        self.assertGreaterEqual(summary["frequency_explicit_rows"], 2)
        self.assertGreaterEqual(summary["multi_factor_rows"], 2)

    def test_no_speed_specific_threshold_or_practical_pass(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["speed_specific_threshold_rows"], 0)
        self.assertEqual(summary["high_speed_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
