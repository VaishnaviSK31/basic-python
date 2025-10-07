try:
    print("Enter the value for a")
    a=int(input())
    print("Enter the value for b")
    b=int(input())
    res=a/b
    print(res)
except ValueError as e:
    print("It is VE")
    print(e.__str__)
except ZeroDivisionError as e:
    print("It is ZDE")
except Exception as e:
    print("It is an error")
