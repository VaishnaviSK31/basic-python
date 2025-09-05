print("Enter the string")
str1=input()
i=0
newstr=" "
while(i<=len(str1)-1):
    data=str1[i]
    if(data== " "):
        i=i+1
    else:
        newstr=newstr+data
        i=i+1
print(newstr)
      
