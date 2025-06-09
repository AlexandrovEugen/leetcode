import unittest

from dynamic_programming.Solution import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_count_palindromic_substrings(self):
        res = count_palindromic_substrings("topot")

        self.assertEqual(res, 24)

    def test_coin_change(self):
        res = coin_change([2, 3, 4, 6, 8], 23)

        self.assertEqual(res, 4)

    def test_can_partition_array(self):
        res = can_partition_array([4, 1, 3])

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
