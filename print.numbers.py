def printnum(n):
    if n<=0:
        return
    printnum(n-1)
    print(n,end=" ")
    return
    

n=int(input("Enter num:"))
printnum(n)
