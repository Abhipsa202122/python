#Add two numbers without using addition operator:
def add(a,b):
    for i in range(1,b+1):
        a=a+1
    return a
a=add(6,7)    
print(a)

