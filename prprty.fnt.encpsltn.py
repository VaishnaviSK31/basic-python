class Student:
    def __init__(self):
        self.__name1="  "
        self.__name2="  "
    def getter1(self):
        return self.__name1
    def setter1(self,value):
        self.__name1=value
    getset=property(getter1,setter1)
    def getter2(self):
        return self.__name2
    def setter2(self,value):
        self.__name2=value
    setget=property(getter2,setter2)
s=Student()
s.getset="Rama"
res=s.getset
print(res)
s.setget="Sita"
print(s.setget)
