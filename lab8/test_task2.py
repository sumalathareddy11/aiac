import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):

    def test_valid_scores(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(59.9), "F")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(100), "A")

    def test_invalid_type(self):
        self.assertEqual(assign_grade("abc"), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade(None), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade([90]), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade({}), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade((90,)), "Invalid input: score must be a number.")

    def test_out_of_range(self):
        self.assertEqual(assign_grade(-1), "Invalid input: score must be between 0 and 100.")
        self.assertEqual(assign_grade(101), "Invalid input: score must be between 0 and 100.")
        self.assertEqual(assign_grade(100.1), "Invalid input: score must be between 0 and 100.")
        self.assertEqual(assign_grade(-100), "Invalid input: score must be between 0 and 100.")

    def test_boundary_values(self):
        self.assertEqual(assign_grade(89.99), "B")
        self.assertEqual(assign_grade(79.99), "C")
        self.assertEqual(assign_grade(69.99), "D")
        self.assertEqual(assign_grade(59.99), "F")
        self.assertEqual(assign_grade(99.99), "A")

    def test_float_and_int_equivalence(self):
        self.assertEqual(assign_grade(80.0), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(60.0), "D")
        self.assertEqual(assign_grade(60), "D")

if __name__ == "__main__":
    unittest.main()