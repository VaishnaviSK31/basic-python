def reversenum(n,rev):
    if n<=0:
        return rev
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return reversenum(n,rev)
n=int(input("Enter num:"))
res=reversenum(n,0)
print(f"The reversal of {n} is: {res}")