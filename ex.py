#print("hy"+"abhi")
#print("hy"*"abhi")
#print("hy"*3)
#print("hy"/"abhi")
#some_string ="Python"
#a, b, c, d = some_string
#print(a,b,c,d)
'''s = {2, 4, 6, 8}
s1= {1, 2, 5, 6, 7, 8}
s.union(s1)
print(s)
s.difference(s1)
print(s)
s.intersection(s1)
print(s)
if 'bin' in {'float': 1.2, 'bin': 0b010}:
     print('a')
     print('b')
print('c')
a='1' + '2' 
if  '123'.isdigit():
    print(a)
else:
    print('2'  + '3')
a = "six"
b = (int(a), float(a))
print(b)
new_list = ["Red", "Blue", "White", "Green"]
z = sorted(new_list)
print(z)
d = list(z)
print(d)
d[0], d[1], d[2], d[3] = d[3], d[2], d[1], d[0]
print(d)
total_classes = 100
attended_classes = 67

attendance = (attended_classes/total_classes)*100
print(attendance)
if attendance >= 75:
    print ("You are eligible to appear for the test.")
else:
    print ("Sorry, you are ineligible to appear for the test.")
my_list = [["tiger", "lion", "leopard"], ["camel", "llama", "alpaca"], ["zebra", "donkey", "wildebeest"]]

for x in my_list:
    print(x)
x = 4
while x < 4+6:
    print(x)
    x += 1
inventory = []
item = ""
while item != "quit":
    item = input("Enter an item to add to the inventory: ")
    print("Adding item:", item)
    inventory.append(item)
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vowels = ['a', 'e', 'i', 'o', 'u']
i = 0

while i < len(my_list):

    if(my_list[i] in vowels):
        i += 1
        continue
        
    print(my_list[i])
    i += 2
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)
def fun1(num):
    return num + 25

print(fun1(5))
a={"b":10,"c":30}
a["b"]=40
print(a)
a={b:10,c:20}
a[b]=40
print(a)
a="Hi"
def fun(b):
    b="hy"
    return b
fun(a)'''
def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))
x = 'abcd'
for i in range(len(x)):
    print(i)













    

    
    
    

    





