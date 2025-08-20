# Python script to collect user data

def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")
    return user_data

data = collect_user_data()
print("Collected Data:", data)
# To anonymize or protect this data:
# - Do not store raw data in plain text files or logs.
# - Hash or pseudonymize identifiers (e.g., use a hash of the email instead of the actual email).
# - Remove or mask direct identifiers (e.g., replace name with initials or a random ID).
# - Store data in encrypted storage or use secure databases.
# - Limit access to the data to only those who need it.
# - Regularly delete data that is no longer needed.
