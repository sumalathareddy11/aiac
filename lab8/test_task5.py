import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(convert_date_format("2024-06-01"), "01-06-2024")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("0001-01-01"), "01-01-0001")

    def test_invalid_format_missing_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2024-06")
        with self.assertRaises(ValueError):
            convert_date_format("2024")
        with self.assertRaises(ValueError):
            convert_date_format("2024-06-01-02")

    def test_invalid_format_wrong_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("2024/06/01")
        with self.assertRaises(ValueError):
            convert_date_format("2024.06.01")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

if __name__ == "__main__":
    unittest.main()