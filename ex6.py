#PALINDROME OR NOT:
name=input("enter name")
pal=(name[::1])
if pal==name:
    print(name," is a Palindrome")
else:
    print(name,"is not a Palindrome")    