import re
def is_valid_email(email):
    if email.count('@') != 1:
        return False
    if '.' not in email:
        return False
    if not re.match(r'^[A-Za-z0-9][A-Za-z0-9@._-]*[A-Za-z0-9]$', email):
        return False
    if email.startswith('@') or email.endswith('@'):
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    return True

email = input("Enter your email: ")
if is_valid_email(email):
    print("Valid email.")
else:
    print("Invalid email.")