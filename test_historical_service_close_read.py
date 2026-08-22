import unittest

from historical_service_close_read import load_rows, summarize


class HistoricalServiceCloseReadTests(unittest.TestCase):
    def test_rows_and_service_states_are_unique(self):
        rows = load_rows()
        self.assertEqual(len(rows), 3)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))
        self.assertEqual(
            {row["service_state"] for row in rows},
            {
                "scheduled_passenger_service",
                "limited_airline_passenger_service",
                "research_only_follow_on",
            },
        )

    def test_mach_two_is_the_only_anchored_speed_class(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["historical_service_anchor_rows"], 2)
        self.assertEqual(summary["historical_service_anchor_speed_classes"], 1)
        self.assertEqual(summary["current_service_rows"], 0)

    def test_no_current_practical_pass(self):
        self.assertEqual(summarize(load_rows())["current_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
