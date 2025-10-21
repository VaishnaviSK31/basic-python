def createintarray():
    l1=[]
    while True:
        try:
            a=int(input("Enter the number:"))
            l1.append(a)
        except Exception as e:
            return l1
def findmin(arr):
    min,minind=2**31,-1
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
            minind=i
    return min,minind
print("Insert value into array")
arr=createintarray()
min,minind=findmin(arr)
print(f"The min value is {min} in index {minind}")