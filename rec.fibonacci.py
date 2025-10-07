def fibo(pos,n1,n2):
    if pos<=0:
        return 
    print(n1,end=" ")
    fibo((pos-1),n2,(n1+n2))
pos=int(input("Enter num:"))
fibo(pos,0,1)
