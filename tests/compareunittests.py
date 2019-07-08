import unittest, sys
sys.path.append('..')
from analysis.compare import *

class CompareUnitTests(unittest.TestCase):
    valid_file_array = ["../resources/images/test.png", "../resources/images/test2.jpg", "../resources/images/test3.jpg"]
    def test_compare_two_images_same_images(self):
        print('test_compare_two_images_same_images')
        self.assertEqual(compare_two_images(self.valid_file_array[0], self.valid_file_array[0]), 0.0)

    def test_compare_two_images_similar_images(self):
        print('test_compare_two_images_similar_images')
        result = compare_two_images(self.valid_file_array[0], self.valid_file_array[2]) 
        self.assertTrue(result < 0.5 and result != 0.0 )

    def test_compare_two_images_different_images(self):
        print('test_compare_two_images_different_images')
        result = compare_two_images(self.valid_file_array[0], self.valid_file_array[1]) 
        self.assertTrue(result > 0.5 and result != 0.0 )

if __name__ == '__main__':
    unittest.main()
