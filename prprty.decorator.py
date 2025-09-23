class Person:
    def __init__(self):
        self.__name="  "
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value
p=Person()
p.dataAccess="Vaishh"
res=p.dataAccess
print(res)
print(p.dataAccess)