ages=[5,12,17,18,24,32]
def myfunc(x):
    if x<18:
        return False
    else:
        return True
def myFunc1(x):
    return x*x
adults= filter(myfunc,ages)

for x in adults:
    print(x)
squares= map(myFunc1,adults)
for x in squares:
    print(x)        