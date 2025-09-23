def printfactors(n):
    i=1
    countfact=0
    countcycles=0
    while i*i<=n:
        countcycles+=1
        if n%i==0:
            print(i,end=" ")
            countfact+=1
            if i!=(n//i):
                print((n//i),end=" ")
                countfact+=1
        i+=1
    return countfact,countcycles
n=int(input("Enter num:"))
resfact,rescycles=printfactors(n)
print(f"\nTotal num of factors of {n} is : {resfact}")
print(f"The total num of cycles of {n} is : {rescycles}")

