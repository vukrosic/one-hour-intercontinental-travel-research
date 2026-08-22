import unittest

from effective_time_sensitivity import calculate, load_rows


class EffectiveTimeSensitivityTests(unittest.TestCase):
    def test_expected_row_count(self):
        self.assertEqual(len(calculate(load_rows())), 12)

    def test_subsonic_reference_is_zero_adjusted_saving(self):
        rows = calculate(load_rows())
        reference = [row for row in rows if row["speed_bin"] == "subsonic_reference"]
        self.assertTrue(all(abs(row["acceleration_adjusted_saved_fraction_vs_subsonic"]) < 1e-12 for row in reference))

    def test_faster_bins_remain_faster_after_acceleration_adjustment(self):
        rows = calculate(load_rows())
        faster = [row for row in rows if row["speed_bin"] != "subsonic_reference"]
        self.assertTrue(all(row["acceleration_adjusted_time_ratio_vs_subsonic"] < 1.0 for row in faster))

    def test_acceleration_adjustment_never_increases_claimed_saving(self):
        rows = calculate(load_rows())
        for row in rows:
            self.assertLessEqual(
                row["acceleration_adjusted_saved_fraction_vs_subsonic"],
                row["speed_only_saved_fraction_vs_subsonic"] + 1e-12,
            )

    def test_saved_fraction_lost_is_nonnegative(self):
        rows = calculate(load_rows())
        self.assertTrue(all(row["saved_fraction_lost_to_acceleration"] >= -1e-12 for row in rows))


if __name__ == "__main__":
    unittest.main()
