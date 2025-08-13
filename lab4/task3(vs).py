def swap_names():
    full_name = input("Enter first name and last name: ").strip()
    parts = full_name.split()
    if len(parts) != 2:
        return "Please enter exactly two names."
    first_name, last_name = parts
    return f"{last_name} {first_name}"

# Example usage:
result = swap_names()
print(result)