from math import pi
pi=10
def fun1():
    pi=15
    def fun2():
        pi=20
        print(pi)
    fun2()
fun1()
