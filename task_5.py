def string_frequency_from_input():
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage:
frequencies = string_frequency_from_input()
print(frequencies)