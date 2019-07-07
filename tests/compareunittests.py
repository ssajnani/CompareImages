import unittest

class CompareUnitTests(unittest.TestCase):
    valid_file_array = ["../resources/images/test.png", "../resources/images/test2.jpg", "../resources/images/test3.jpg"]
    def compare_two_images_same_images(self):
        self.assertEqual(compare_two_images(valid_file_array[0], valid_file_array[0]), 0.0)

    def compare_two_images_similar_images(self):
        result = compare_two_images(valid_file_array[0], valid_file_array[2]) 
        self.assertTrue(result < 0.5 && result != 0.0 )

    def compare_two_images_different_images(self):
        result = compare_two_images(valid_file_array[0], valid_file_array[1]) 
        self.assertTrue(result > 0.5 && result != 0.0 )

if __name__ == '__main__':
    unittest.main()