a=input("enter the name: ")
v=0
c=0
for i in range(0,len(a)):
    if(a[i!=""]):
        if(a[i]=='a' or a[i]=='e' or a[i]=='i' or  a[i]=='o' or  a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
            v+=1
        else:
            c+=1
print("total vowel: ",v)
print("total consonant=",c)                