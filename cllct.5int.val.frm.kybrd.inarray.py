L=[]
i=0
while(i<=4):
    print("Enter the value")
    data=int(input())
    L.insert(i,data)
    i=i+1
print(L)
i=0
while(i<=4):
    print(L[i])
    i=i+1
for i in L:
    print(i)