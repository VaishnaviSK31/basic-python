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
n=int(input("Enter num:"))
print(f"First {n} non palindrome numbers:--->Vaishnavi")
count = 0
series = 0
while count < n:
    if not ispalindrome(series):
        print(series, end=" ")
        count += 1
    series += 1
