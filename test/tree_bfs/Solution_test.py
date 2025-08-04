import unittest

from src.tree_bfs.Solution import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_zigzag_level_order(self):

        root = TreeNode(91)
        root.left = TreeNode(-41)
        root.left.left = TreeNode(10)
        root.right = TreeNode(-27)

        arrs = zigzag_level_order(root)

        self.assertEqual(arrs, [[20], [50, 10]])

    def test_populate_next_pointers(self):

        root  = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(25)
        root.left.right = TreeNode(75)
        root.right = TreeNode(20)
        root.right.left = TreeNode(300)
        root.right.right = TreeNode(10)

        node = populate_next_pointers(root)

        self.assertTrue(node is not None)


if __name__ == '__main__':
    unittest.main()
