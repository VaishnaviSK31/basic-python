def sum(n):
    if n==0 or n==1:
        return 1
    return n+sum(n-1)

n=int(input("Enter num:"))
res=sum(n)
print(res)