def isprime(n):
    countfact=0
    i=1
    while i*i<=n:
        if n%i==0:
            countfact+=1
            if (n//i)!=i:
                countfact+=1
        i+=1
    return countfact==2
n=int(input("Enter a num:"))
flag=isprime(n)
if flag:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
