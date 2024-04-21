def count_multiples(numbers):
    counts = {'3': 0, '5': 0, '7': 0}

    for num in numbers:
        if num % 3 == 0:
            counts['3'] += 1
        if num % 5 == 0:
            counts['5'] += 1
        if num % 7 == 0:
            counts['7'] += 1

    return counts

# Taking input
numbers = list(map(int, input().split()))

# Counting multiples
result = count_multiples(numbers)

# Printing the result
print(result)
