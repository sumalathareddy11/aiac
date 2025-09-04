def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input: score must be a number."
    if score < 0 or score > 100:
        return "Invalid input: score must be between 0 and 100."
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

user_input = input("Enter the score: ")
try:
    score = float(user_input)
except ValueError:
    print("Invalid input: score must be a number.")
else:
    print(assign_grade(score))