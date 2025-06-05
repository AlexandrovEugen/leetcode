import unittest

from src.greedy_techniques.Solution import jump_game, jump_game_two


class MyTestCase(unittest.TestCase):

    def test_jump_game(self):
        nums = [3, 2, 2, 0, 1, 4]

        res = jump_game(nums)

        self.assertTrue(res)

    def test_jump_game_two(self):
        nums = [3, 2, 2, 0, 1, 4]

        res = jump_game_two(nums)

        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
