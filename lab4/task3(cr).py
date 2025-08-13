def swap_first_last_name():
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    return f"{last_name} {first_name}"

# Example usage:
result = swap_first_last_name()
print("Output:", result)
