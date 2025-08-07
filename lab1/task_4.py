class Students:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

def main():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student = Students(name, roll_no, marks)
    student.display()

if __name__ == "__main__":
    main()