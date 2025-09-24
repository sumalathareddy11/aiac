items = [10, 20, 30, 40, 50]

# Manual Loop approach (inefficient)
found = False
for i in items:
    if i == 30:
        found = True
        break
print("Found" if found else "Not Found")

# Optimized approach using 'in' keyword
result = "Found" if 30 in items else "Not Found"
print(result)
