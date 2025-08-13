def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Example usage
input_str = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_str))