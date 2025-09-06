class Demo:
    def swap(self,a,b):
        temp=a
        a=b
        b=temp
d=Demo()
x=10
y=20
print("Before Swapping")
print(x)
print(y)
d.swap(x,y)
print("After Swapping")
print(x)
print(y)