# ...existing code...
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


if __name__ == "__main__":
    c1 = Car("Toyota", "Corolla", 2020)
    c2 = Car("Honda", "Civic", 2018)
    c1.display_details()
    c2.display_details()
# ...existing code...