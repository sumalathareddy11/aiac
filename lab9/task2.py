class sru_student:
    """
    A class to represent a student at SRU.
    Attributes:
        name (str): The name of the student.
        roll_no (str): The roll number of the student.
        hostel_status (str): The hostel accommodation status of the student.
        fee (float): The fee amount for the student.
    Methods:
        fee_update(new_fee):
            Updates the student's fee to the new value and prints a confirmation message.
        display_details():
            Prints the student's details including name, roll number, hostel status, and fee.
    """
    def __init__(self, name, roll_no, hostel_status, fee):
        # Initialize the student object with name, roll number, hostel status, and fee
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee = fee
    def fee_update(self, new_fee):
        # Update the student's fee to the new value
        self.fee = new_fee
        print("Fee updated successfully!")

    def display_details(self):
        # Print the student's details
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Fee:", self.fee)
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Enter hostel status (Yes/No): ")
fee = float(input("Enter current fee: "))
student = sru_student(name, roll_no, hostel_status, fee)
student.display_details()
new_fee = float(input("\nEnter updated fee: "))
student.fee_update(new_fee)
student.display_details()
