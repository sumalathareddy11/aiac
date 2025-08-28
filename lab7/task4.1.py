values = [10, 0, 5, 0, 2]
for v in values:
    try:
        result = 100 / v
        print(f"100 divided by {v} is {result}")
    except ZeroDivisionError:
        print(f"Cannot divide by zero for value {v}, skipping.")
        continue
