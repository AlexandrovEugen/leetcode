import unittest

from src.modified_binary_search.Solution import single_non_duplicate, find_closest_elements, binary_search_rotated


class MyTestCase(unittest.TestCase):

    def test_single_non_duplicate(self):
        num = [1, 2, 2, 3, 3, 4, 4, 5, 5]

        self.assertTrue(len(num) % 2 != 0)

        el = single_non_duplicate(num)

        self.assertEqual(el, 1)

    def test_find_closest_elements(self):
        res = find_closest_elements([-29,-11,-3,0,5,10,50,63,198] , 6 , 8)

        self.assertEqual(res, [-29,-11,-3,0,5,10])


    def test_binary_search_rotated(self):

        res = binary_search_rotated([6,7,1,2,3,4,5], 6)

        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
