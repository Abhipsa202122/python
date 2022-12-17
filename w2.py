#Here you are given unbised dice containing faces.you will be given an output sum which should be obtained by throwing 2 dice.you need to return the no.of all posiblities where the sum on both the dice is equal to the output sum.If thre are no posiblities return 0.  
n=int(input())
c=0
if n>=0 and n<=12:
    for i in range(1,7):
        for j in range(1,7):
            if i+j==n:
                c+=1
    print(c)
else:
    print("not valid")   
#enter10
#3