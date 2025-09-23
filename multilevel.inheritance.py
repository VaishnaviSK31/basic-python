class A:
    def dispA(self):
        print("Inside dispA")
class B(A):
    def dispB(self):
        print("Inside dispB")
class C(B):
    def dispC(self):
        print("Inside dispC")
c1=C()
c1.dispC()
c1.dispB()
c1.dispA()