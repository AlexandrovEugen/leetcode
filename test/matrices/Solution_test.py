import unittest

from matrices.Solution import *


class MyTestCase(unittest.TestCase):

    def test_spiral_order(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

        res = spiral_order(matrix)

        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_rotate_image(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        res = rotate_image(matrix)

        self.assertEqual(
            [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4],
            ], res)

    def test_find_exit_column(self):
        grid = [
            [1,1,1,1,1,1],
            [-1,-1,-1,-1,-1,-1],
            [1,1,1,1,1,1],
            [-1,-1,-1,-1,-1,-1]
        ]

        res = find_exist_column(grid)

        self.assertEqual([0,1,2,3,4,-1], res)



if __name__ == '__main__':
    unittest.main()
