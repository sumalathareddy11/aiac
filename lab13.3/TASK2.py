def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: '{filename}' was not found."
    except PermissionError:
        return f"Error: Permission denied for '{filename}'."
    except OSError as e:
        return f"Error: Could not read '{filename}': {e}"


if __name__ == "__main__":
    # Read and print the contents of the specified file
    print(read_file(r"C:\Users\Sumalatha\OneDrive\Desktop\AIAC\lab13.3\poem.txt"))
