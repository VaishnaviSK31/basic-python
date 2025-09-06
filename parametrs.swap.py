class Demo:
    def swap(self,a,b):
        temp=a
        a=b
        b=temp
        return a,b 
d=Demo()
x=10
y=20
print("Before Swapping")
print(x)
print(y)
x,y=d.swap(x,y)
print("After Swapping")
print(x)
print(y)