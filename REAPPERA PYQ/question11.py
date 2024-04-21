# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    digits = str(number)
    # Initialize the sum to 0
    total = 0
    # Iterate over each digit and add it to the total
    for digit in digits:
        total += int(digit)
    return total

# Taking input
number = int(input())

# Calculating and printing the sum of digits
print(sum_of_digits(number))
