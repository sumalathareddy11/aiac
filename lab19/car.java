// ...new file...
public class Car {
    private String brand;
    private String model;
    private int year;

    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("          Year: " + year);
    }

    public static void main(String[] args) {
        Car c1 = new Car("Toyota", "Corolla", 2020);
        Car c2 = new Car("Honda", "Civic", 2018);
        c1.displayDetails();
        c2.displayDetails();
    }
}
// ...new file...