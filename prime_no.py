       # prime no #


num=int(input("enter "))

i = 2
while (i<num):
    if (num%i == 0):
        print(num, 'is not a prime number')
        break
    i = i + 1
else:
    print(num, 'is a prime number')








