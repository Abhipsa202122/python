#Excelsheet questions:
#23.Write a program to display a bar graph for two departments in a company, where the employee ids is in the x-axis and their salaries in the y-axis
#import matplotlib.pyplot as plt#for drawing a graph
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
#24.Create a program to display a pie chart showing the percentage of employees in different departments of a company
import matplotlib.pyplot as plt
emp=[23,44,55,66,80]
x=[0,0.3,0,0.5,0]
depart_of_company=["Marketing", "Finance","Operations_management","Human Resource","IT"]
plt.pie(emp,labels=depart_of_company)
plt.pie(emp,labels=depart_of_company,shadow = True,autopct = "%1.0f%%")
#plt.legend(loc="best")

plt.show()
#25.Write a program to create a line graph to show the profits of a company for the years 2015, 2016, 2017, 2018, 2019
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

#27.Write a program to display the next consecutive 10 dates from the current date
import datetime
d=datetime.datetime.now()
print(d)
i=1
n=int(input("enter no"))
while i<n:
    consecutive_date=d+datetime.timedelta(days=i)
    print(consecutive_date)
    cd_str=consecutive_date.strftime("%Y: %d: %B")
    i+=1
print(cd_str)
#28.Write a program to accept the date of birth of two persons and find out, who is the older of the two [Hint:Usethe datetime module]
#import datetime
#birth_date1= datetime.date(1993,4,23)
#print(birth_date1)
#birth_date2 = datetime.date(1994,5,28)
#print(birth_date2)
#age=(date.today()-birth_date1)//datetime.timedelta(days=365.2425)
#print(age)
#15.Write a program to create a dictionary with cricket players names and their scores in a match. Ask the user to enter the name of a player and return the runs scored by the player
players=input("Enter cricket player name :")
s=int(input("Enter  player score :"))
dic={}
dic[players]=s
print(dic)
#29.Create a dataframe from:
#- CSV file
#- Dictionary
#Using the dataframe retrieve:
#- the first two rows
#- the last two rows
#- the 2nd to 4th row

import pandas as pd
#a=pd.read_excel(r"C:\Users\abhipsa.moharana\Desktop\task1.csv.xlsx")
#print(a)
#print(type(a))
data={"NAME":["ALEX","PALEX","JAM","SAM","GENEVA","HALA","HAMJA"],"GRADE":["B2","C","B2","B1","A1","C","C"],"NO":[1,2,3,4,5,6,7]}
#Laod data into a dataframe object:
a1=pd.DataFrame(data)
print(a1)
print(type(a1))
print(a1.head(2))
print(a1.tail(2))
print(a1[2:])
#
#a1=pd.read_csv("data.csv")
#print(a1.to_string())

