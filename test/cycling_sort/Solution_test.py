import unittest

from cycling_sort.Solution import *


class MyTestCase(unittest.TestCase):

    def test_find_corrupt_pair(self):

        missing, duplicated = find_corrupt_pair([3,1,2,3,6,4])


        self.assertEqual(missing, 5)
        self.assertEqual(duplicated, 3)



if __name__ == '__main__':
    unittest.main()
