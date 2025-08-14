# Take input from the user as a list of integers
input_list = input("Enter a list of integers separated by commas: ")
# Convert input string to a list of integers
numbers = [int(x.strip()) for x in input_list.split(',') if x.strip().isdigit()]
# Remove duplicates using set and sort the list
unique_sorted_numbers = sorted(set(numbers))
# Print the result
print("Output list:", unique_sorted_numbers)