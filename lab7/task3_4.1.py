f = open("numbers.txt", "r")
nums = f.readlines()
f.close()
 
squares = []
for num in nums:
    n = num.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

f2 = open("squares.txt", "w")
for square in squares:
    f2.write(str(square) + "\n")
f2.close()
print("Squares written")