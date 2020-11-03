# when i put 4 so give me 4 prime no.  #




n=int(input("enter no."))
a=2
c=1
while 1>0:
    i=2
    
    while i<a:
        if a%i==0:
            break
        i+=1
    else:
        print(a)
        if c==n:
            break
        c+=1
    a+=1
