class Demo:
    def arith_op(self,x,y):
        res1=x+y
        res2=x-y
        res3=x*y
        res4=x/y
        return res1,res2,res3,res4
d=Demo()
a=20
b=10
x1,x2,x3,x4=d.arith_op(a,b)
print(x1,x2,x3,x4)