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
n=int(input("enter a number : "))
count=0
series=2
while count<n:
   if primenumber(series):
       print(series,end=" ")
       count+=1
   series+=1