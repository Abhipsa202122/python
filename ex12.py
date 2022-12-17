#Swap two no. using third variable:
a = int(input("enter first no.:"))
b = int(input("enter second no.:"))
c=a+b
b=c-b
a=c-a
print("After swapping no.:")
print("value of a is : ", a)
print("value of b is : ", b) 
