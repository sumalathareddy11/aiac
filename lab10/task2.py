def find_common(a, b):
    return [i for i in a if i in b]
print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))
print(find_common(['apple', 'banana', 'cherry'], ['banana', 'kiwi', 'apple']))