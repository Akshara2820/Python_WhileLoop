#  (10,2,20,4,30,6,40,8,50)

n=int(input("enter no--"))
i=1
c=10
while i<=n:
    if i%2==0:
        c+=10
        print(i,end=",")
        i+=1
    i+=1
    print(c,end=",")



#  (1+10=11, 11+20=31, 31+30=61, 61+40=101)
n=int(input("enter no,-"))
i=0
d=1
s=10
while i<n:
    print(d,end=",")
    d=d+s
    s+=10
    i+=1

# (1+10=11, 11+20=31, 31+30=61, 61+40=101)

n=int(input("enter no.=="))
i=1
d=1
while i<=n:
    print(d,end=" ")
    d=d+10*i
    i+=1



