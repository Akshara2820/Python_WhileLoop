x=int(input("enter no."))
y=int(input("enter no."))
lcm=x*y
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
lcm=lcm//y
print(lcm)
# print(y)



# n=int(input("enter no."))
# i=int(input("enter no."))
# if n>i:
#     lcm= n
# else:
#     lcm= i
# while n!=i:
#     if (lcm%n==0 and lcm%i==0):
#         print(lcm)
#         break
#     lcm=lcm+1



# s=int(input('enter no'))
# a=int(input('enter no'))
# i=1
# while i<=s*a:
#     if i%s==0 and i%a==0:
#         print(i)
#         break
        
#     i+=1


