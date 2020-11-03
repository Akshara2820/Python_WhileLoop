
s=input("enter name--")
x = len(s)        
a = 0
cosonant = 0      
vowel= 0

while (a < x):        
    if s[a] =="a" or s[a] =="e" or s[a] == "i" or s[a] =="o" or s[a] =="u":        
        vowel  += 1       
    elif s[a]=="A" or s[a]=="E" or s[a]=="I" or s[a]=="O" or s[a]=="U":
        vowel+=1
    else:
        cosonant +=1  
    
    a = a+1 

print ("Number of vowels: ",(vowel ))
print("No. of consonent:",(cosonant ))