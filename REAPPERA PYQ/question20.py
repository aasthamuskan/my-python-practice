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

# Sample Test Cases
input_numbers = [15, 25, 35, 45, 55]
counts_dict = count_multiples(input_numbers)
print(' '.join(map(str, input_numbers)))
print(counts_dict)
