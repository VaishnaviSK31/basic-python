class Radio:
    def turnOn(self,x):
        if(x==1):
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=Radio()
c1=Car(60,180)
print(c1.min)
print(c1.max)
c1.r.turnOn(1)
c1.r.turnOn(2)