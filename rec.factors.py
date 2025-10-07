def dispfactors(n,i):
    if i>n:
        return
    if n%i==0:
        print(i,end=" ")
    dispfactors(n,i+1)
n=int(input("Enter number:"))
dispfactors(n,1)

