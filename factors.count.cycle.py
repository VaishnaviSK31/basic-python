def dispfactors(n):
    countfact=0
    countcycles=0
    for i in range(1,(n+1)):
        countcycles+=1
        if n%i==0:
            print(i,end=" ")
            countfact+=1
    return countfact,countcycles
n=int(input("Enter num:"))
resfact,rescycles=dispfactors(n)
print(f"\nTotal num of factors of {n} is : {resfact}")
print(f"The total num of cycles of {n} is : {rescycles}")