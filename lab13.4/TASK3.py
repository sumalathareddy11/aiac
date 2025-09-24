student_scores = {"Alice": 85, "Bob": 90}

# Manual dictionary lookup (verbose approach)
if "Charlie" in student_scores:
    print(student_scores["Charlie"])
else:
    print("Not Found")

# Safer approach using .get() method
score = student_scores.get("Charlie", "Not Found")
print(score)
