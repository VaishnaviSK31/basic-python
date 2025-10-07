def printfactors(n,i):
    if i*i>n:
        return
    if n%i==0:
        print(i,end=" ")
        if i!=(n//i):
            print((n//i),end=" ")
    return printfactors(n,i+1)
    
n=int(input("Enter num:"))
printfactors(n,1)