def fibo1(pos):
    #decrementing while
    n1,n2=0,1
    while pos>0:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        pos-=1
def fibo2(pos):
    #decrementing for
    n1,n2=0,1
    for i in range(pos,0,-1):
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
def fibo3(pos):
    #incrementing for
    n1,n2=0,1
    for i in range(1,pos+1):
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
def fibo4(pos):
    #incrementing while
    n1,n2=0,1
    count=0
    while count<pos:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1


pos=int(input("Enter num:"))
print("Print decrementing while:")
fibo1(pos)
print("\nPrint decrementing for:")
fibo2(pos)
print("\nPrint incrementing for:")
fibo3(pos)
print("\nPrint incrementing while:")
fibo4(pos)