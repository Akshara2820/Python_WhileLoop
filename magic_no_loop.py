n=int(input("enter any no--"))
i=0
c=0
c1=0
n1=str(n)
l=len(n1)
while i<l:
    if n1[i]=="7":
        c+=1
    if n1[i]=="5":
        c1+=1
    i+=1
if c!=0:
    if c1!=0:
        print("magic no ")
    else:
        print("not magic")
else:
    print("not magic")
