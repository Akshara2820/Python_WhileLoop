

            # loop me piche k 3 even no. and aaghye ke 3 odd no. print kro   #




# user=int(input("enter the no."))
# sum=1
# num=user
# while sum<=6:
#     if user%2==0:
#         print(user)
#     user-=1
#     sum+=1

# sum=1
# while sum<=6:
#     if num%2==1:
#         print(num)
#     num+=1
#     sum+=1


year=int(input("enter year."))
sum=1
sum1=year
while sum<=6:
    if year%4==0 and year%100!=0:
        if year%100==0 and year%400==0:
            print(year)
    year-=1
    sum+=1