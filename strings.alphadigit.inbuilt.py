print("Enter the string")
str1=input()
if(str1.isalpha()):
    print("String contains only alphabets")
elif(str1.isdigit()):
    print("String contains only digits")
elif(str1.isalnum()):
    print("String contains both alphabets and numbers")
else:
    print("Enter valid string")