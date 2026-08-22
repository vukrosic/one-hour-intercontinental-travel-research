import unittest

from airport_compatibility_summary import load_rows, summarize


class AirportCompatibilitySummaryTests(unittest.TestCase):
    def test_gate_ids_are_unique(self):
        rows = load_rows()
        ids = [row["gate_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_historical_evidence_is_not_generic_pass(self):
        historical = next(row for row in load_rows() if row["gate_id"] == "AC-001")
        self.assertEqual(historical["current_generic_pass"], "historical_only")

    def test_no_current_generic_high_speed_pass(self):
        self.assertEqual(summarize(load_rows())["current_generic_high_speed_pass_rows"], 0)

    def test_candidate_characteristics_are_required_for_multiple_gates(self):
        self.assertGreaterEqual(summarize(load_rows())["rows_requiring_candidate_characteristics"], 4)


if __name__ == "__main__":
    unittest.main()
