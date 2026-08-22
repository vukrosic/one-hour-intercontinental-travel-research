import unittest

from evidence_refresh_summary import load_rows, summarize


class EvidenceRefreshSummaryTests(unittest.TestCase):
    def test_audit_ids_are_unique(self):
        rows = load_rows()
        ids = [row["audit_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_refresh_contains_current_prospective_and_research_states(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["supported_current_rows"], 1)
        self.assertEqual(summary["prospective_policy_rows"], 1)
        self.assertEqual(summary["research_in_progress_rows"], 1)

    def test_no_high_speed_practical_pass_is_asserted(self):
        self.assertEqual(summarize(load_rows())["high_speed_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
