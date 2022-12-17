#Swap two no. without using third variable:
a = int(input("enter first no.:"))
b = int(input("enter second no.:"))
a=a-b
b=a+b
a=b-a
print("After swapping no.:")
print("value of a is : ", a)
print("value of b is : ", b) 
