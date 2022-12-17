#Recursive Palindrome or not:
def fun():
    n=int(input("enter a num:"))
    rev=0
    while n!=0:
        rev=rev*10+n%10       
        n = (n//10)
    print("Reverse Num",rev)
fun()     
