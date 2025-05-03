import unittest

from src.two_pointers.ListNode import ListNode
from src.two_pointers.Solution import sort_colors, find_duplicate, circular_array_loop, count_cycle_length, \
    remove_duplicates, length_of_longest_substring, character_replacement, find_repeated_dna_sequences, least_interval, \
    insert_interval


class MyTestCase(unittest.TestCase):

    def test_sort_colors(self):
        sorted_colors = sort_colors([2, 1, 1, 0, 0])
        expected_sorted_colors = [0, 0, 1, 1, 2]
        for i in range(0, len(sorted_colors)):
            self.assertEqual(sorted_colors[i], expected_sorted_colors[i])  # add assertion here

    def test_find_duplicate(self):
        dup = find_duplicate([1, 3, 6, 2, 7, 3, 5, 4])
        expected_dup = 3
        self.assertEqual(dup, expected_dup)

    def test_circular_array_loop(self):
        nums = [3, 1, 2]

        hasCycle = circular_array_loop(nums)

        self.assertEqual(hasCycle, True)

    def test_linked_list_cycle3(self):
        head = ListNode(1)
        n = ListNode(2)
        n1 = ListNode(3)
        n2 = ListNode(4)
        n3 = ListNode(5)
        n4 = ListNode(6)
        n5 = ListNode(7)
        n6 = ListNode(8)

        head.next = n
        n.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n

        length = count_cycle_length(head)

        self.assertEqual(length, 7)

    def test_remove_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)

        expected_nums = [0, 1, 2, 3, 4, 5]

        self.assertEqual(k, 5)

        for i in range(0, k):
            self.assertEqual(nums[i], expected_nums[i])


    def test_length_of_longest_substring(self):
        s = "abcabcbb"

        res = length_of_longest_substring(self, s)

        self.assertEqual(res, 3)

    def test_character_replacement(self):

        s = "ABAB"
        k = 2

        res = character_replacement(self, s, k)

        self.assertEqual(res, 4)

    def test_find_repeated_dna_sequences(self):

        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

        res = find_repeated_dna_sequences(s)

        self.assertListEqual(res, ['AAAAACCCCC', 'CCCCCAAAAA'])

    def test_least_interval(self):

        res = least_interval(["S","I","V","U","W","D","U","X"], 0)

        self.assertEqual(res, 8)

    def test_insert_interval(self):

        res = insert_interval([[1, 3], [4, 5], [6, 9], [10, 17], [18, 21]], [4, 16])

        self.assertEqual(res, [[1, 3], [4, 17], [18, 21]])


if __name__ == '__main__':
    unittest.main()
