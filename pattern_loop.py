# 1
# 121
# 12321
# 1234321
# 123454321

n=1
while n<=5:
    j=1
    while j<n:
        print(j,end=" ")
        j+=1
    while j>=1:
        print(j,end=" ")
        j-=1
    print()
    n+=1


# 1 
# 2 3 2 
# 3 4 5 4 3 
# 4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5

r=1
while r<=5:
    c=1
    r1=r
    while c<=r:
        print(r1,end=" ")
        c+=1
        r1+=1
    r1-=1
    while r1>r:
        print(r1-1,end=" ")
        r1-=1
    print()
    r+=1
    
