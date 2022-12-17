#Find prime factors of a given integer:
i=1
n=int(input("enter no:"))
while (i<=n):
    if n%i==0:
        print(i)
    i+=1    