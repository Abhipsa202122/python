#Python program to calculate the factorial using iterative approach:
n=int(input("enter no.="))
f=1
i=1
while i<=n:
    f=f*i
    i+=1
print("Factorial no.",f)    
#Factorial in Recursive 
def fact(n):  
   if n == 0:  
       return n  
   else:  
#recursion 
       return n*fact(n-1)
num=4
print("factorial of",num,"is",fact(num))   
   