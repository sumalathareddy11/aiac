import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_sentences(self):
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("No lemon, no melon", True),
            ("Was it a car or a cat I saw?", True),
            ("Hello, World!", False),
            ("", True),
            ("12321", True),
            ("12345", False),
            ("Eva, can I see bees in a cave?", True),
            ("Not a palindrome", False),
        ]
        for sentence, expected in test_cases:
            with self.subTest(sentence=sentence):
                self.assertEqual(is_sentence_palindrome(sentence), expected)

if __name__ == "__main__":
    unittest.main()