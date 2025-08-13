def centimeters_to_inches():
    try:
        cm = float(input("Enter value in centimeters: "))
        inches = cm / 2.54
        print(f"{cm} centimeters is {inches:.3f} inches")
    except ValueError:
        print("Please enter a valid number.")

# Example usage
centimeters_to_inches()