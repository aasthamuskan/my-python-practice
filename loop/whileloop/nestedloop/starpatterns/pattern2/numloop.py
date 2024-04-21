i=1
while i<=5:#no of rows
    b=1
    while b<=5-i:#for blank spaces
        print(" ",end="")
        b+=1
    j=1
    while (j<=i): #star printing
        print(j,end="")
        j+=1
    print()
    i=i+1      