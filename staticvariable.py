class Demo:
    x=99
    y=88
    def __init__(self):
        self.a=10
        self.b=20
d1=Demo()
d2=Demo()
d3=Demo()
print(Demo.x)
print(Demo.y)
Demo.x=555
Demo.y=666
print(Demo.x)
print(Demo.y)