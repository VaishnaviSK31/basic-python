n=int(input("Enter num:"))
noc=n
for i in range(1,(n*2)):
    for j in range(1,noc+2):
        print("*",end=" ")
    print()
    if i<n:
        noc-=2
    else:
        noc+=2