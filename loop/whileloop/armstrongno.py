# n=int(input("enter the number: "))
# sum=0
# i=1
# while(i<=n):
#     sum+=(i%10)*(i%10)*(i%10)
#     i//=10
    
# if(sum==n):
#     print("armstrong number")
# else:
#     print("not an armstrong number")     
#wrong logic

n=int(input("enter the no: "))
i=n
count=0
while(i>0):
    i=i//10
    count=count+1
sum=0
while(i>0):
    digit=i%10
    x=1
    pro=1
    while(x<=count):
        pro=pro*digit
        x=x+1  
    sum=sum+pro
    i//=10
if(sum==n):
    print("the no is armstrong")
else:
    print("the no is not an armstrong")           
