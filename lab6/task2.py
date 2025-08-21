def multiple_num(n):
    print("Multiples of given number using for loop")
    for i in range(1, 11):
        print(n * i)
    print("End of multiples")
    print("Multiples of given number using while loop")
    i=1
    while i <= 10:
        print(n * i)
        i += 1
    print("End of multiples")
n=int(input("Enter the number: "))
multiple_num(n)