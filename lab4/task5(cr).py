def count_lines_in_file():
    file_path = r"C:\Users\Sumalatha\OneDrive\Documents\Desktop\sample1.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print("File not found.")
        return 0

# Example usage:
if __name__ == "__main__":
    num_lines = count_lines_in_file()
    print(num_lines)
