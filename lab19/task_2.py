# ...existing code...
def check_number(num):
    """Print whether num is positive, negative, or zero."""
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

def check_number_str(num):
    """Return 'positive', 'negative', or 'zero' for reuse in comparisons."""
    if num > 0:
        return "positive"
    if num < 0:
        return "negative"
    return "zero"

if __name__ == "__main__":
    tests = [10, -3, 0]
    expected = {10: "positive", -3: "negative", 0: "zero"}

    for n in tests:
        print("Calling check_number:")
        check_number(n)                     # prints result
        result = check_number_str(n)        # return value for comparison
        print(f"check_number_str({n}) -> '{result}'", end="; ")
        print("PASS" if result == expected[n] else "FAIL")
        print("-" * 20)
# ...existing code...