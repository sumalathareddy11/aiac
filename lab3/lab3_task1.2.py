def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num} is {factorial_recursive(num)}")
    except ValueError as e:
        print("Invalid input:", e)
