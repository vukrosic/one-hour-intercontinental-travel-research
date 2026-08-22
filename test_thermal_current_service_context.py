import unittest

from thermal_current_service_context import calculate_rows, load_current_speeds, summarize
from thermal_sensitivity import load_inputs


class ThermalCurrentServiceContextTests(unittest.TestCase):
    def test_current_rows_and_mach_two_comparison_are_present(self):
        rows = calculate_rows(load_inputs(), load_current_speeds())
        self.assertEqual(len(rows), 5)
        summary = summarize(rows)
        self.assertEqual(summary["current_reference_rows"], 4)
        self.assertEqual(summary["mach2_comparison_rows"], 1)

    def test_mach_two_lower_bound_exceeds_current_reference_upper_bound(self):
        summary = summarize(calculate_rows(load_inputs(), load_current_speeds()))
        self.assertEqual(summary["mach2_lower_exceeds_highest_current_upper"], 1)
        self.assertGreater(summary["mach2_lower_to_highest_current_upper_ratio"], 1.0)


if __name__ == "__main__":
    unittest.main()
