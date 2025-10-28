// ...existing code...
#include <iostream>
#include <string>
#include <sstream>
#include <stdexcept>

long long factorial(int n) {
    if (n < 0) throw std::invalid_argument("factorial() not defined for negative values");
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    std::cout << "Enter a non-negative integer (or press Enter to run demo for 5 and 0): ";
    std::string line;
    if (!std::getline(std::cin, line)) {
        // EOF -> run demo
        int demo_vals[] = {5, 0};
        for (int v : demo_vals) std::cout << v << "! = " << factorial(v) << '\n';
        return 0;
    }

    if (line.empty()) {
        int demo_vals[] = {5, 0};
        for (int v : demo_vals) std::cout << v << "! = " << factorial(v) << '\n';
        return 0;
    }

    std::stringstream ss(line);
    int n;
    if (!(ss >> n) || (ss >> std::ws, !ss.eof())) {
        std::cerr << "Invalid input. Please enter a valid integer.\n";
        return 1;
    }

    if (n < 0) {
        std::cerr << "Error: please enter a non-negative integer.\n";
        return 1;
    }

    try {
        std::cout << n << "! = " << factorial(n) << '\n';
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    }
    return 0;
}
// ...existing code...