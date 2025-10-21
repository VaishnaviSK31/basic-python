def createintarray():
    l1=[]
    while True:
        try:
            n=int(input("enter num:"))
            l1.append(n)
        except Exception as e:
            return l1
def selectionsortasc(arr):
    n=len(arr)
    #cycles
    for i in range(0,n-1):
        actualind=(n-1-i)
        #find max ele's curr ind
        currmax,currmaxind=-2**31,-1
        for j in range(0,n-i):
            if currmax<arr[j]:
                currmax=arr[j]
                currmaxind=j
        arr[actualind],arr[currmaxind]=(arr[currmaxind],arr[actualind])
print("Insert the values into the array:")
arr=createintarray()
print("Original array:,arr")
selectionsortasc(arr)
print("Selection sort ASC: ",arr)

