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
sr=int(input("Enter start num:"))
er=int(input("Enter end num:"))
if sr>er:
    print("Invalid input")
else:
    print("Integer Palindromes are:")
    for i in range(sr,er+1):
        flag=ispalindrome(i)
        if flag:
            print(i,end=" ")
    

