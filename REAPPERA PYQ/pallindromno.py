n=int(input("enter the number: "))
sum=0
i=n
while(i>0):#ye condition kiu lag rahi hai i<=n kiu nahiiiii??
    sum+=(n*10)+i%10
    i//=10
if(i==n):
    print("pallindrom number")
else:
    print("the no is not pallindrom")        