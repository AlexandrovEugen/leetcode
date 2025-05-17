import unittest
from src.subsets.Solution import permute_word, generate_combinations, letter_combinations


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_permuted_word(self):
        word = "abcd"

        result = permute_word(word)

        expected_result = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac",
                           "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca",
                           "dcab", "dcba"]

        self.assertSequenceEqual(sorted(result), sorted(expected_result))

    def test_generate_combinations(self):
        n = 3

        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]

        result = generate_combinations(n)

        self.assertSequenceEqual(sorted(expected), sorted(result))

    def test_letter_combinations(self):
        result = letter_combinations("2")

        expected = ["a", "b", "c"]

        self.assertSequenceEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
