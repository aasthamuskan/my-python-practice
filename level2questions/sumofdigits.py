a=[int(input("enter the no: "))]
i=1
sum=0
for i in range(len(a)):
    sum+=a%10
    a//=10
    i+=1
print(sum)    
