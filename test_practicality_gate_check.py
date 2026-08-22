import unittest

from practicality_gate_check import check


class PracticalityGateCheckTests(unittest.TestCase):
    def test_all_matrix_rows_pass_semantic_checks(self):
        rows = check()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row["semantic_checks_pass"] for row in rows))

    def test_conceptual_rows_have_multiple_blocking_gates(self):
        conceptual = [row for row in check() if row["practical_status"] == "conceptual_unresolved"]
        self.assertTrue(all(row["blocking_gate_count"] >= 5 for row in conceptual))


if __name__ == "__main__":
    unittest.main()
