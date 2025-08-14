
def convert_temperature():
    try:
        temp = float(input("Enter the temperature: "))
        input_unit = input("Enter the unit of input temperature (c/k/f): ").strip().lower()
        output_unit = input("Enter the option you need to convert (c/k/f): ").strip().lower()
        
        # Normalize input temperature to Celsius
        if input_unit == 'c': 
            celsius = temp
        elif input_unit == 'k':
            celsius = temp - 273.15
        elif input_unit == 'f':
            celsius = (temp - 32) * 5/9
        else:
            print("Invalid input unit.")
            return
        
        # Convert from Celsius to desired output unit
        if output_unit == 'c':
            result = celsius
            unit_str = 'c'
        elif output_unit == 'k':
            result = celsius + 273.15
            unit_str = 'k'
        elif output_unit == 'f':
            result = celsius * 9/5 + 32
            unit_str = 'f'
        else:
            print("Invalid output unit.")
            return
        
        # Format input for output
        input_unit_str = input_unit
        # Print result rounded to 1 decimal if not integer
        if result == int(result):
            result_str = f"{int(result)}"
        else:
            result_str = f"{result:.1f}"
        if temp == int(temp):
            temp_str = f"{int(temp)}"
        else:
            temp_str = f"{temp:.1f}"
        print(f"{temp_str}{input_unit_str} is equal to {result_str}{unit_str}")
    except Exception as e:
        print("Invalid input. Please enter numeric values for temperature.")

convert_temperature()









