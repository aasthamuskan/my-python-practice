def calculate_sum_and_multiplication(number):
    if number < 0 or len(str(number)) < 2:
        return "Invalid input"

    digits = [int(digit) for digit in str(number)]
    digit_sum = 0
    digit_mul = 1

    for index, digit in enumerate(digits):
        if (index + 1) % 2 == 0:  
            digit_mul *= digit
        else:  
            digit_sum += digit

    return digit_sum, digit_mul

if __name__ == "__main__":
    input_number = int(input("Enter a non-negative integer with at least 2 digits: "))
    result_sum, result_mul = calculate_sum_and_multiplication(input_number)

    print("Sum of digits at odd places:", result_sum)
    print("Multiplication of digits at even places:", result_mul)
