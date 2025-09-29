class A:
    def dispA(self):
        print("Inside A")
a=A()
a.dispA()
#a.dispB()
print(A.mro())
class A:
    def dispA(self):
        print("Inside A")
class B(A):
    def dispB(self):
        print("Inside B")
b1=B()
b1.dispB()
b1.dispA()
print(B.mro())
class A:
    def dispA(self):
        print("Inside A")
class B:
    def dispB(self):
        print("Inside B")
class C(A,B):
    def dispC(self):
        print("Inside C")
c1=C()
c1.dispC()
c1.dispB()
c1.dispA()
print(C.mro())

