def ispalindrome(n):
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
    return temp==rev
num=int(input("Enter num:"))
flag=ispalindrome(num)
if flag:
    print(f"{num} is a integer palindrome")
else:
    print(f"{num} is not a palindrome")