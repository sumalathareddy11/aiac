def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")
    return user_data

def hide_sensitive_data(user_data):
    # Hide email except for the first character and domain
    email = user_data.get('email', '')
    if '@' in email:
        name_part, domain = email.split('@', 1)
        if len(name_part) > 1:
            hidden_name = name_part[0] + '*' * (len(name_part) - 1)
        else:
            hidden_name = '*'
        hidden_email = hidden_name + '@' + domain
    else:
        hidden_email = '*' * len(email)
    # Hide age (show only as a range)
    try:
        age = int(user_data.get('age', 0))
        if age < 18:
            age_range = "<18"
        elif age < 30:
            age_range = "18-29"
        elif age < 50:
            age_range = "30-49"
        else:
            age_range = "50+"
    except ValueError:
        age_range = "Unknown"
    # Return a new dictionary with sensitive data hidden
    hidden_data = {
        'name': user_data.get('name', ''),
        'age': age_range,
        'email': hidden_email
    }
    return hidden_data

data = collect_user_data()
print("Collected Data (secured):", hide_sensitive_data(data))



