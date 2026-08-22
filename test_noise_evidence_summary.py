import unittest

from noise_evidence_summary import load_rows, summarize


class NoiseEvidenceSummaryTests(unittest.TestCase):
    def test_gate_ids_are_unique(self):
        rows = load_rows()
        ids = [row["gate_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_proposal_is_not_counted_as_final(self):
        rows = load_rows()
        proposed = next(row for row in rows if row["gate_id"] == "NE-002")
        self.assertEqual(proposed["evidence_state"], "proposed_not_final")
        self.assertEqual(summarize(rows)["final_high_speed_pass_threshold_rows"], 0)

    def test_current_binding_constraint_is_present(self):
        self.assertGreaterEqual(summarize(load_rows())["current_binding_rows"], 1)


if __name__ == "__main__":
    unittest.main()
