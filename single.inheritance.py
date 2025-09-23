class A:
    def dispA(self):
        print("Inside dispA")
class B(A):
    def dispB(self):
        print("Inside dispB")
b1=B()
b1.dispB()
b1.dispA()