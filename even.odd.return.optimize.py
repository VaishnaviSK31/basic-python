def isevenodd(num):
    return num%2==0
    
n=int(input("Enter num:"))
flag=isevenodd(n)
if flag:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
