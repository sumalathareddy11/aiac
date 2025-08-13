def centimeters_to_inches(cm):
    return round(cm / 2.54, 2)

def main():
    try:
        cm = float(input("centimeters to inches("))
        result = centimeters_to_inches(cm)
        print(f"Output:{result}")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()
