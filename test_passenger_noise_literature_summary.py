import unittest

from passenger_noise_literature_summary import load_rows, summarize


class PassengerNoiseLiteratureTests(unittest.TestCase):
    def test_entry_ids_are_unique(self):
        rows = load_rows()
        ids = [row["entry_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_map_contains_multiple_evidence_contexts(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["literature_rows"], 6)
        self.assertGreaterEqual(summary["passenger_ride_rows"], 3)
        self.assertGreaterEqual(summary["noise_rows"], 2)
        self.assertGreaterEqual(summary["certification_context_rows"], 1)

    def test_no_high_speed_practical_pass_is_asserted(self):
        self.assertEqual(summarize(load_rows())["high_speed_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
