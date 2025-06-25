import unittest

from stack.NestedIterator import NestedIterator
from stack.Solution import *


class MyTestCase(unittest.TestCase):

    def test_min_remove_parentheses(self):
        s = "m)no(q)rs("

        res = min_remove_parentheses(s)

        self.assertEqual("mno(q)rs", res)

    def test_nested_iterator(self):
        nested_list = [[1], [2], [3, [4, [5], 6], [7], 8], [9, 10]]

        itt = NestedIterator(nested_list)

        result = []

        while itt.has_next():
            result.append(itt.next())

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], result)

    def test_exclusive_time(self):
        logs = ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"]
        n = 3
        res = exclusive_time(n, logs)

        self.assertEqual([1, 1, 2], res)

        logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
        n = 1
        res = exclusive_time(n, logs)

        self.assertEqual([8], res)


if __name__ == '__main__':
    unittest.main()
