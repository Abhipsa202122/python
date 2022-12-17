# RECURSIVE FIBONACCI SERIES:
def  fun():
    a=0
    b=1
    n=int(input("enter give a no.for fibonnaci series:"))
    print("fibonacci series are:")
    for i in range(0,n):
        if i<=1:
            result=i
        else:
            result=a+b
            a=b
            b=result
        print(result)
fun()    