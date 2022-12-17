#Python program to find the average of numbers:
n=int(input("Enter the number of elements you want in array: "))
l=[]
#taking input of the list
for i in range(0,n):
    elem=int(input("Please give value for index "+str(i)+": "))
    l.append(elem)
#taking average of the elements of the list
avg=sum(l)/n
print("Average of the array elements is ",avg)
