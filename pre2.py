#Python Program to Find the Sum of First N Natural Numbers
n=5
sum=0
for i in range(n+1):
  sum+=i
  print(sum)
#Recursion:
def Sum(num):
  if num == 1:
    return 1
  return num + Sum(num-1)
#
num = 5
print(Sum(num))
num1, num2 = 3, 6
sum = 0
for i in range(num1,num2+1):
  sum+=i
  print(sum)
#
num1, num2, num3 = 10 , 30 , 20
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)
  

  
