def countdigits(n):
    if n<0:
        n=n*-1
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
strt_rnge=int(input("Enter start num:"))
end_rnge=int(input("Enter end num:"))
for i in range(strt_rnge,end_rnge+1):
    result=countdigits(i)
    print(f"The count of digits in {i} is : {result} ---->Vaishnavi")