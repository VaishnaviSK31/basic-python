class Student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    @classmethod
    def class_method(cls,s_info):
        name, age=s_info.split()
        return cls(name, int(age))
s=Student.class_method("Rama, 24")
print(s.name)
print(s.age)