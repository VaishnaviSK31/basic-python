def createintarray():
    l1=[]
    while True:
        try:
            a=int(input("Enter the number:"))
            l1.append(a)
        except Exception as e:
            return l1
def arrayreversal(arr):
    i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
print("Enter the value in the array to be created:")
arr=createintarray()
print("Original array",arr)
arrayreversal(arr)
print("Reverse array",arr)