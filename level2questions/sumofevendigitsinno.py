i=int(input("enter number: "))
sum=0
prd=1
while(i>0):
    d=i%10
    if d%2==0:
        sum = sum+d
    else:
        prd=prd*d
    i=i//10

print("sum of digits=",sum,"products of digits=",prd)            