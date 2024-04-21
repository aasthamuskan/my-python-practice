n=int(input("enter the number: "))
sum=0
i=1
while(i<=n):
    sum+=(i%10)*(i%10)*(i%10)
    i//=10
print("sum of cube: ",sum)