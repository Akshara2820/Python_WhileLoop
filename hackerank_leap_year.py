year=int(input())
if year<1918:
    if year%4==0:
        print("12.09."+str(year))
    else:
        print("13.09."+str(year))
elif year>1918:
    if year%400==0 or (year%4==0 and year%100!=0):
        print("12.09."+str(year))
    else:
        print("13.09."+str(year))
else:
    print("26.09."+str(year))