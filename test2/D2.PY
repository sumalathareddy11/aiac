import unittest

def normalize(scores):
    """Scales numbers in a list to the range [0, 1].

    Args:
        scores (list of float): List of numbers to normalize.

    Returns:
        list of float: Normalized list with values in [0, 1].

    Examples:
        >>> normalize([2, 4, 6])
        [0.0, 0.5, 1.0]
        >>> normalize([])
        []
        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]
        >>> normalize([-2, 0, 2])
        [0.0, 0.5, 1.0]
        >>> normalize([1.5, 2.5, 3.5])
        [0.0, 0.5, 1.0]
    """
    if not scores:
        return []
    min_val = min(scores)
    max_val = max(scores)
    if min_val == max_val:
        return [0.0 for _ in scores]
    return [(x - min_val) / (max_val - min_val) for x in scores]

class TestNormalize(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(normalize([2, 4, 6]), [0.0, 0.5, 1.0])

    def test_empty_list(self):
        self.assertEqual(normalize([]), [])

    def test_all_equal_values(self):
        self.assertEqual(normalize([5, 5, 5]), [0.0, 0.0, 0.0])

    def test_single_value(self):
        self.assertEqual(normalize([10]), [0.0])

    def test_negatives(self):
        self.assertEqual(normalize([-2, 0, 2]), [0.0, 0.5, 1.0])

    def test_floats(self):
        result = normalize([1.5, 2.5, 3.5])
        expected = [0.0, 0.5, 1.0]
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=9)

if __name__ == "__main__":
    unittest.main(exit=False)
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        scores = [float(x) for x in user_input.strip().split()] if user_input.strip() else []
        print("Normalized:", normalize(scores))
    except Exception as e:
        print("Error:", e)
