import unittest

from src.ListNode import ListNode
from src.in_place.Solution import swap_pair, reverse, reverse_between, reorder_list


def build_list_node(array: list) -> ListNode:
    head = ListNode(-1)
    curr = head
    for r in array:
        curr.next = ListNode(r)
        curr = curr.next

    return head.next


class MyTestCase(unittest.TestCase):

    def compare_heads(self, actual: ListNode, expected: ListNode):
        while actual:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next

    def test_swap_pairs(self):
        head = build_list_node([1, 2, 3, 4, 5, 6, 7, 8])

        expected_head = build_list_node([2, 1, 4, 3, 6, 5, 8, 7])

        swapped_head = swap_pair(head)

        while expected_head:
            self.assertEqual(expected_head.val, swapped_head.val)
            swapped_head = swapped_head.next
            expected_head = expected_head.next

    def test_reverse(self):
        head = build_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        reversed_head = build_list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        res = reverse(head)

        while res:
            self.assertEqual(res.val, reversed_head.val)
            res = res.next
            reversed_head = reversed_head.next

    def test_reverse_between(self):
        head = build_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        reversed_head = build_list_node([1, 2, 10, 9, 8, 7, 6, 5, 4, 3])

        res = reverse_between(head, 3, 10)

        while res:
            self.assertEqual(res.val, reversed_head.val)
            res = res.next
            reversed_head = reversed_head.next

    def test_reorder_list(self):
        head = build_list_node([1,1,2,2,3,-1,10,12])

        expected_head = build_list_node([1,12,1,10,2,-1,2,3])

        reordered_head = reorder_list(head)

        self.compare_heads(expected_head, reordered_head)


if __name__ == '__main__':
    unittest.main()
