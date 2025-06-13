import unittest

from sort_search.Solution import *

class MyTestCase(unittest.TestCase):

    def test_find_best_value(self):
        res=find_best_value([2,3,5,10] , 13)

        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
