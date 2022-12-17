#3. Accept and long string from user and find the number of vowels in that string.

a="My name is Paul I live in Mumbai"
print(len(a))
c=0
c1=0
for i in a:
    if i=="a" or i=="e" or i=="i"or i=="o" or i=="u":
       c+=1
    else:
       c1+=1
print("vowels",c)
print("consonant",c1)
        
