x=int(input("enter the number"))
a=[]
for i in range(x):
    val=input("enter the num: ")
    a.append(val)
sum=0
for i in range(x):
    sum+=a[i]
print("sum of list =",sum)        
