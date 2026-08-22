import unittest

from claim_replication_summary import load_rows, summarize


class ClaimReplicationTests(unittest.TestCase):
    def test_claim_ids_are_unique(self):
        rows = load_rows()
        ids = [row["claim_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_current_prospective_research_and_general_states_are_present(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["observed_current_rows"], 1)
        self.assertEqual(summary["observed_prospective_rows"], 1)
        self.assertEqual(summary["observed_research_in_progress_rows"], 1)
        self.assertEqual(summary["observed_general_rows"], 1)

    def test_no_practical_pass_is_asserted(self):
        self.assertEqual(summarize(load_rows())["high_speed_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
