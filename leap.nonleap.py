year=int(input("enter a year: "))
if ((year % 100!=0 and year % 4 == 0)or(year % 400==0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")    