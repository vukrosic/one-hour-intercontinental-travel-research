import unittest

from practicality_summary import load_rows, summarize


class PracticalitySummaryTests(unittest.TestCase):
    def test_speed_bins_are_unique(self):
        rows = load_rows()
        bins = [row["speed_bin"] for row in rows]
        self.assertEqual(len(bins), len(set(bins)))

    def test_no_class_receives_a_practical_pass(self):
        self.assertEqual(summarize(load_rows())["current_practical_pass_rows"], 0)

    def test_mach_two_energy_gate_is_explicitly_contradicted(self):
        mach_two = next(row for row in load_rows() if row["speed_bin"] == "Concorde_historical")
        self.assertEqual(mach_two["energy_climate"], "contradicted_vs_modern_benchmark")

    def test_conceptual_bins_have_no_service_anchor(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["classes_with_no_service_anchor"], 2)


if __name__ == "__main__":
    unittest.main()
