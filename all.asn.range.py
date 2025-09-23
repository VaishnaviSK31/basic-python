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

sr = int(input("Enter start range: "))
er = int(input("Enter end range: "))

if sr > er:
    print("Invalid input")
else:
    print("Armstrong numbers in range:")
    for i in range(sr, er + 1):
        if isasn(i):
            print(f"{i}--->Vaishnavi")

