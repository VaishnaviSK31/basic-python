def reversenum(n):
    temp=n
    if n<0:
        n=n*-1
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp<0:
        rev=rev*-1
    return rev
n=int(input("Enter num:"))
res=reversenum(n)
print(f"The reversal of {n} is: {res}")