n=int(input("enter prime no--"))
if n>1:
    i=2
    while i<n:
        if n%i==0:
            print("not prime.")
            break
        i+=1
    else:
        if n%2==0:
            print("even prime no.")
        else:
            print("odd prime no.")
else:
    print("composite number")
