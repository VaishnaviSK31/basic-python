def lcm(n1,n2):
    higher=n1
    if n2>n1:
        higher=n2
    lcm=higher
    while lcm:
        if lcm%n1==0 and lcm%n2==0:
            return lcm
        lcm=lcm+1
n1=int(input("Enter a frst num:"))
n2=int(input("Enter scnd num:"))
result=lcm(n1,n2)
print(f"the lcm of {n1} and {n2} is : {result}")