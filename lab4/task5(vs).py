file_path = r"C:\Users\Sumalatha\OneDrive\Documents\Desktop\sample1.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")