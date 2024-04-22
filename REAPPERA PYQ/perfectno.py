a = int(input("Enter the number: "))
sum = 0

for i in range(a):
    if a % i == 0:
        sum+= i

if sum == a:
    print(a, "is a perfect number.")
else:
    print(a, "is not a perfect number.")
