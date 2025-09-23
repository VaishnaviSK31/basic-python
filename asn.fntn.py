def countdig(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
def isasn(n):
    temp=n
    if n<0:
        n=n*-1
    pow=countdig(n)
    asn=0
    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
    if temp<0:
        asn=asn*-1
    return temp==asn
n=int(input("Enter num:"))
flag=isasn(n)
if flag:
    print(f"{n} is ASN")
else:
    print(f"{n} not an ASN")