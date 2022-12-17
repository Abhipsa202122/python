#Python Program to Print Prime Numbers In a Given Range
n=int(input("enter no:"))
f=0
i=1
l=[]
while i<=n:
    if n%i==0:
       f+=1
    i+=1
if f==2:
    l.append(n)
    print(l," is Prime no.")
else:
    print(l,"is not prime no.")            
