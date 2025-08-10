def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value (float): The temperature value to convert.
        from_unit (str): The unit of the input temperature ('C', 'F', or 'K').
        to_unit (str): The unit to convert to ('C', 'F', or 'K').

    Returns:
        float: The converted temperature value.
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert input to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit. Use 'C', 'F', or 'K'.")

    # Convert Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit. Use 'C', 'F', or 'K'.")

def main():
    print("=== Temperature Conversion Program ===")
    print("Supported units: Celsius (C), Fahrenheit (F), Kelvin (K)")
    try:
        value = float(input("Enter the temperature value to convert: "))
        from_unit = input("Enter the unit of the input temperature (C/F/K): ").strip()
        to_unit = input("Enter the unit to convert to (C/F/K): ").strip()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit.upper()} is equal to {result:.2f}°{to_unit.upper()}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
