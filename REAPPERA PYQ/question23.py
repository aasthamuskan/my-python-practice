def print_pattern(rows):
    for i in range(1, rows + 1):
        pattern = []
        for j in range(1, i + 1):
            pattern.append(str(j))
        print(' '.join(pattern))

# Test Case 2
print_pattern(7)
