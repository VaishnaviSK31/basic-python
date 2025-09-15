def fun1():
        
    print("I am outer")
    def fun2():
        print("I am inner")
    return fun2
res=fun1()
print(res)
res()
