class Demo:
    def __init__(self):
        self.a=10
        self.b=20

    def disp(self):
        x=100
        y=200
        z=x+y
        return z
d1=Demo()
print(d1.a)
print(d1.b)
r1=d1.disp()
print(r1)