def sum_and_count_zeros(number):
    digits = [int(digit) for digit in str(number)]
    digit_sum = sum(digits)
    zero_count = digits.count(0)
    
    return digit_sum, zero_count

if __name__ == "__main__":
    input_number = int(input("Enter an integer: "))
    result_sum, result_zeros = sum_and_count_zeros(input_number)

    print("Sum of digits:", result_sum)
    print("Count of zeros:", result_zeros)
