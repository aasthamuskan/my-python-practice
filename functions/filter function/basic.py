a=[5,12,17,18,24,32]
def myfunc(x):
    if x<18:
        return False
    else:
        return True
adults=list(filter(myfunc,a)) 
for x in adults:
    print(x)   