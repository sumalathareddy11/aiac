operation = "multiply"
a, b = 5, 3

# Repetitive if-elif approach (not scalable)
if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
else:
    result = None
print(result)

# Clean approach using dictionary mapping
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

result = operations.get(operation, lambda x, y: None)(a, b)
print(result)
