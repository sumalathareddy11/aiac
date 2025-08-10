def sort_numbers():
    try:
        input_str = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, input_str.strip().split()))
        sorted_numbers = sorted(numbers)
        print("Sorted numbers:", ' '.join(map(str, sorted_numbers)))
    except ValueError:
        print("Invalid input: Please enter only integers separated by spaces.")

if __name__ == "__main__":
    sort_numbers()
