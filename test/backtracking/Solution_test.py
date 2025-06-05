import unittest

from src.backtracking.Solution import *


def transform_from_array_to_node(nums: list[int]) -> TreeNode:
    def helper(index: int) -> TreeNode:
        if index >= len(nums):
            return None

        root = TreeNode(nums[index])
        root.left = helper(index + 1)
        root.right = helper(index + 2)
        return root

    return helper(0)


class MyTestCase(unittest.TestCase):
    def test_word_search(self):
        grid = [["N", "W", "L", "I", "M"],
                ["V", "I", "L", "Q", "O"],
                ["O", "L", "A", "T", "O"],
                ["R", "T", "A", "I", "N"],
                ["O", "I", "T", "N", "C"]]

        word = "LATIN"

        found = word_search(grid, word)

        self.assertTrue(found)

    # def test_rob(self):
    #     root = transform_from_array_to_node([9, 7, 11, 1, 8, 10, 12])


    def test_restore_ip_addresses(self):
        s = "113242124"

        result = restore_ip_addresses(s)

        self.assertEqual(len(result), 10)


if __name__ == '__main__':
    unittest.main()
