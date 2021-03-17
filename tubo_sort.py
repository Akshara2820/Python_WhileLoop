List1=[]
user=int(input())
for i in range(user):
    List1.append(int(input()))
    n=len(List1)
    for k in range(n-1):
    	for j in range(n-1-k):
    		if List1[j]>List1[j+1]:
    			List1[j],List1[j+1]=List1[j+1],List1[j]
for i in List1:
    print(i)
