def countdig(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdig(n,count)
num=int(input("Enter num:"))
res=countdig(num,0)
print(f"The count of digits in {num} is : {res}")