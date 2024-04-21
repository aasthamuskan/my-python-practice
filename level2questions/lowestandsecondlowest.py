a=[]
s=int(input("enter the size: "))
for i in range(s):
    v=int(input("enter the num:"))
    a.append(v)
m=min(a)
print("minimum value:",m)
a.remove(m)
s=min(a)
print("second minimum value is: ",s)    