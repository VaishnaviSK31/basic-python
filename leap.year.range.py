def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
s_year=int(input("enter start year:  "))
e_year=int(input("enter end year:  "))
if s_year>e_year:
    print("invalid input")
else:
    print("leap year: ")    
    for i in range(s_year,e_year+1):
        flag= is_leap_year(i)
        if flag:
            print(i,end=" ")
        
