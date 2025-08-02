import unittest

from src.tree_dfs.Solution import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def test_build_tree(self):
        p_order = [3, 9, 20, 15, 7]
        i_order = [9, 3, 15, 20, 7]

        root = build_tree(p_order, i_order)

        




if __name__ == '__main__':
    unittest.main()
