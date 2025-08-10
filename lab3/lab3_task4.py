# Python program with two linked functions: login_user() and register_user()

users_db = {}

def register_user():
    print("=== Register User ===")
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter a new password: ")
    users_db[username] = password
    print("Registration successful! You can now log in.")

def login_user():
    print("=== Login User ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print(f"Welcome, {username}! Login successful.")
    else:
        print("Invalid username or password. Please try again.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
