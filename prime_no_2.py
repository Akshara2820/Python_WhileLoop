
         # PRIME NO. #



n=int(input("enter the number"))
i=2
while i<=n:

	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i)
	i=i+1
