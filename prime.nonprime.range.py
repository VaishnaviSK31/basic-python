def primenumber(n):
   countfactors=0
   i=1
   while i*i<=n:
       if n%i==0:
           countfactors+=1
           if i!=(n//i):
               countfactors+=1
       i=i+1
   return countfactors==2
sr=int(input("enter start number :"))
er=int(input("enter end number :"))
if sr>er:
   print("Invalid Input")
else:
   for i in range(sr,er+1):
       flag=primenumber(i)
       if flag:
           print(f"{i} is primenumber---->Vaishnavi")
   for i in range(sr,er+1):
       flag=primenumber(i)
       if not flag:
           print(f"{i} is not primenumber---->VAishnavi")