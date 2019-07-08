import unittest, sys, os
sys.path.append('..')
from parse_analyze import *
os.getcwd()
os.chdir('..')

class ParseAnalyzeIntegration(unittest.TestCase):
    def test_default_csv(self):
        print('test_default_test_csv')
        self.assertTrue(parse_analyze_write_back('test.csv'))

    def test_invalid_csv(self):
        print('test_invalid_csv')
        self.assertFalse(parse_analyze_write_back('test3.csv'))
        
    def test_nonexistent_csv(self):
        print('test_nonexistent_csv')
        self.assertFalse(parse_analyze_write_back('test2.csv'))

if __name__ == '__main__':
    unittest.main()
