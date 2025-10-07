def fibo(n):
    if n==1 or n==0:
        return n
    return fibo(n-1)+fibo(n-2)


n=int(input("Enter num:"))
res=fibo(n)
print(f"The fibonacci series of {n} is : {res}")