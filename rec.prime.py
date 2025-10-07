def isprime(n,i,countfact):
    if i*i>n:
        return countfact==2
    if n%i==0:
        countfact+=1
        if i!=(n//i):
            countfact+=1
    return isprime(n,i+1,countfact)

n=int(input("Enter num:"))
flag=isprime(n,1,0)
if flag:
    print("is prime")
else:
    print("not prime")