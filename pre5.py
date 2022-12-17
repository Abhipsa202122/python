#Python Program to Find Sum Of Digits Of a Number
num = input("Enter Number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)
#
num = 12345
sum = 0
while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10
print(sum)
