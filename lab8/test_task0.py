import unittest
from task0 import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(10, 5, 'add'), 15)
        self.assertEqual(calculator(-2, 3, 'add'), 1)

    def test_subtract(self):
        self.assertEqual(calculator(10, 5, 'subtract'), 5)
        self.assertEqual(calculator(5, 10, 'subtract'), -5)

    def test_multiply(self):
        self.assertEqual(calculator(10, 5, 'multiply'), 50)
        self.assertEqual(calculator(0, 100, 'multiply'), 0)

    def test_divide(self):
        self.assertEqual(calculator(10, 5, 'divide'), 2.0)
        self.assertEqual(calculator(9, 3, 'divide'), 3.0)

    def test_divide_by_zero(self):
        self.assertEqual(calculator(10, 0, 'divide'), "Error: Division by zero")

    def test_invalid_operation(self):
        self.assertEqual(calculator(10, 5, 'modulus'), "Error: Invalid operation")
        self.assertEqual(calculator(10, 5, 'power'), "Error: Invalid operation")

if __name__ == "__main__":
    unittest.main()