import unittest

from sort_search.Solution import *


class MyTestCase(unittest.TestCase):

    def test_find_best_value(self):
        res = find_best_value([2, 3, 5, 10], 13)

        self.assertEqual(res, 4)



    def test_contains_nearby_duplicates(self):
        nums = [7, 8, 6, 7, 9]

        k = 3

        res = contains_nearby_duplicates(nums, k)

        self.assertEqual(res, True)


    def test_max_count(self):
        nums = [10, 20, 30]
        n = 50
        max_sum = 6

        res = max_count(nums, n, max_sum)

        self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()
