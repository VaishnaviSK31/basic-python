def countdig(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdig(n,count)
def isasn(n,pow,asn,temp):
    if n<=0:
        return temp==asn

    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isasn(n,pow,asn,temp)

n=int(input("Enter num:"))
pow=countdig(n,0)
flag=isasn(n,pow,0,n)
if flag:
    print("ASN")
else:
    print("NOT ASN")
