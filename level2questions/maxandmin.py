a=[]
size=int(input())
for i in range(size):
    v=int(input("enter the elements"))
    a.append(v)

b=max(a)
c=min(a)
print("maximum in a: ",b)
print("minimum in a: ",c)    