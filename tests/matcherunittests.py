import unittest

class MatcherUnitTests(unittest.TestCase):
    valid_file_array = [""]
    ma = None
    def test_init(self):
        try:
            ma = Matcher('test.pck')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_match(self):
        if (ma != None):
            self.assertEqual(ma.match('../resources/images/test.png'), 'FOO')

if __name__ == '__main__':
    unittest.main()