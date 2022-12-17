#22.09.2022
#ACTIVITY-1:
#Create a class mobile with 3 instance variables :brand , model, price
#Create two functions  : call and discount
#Def call (self,mobile_number):
#Print(“calling to “,mobile_number)
class Mobile:
     def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
     def get__model(self):
        return self.__mobile__brand
     def get__brand(self):
        return self.__mobile__model
     def get__price(self):
        return self.__mobile__price
     def set__price(self, new_price):
         self.__price = new_price
     def call (self,mobile_number):
         print("calling to " ,mobile_number)
     def discount(self,discount_amt):
         self.__price -= discount_amt
a=Mobile("vivo", "Vivo T1",13499)       
#print(a.brand,a.model,a.price)
a.call("9438394703")
a.discount(12000)
print(a.get__price())

print(a.get__mobile__brand())
print(a.get__mobile__model())
print(a.get__mobile__price())
a.set__price(14000)
print("After changing the value of mobile ",a.get__mobile__price())
#ACTIVITY-2:
#17.Create a simple calculator using functions
class cal:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    def add(self):
        print(self.m+self.n)
    def sub(self):
        print(self.m-self.n)
    def mul(self):
        print(self.m*self.n)
    def div(self):
        print(self.m/self.n)
a1=cal(8,9)
a1.add()
a1.sub()
a1.mul()
a1.div()
#Write a program to define a student class that has the following attributes:
#- Name
#- Student ID
#- Marks
#The class must have a method to display the details.
#Also create an object that calls the method to display the details 
#class student:
   # Name="Twinkle"
   # Student_ID="@twinkle"
   # Marks=45
    #l=[]
    #def __init__(self,Name,Student_ID,Marks):
    #    self.Name=Name
     #   self.Student_ID=Student_ID
     #   self.Marks=Marks
#a1=student("Twinkle","@twinkle",45)
#print(a1.Name,a1.Student _ID,a1.Marks)
#18.Write a lambda function:
#- to calculate the sum of two numbers
#- that returns the square of a number
#- that returns the even numbers in a list 
sum=lambda a,b:(a+b)
print(sum(15,13))      
#        
square=lambda a:a**2
print(square(7))    
      
l=lambda a:[i for i in range(1,a) if i%2==0]  
print(l(10)) 
#26.  Write a program to :
#- Read the data from an existing file
#- Append data to the file
#-Display the data with - newly appended data

f=open(r"file.txt","w")
a1=("my name is abhipsa")
f.write(a1)
f.close()
#
f=open(r"file.txt","a")
f.write( "moharana")
f.close()
#Display the data with - newly appended data
       
