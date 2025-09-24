def square_numbers(numbers):
    return [n * n for n in numbers]

nums = [1,2,3,4,5,6,7,8,9,10]
squares = square_numbers(nums)
print("Squares of all numbers:", squares)
even_squares = [n * n for n in nums if n % 2 == 0]
print("Even squares:", even_squares)