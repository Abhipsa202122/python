#display count of all permutations of strings without using any built in function: 
n=input()
a=len(n)
c=0
f=1
i=1
while i<=a:
    f=f*i
    i+=1
print("Factorial no.",f) 