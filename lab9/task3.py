def add(a, b):  # Function to add two numbers
    return a + b  # Return the sum
def subtract(a, b):  # Function to subtract two numbers
    return a - b  # Return the difference
def multiply(a, b):  # Function to multiply two numbers
    return a * b  # Return the product
def divide(a, b):  # Function to divide two numbers
    if b == 0:  # Check for division by zero
        return "Error! Division by zero."  # Return error message if denominator is zero
    return a / b  # Return the quotient
def calculator():  # Main calculator function
    """
    A simple interactive calculator function that allows the user to perform basic arithmetic operations:
    addition, subtraction, multiplication, and division. The user is prompted to select an operation and
    enter two numbers. The calculator continues to run until the user chooses to exit.

    Operations:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit

    Prompts the user for input and displays the result of the selected operation.
    """
    while True:  # Infinite loop to keep the calculator running
        print("\n--- Simple Calculator ---")  # Print calculator menu header
        print("1. Add")  # Print option for addition
        print("2. Subtract")  # Print option for subtraction
        print("3. Multiply")  # Print option for multiplication
        print("4. Divide")  # Print option for division
        print("5. Exit")  # Print option to exit
        choice = input("Enter choice (1-5): ")  # Get user's choice
        if choice == '5':  # If user chooses to exit
            print("Exiting Calculator. Goodbye!")  # Print exit message
            break  # Break the loop to exit
        a = float(input("Enter first number: "))  # Get first number from user
        b = float(input("Enter second number: "))  # Get second number from user
        if choice == '1':  # If user chose addition
            print("Result:", add(a, b))  # Print result of addition
        elif choice == '2':  # If user chose subtraction
            print("Result:", subtract(a, b))  # Print result of subtraction
        elif choice == '3':  # If user chose multiplication
            print("Result:", multiply(a, b))  # Print result of multiplication
        elif choice == '4':  # If user chose division
            print("Result:", divide(a, b))  # Print result of division
        else:  # If user entered an invalid choice
            print("Invalid choice! Please try again.")  # Print error message
calculator()  # Call the calculator function to start the program
