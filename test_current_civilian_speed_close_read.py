import unittest

from current_civilian_speed_close_read import load_rows, summarize


class CurrentCivilianSpeedCloseReadTests(unittest.TestCase):
    def test_service_and_marketing_states_are_separate(self):
        rows = load_rows()
        self.assertEqual(len(rows), 3)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))
        summary = summarize(rows)
        self.assertEqual(summary["current_airline_service_rows"], 1)
        self.assertEqual(summary["current_certified_business_aviation_rows"], 2)
        self.assertEqual(summary["manufacturer_only_rows"], 0)

    def test_service_frontier_does_not_include_marketed_claim(self):
        summary = summarize(load_rows())
        self.assertAlmostEqual(summary["highest_published_subsonic_mach"], 0.935)
        self.assertAlmostEqual(summary["highest_service_anchored_mach"], 0.935)
        self.assertEqual(summary["speed_frontier_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
