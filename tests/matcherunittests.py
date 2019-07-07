import unittest, sys
sys.path.append('..')
from analysis.matcher import Matcher

class MatcherUnitTests(unittest.TestCase):
    valid_file_array = [""]
    ma = None
    def test_init(self):
        print('Test initialization of matcher')
        try:
            self.ma = Matcher('test.pck')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_match(self):
        print('Test matching capabilities of matcher')
        self.ma = Matcher('test.pck')
        match_result = self.ma.match('../resources/images/test.png')[1][0]
        self.assertTrue(match_result < 0.5 and match_result > 0.3)

if __name__ == '__main__':
    unittest.main()
