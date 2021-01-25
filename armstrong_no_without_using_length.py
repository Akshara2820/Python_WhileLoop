n=int(input("enter no--"))
c=0
s=0
n1=n
while n1>0:
    c+=1
    n1//=10
n1=n
while n1>0:
    r=n1%10
    s+=(r**c)
    n1//=10
if n==s:
    print(s,"armstrong no")
else:
    print(s,"not armstrong no")
    
    