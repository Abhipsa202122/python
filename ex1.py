# Reverse  an integer in python:
'''n=int(input("enter a num:"))
rev=0
while n!=0:
    rev=rev*10+n%10       
    n = (n//10)
print("Reverse Num",rev) 
a=[[10,3,5,9],[6,7,9]]
l=[]
for i in a:
    l.append(max(i))
print(l)'''
a=input("enter") 
for i in range(len(a)):
    str=(a[::-1])
print(str) 
  