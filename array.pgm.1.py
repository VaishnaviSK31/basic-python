n1=input("Enter the number:")
print(type(n1))
print(len(n1))
print("-----------------------------")
try:
    n1=int(input("Enter the number:"))
    print(type(n1))
    print(n1)
except Exception as e:
    print("INVALID INPUT")