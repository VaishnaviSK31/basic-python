class Demo:
    def add(self,x,y):
        res1=x+y
        return res1
    def sub(self,x,y):
        res2=x-y
        return res2
    def mul(self,x,y):
        res3=x*y
        return res3
    def div(self,x,y):
        res4=x/y
        return res4
d=Demo()
a=20
b=10
x1=d.add(a,b)
x2=d.sub(a,b)
x3=d.mul(a,b)
x4=d.div(a,b)
print(x1)
print(x2)
print(x3)
print(x4)