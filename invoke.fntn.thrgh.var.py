def fun1():
    print("Fun1 is invoked")
def fun2(a,b):
    c=a+b
    print("The sum is",c)
fun1()
a=10
b=20
fun2(a,b)
ptr1=fun1
ptr2=fun2
ptr1()
ptr2(a,b)