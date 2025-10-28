// ...existing code...
import java.util.Scanner;

public class NumberUtils{
    // Prints whether num is positive, negative, or zero
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is positive");
        } else if (num < 0) {
            System.out.println(num + " is negative");
        } else {
            System.out.println(num + " is zero");
        }
    }

    // Optional: returns the result as a String for reuse
    public static String checkNumberString(int num) {
        if (num > 0) return "positive";
        if (num < 0) return "negative";
        return "zero";
    }

    // Demo: take input from the user
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        if (scanner.hasNextInt()) {
            int n = scanner.nextInt();
            checkNumber(n);
        } else {
            System.out.println("Invalid input. Please enter a valid integer.");
        }
        scanner.close();
    }
}
// ...existing code...