import unittest

class FeatureExtractionUnitTests(unittest.TestCase):

    def test_extract_features_valid_file(self):
        valid_path = ""
        self.assertEqual(extract_features(valid_file), 'FOO')

    def test_extract_features_invalid_file(self):
        invalid_path = "asdasd"
        self.assertEqual(extract_features(valid_file), None)

    def test_batch_extractor_single_file(self):
        valid_file_array = [""]
        self.assertEqual(batch_extractor(valid_file_array), 'FOO')

if __name__ == '__main__':
    unittest.main()