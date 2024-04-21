try:
    elements = list(map(int, input().split()))
    n = int(input())

    for i in range(n):
        print(elements[i])

except IndexError:
    print("Index out of range")
