def fun1():
    a=10
    print("From fun1 a",a)

    def fun2():
        a=100
        b=20
        print("From fun2 b",b)
        print("From fun2 a",a)
    fun2()
    print("From fun1 a",a)
    
fun1()