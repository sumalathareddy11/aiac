def min_max_divide_conquer(arr, low, high):
    """
    Return (min_value, max_value) in arr[low:high+1] using divide and conquer.
    """
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    left_min, left_max = min_max_divide_conquer(arr, low, mid)
    right_min, right_max = min_max_divide_conquer(arr, mid + 1, high)
    return (left_min if left_min < right_min else right_min,
            left_max if left_max > right_max else right_max)


if __name__ == "__main__":
    # 12-element test list
    test_list = [3, -1, 45, 7, 0, 23, -10, 99, 12, 8, 8, 50]
    print("List:", test_list)
    minimum, maximum = min_max_divide_conquer(test_list, 0, len(test_list) - 1)
    print("Divide & Conquer -> min:", minimum, "max:", maximum)
    # verify with built-ins
    print("Built-in verification -> min:", min(test_list), "max:", max(test_list))




    