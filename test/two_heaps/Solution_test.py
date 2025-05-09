import unittest

from two_heaps.Solution import most_booked


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_most_booked(self):
        meetings = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15]]
        rooms = 3
        most_booked_room = most_booked(meetings, rooms)

        self.assertEqual(most_booked_room, 0)

        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        rooms = 2

        most_booked_room = most_booked(meetings, rooms)

        self.assertEqual(most_booked_room, 0)

if __name__ == '__main__':
    unittest.main()
