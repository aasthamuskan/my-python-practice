def collect_values_and_squares():
    n = int(input("Enter the number of elements: "))
    values_and_squares = []

    for _ in range(n):
        value = int(input("Enter an integer value: "))
        values_and_squares.append((value, value ** 2))

    result_tuple = tuple(values_and_squares)
    print(result_tuple)

# Test Case 1
collect_values_and_squares()
