class A:
    def display(self):
        print("Inside class A")
class B(A):
    def display(self):
        print("Inside class B")
class C(B):
    def display(self):
        print("Inside class C")
class D(C):
    def display(self):
        print("Inside class D")
        A.display(self)
        B.display(self)
        C.display(self)
d1=D()
d1.display()


