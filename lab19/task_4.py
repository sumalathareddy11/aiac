# ...existing code...
def print_students(students):
    if not isinstance(students, list):
        raise TypeError("Expected a list of names")
    for name in students:
        print(name)

if __name__ == "__main__":
    try:
        answer = input("Enter student names (comma-separated). Or press Enter to input one name per line:\n").strip()
        if answer == "":
            print("Enter names one per line. Press Enter on an empty line to finish.")
            names = []
            while True:
                try:
                    line = input().strip()
                except EOFError:
                    break
                if line == "":
                    break
                names.append(line)
            if not names:
                print("No names entered.")
            else:
                print_students(names)
        else:
            students = [s.strip() for s in answer.split(",") if s.strip()]
            if not students:
                print("No names entered.")
            else:
                print_students(students)
    except KeyboardInterrupt:
        print("\nInterrupted.")
# ...existing code...