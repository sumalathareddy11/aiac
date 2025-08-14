# Python code to calculate sum of even and odd numbers individually

even_sum = 0
odd_sum = 0

n = int(input("How many numbers will you enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)