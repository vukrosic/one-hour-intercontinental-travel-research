import unittest

from hash_manifest_check import inspect


class HashManifestTests(unittest.TestCase):
    def test_manifest_is_well_formed_and_registered(self):
        result = inspect()
        self.assertEqual(result["hash_rows"], 4)
        self.assertEqual(result["missing_source_register_ids"], 0)
        self.assertEqual(result["duplicate_source_ids"], 0)
        self.assertEqual(result["invalid_sha256_values"], 0)
        self.assertEqual(result["pass"], 1)


if __name__ == "__main__":
    unittest.main()
