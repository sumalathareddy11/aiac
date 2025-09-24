class Student:
    """
    A class to represent a student with name, age, and a list of marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize the student with name, age, and marks.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            marks (list of int/float): The marks obtained by the student.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        """
        Print the student's details in a readable format.
        """
        print(f"Student Details:\n  Name: {self.name}\n  Age: {self.age}")

    def total(self):
        """
        Calculate and return the total marks.

        Returns:
            int/float: The sum of all marks.
        """
        return sum(self.marks)

# Take inputs from the user
name = input("Enter the student's name: ")
while True:
    try:
        age = int(input("Enter the student's age: "))
        break
    except ValueError:
        print("Please enter a valid integer for age.")

while True:
    marks_input = input("Enter the student's marks separated by spaces: ")
    try:
        marks = [float(mark) for mark in marks_input.strip().split()]
        if not marks:
            print("Please enter at least one mark.")
            continue
        break
    except ValueError:
        print("Please enter valid numbers for marks, separated by spaces.")

student1 = Student(name, age, marks)
student1.details()
print(f"Total Marks: {student1.total()}")
