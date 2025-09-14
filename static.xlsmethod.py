class Demo:
    x=11
    def __init__(self):
        self.y=22
        self.z=33
    def disp(self):
        print(self.y)
        print(self.z)
    @staticmethod
    def static_method():
        print(Demo.x)
        Demo.x=44
        print(Demo.x)
    @classmethod
    def class_method(cls):
        print("Python")
d=Demo()
d.disp()
Demo.static_method()
Demo.class_method
