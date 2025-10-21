def createintarray():
    l1=[]
    while True:
        try:
            a=int(input("Enter the number:"))
            l1.append(a)
        except Exception as e:
            return l1
def findmax(arr):
    max,maxind=-2**31,-1
    for i in range(0,len(arr)):
        if max<arr[i]:
            max=arr[i]
            maxind=i
    return max,maxind
print("Insert value into array")
arr=createintarray()
max,maxind=findmax(arr)
print(f"The min value is {max} in index {maxind}")


            