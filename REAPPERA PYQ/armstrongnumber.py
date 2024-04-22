# a=int(input("Enter the value of 'a':"))
# i=1
# sum=0
# for i in range(1,a):
#     sum+=sum*10+i%10+i%10+i%10
#     i//=10
# if(sum==a):
#     print("armstrong number:")
# else:
#     print("not an armstrong number")
a = input("Enter the value of 'a': ")
num = len(a)
sum = 0

for digit in a:
    sum += int(digit) ** num

if sum == int(a):
    print(a, "is an Armstrong number.")
else:
    print(a, "is not an Armstrong number.")