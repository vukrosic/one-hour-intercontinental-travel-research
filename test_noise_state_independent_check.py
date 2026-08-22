import unittest

from noise_state_independent_check import compare


class NoiseStateIndependentCheckTests(unittest.TestCase):
    def test_all_state_metrics_match(self):
        rows = compare()
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(row["pass"] for row in rows))


if __name__ == "__main__":
    unittest.main()
