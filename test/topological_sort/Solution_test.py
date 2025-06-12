import unittest

from topological_sort.Solution import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_find_recipes(self):
        res = find_recipes(["pasta", "egg", "chicken"],
                           [["yeast", "flour"], ["pasta", "meat"], ["egg", "meat", "pasta"]],
                           ["yeast", "flour", "meat"])

        self.assertEqual(res, ["pasta", "egg", "chicken"])

    def test_find_order(self):
        res = find_order(10 , [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]])

        self.assertEqual([i for i in range(10)], res)

    def test_can_finish(self):
        res = can_finish(2, [[1,0],[0,1]])

        self.assertFalse(res)

        res = can_finish(5, [[1,0],[2,1],[3,2],[4,3]])

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
