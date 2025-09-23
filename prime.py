def printfactors(n):
    countfact=0
    countcycles=0
    for i in range(1,(n+1)):
        countcycles+=1
        if n%i==0:
            print(i,end=" ")
            countfact+=1
    return countfact,countcycles
def isprime(n):
    countfact=0
    i=1
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (n//i)!=i:
                countfact+=1
        i+=1
n=int(input("Enter a num:"))
resfact,rescycles=printfactors(n)
print(f"\nTotal num of factors of {n} is : {resfact}")
print(f"The total num of cycles of {n} is : {rescycles}")
flag=isprime(n)
if flag:
    print(f"prime")
else:
    print("not prime")
