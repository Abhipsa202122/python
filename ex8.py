#Program to Find the max of 3 numbers in python:
a=int(input("enter no:"))
b=int(input("enter no:"))
c=int(input("enter no:"))
if a>=b and a>=c: 
	print(a,"a is greatest")
elif b>=a and b>=c:
	print(b,"b is greatest")
elif c>=a and c>=b:
	print(c,",","c is greatest")
else:
    print("smallest no.")  


