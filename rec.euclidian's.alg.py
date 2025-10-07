def findgcd(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return findgcd((n1%n2),n2)
n1=int(input("Enter 1st num:"))
n2=int(input("Enter 2nd num:"))
res=findgcd(n1,n2)
print(res)