#Python program to print first n prime numbers
n=int(input("enter no:"))
f=0
i=1
while i<=n:
    if n%i==0:
       f+=1
    i+=1
if f==2:
    print(n," is Prime no.")
else:
    print(n,"is not prime no.")            
