import unittest

from source_integrity_check import inspect


class SourceIntegrityTests(unittest.TestCase):
    def test_source_register_has_clean_record_hygiene(self):
        result = inspect()
        self.assertEqual(result["duplicate_source_ids"], 0)
        self.assertEqual(result["blank_required_fields"], 0)
        self.assertEqual(result["invalid_urls"], 0)
        self.assertEqual(result["invalid_access_dates"], 0)
        self.assertEqual(result["pass"], 1)


if __name__ == "__main__":
    unittest.main()
