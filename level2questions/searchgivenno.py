a=[]
s=int(input("enter the size: "))
for i in range(s):
    v=input("enter the elemnets: ")
    a.append(v)
y=input("enter the value to search: ") 
f=0
for i in range(s):
    if(a[i]==y):
        f=1 
        pos=i+1
        break
if(f==1):
    print("element found at: ",pos,"position.")
else:
    print("element not found: ")          
