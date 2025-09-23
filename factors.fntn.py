def dispfactors(n):
    i=0
    for i in range(1,(n+1)):
        if n%i==0:
            print(i,end=" ")
n=int(input("Enter num:"))
dispfactors(n)
