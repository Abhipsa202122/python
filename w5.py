#21.09.2022
#Activity:1
#1.Write a Python program to create a Vehicle class with max_speed and mileage instance
# class bike:
#    max_speed= 96
#    mileage= 87
# print(bike.max_speed) 
# print(bike.mileage)   
#2.Create a class named Student. Create class variable called school name. create instance variables (name,age,class) using init method. Create two objects and print all the values using the objects
# class Student:
#     school_name="sam"
#     def __init__(self,Name,Age, Class):
#        self.Name = Name
#        self.Age = Age
#        self.Class = Class
#     def school(self):
#      print(self.Name+" "+self.Age+" "+self.Class+" ")
# Student_data= school("sam","5th",10)
# Student_data.school()
# print(Student_data.School())
#Activity:2
#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#Create a vehicle class with 3 instance variables, type,milage and model
# class vehicle:
#       def __init__(self,type,milage,model):
#           self.type="School_bus"
#           self.milage=108
#           self.model="TVM"
# bus=vehicle("School_bus",108,"TVM")
# print(bus.type,bus.milage,bus.model)
# #
# class Bus(vehicle):    
#     def __init__(self,type,milage,model,max_speed):        
#         vehicle.__init__(self,type,milage,model,max_speed)        
#         self.type="school_bus"        
#         self.milage=108
#         self.model="TVM"
#         self.max_speed=212

# a=Bus("School_bus",108,"TVM",212)
# print(a.type,a.milage,a.model,a.max_speed)
2. #1.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#Create a vehicle class with 3 instance variables, type,milage and model
#2.Create a child class with two instance variables capacity and build_year
#Create a object for child class and print all the values 

class child:
      def __init__(self,name,age):
          self.name="sam"
          self.age=6
#
class b(child):    
    def __init__(self,name,age,capacity,build_year):        
        child.__init__(self,name,age,capacity,build_year)
        self.name="sam"        
        self.age=6
        self.capacity="A"
        self.build_year=2014

a=b("sam",6,"A",2014)
print(a.name,a.age,a.capacity,a.build_year)
#3.Create a class and two child classes. 
#Create a example for multilevel inheritance . 
class Child:
    def __init__(self,name):
        self.name="sam"
class A(Child):
      def __init__(self,name,age):
          Child.__init__(self,name)
          self.age=10
class B(Child):
      def __init__(self,name,age,dist):
          Child.__init__(self,name,age)
          self.dist="Jajpur"
      def f(self):
          return self.dist
c=B("sam",10,"Jajpur")
print(c.name,c.age,c.dist)
     

#Activity:3
#FUNCTION QUESTIONS:
#Exercise 1: Create a function that can accept two arguments name and 
#  age and print its value
#def f():
#    a=input("Enter Name:")
#    print(a,b)
#f()
#Exercise 2: Write a function func1() such that it can accept a variable 
#  length of  argument and print all arguments value
#def func1(*a):
  #  for i in a:
  #       print(i)
#func1("hello mama","how are you")
#Exercise 3: Write a function calculation() such that it can accept two 
#  variables and calculate the addition and subtraction of them. And a
#  lso it must return both addition and subtraction in a single return 
#  call
#def calculation(a,b):
    #add=a+b
    #sub=a-b
    #return add,sub
#calculation(45,34)
#Exercise 4: Create a function showEmployee() in such a way that it 
#  should accept employee name, and its salary and display both. 
#  If the salary is missing in the function call assign default value 
#  9000 to salary
#def showEmployee():
#    a=input("Enter Employeename:")
#    b=int(input("salary:"))
#    if b==9000:
 #       print(b)
#print(showEmployee())  
#Exercise 5: Create an inner function to calculate the addition in the 
#  following way
#def outer_func():
 #   a=int(input("enter no"))
 #   b=int(input("enter no"))
  #  sum=0
  #  def inner_func():
   #     nonlocal sum
   #     sum=a+b
   # inner_func()    
   # sum+=5
    #return sum
#print(outer_func())
#Exercise 6: Write a recursive function to calculate the sum of numbers 
#  from 0 to 10
#def sum(n):
 #   if n:
 #       return 0    
  #  else:
  #      return n+sum(n-1)
#print(sum(10))

#Exercise 7: Assign a different name to function and call it through the new name
def func(name,age):
    print(name,age)
func("sam",10)    
