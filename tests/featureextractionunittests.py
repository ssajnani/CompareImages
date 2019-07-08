import unittest, sys
sys.path.append('..')
from analysis.feature_extractor import *
import os, os.path
class FeatureExtractionUnitTests(unittest.TestCase):

    def test_extract_features_valid_file(self):
        valid_path = "../resources/images/test.png"
        print('Test extract_features on a valid file')
        self.assertEqual(str(type(extract_features(valid_path))), "<class 'numpy.ndarray'>")

    def test_extract_features_invalid_file(self):
        invalid_path = "asdasd"
        print('Test extract_features on a invalid path')
        self.assertEqual(extract_features(invalid_path), None)


if __name__ == '__main__':
    unittest.main()
