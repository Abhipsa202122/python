#25.09.2022
#DATE AND TIME PYTHON
#ACTIVITY:2
#1. Write a Python script to display the various Date Time formats -  a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of week
#A.Current date and time:
import datetime
cur_datetime = datetime.datetime.now()
print(cur_datetime)
#B.Current  year:
cur_year=datetime.date.today().strftime("%Y")
print(cur_year)
#C.Month of year:
Month_of_year=datetime.date.today().strftime("%B")
print(Month_of_year)
#D.Week no. of the year:
Week_no_year=datetime.date.today().strftime("%W")
print(Week_no_year)
#E.Weekday of the week:
Weekday_of_the_week=datetime.date.today().strftime("%w")
print(Weekday_of_the_week)
#F.Day of year:
Day_of_year=datetime.date.today().strftime("%j")
print(Day_of_year)
#G.Day of the month:
Day_month=datetime.date.today().strftime("%d")
print(Day_month)
#H.Day of week
Day_week=datetime.date.today().strftime("%A")
print(Day_week)
#2.Write a Python program to determine whether a given year is a leap year
#y=int(input('enter year:'))
#if y%400==0:
#    print(y,"is leap year")
#elif (y%4==0 and y%100!=0) :
#    print(y,"is a leap year.")
#else :
#    print(y,"is not a leap year.")

  #  3.Write a Python program to convert a string to datetime.  Sample String : Jan 1 2014 2:43PM
from datetime import datetime
time="Jan 1 2014 2:43PM"
a=datetime.strptime(time,'%b %d %Y %I:%M%p')
print(type(a))
print(a)
#4.Write a Python program to get the current time in Python
#cur_time = datetime.datetime.now()
#print(cur_time)
#5.Write a Python program to subtract five days from current date
#from datetime import date,timedelta
#t=date.today()-timedelta(5)
#print(date.today())
#print(t)
#6.Write a Python program to print yesterday, today, tomorrow.
import datetime
today=datetime.date.today()
print("TODAY:",today)
yd=today-datetime.timedelta(days=1)
print("YESTERDAY:",yd)
tomorrow=today+datetime.timedelta(days=1)
print("TOMORROW:",tomorrow)
# 7.Write a Python program to add 5 seconds with the current time
import datetime
cur_time=datetime.datetime.now()
print("currenttime:",cur_time)
add=cur_time+datetime.timedelta(0,5)
print(add)

#8.Write a Python program to add year(s) with a given date and display the new date.
#9.Write a Python prog#ram to get days between two dates. Sample Dates : 2000,2,28, 2001,2,28
from datetime import date
fd=date(2000,2,28)
sd=date(2001,2,28)
print(fd-sd)
#10.Write a Python program to add a month with a specified date.
#from datetime import date,timedelta
#import calendar
#sd=date(2022,9,25)
#am=calendar.monthrange(sd.year,sd.month)[1]
#print(sd+timedelta(days=am))
#12.Write a program to accept the date of birth of two persons and find out, who is the older of the two [Hint:Usethe datetime module]
import datetime
birth_date1= datetime.date(1993,4,23)
print(birth_date1)
birth_date2 = datetime.date(1994,5,28)
print(birth_date2)
age=(date.today()-birth_date1)//datetime.timedelta(days=365.2425)
print(age)
print(datetime.datetime.now())
#Matplotlib Python
#ACTIVITY:3
#Write a program to display a bar graph for two departments in a company, where the employee ids is in the x-axis and their salaries in the y-axis
import matplotlib.pyplot as plt#for drawing a graph
#y=[1000,2000,3000,4000]
#x=[87,67,56,74]
#plt.figure(figsize = (10,10))
#plt.bar(x,y,label="Employee_Data",color="purple")
#plt.xlabel("Employee id")
##plt.ylabel("Employee_salaries")
#plt.title("Company")
#plt.grid()
#plt.legend()
#plt.show()
#2.Create a program to display a pie chart showing the percentage of employees in different departments of a company
import matplotlib.pyplot as plt
emp=[23,44,55,66,80]
x=[0,0.3,0,0.5,0]
depart_of_company=["Marketing", "Finance","Operations_management","Human Resource","IT"]
plt.pie(emp,labels=depart_of_company)
plt.pie(emp,labels=depart_of_company,shadow = True,autopct = "%1.0f%%")
#plt.legend(loc="best")

plt.show()
#3.Write a program to create a line graph to show the profits of a company for the years 2015, 2016, 2017, 2018, 2019
import matplotlib.pyplot as plt
plt.style.use("dark_background")
x=[2015,2016,2017,2018,2019]
y=["63%","70%","45%","73%","55%"]
plt.figure(figsize = (10,10))
plt.title("Line Graph")
plt.plot(x,y,color = "brown",linewidth = 5,marker = '*',ms = 25,mfc = "blue")
plt.xlabel("year")
plt.ylabel("profit")
plt.show()
#POLYMORPHISM PYTHON QUESTIONS:
#ACTIVITY:1
#1.Create a class called Mathematics. Define a add function. The function should work if u are giving 2 numbers or 3 number or n numbers , it should add and give the output. If no number is given it should return 0 as output.
#class Mathematics:
 #   def add(self,*a):
  #      if a!=None:
  #          return sum(a)
  #      else:
   #         return 0
#subj=Mathematics()
#print(subj.add(4,6,7)) 
#2.Create a class called area. Create a function which will calculate area of square if one input is given, if two inputs given calculate and print the area of rectange, if no input is given it should print “Nothing to find”
#class Area:    
 #   def area_of_squre(self,m=None,n=None):        
      #  if m!=None:            
  #          print("area of square",m*m)        
   #     elif m!=None and n!=None:            
       #     print("area of rectangle",m*n)                    
       # else:            
          #  print("Nothing to find")

#a1=Area()
#a1.area_of_squre(9,4)            
#3.Create a parent class Robot. Then a class that inherits from the class Robot. We add a method action that we override: . Create a method named action in both parent and child class. Create a object for child class and call the action method. 

class Robot:    
    def Alex(self):        
        print("HELLO")    
        
    def Jaction(self):        
        print("I am Robot")        
class Robot1(Robot):    
    def Geneva(self):        
        print("I can do any work")        
a=Robot1()
a.Alex()
a.Jaction()
a.Geneva()



