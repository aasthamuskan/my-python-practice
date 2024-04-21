# Taking input for the number of rows
rows = int(input())

# Printing the pattern
for i in range(rows, 0, -1):
    if i % 2 == 0:
        print('.' * i)
    else:
        print('-' * i)
