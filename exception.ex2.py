print("Enter the value for a")
a=int(input())
print("Enter the value for b")
b=int(input())
try:
    c=a/b
    print(c)
except Exception as e:
    print("Error in program")
print("Program Ended")