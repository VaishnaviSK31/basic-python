def dispfactors(n,i,countfact):
    if i>n:
        return countfact
    if n%i==0:
        print(i,end=" ")
        countfact+=1
    return dispfactors(n,i+1,countfact)
n=int(input("Enter number:"))
res=dispfactors(n,1,0)
print(f"\nThe number of factors of {n} is : {res} ")

