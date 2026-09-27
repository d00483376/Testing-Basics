import unittest
from challenge import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_capitalization(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("taco cat"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_numbers(self):
        self.assertTrue(is_palindrome("12321"))

    def test_mixed_letters_and_numbers(self):
        self.assertTrue(is_palindrome("A1b2b1A"))


if __name__ == "__main__":
    unittest.main()
