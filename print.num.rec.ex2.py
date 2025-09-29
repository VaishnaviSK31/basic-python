def printnum(n, i=1):
    if i > n:
        return
    print(i, end=" ")
    printnum(n, i+1)
    print(i, end=" ")

n = int(input("Enter num: "))
printnum(n)
