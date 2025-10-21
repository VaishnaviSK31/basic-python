n=int(input("Enter num:"))
odd=(n*2)-1
for i in range(n,0,-1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(odd+1)):
        print("*",end=" ")
    print()
    odd-=2