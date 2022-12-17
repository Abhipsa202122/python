#Armstrong no.:
n=int(input("enter a no.:"))
sum=0
a=n
b=len(str(n))
print(b)
while a>0:
    digit=a%10
    sum=sum+digit**b
    a=a//10
if sum==n:
    print("Armstrong no. is:",n)
else:
    print(n,"is not Armstrong no.")        