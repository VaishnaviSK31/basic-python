class Car:
    def __init__(self,name):
        self.cname=name
        print("Car is ready")
    def getCar(self):
        print("Car is used for driving")
class Heart:
    def __init__(self):
        self.status=True
        print("Heart is ready")
    def getHeart(self):
        print("Heart is waiting")
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart()
        self.c1=" "
        print("Person is ready")
    def hasPerson(self,x):
        self.c1=x
        print("Person is using car to drive")
p=Person("Vaish")
c2=Car("Nano")
p.hasPerson(c2)
print(p.pname)
print(p.h.status)
print(p.c1.cname)
p.h.getHeart()
p.c1.getCar()
del p
print("After deleting")
#print(p.pname)
#print(p.h.status)
#print(p.c1.cname)
#p.h.getHeart()
#p.c1.getCar()
print(c2.cname)
c2.getCar()        