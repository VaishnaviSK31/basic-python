class Student :
    def __init__(self):
        self.name="Rama"
        self.age=23
        self.height=5.7
    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)
s1 = Student()
s1.display()
print(s1.name)
print(s1.age)
print(s1.height)