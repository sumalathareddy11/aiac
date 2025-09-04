import unittest
from task1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe123@domain.co"))
        self.assertTrue(is_valid_email("a_b-c@sub.domain.com"))

    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user@@example.com"))

    def test_missing_dot(self):
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("user@com"))

    def test_invalid_start_end(self):
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))

    def test_invalid_characters(self):
        self.assertFalse(is_valid_email("user!@example.com"))
        self.assertFalse(is_valid_email("user@exa$mple.com"))
        self.assertFalse(is_valid_email("user@exam ple.com"))

if __name__ == "__main__":
    unittest.main()