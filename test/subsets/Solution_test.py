import unittest
from src.subsets.Solution import permute_word

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_permuted_word(self):

        word = "abcd"

        result = permute_word(word)

        expected_result = ["abcd","abdc","acbd","acdb","adbc","adcb","bacd","badc","bcad","bcda","bdac","bdca","cabd","cadb","cbad","cbda","cdab","cdba","dabc","dacb","dbac","dbca","dcab","dcba"]

        self.assertSequenceEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
