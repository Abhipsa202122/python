#Perfect number program in Python:
n=int(input("enter no."))
f=0
i=1
while i<n:
    if n%i==0:
        f=f+i
    i=i+1
if f==n:
    print(n,"is perfect no.")
else:
    print(n,"is not a perfect no.")            