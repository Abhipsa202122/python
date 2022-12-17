#4. Input 2 numbers from user and an operator from user + , - ,* , / based on operator do the operation
 #10 10 * it should do multiplication and display the output.
# a=int(input("enter no"))
# o=input("enter no") 
# print(a,o,a)
#2. Accept a character from user and check whether is vowel or not.   
# a=input("enter a character:")
# for i in a:
#     if i=="a" or i=="e" or i=="i"or i=="o" or i=="u":
#       print("vowel",i)
#     else:
    #   print("not",i)
#3. Accept username and password as string from user. If the username==” Admin” and password==”123” then print Welcome Admin else print invalid username or password.
# username=input("enter name") 
# password=int(input("enter pw"))
# if username=="Admin" and password=="123":
#    print("welcome Admin")
# else:
#    print("invalid un and pw") 
#If-else questions:
#1.Ans:
# n=int(input("enter no:"))
# if n%2==0:
#     print("no. is even")
# else:
#     print("no is odd")
#2.
#Ans:
# n=int(input("enter no:"))
# if n%5==0:
#     print("no. is divisible")
# else:
#     print("no is not divisible")

#3.
# a=int(input("enter 1st no"))
# b=int(input("enter 2nd no"))
# c=int(input("enter 3rd no"))
# if a>b:
#    print("1st no. is big")
# elif a<b:
#    print("2nd no is small")
# else:
#     print("3rd no is big")
#while loop questions:
#1.Ans:
# i=1
# while i<25:
#      if i%2==0:
#          print("even",i)
#      i+=1
# 2.
# n=int(input("enter"))
# f=1
# i=1
# while i<=n:
#      f=f*i
#      i+=1
# print("factorial of a no.",f)
# 3.
# a=int(input("enter no:"))
# if a>=18 and a==60:
#     print("person can vote")
# elif a<=18 and a>=0:
#     print("person can not vote")
# else:
#     print("invalid age")
#LIST QUESTIONS:
#1.Create a list with 10 numbers and  Display numbers from a list using  a for   loop.
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range (len(a)):
#     print(a[i]) 
#2.Create a list and print in reverse order using slicing
# list=["abhi","twinkle","mama"]
# for i in range(len(list)):
#     print(list[::-1]) 
#3.Create two list and join two list using + operator
# List1=["m","na","i","abhi"]
# List2=["y","me","s","psa"]
# List1=[3,5,7,8]
# List2=[4,5,6,8]
# l=[]
# for i in range(len(List1) and len(List2)):
#      d=List1[i]+List2[i]
#      l.append(d)
# print(l)
#4.Create a list and add a new item in the 4th index
# list1=["python","java","javascript","html","c++"]
# for i in list1:
#      list1.insert(4,"css")
# print(list1)
#5.Write a program to find value 20 in a list. If 20 is present in the list replace it with 200. 
# List=[10,20,30,40,50]
# index=List.index(20)
# List[index]=200
# print(List)
# for  index  in range(len(List)):
#     index=List.index(200)
#     List[index]=200
# print(List)
#TUPLE QUESTIONS:
#1.Create a tuple with 10 items and reverse it .
# List=(["banana","apple","papaya","kiwi","mango","orange","cherry","watermelon","coconut","guava"])
# for i in range(len(List)):
#      print(List[::-1]) 

#2.Given is a nested tuple. Write a program to modify the first item(22) of the list inside a following tuple to 222.
#Eg: t1 = (11,[22,33],44,55)
#1.Adding two numbers and storing it in a variable:
#ANS:
# a=15
# b=13
# c=a+b
# print(c)
#2.- Write a program to print "Welcome to the world of Python"
#- Converting from one numeric datatype to another (casting)

# a="welcome to the world of python"
# print(type(a))
#3.Accept a number from the user and test whether it is zero, positive or negative number. Display a message accordingly


# a=int(input("enter no:"))
# if a>0:
#     print("+ve")
# elif a<0:
#     print("-ve")
# else:
#     print("zero")  
#4.Accept two numbers and an operator from the user. Basis the operator, perform the operation on the numbers
# a=int(input("enter no:"))
# b=int(input("enter no:"))
# print(a+b,a-b,a*b,a/b,a**b,a//b) 
#5.Write a program to display and find the sum of a list of numbers
# a=[1,2,3,4]
# s=0
# for i in a:
#     s+=i
# print(s)
 # 6.Write a program to display the numbers 10 to 6, and break the loop when it is about to display the number 5
# i=10
# while i>6:
#     if i==5:
#         break
#     i+=1
# print(i)
#7.Accepting three numbers from the user and displaying the product
# a=int(input("enter"))
# b=int(input("enter"))
# print(a*b)
#Program that creates a list of computer languages. Use the appropriate list methods to:
#- sort the list
#- append to the list
#- remove an item from the list
list=["python","js","html","css"]
for i in range(len(list)):
    list.append("c++")
print(list)
#sort method():
list=["python","js","html","css"]
for i in range(len(list)):
    a=list.sort()
print(a)
#remove():
list=["python","js","html","css"]
for i in range(len(list)):
    a=list.remove("js")
print(a)

   
   
