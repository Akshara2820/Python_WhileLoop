       #  armstrong no.#

num=int(input("enter the no."))
num1=num
sum=len(str(num))
sum1=0
while num>0:
    index=num%10
    sum1+=index**(sum)
    num//=10
if sum1==num1:
    print("armstrong no.",sum1)
else:
    print("not armstrong no.",num)



