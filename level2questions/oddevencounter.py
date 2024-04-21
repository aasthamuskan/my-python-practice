a=int(input("enter the no of elements:"))
x=[]
for i in range(a):
    val=input("enter the elements:")
    x.append(val)

even=0
odd=0
for i in range(a):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("even no is: ",even)
print("odd no is: ",odd)                