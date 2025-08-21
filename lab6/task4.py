def sum_to_n_for(n):
    print("By for loop")
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def sum_to_n_while(n):
    print("By while loop")
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Sum using for loop:", sum_to_n_for(n))
    print("Sum using while loop:", sum_to_n_while(n))

