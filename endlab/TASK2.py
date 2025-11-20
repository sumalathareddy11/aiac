"""
Merge Sort for Parcel Weights (Logistics Scenario)

This module provides an implementation of Merge Sort, a classic divide-and-conquer algorithm,
to sort millions of parcel weight entries efficiently. Merge Sort is ideal for large datasets due to its O(n log n)
performance, making it suitable for logistics and supply chain applications where quick and reliable sorting is crucial.

Author: AI Assistant
"""

from typing import List

def merge_sort(weights: List[float]) -> List[float]:
    """
    Sorts a list of parcel weights using the Merge Sort algorithm.

    Args:
        weights (List[float]): The unsorted list of parcel weights (can be integers or floats).

    Returns:
        List[float]: A new list containing the sorted parcel weights in ascending order.

    Example:
        >>> merge_sort([2.3, 1.2, 3.8])
        [1.2, 2.3, 3.8]
    """
    if len(weights) <= 1:
        return weights

    mid = len(weights) // 2
    left = merge_sort(weights[:mid])
    right = merge_sort(weights[mid:])

    return _merge(left, right)

def _merge(left: List[float], right: List[float]) -> List[float]:
    """
    Merges two sorted lists into one sorted list.

    Args:
        left (List[float]): First sorted list.
        right (List[float]): Second sorted list.

    Returns:
        List[float]: Merged sorted list.
    """
    merged = []
    i = j = 0

    # Compare elements from both lists and append the smallest
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# -------------------------- #
#       Unit Tests           #
# -------------------------- #

def _test_merge_sort():
    """
    Basic tests for merge_sort to validate correctness.
    """
    print("Running tests for merge_sort...")

    # Test 1: Empty List
    assert merge_sort([]) == []

    # Test 2: Single Element
    assert merge_sort([42.0]) == [42.0]

    # Test 3: Already Sorted
    assert merge_sort([1.1, 2.2, 3.3]) == [1.1, 2.2, 3.3]

    # Test 4: Reverse Order
    assert merge_sort([3, 2, 1]) == [1, 2, 3]

    # Test 5: Large Numbers and Floats
    assert merge_sort([10.5, 1.0, 99999.9, 5.5, 2.1]) == [1.0, 2.1, 5.5, 10.5, 99999.9]

    # Test 6: Duplicate Values
    assert merge_sort([2, 3, 2, 1, 1]) == [1, 1, 2, 2, 3]

    # Test 7: Negative Weights
    assert merge_sort([-1.0, 3.0, 0.0, -5.5, 2.2]) == [-5.5, -1.0, 0.0, 2.2, 3.0]

    # Test 8: Mixed floats and ints
    assert merge_sort([5, 3.2, 4.4, 3.2]) == [3.2, 3.2, 4.4, 5]

    print("All tests passed!")

if __name__ == "__main__":
    # Run tests
    _test_merge_sort()

    # Example usage:
    weights = [45.5, 10.2, 33.0, 4.1, 29.9, 87.3, 20.5]
    print("Original weights:", weights)
    sorted_weights = merge_sort(weights)
    print("Sorted weights:  ", sorted_weights)
