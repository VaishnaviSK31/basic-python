def isevenodd(num):
    return num%2 == 0
sr=int(input("Enter start value:"))
er=int(input("Enter end value:"))
if sr>er:
    print("Invalid input")
else:
    print("Even num's: ")
    for i in range(sr,er+1):
        flag=isevenodd(i)
        if flag:
            print(i,end=" ")
    print("\n Odd num's:")
    for i in range(sr,er+1):
        flag=isevenodd(i)
        if not flag:
            print(i,end=" ")