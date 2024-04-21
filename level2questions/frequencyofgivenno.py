a=[]
s=int(input("enter the sixe"))
for i in range(s):
    val=input("enter the elements: ")
    a.append(val)
key=input("enter the eleme t u want to search: ") 
count=0
for i in range(s):
    if(a[i]==key):
        count+=1
print("frequency=:",count)           