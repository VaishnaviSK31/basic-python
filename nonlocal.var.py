def fun1():
    a=10
    print("From fun1 a",a)

    def fun2():
        b=20
        print("From fun2 b",b)
        print("From fun2 a",a)
    fun2()
    print("From fun1 a",a)
    print("From fun1 b",b)
fun1()