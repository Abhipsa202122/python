length = int(input())
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(length):
    if i % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
print(odd_arr)       
even_arr = sorted(even_arr)
print(even_arr)
odd_arr = sorted(odd_arr)
print(odd_arr)
print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])
#Input:
#7
#1 8 0 2 3 5 6 
#Output:
#8
def mylist():
    a=[3,5,6,[7,8,44],[33,1,99]] 
    i=0
    l=[] 
    while i<(len(a)):
        if type(a[i])==int:
            l.append(a[i])
        if type(a[i])==list:
            j=0
            while j<len(a[i]):
                l.append(a[i][j])
                j+=1  
        i+=1
    print(l)      
    m1=0
    m2=l[0]
    s1=0
    for i in range(len(l)):
        s1+=l[i]
        if l[i]>m1:
            m1=l[i]
        if l[i]<m2:
            m2=l[i]
    print("max",m1)
    print("min",m2) 
    print(s1)             
mylist()  

