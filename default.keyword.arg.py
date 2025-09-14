class Demo:
    def disp(self,a=111,b=222,c=333):
        print(a)
        print(b)
        print(c)
d=Demo()
x=100
y=200
z=300

d.disp(x, y, z)
d.disp(x,y)
d.disp(x)
d.disp()
d.disp(y)
d.disp(y,z)
d.disp(b=y,c=z)