#a="My name is Sam I live in Mumbai"-reverse questions
a="My name is Sam I live in Mumbai"
r=" "
i=len(a)
while i>0:
    r+=a[i-1]
    i-=1
print(r)    
        
a="My name is Sam", "Sam lives in Mumbai","Sam plays crickets"
print(a.count("Sam"))
i=0
c=0
while i<len(a):
    if a[i]=="Sam":
       c+=1
    i+=1
