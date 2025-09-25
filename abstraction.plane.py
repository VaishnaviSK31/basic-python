from abc import ABC,abstractmethod
class Plane(ABC):
    @abstractmethod
    def takeoff(self):...
    @abstractmethod
    def fly(self):...
    @abstractmethod
    def land(self):...
class Cargo(Plane):
    def takeoff(self):
        print("Cargo is takeoff")
    def fly(self):
        print("Cargo is flying")
    def land(self):
        print("Cargo is landing")
class Passenger(Plane):
    def takeoff(self):
        print("Passenger is takeoff")
    def fly(self):
        print("Passeneger is flying")
    def land(self):
        print("Passenger is landing")
class Fighter(Plane):
    def takeoff(self):
        print("Fighter is takeoff")
    def fly(self):
        print("Fighter is flying")
    def land(self):
        print("Fighter is landing")
def allowPlanes(p:Plane):
    p.takeoff()
    p.fly()
    p.land()
allowPlanes(Cargo())
allowPlanes(Passenger())
allowPlanes(Fighter())