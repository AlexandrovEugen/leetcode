import unittest

from graphs.Solution import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_network_delay_time(self):
        res = network_delay_time([[1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5]], 4, 1)

        self.assertEqual(5, res)


    def test_valid_tree(self):

        res = valid_tree(5 , [[0,1],[0,2],[0,3],[0,4],[3,4]])

        self.assertEqual(False, res)


    def test_number_of_paths(self):
        res = number_of_paths(5 , [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]])

        self.assertEqual(2, res)


    def test_find_judge(self):
        res = find_judge(6 , [[1,6],[2,6],[3,6],[4,6],[5,6]])

        self.assertEqual(6,res)

    def test_max_probability(self):
        res = max_probability(4 , [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]] , [0.99917,0.41044,0.28344,0.46291,0.32278,0.42514] , 0 , 3)

        self.assertEqual(0.32251, round(res,5))


if __name__ == '__main__':
    unittest.main()
