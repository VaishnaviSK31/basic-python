def palindrome(n,rev,temp):
    if n<=0:
        return temp==rev
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return palindrome(n,rev,temp)
n=int(input("Enter num:"))
flag=palindrome(n,0,n)
if flag:
    print(f"is palindrome")
else:
    print("not a palindrome")