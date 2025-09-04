def convert_date_format(date_str):
    
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format.")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

if __name__ == "__main__":
    user_input = input("Enter a date in YYYY-MM-DD format: ")
    try:
        converted = convert_date_format(user_input)
        print("Converted date:", converted)
    except Exception as e:
        print("Error:", e)