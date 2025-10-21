n=int(input("Enter num:"))
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    print()