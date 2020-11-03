num=int(input("enter no."))
sum=0
num1=num
while num>0:
    rem=num%10
    sum=sum+rem
    num//=10
if num1%sum==0:
    print("harshad no.",num1)
else:
    print("not harshad no.",num1)