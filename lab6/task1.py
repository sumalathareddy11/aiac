def calculate_marks(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=60:
        return "C"
    else:
        return "F"

def student(name,rollno,marks):
    print("---Student Details---")
    print("Name:",name)
    print("Roll no:",rollno)
    print("Marks:",marks)
    print("Grade:",calculate_marks(marks))
    print("--------------------------------")

def read_student_details():
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    while True:
        try:
            marks = float(input("Enter marks: "))
            break
        except ValueError:
            print("Please enter a valid number for marks.")
    grade = calculate_marks(marks)
    details = {
        "name": name,
        "rollno": rollno,
        "marks": marks,
        "grade": grade
    }
    return details

# Read details and call the student function
details = read_student_details()
student(details["name"], details["rollno"], details["marks"])
print("Returned Grade:", details["grade"])