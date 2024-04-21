def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors

def collect_factors():
    n = int(input())
    numbers_and_factors = []

    for _ in range(n):
        num = int(input())
        factors = prime_factors(num)
        numbers_and_factors.append([num, factors])

    return numbers_and_factors

# Test Case 1
test_case_1 = collect_factors()
print(test_case_1)

# Test Case 2
test_case_2 = collect_factors()
print(test_case_2)
