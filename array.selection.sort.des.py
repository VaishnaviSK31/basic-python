def createintarray():
    l1=[]
    while True:
        try:
            n=int(input("enter num:"))
            l1.append(n)
        except Exception as e:
            return l1
def selectionsortdesc(arr):
    n=len(arr)
    #cycles
    for i in range(0,n-1):
        actualind=(n-1-i)
        #find max ele's curr ind
        currmin,currminind=2**31,-1
        for j in range(0,n-i):
            if currmin>arr[j]:
                currmin=arr[j]
                currminind=j
        arr[actualind],arr[currminind]=(arr[currminind],arr[actualind])
print("Insert the values into the array:")
arr=createintarray()
print("Original array:,arr")
selectionsortdesc(arr)
print("Selection sort DES: ",arr)