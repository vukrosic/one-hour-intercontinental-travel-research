import unittest

from current_programme_close_read import load_rows, summarize


class CurrentProgrammeCloseReadTests(unittest.TestCase):
    def test_programme_classes_are_explicit(self):
        rows = load_rows()
        self.assertEqual(len(rows), 4)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))
        self.assertEqual(
            {row["program_class"] for row in rows},
            {
                "research_demonstrator",
                "experimental_test_authorization",
                "company_reported_future_airliner",
                "proposed_regulatory_path",
            },
        )

    def test_no_current_passenger_service_or_certification_evidence(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["current_passenger_service_rows"], 0)
        self.assertEqual(summary["passenger_certification_evidence_rows"], 0)
        self.assertEqual(summary["high_speed_practical_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
