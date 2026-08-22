import unittest

from passenger_evidence_summary import load_rows, summarize


class PassengerEvidenceSummaryTests(unittest.TestCase):
    def test_table_has_unique_gate_ids(self):
        rows = load_rows()
        ids = [row["gate_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_emergency_crash_limit_is_not_comfort(self):
        rows = load_rows()
        crash = next(row for row in rows if row["gate_id"] == "PE-006")
        self.assertEqual(crash["status"], "supported_not_comfort")

    def test_no_supported_high_speed_comfort_threshold_yet(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["supported_high_speed_comfort_thresholds"], 0)


if __name__ == "__main__":
    unittest.main()
