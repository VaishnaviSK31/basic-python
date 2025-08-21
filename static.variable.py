class Demo:
    x=77
    y=33
    def __init__(self):
        self.a=10
        self.b=20
d1=Demo()
d2=Demo()
d3=Demo()
print(Demo.x)
print(Demo.y)
Demo.x=5503
Demo.y=6830
print(Demo.x)
print(Demo.y)

