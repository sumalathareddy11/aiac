def age_group(age):
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"
# Read age from user and print their group
age_input = int(input("Enter your age: "))
group = age_group(age_input)
print("You are in the group:", group)


  