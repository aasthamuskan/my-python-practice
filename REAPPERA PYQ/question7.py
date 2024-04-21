def is_armstrong(num):
    # Convert number to string to count digits
    num_str = str(num)
    # Get the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum equals the original number
    return armstrong_sum == num

def generate_armstrong_numbers(N):
    armstrong_list = []
    num = 0
    while len(armstrong_list) < N:
        num += 1
        if is_armstrong(num):
            armstrong_list.append(num)
    return armstrong_list

# Taking input
N = int(input())

# Generating Armstrong numbers
armstrong_numbers = generate_armstrong_numbers(N)

# Printing the list of Armstrong numbers
print(N)
print(armstrong_numbers)
