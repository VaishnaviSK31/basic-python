print("-----------------------------------")
print("STRING ARRAY")
def array():
    l1=[]
    while True:
        data=input("Enter the string:")
        if data=="":
            return l1
        l1.append(data)
res=array()
print(res)
print("-----------------------------------------")
print("CHARACTER ARRAY")
def array():
    l1=[]
    while True:
        data=input("Enter the string:")
        if data=="":
            return l1
        l1.append(data[0])
res=array()
print(res)