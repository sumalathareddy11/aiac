# Python program to calculate electricity (power) bill

def calculate_bill(previous_units, present_units, purpose):
    if present_units < previous_units:
        raise ValueError("Present units cannot be less than previous units.")
    units_consumed = present_units - previous_units

    # Set rate per unit based on purpose
    if purpose.lower() == "domestic":
        rate = 5.0  # Example rate per unit for domestic
    elif purpose.lower() == "industrial":
        rate = 8.0  # Example rate per unit for industrial
    else:
        raise ValueError("Invalid purpose. Please enter 'Domestic' or 'Industrial'.")

    bill_amount = units_consumed * rate
    return units_consumed, rate, bill_amount

def main():
    print("Electricity Bill Calculator")
    house_number = input("Enter your house number: ")
    try:
        previous_units = int(input("Enter previous meter reading (units): "))
        present_units = int(input("Enter present meter reading (units): "))
        purpose = input("Enter purpose (Domestic/Industrial): ")

        print("\n--- Bill Calculation Steps ---")
        print(f"House Number: {house_number}")
        print(f"Previous Units: {previous_units}")
        print(f"Present Units: {present_units}")
        units_consumed, rate, bill_amount = calculate_bill(previous_units, present_units, purpose)
        print(f"Units Consumed: {units_consumed}")
        print(f"Purpose: {purpose.capitalize()}")
        print(f"Rate per Unit: Rs. {rate:.2f}")
        print(f"Total Bill Amount: Rs. {bill_amount:.2f}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
