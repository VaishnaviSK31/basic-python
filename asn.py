def countdig(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
n=int(input("Enter num:"))
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
if temp==asn:
    print(f"{temp} is ASN")
else:
    print(f"{temp} not an ASN")


