def fun1():
    print("Fun1 Connected to DB")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    finally:
        print("Fun1 closing DB")
def fun2():
    print("Fun2 connected to DB")
    try:
        res=10/5
        print(res)
    except Exception as e:
        print("Error in fun2")
        raise e
    finally:
        print("Fun2 closing DB")
        
print("program started")
try:
    fun1()
except Exception as e:
    print("Error in main")
print("program ended")