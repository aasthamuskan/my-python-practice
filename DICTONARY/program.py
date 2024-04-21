s_dob={}
while True:
    line=input("please input the id and name seprated by commas or q to exit: ")
    if line=='q':
        break
    id,name=line.split(',')
    s_dob.update({id:name})

for x,y in s_dob.items():
    print(x,y)
key=input("enter the id to search: ")
if key in s_dob:
    print("key=",key,"value=",s_dob[key]) 
else:
    print("key not found||")           