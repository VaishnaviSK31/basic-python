def countdig(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

def isasn(n):
    temp = n
    if n < 0:
        n = -n
    pow = countdig(n)
    asn = 0
    while n > 0:
        base = n % 10
        asn = asn + (base ** pow)
        n = n // 10
    if temp < 0:
        asn = -asn
    return temp == asn
n=int(input("Enter num:"))
print(f"First {n} ASN numbers:--->Vaishnavi")
count = 0
series = 0
while count < n:
    if isasn(series):
        print(series, end=" ")
        count += 1
    series += 1
