n=int(input("Enter num:"))
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if j<i:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()