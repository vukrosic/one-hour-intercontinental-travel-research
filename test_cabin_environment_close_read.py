import unittest

from cabin_environment_close_read import load_rows, summarize


class CabinEnvironmentCloseReadTests(unittest.TestCase):
    def test_rows_are_unique(self):
        rows = load_rows()
        self.assertEqual(len(rows), 6)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))

    def test_normal_and_failure_evidence_are_separate(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["normal_certification_rows"], 2)
        self.assertEqual(summary["failure_or_emergency_rows"], 3)
        self.assertEqual(summary["partial_qualitative_rows"], 1)

    def test_no_high_speed_serviceability_pass(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["high_speed_specific_rows"], 0)
        self.assertEqual(summary["comfort_threshold_rows"], 0)
        self.assertEqual(summary["high_speed_serviceability_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
