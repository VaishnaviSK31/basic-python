class Person:
    def __init__(self):
        self.__name=" "
    def setter1(self,value):
        self.__name=value
    def getter1(self):
        return self.__name
p=Person()
p.setter1("Rama")
res=p.getter1()
print(res)
print(p.getter1())