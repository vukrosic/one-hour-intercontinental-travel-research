import unittest

from speed_tradeoff import tradeoff_rows


class SpeedTradeoffTests(unittest.TestCase):
    def test_reference_has_no_time_saving(self):
        first = tradeoff_rows()[0]
        self.assertAlmostEqual(first[1], 1.0)
        self.assertAlmostEqual(first[2], 0.0)

    def test_time_decreases_and_burdens_increase(self):
        rows = tradeoff_rows()
        self.assertTrue(all(a[1] > b[1] for a, b in zip(rows, rows[1:])))
        self.assertTrue(all(a[3] < b[3] for a, b in zip(rows, rows[1:])))
        self.assertTrue(all(a[4] < b[4] for a, b in zip(rows, rows[1:])))

    def test_marginal_ke_efficiency_declines(self):
        efficiencies = [row[5] for row in tradeoff_rows()[1:]]
        self.assertTrue(all(a > b for a, b in zip(efficiencies, efficiencies[1:])))


if __name__ == "__main__":
    unittest.main()
