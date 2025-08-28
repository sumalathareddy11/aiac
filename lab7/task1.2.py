def factr(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return n*factr(n-1)
print(factr(5))