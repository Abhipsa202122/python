'''n=int(input())
s=list(map(int,n.split(",")))
print(s)
i=0
while i<len(s):
    max=max(s)
    min=min(s)
    i+=1
print((max)+(min))
#second largest no:
l=[3,4,5,6,7] 
m1=0
m2=0
i=0
while i<len(l):
    if l[i]>m1:
        m2=m1
        m1=l[i]
    elif l[i]>m2:
        m2=l[i] 
    i+=1
print("max",m2) 
# max 6 '''  
     