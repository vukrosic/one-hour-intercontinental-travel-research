import unittest

from noise_state_guard import load_rows, semantic_errors, summarize


class NoiseStateGuardTests(unittest.TestCase):
    def test_current_table_has_no_semantic_errors(self):
        self.assertEqual(semantic_errors(load_rows()), [])

    def test_current_table_has_no_practical_pass(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["final_high_speed_pass_rows"], 0)
        self.assertEqual(summary["semantic_error_count"], 0)
        self.assertEqual(summary["certified_subsonic_aircraft_record_rows"], 1)

    def test_proposal_cannot_be_a_pass(self):
        rows = load_rows()
        rows[1]["high_speed_practical_pass"] = "yes"
        self.assertTrue(any("non-final state marked pass" in error for error in semantic_errors(rows)))

    def test_research_program_cannot_be_a_pass(self):
        rows = load_rows()
        research = next(row for row in rows if row["evidence_state"] == "empirical_program_in_progress")
        research["high_speed_practical_pass"] = "yes"
        self.assertTrue(any("non-final state marked pass" in error for error in semantic_errors(rows)))


if __name__ == "__main__":
    unittest.main()
