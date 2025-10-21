n=int(input("Enter num:"))
if n%2==0:#only when there is a mid star
    n=n+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n  or i==j or (i+j)==(n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()