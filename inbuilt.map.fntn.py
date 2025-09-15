def operation(data):
    return data+10
L=[]
i=0
while(i<=4):
    print("Enter the value")
    data=int(input())
    L.insert(i,data)
    i=i+1
print(L)
k=list(map(operation,L))
print(k)