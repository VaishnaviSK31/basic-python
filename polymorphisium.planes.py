class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
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
c=Cargo()
p=Passenger()
f=Fighter()
def allowPlanes(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowPlanes(c)
allowPlanes(p)
allowPlanes(f)