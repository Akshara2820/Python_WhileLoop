n=int(input())
c=0
for i in range(n):
    N=int(input())
    if N<=2:
        print(1)
    elif N==3:
        print(2)
    else:
    
        s=0
        c=0
        for i in range(1,N):
            
            if s<=N:
                c+=1

            else:
                break
            s+=i        
        print(c-1)