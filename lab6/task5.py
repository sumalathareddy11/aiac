def create_account(name, balance=0):
    return {"name": name, "balance": balance}
def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        print(f"Deposited: {amount}. New Balance: {account['balance']}")
    else:
        print("Deposit amount must be positive.")
        # INSERT_YOUR_CODE
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New Balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance

if __name__ == "__main__":
    name = input("Enter account holder's name: ")
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance. Setting balance to 0.")
        balance = 0
    account = BankAccount(name, balance)
    print(f"Account created for {account.name} with balance {account.balance}")

    # Example usage:
    while True:
        print("\nOptions: 1) Deposit 2) Withdraw 3) Balance 4) Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.get_balance()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")
