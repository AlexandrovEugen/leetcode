import unittest

from two_heaps.Solution import most_booked, minimum_machines, connect_sticks


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


    def test_minimum_machines(self):

        tasks = [[1,3],[3,5],[5,9],[9,12],[12,13],[13,16],[16,17]]

        min_mach = minimum_machines(tasks)

        self.assertEqual(1, min_mach)

    def test_connect_sticks(self):
        sticks = [1,10,3,3,3]

        cost = connect_sticks(sticks)

        self.assertEqual(cost, 40)


if __name__ == '__main__':
    unittest.main()
