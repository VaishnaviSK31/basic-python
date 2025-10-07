def printfactors(n,i,countfact):
    if i*i>n:
        return countfact
    if n%i==0:
        print(i,end=" ")
        countfact+=1
        if i!=(n//i):
            print((n//i),end=" ")
            countfact+=1
    return printfactors(n,i+1,countfact)

n=int(input("Enter num:"))
res=printfactors(n,1,0)
print(f"\nThe num of factors in {n} is : {res}")