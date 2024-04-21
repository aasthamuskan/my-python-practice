a=[]
for i in range(8):
    x=input("enter the value: ")
    a.append(x)
print("original list is ",a) 
index=input("enter where u want to insert:")
value=input("")   
a.insert(index,value)
print("list after insersion: ",a)