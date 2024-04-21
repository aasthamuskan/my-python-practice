def generate_pattern(numbers):
    pattern = []
    for num in numbers:
        pattern.append(num)
        pattern.append(num ** 2 * -1)
    return pattern

numbers = [int(x) for x in input().split()]

result = generate_pattern(numbers)

print(*result)
