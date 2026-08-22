import unittest

from economics_close_read import load_rows, summarize


class EconomicsCloseReadTests(unittest.TestCase):
    def test_rows_are_unique_and_nonempty(self):
        rows = load_rows()
        self.assertEqual(len(rows), 4)
        self.assertEqual(len(rows), len({row["entry_id"] for row in rows}))

    def test_historical_and_current_contexts_are_separate(self):
        summary = summarize(load_rows())
        self.assertEqual(summary["quantified_historical_rows"], 1)
        self.assertEqual(summary["current_market_research_rows"], 1)
        self.assertEqual(summary["qualitative_synthesis_rows"], 1)

    def test_no_economic_practical_pass(self):
        self.assertEqual(summarize(load_rows())["economic_pass_rows"], 0)


if __name__ == "__main__":
    unittest.main()
