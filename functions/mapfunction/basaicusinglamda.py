ages=[5,12,17,18,24,32]
adults=filter(lambda a:a%2==0,ages)
square=list(map(lambda a:a*a,adults))
print(square)