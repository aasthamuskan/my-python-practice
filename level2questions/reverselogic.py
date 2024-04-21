a=[]
s=int(input())
for i in range(s):
    v=int(input("enter the num: "))
    a.append(v)
i=0
j=s-1 
while(i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
    print("list after reverse: ")
    for i in range(s):
        print(a[i]) 