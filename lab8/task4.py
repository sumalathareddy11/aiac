class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name].append(price)
        else:
            self.items[name] = [price]

    def remove_item(self, name):
        if name in self.items:
            self.items[name].pop()
            if not self.items[name]:
                del self.items[name]
        else:
            print(f"Item '{name}' not found in cart.")

    def total_cost(self):
        return sum(price for prices in self.items.values() for price in prices)

if __name__ == "__main__":
    cart = ShoppingCart()
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View total cost")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            name = input("Enter item name: ").strip()
            price_input = input("Enter item price: ").strip()
            try:
                price = float(price_input)
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                cart.add_item(name, price)
                print(f"Added '{name}' with price {price:.2f} to cart.")
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == "2":
            name = input("Enter item name to remove: ").strip()
            cart.remove_item(name)
        elif choice == "3":
            total = cart.total_cost()
            print(f"Total cost of items in cart: {total:.2f}")
        elif choice == "4":
            print("Exiting Shopping Cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")