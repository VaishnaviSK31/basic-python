def isevenodd(num):
    if num%2==0:
        return True
    else:
        return False
    
n=int(input("Enter num:"))
flag=isevenodd(n)
if flag:
    print(f"{n} is even")
else:
    print(f"{n} is odd")