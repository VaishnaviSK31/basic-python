class Student:
    def __init__(self,name,age,height,addr):
        self.name=name
        self.age=age
        self.height=height
        self.addr=addr
s1=Student("rama",18,5.3,'bang')
s2=Student("sita",10,3.5,'hyd')
print(s1.name,s1.age,s1.height,s1.addr)
