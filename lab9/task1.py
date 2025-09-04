def sum_even_odd():
    # This function prompts the user to enter a sequence of integers separated by spaces.
    # It then calculates and returns the sum of even and odd numbers from the input.
    """
    Calculates the sum of even and odd numbers from user input.
    Prompts the user to enter a sequence of integers separated by spaces,
    then computes and returns the sum of even numbers and the sum of odd numbers.
    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.
    """
    # Take input from user
    # Take input from user and convert it to a list of integers
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    even_sum = 0  # Initialize sum for even numbers
    odd_sum = 0   # Initialize sum for odd numbers
    
    for num in numbers:  # Iterate through each number in the list
        if num % 2 == 0:  # Check if the number is even
            even_sum += num  # Add even number to even_sum
        else:  # If the number is odd
            odd_sum += num  # Add odd number to odd_sum
    
    return even_sum, odd_sum  # Return the sums as a tuple


# Call the function
even_total, odd_total = sum_even_odd()
print("Sum of even numbers:", even_total)
print("Sum of odd numbers:", odd_total)
