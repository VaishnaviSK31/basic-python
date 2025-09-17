def countdigits(n):
    if n<0:
        n=n*-1
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
n=int(input("Enter num:"))
res=countdigits(n)
print(f"The count of digits in {n} is : {res}")