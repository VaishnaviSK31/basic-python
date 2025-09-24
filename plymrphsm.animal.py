class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def breath(self):
        print("Animal is breathing")
class Tiger(Animal):
    def eat(self):
        print("Tiger is eating")
    def sleep(self):
        print("Tiger is sleeping")
    def breath(self):
        print("Tiger is breathing")
class Deer(Animal):
    def eat(self):
        print("Deer is eating")
    def sleep(self):
        print("Deer is sleeping")
    def breath(self):
        print("Deer is breathing")
class Monkey(Animal):
    def eat(self):
        print("Monkey is eating")
    def sleep(self):
        print("Monkey is sleeping")
    def breath(self):
        print("Monkey is breathing")
t=Tiger()
d=Deer()
m=Monkey()
def allowAnimal(ref):
    ref.eat()
    ref.sleep()
    ref.breath()
allowAnimal(t)
allowAnimal(d)
allowAnimal(m)