def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
# Example usage:
result = calculator(10, 5, 'add')
print(result)  # Output: 15
result = calculator(10, 5, 'subtract')
print(result)  # Output: 5
result = calculator(10, 5, 'multiply')
print(result)  # Output: 50
result = calculator(10, 5, 'divide')
print(result)  # Output: 2.0
result = calculator(10, 0, 'divide')
print(result)  # Output: Error: Division by zero
result = calculator(10, 5, 'modulus')
print(result)  # Output: Error: Invalid operation