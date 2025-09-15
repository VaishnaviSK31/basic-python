def fun1():
    print("Inside fun1")
def fun2(x,y):
    z=x+y
    print("The sum is",z)
def display(ptr1,ptr2):
    ptr1()
    a=100
    b=200
    ptr2(a,b)
fun1()
fun2(40,30)
ptr3=fun1
ptr4=fun2
ptr3()
ptr4(40,30)
display(ptr3,ptr4)