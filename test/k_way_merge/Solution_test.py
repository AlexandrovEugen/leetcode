import unittest
from src.k_way_merge.Solution import k_smallest_pairs, kth_smallest_element


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_k_smallest_pairs(self):
        list1 = [1, 2, 300]
        list2 = [1, 11, 20, 35, 300]
        k = 30

        exp = [[1, 1], [2, 1], [1, 11], [2, 11], [1, 20], [2, 20], [1, 35], [2, 35], [1, 300], [300, 1], [2, 300],
               [300, 11], [300, 20], [300, 35], [300, 300]]

        res = k_smallest_pairs(list1, list2, k)

        self.assertEqual(res, exp)

    def test_kth_smallest_element(self):
        matrix = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
        k = 11

        res = kth_smallest_element(matrix, k)

        self.assertEqual(res,11)

if __name__ == '__main__':
    unittest.main()
