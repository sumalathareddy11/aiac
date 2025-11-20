import unittest
from TASK2 import merge_sort

"""
Unit tests for TASK2.py - Merge Sort implementation
"""



class TestMergeSort(unittest.TestCase):
    """Test cases for the merge_sort function"""

    def test_empty_list(self):
        """Test sorting an empty list"""
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        """Test sorting a single element"""
        self.assertEqual(merge_sort([42.0]), [42.0])

    def test_already_sorted(self):
        """Test sorting an already sorted list"""
        self.assertEqual(merge_sort([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])

    def test_reverse_order(self):
        """Test sorting a reverse-ordered list"""
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

    def test_large_numbers_and_floats(self):
        """Test sorting with large numbers and floats"""
        self.assertEqual(
            merge_sort([10.5, 1.0, 99999.9, 5.5, 2.1]),
            [1.0, 2.1, 5.5, 10.5, 99999.9]
        )

    def test_duplicate_values(self):
        """Test sorting with duplicate values"""
        self.assertEqual(merge_sort([2, 3, 2, 1, 1]), [1, 1, 2, 2, 3])

    def test_negative_weights(self):
        """Test sorting with negative values"""
        self.assertEqual(
            merge_sort([-1.0, 3.0, 0.0, -5.5, 2.2]),
            [-5.5, -1.0, 0.0, 2.2, 3.0]
        )

    def test_mixed_floats_and_ints(self):
        """Test sorting with mixed float and int types"""
        self.assertEqual(merge_sort([5, 3.2, 4.4, 3.2]), [3.2, 3.2, 4.4, 5])

    def test_real_world_parcel_weights(self):
        """Test with realistic parcel weight scenario"""
        weights = [45.5, 10.2, 33.0, 4.1, 29.9, 87.3, 20.5]
        expected = [4.1, 10.2, 20.5, 29.9, 33.0, 45.5, 87.3]
        self.assertEqual(merge_sort(weights), expected)


if __name__ == "__main__":
    unittest.main()