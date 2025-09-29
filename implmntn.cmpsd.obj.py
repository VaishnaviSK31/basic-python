class Os:
    def __init__(self):
        self.status=True
        print("Os is ready")
    def getOs(self):
        print("Os is still executing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("Mobile is ready")
        print("With Os installed")
m=Mobile("iphone")
print(m.mname)
print(m.o.status)
m.o.getOs()
del m
print("After deleting")
print(m.mname)
print(m.o.status)
m.o.getOs()
