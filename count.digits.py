n=int(input("enter the num: "))
count=0
if n<0:
    n=n*(-1)
    count=0
while n>0:
    n=n//10
    count+=1
print(count)    