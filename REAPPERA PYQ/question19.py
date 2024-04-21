def print_pattern(rows):
    for i in range(1, rows + 1):
        pattern = []
        for j in range(1, i + 1):
            pattern.append(str(j))
        print(' '.join(pattern))

# Sample Test Cases
print_pattern(5)  # Test Case 1
print()  # Empty line for separation
print_pattern(7)  # Test Case 2
