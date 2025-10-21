import pickle
class Employee:
    def __init__(self,name,age,addr,mob):
        self.ename=name
        self.eage=age
        self.eaddr=addr
        self.emob=mob
    def display(self):
        print(self.ename)
        print(self.eage)
        print(self.eaddr)
        print(self.emob)
e=Employee("Rama",24,"Bang",9988)
f=open("names.txt","wb")
pickle.dump(e,f)
print("Object is saved into text file")
f.close()