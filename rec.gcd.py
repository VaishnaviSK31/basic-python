def findgcd(n1,n2,lower,i,hcf):
    if i>lower:
        return hcf


    if n1%i==0 and n2%i==0:
        hcf=i
    return findgcd(n1,n2,lower,i+1,hcf)
n1=int(input("Enter first num: "))
n2=int(input("Enter second num:"))
lower=n1
if n1>n2:
    lower=n2
res=findgcd(n1,n2,lower,2,1)
print(res)