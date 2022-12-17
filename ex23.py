#anagram :
def anagramCheck(str1, str2):
    print(sorted(str1))
    print(sorted(str2))
    if (sorted(str1) == sorted(str2)):
        return True
    else:  
	    return False 
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if anagramCheck(str1,str2):
    print("Anagram")
else:
    print("Not an anagram")
   
